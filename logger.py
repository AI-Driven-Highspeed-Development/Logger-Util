import logging
import os
import sys
from typing import Optional
from datetime import datetime

class Logger:
    """
    A centralized logger utility for consistent logging across the application.
    """
    
    def __init__(self, 
                 name: str = "Logger",
                 level: str = "INFO", 
                 log_to_file: bool = False,
                 log_file_path: Optional[str] = None,
                 verbose: bool = False):
        """
        Initialize the Logger.
        
        Args:
            name (str): Logger name
            level (str): Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_to_file (bool): Whether to log to a file
            log_file_path (Optional[str]): Path to log file (if log_to_file is True)
            verbose (bool): Enable verbose logging (sets level to DEBUG)
        """
        
        self.name = name
        self.level = logging.DEBUG if verbose else getattr(logging, level.upper(), logging.INFO)
        self.log_to_file = log_to_file
        self.log_file_path = log_file_path or f"logs/{name}_{datetime.now().strftime('%Y%m%d')}.log"
        
        # Create the main logger
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)
        
        # Clear existing handlers to prevent duplicates
        self.logger.handlers.clear()
        
        # Setup handlers
        self._setup_console_handler()
        if self.log_to_file:
            self._setup_file_handler()
    
    def _setup_console_handler(self):
        """Setup console handler for logging to stdout."""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self.level)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
    
    def _setup_file_handler(self):
        """Setup file handler for logging to file."""
        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(self.log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(self.level)
        
        # Create formatter for file (more detailed)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
    
    def get_logger(self, module_name: Optional[str] = None):
        """
        Get a logger instance for a specific module.
        
        Args:
            module_name (Optional[str]): Name of the module requesting the logger
            
        Returns:
            logging.Logger: Logger instance
        """
        if module_name:
            return logging.getLogger(f"{self.name}.{module_name}")
        return self.logger
    
    def debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)
    
    def info(self, message: str):
        """Log an info message."""
        self.logger.info(message)
    
    def warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)
    
    def error(self, message: str):
        """Log an error message."""
        self.logger.error(message)
    
    def critical(self, message: str):
        """Log a critical message."""
        self.logger.critical(message)
    
    def set_level(self, level: str):
        """
        Change the logging level.
        
        Args:
            level (str): New logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        new_level = getattr(logging, level.upper(), logging.INFO)
        self.logger.setLevel(new_level)
        self.level = new_level
        
        # Update all handlers
        for handler in self.logger.handlers:
            handler.setLevel(new_level)
    
    def add_custom_handler(self, handler: logging.Handler):
        """
        Add a custom handler to the logger.
        
        Args:
            handler (logging.Handler): Custom handler to add
        """
        self.logger.addHandler(handler)
    
    def remove_all_handlers(self):
        """Remove all handlers from the logger."""
        self.logger.handlers.clear()





# Global centralized logger instance for debugging and special purposes
_central_logger = None

def get_central_logger(verbose: bool = False, log_to_file: bool = True) -> logging.Logger:
    """
    Get the centralized "mother of all loggers" for debugging and special purposes.
    This is a singleton logger that you can throw anything at.
    
    Args:
        verbose (bool): Enable verbose logging
        log_to_file (bool): Enable file logging (default True for central logger)
        
    Returns:
        logging.Logger: The centralized logger instance
    """
    global _central_logger
    if _central_logger is None:
        logger_instance = Logger(
            name="CENTRAL",
            verbose=verbose,
            log_to_file=log_to_file,
            log_file_path=f"logs/central_{datetime.now().strftime('%Y%m%d')}.log"
        )
        _central_logger = logger_instance.get_logger()
    return _central_logger


# Convenience function for quick logger access
def get_logger(module_name: str = None, verbose: bool = False, log_to_file: bool = False) -> logging.Logger:
    """
    Get a logger instance.
    
    Args:
        module_name (str): Name of the module
        verbose (bool): Enable verbose logging
        log_to_file (bool): Enable file logging
        
    Returns:
        logging.Logger: Logger instance
    """
    if module_name:
        logger_instance = Logger(
            name=module_name,
            verbose=verbose,
            log_to_file=log_to_file
        )
        return logger_instance.get_logger()
    else:
        logger_instance = Logger(verbose=verbose, log_to_file=log_to_file)
        return logger_instance.get_logger()


# Convenience functions for central logger - no-brainer logging
def log_debug(message: str):
    """Quick debug logging to central logger."""
    get_central_logger(verbose=True).debug(message)

def log_info(message: str):
    """Quick info logging to central logger."""
    get_central_logger().info(message)

def log_warning(message: str):
    """Quick warning logging to central logger."""
    get_central_logger().warning(message)

def log_error(message: str):
    """Quick error logging to central logger."""
    get_central_logger().error(message)

def log_critical(message: str):
    """Quick critical logging to central logger."""
    get_central_logger().critical(message)


if __name__ == "__main__":
    print("Testing logger functionality...")
    
    # Test module-specific logger
    print("\n1. Testing module-specific logger:")
    logger = get_logger("TestModule", verbose=True)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Test central logger
    print("\n2. Testing central logger:")
    central = get_central_logger(verbose=True)
    central.debug("Central logger debug message")
    central.info("Central logger info message")
    
    # Test convenience functions
    print("\n3. Testing convenience functions:")
    log_debug("No-brainer debug message")
    log_info("No-brainer info message")
    log_warning("No-brainer warning message")
    log_error("No-brainer error message")
    log_critical("No-brainer critical message")
    
    print("\nAll tests completed!")
