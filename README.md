# Logger Utility

Small, centralized, pluggable logging for console and files. Provides compact and normal styles, a central logger, and convenience helpers built on the Python standard `logging` module.

## Overview
- Create named loggers with optional verbose (DEBUG) mode
- Switch styles at runtime (compact or normal)
- Optional file logging with daily timestamped filenames
- Central singleton logger and convenience functions
- Safe handler management and child logger inheritance

## Features
- Pluggable console styles
  - `CompactStyle` (default): succinct, TTY‑aware colors
  - `NormalStyle`: verbose classic formatting
- Helpers and singletons
  - `get_logger(name, verbose=False)` returns a configured `logging.Logger`
  - `get_central_logger(verbose=False)` returns the shared central logger
  - `set_logger_style(logger, style)` switches styles on the fly
  - Convenience shorthands: `log_debug/info/warning/error/critical`
- File logging
  - `Logger(..., log_to_file=True)` adds a file handler with normal style
  - Filenames like `logs/<Name>_YYYYMMDD.log`

## Quickstart

```python
from utils.logger_util.logger import get_logger, set_logger_style, get_central_logger
from utils.logger_util.logger_style import NormalStyle
from utils.logger_util.compact_style import CompactStyle

# Compact by default
log = get_logger("MyModule", verbose=True)
log.debug("Debug in compact style")

# Switch to normal style at runtime
set_logger_style(log, NormalStyle())
log.info("Now in normal style")

# Central logger
central = get_central_logger(verbose=True)
central.debug("Central diagnostics")
```

## API

```python
# Factory helpers
get_logger(name: str | None = None, verbose: bool = False) -> logging.Logger
get_central_logger(verbose: bool = False) -> logging.Logger
set_logger_style(logger: logging.Logger, style: LoggerStyle) -> None

# Logger class (optional higher‑level orchestration)
class Logger:
    def __init__(self, name: str | None = None, verbose: bool = False, log_to_file: bool = False): ...
    def get_logger(self) -> logging.Logger: ...
    def set_style(self, style: LoggerStyle) -> None: ...
    def set_level(self, level: str) -> None: ...

# Styles
class LoggerStyle: ...
class NormalStyle(LoggerStyle): ...
class CompactStyle(LoggerStyle): ...
```

Notes
- Stream handler is created on demand by `apply_style` and reused.
- Child loggers inherit handlers from parents; avoid adding duplicate handlers to children.
- File handlers always use NormalStyle (full context), independent of console style.

## Requirements & prerequisites
- Python standard library only (uses `logging`).

## Troubleshooting
- Duplicate messages: Don’t attach multiple handlers to the same logger.
- No color output: Set `LOGGER_COLOR=1` and run in a TTY; some terminals/CI strip ANSI.
- Missing log files: Ensure `./logs/` is writable.
- Too verbose: Use `verbose=False` or set level to `INFO`.

## Module structure

```
utils/logger_util/
├─ __init__.py               # package exports
├─ logger.py                 # core helpers and Logger class
├─ logger_style.py           # LoggerStyle base + NormalStyle
├─ compact_style.py          # CompactStyle + apply_style
├─ init.yaml                 # module metadata
└─ README.md                 # this file
```

## See also
- Temp Files Manager: create and clean temp directories used by other modules
- YAML Reading Core: read/write YAML files and configs you may log about