import logging
import os


class LogGen:
    @staticmethod
    def loggen(log_file="C:/Users/Alian Testing/PycharmProjects/alianhub-test-automation/logs/automation.log"):
        """Generate a logger instance."""
        # Ensure log directory exists
        log_file = os.path.abspath(log_file)
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a logger instance
        logger = logging.getLogger("automation_logger")  # Named logger
        if not logger.hasHandlers():  # Avoid adding multiple handlers
            # Configure handler and formatter
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                           datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Set logger level
            logger.setLevel(logging.INFO)

        # Disable propagation to avoid duplicate logs
        logger.propagate = False
        return logger
