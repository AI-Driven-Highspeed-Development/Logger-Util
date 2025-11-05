"""
ADHD Logger Utility Package

A centralized logging utility for consistent logging across the ADHD project template.

Usage:
    from utils.logger_util import Logger, get_central_logger
    from utils.logger_util import log_debug, log_info, log_warning, log_error, log_critical
    from utils.logger_util.logger_style import NormalStyle

    # Per-name singleton wrapper
    logger = Logger(name="MyModule", verbose=True)
    logger.info("This is a message")

    # Switch console style
    from utils.logger_util import set_logger_style
    set_logger_style(logger, NormalStyle())

    # Centralized "mother of all loggers" (stdlib logger)
    central = get_central_logger(verbose=True)
    central.debug("Throw anything at this logger!")

    # No-brainer convenience functions (uses central logger)
    log_debug("Quick debug message")
    log_error("Something went wrong!")

    # File logging (default path: ./logs/MyModule_YYYYMMDD.log)
    Logger(name="MyModule", log_to_file=True).info("Also logged to file")
"""