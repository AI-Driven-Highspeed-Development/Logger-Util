"""
ADHD Logger Utility Package

A centralized logging utility for consistent logging across the ADHD project template.

Usage:
    from utils.logger import Logger, LoggerFactory, get_logger
    
    # Quick logger access
    logger = get_logger("MyModule", verbose=True)
    logger.info("This is a message")
    
    # Using LoggerFactory
    logger = LoggerFactory.create_module_logger("MyModule", verbose=True)
    logger.debug("Debug message")
    
    # Direct Logger class usage
    logger_instance = Logger(verbose=True, log_to_file=True)
    logger = logger_instance.get_logger("MyModule")
"""

try:
    from .logger import Logger, LoggerFactory, get_logger
except ImportError:
    from logger import Logger, LoggerFactory, get_logger

__all__ = ['Logger', 'LoggerFactory', 'get_logger']
