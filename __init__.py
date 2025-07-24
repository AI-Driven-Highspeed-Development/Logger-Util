"""
ADHD Logger Utility Package

A centralized logging utility for consistent logging across the ADHD project template.

Usage:
    from utils.logger_util import Logger, get_logger, get_central_logger
    from utils.logger_util import log_debug, log_info, log_warning, log_error, log_critical
    
    # Quick logger access for specific modules
    logger = get_logger("MyModule", verbose=True)
    logger.info("This is a message")
    
    # Centralized "mother of all loggers" for debugging
    central = get_central_logger(verbose=True)
    central.debug("Throw anything at this logger!")
    
    # No-brainer convenience functions (uses central logger)
    log_debug("Quick debug message")
    log_error("Something went wrong!")
    
    # Direct Logger class usage
    logger_instance = Logger(verbose=True, log_to_file=True)
    logger = logger_instance.get_logger("MyModule")
"""