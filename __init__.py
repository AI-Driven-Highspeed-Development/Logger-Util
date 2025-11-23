"""
ADHD Logger Utility Package

A centralized logging utility for consistent logging across the ADHD project template.
"""

from utils.logger_util.logger import (
    Logger,
    get_central_logger,
    set_logger_style,
    log_debug,
    log_info,
    log_warning,
    log_error,
    log_critical,
)
from utils.logger_util.logger_style import NormalStyle, LoggerStyle
from utils.logger_util.compact_style import CompactStyle

__all__ = [
    "Logger",
    "get_central_logger",
    "set_logger_style",
    "log_debug",
    "log_info",
    "log_warning",
    "log_error",
    "log_critical",
    "NormalStyle",
    "LoggerStyle",
    "CompactStyle",
]
