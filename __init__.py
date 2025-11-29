"""
ADHD Logger Utility Package

A centralized logging utility for consistent logging across the ADHD project template.
"""

# Add path handling to work from the new nested directory structure
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.getcwd()  # Use current working directory as project root
if project_root not in sys.path:
    sys.path.insert(0, project_root)

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
