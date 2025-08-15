# AI Driven Highspeed Development Framework Module — Logger Utility

## Overview
A centralized logging system with pluggable styles. Provides standard Python loggers configured with either a compact console format (default) or a normal verbose format, optional file logging, and a singleton “central logger” for quick global logging.

## Capabilities
- Pluggable console styles: compact (default) and normal
- Create named module loggers with optional verbose (DEBUG) mode
- Optional file logging with daily timestamped filenames
- Hierarchical child loggers (inherit handlers/style)
- Central logger singleton and convenience functions
- Runtime style switching for any logger
- ANSI color support in compact style (TTY-aware)

## Components
### Logger
Central controller that configures a standard `logging.Logger`.
- Source: [`utils.logger_util.logger.Logger`](utils/logger_util/logger.py)
- Key methods:
  - `get_logger(module_name: Optional[str] = None) -> logging.Logger`
  - `set_style(style: LoggerStyle) -> None`
  - `set_level(level: str) -> None`
  - `add_custom_handler(handler)`
  - `remove_all_handlers()`

### Styles
- [`utils.logger_util.logger_style.LoggerStyle`](utils/logger_util/logger_style.py): abstract base
- [`utils.logger_util.logger_style.NormalStyle`](utils/logger_util/logger_style.py): verbose console format
- [`utils.logger_util.compact_style.CompactStyle`](utils/logger_util/compact_style.py): compact console format (default), optional colors
- [`utils.logger_util.compact_style.apply_style`](utils/logger_util/compact_style.py): apply a style to a logger’s stream handlers (creates one if missing)

### Helpers
- [`utils.logger_util.logger.get_logger`](utils/logger_util/logger.py): quick logger factory (compact by default)
- [`utils.logger_util.logger.get_central_logger`](utils/logger_util/logger.py): singleton “CENTRAL” logger
- [`utils.logger_util.logger.set_logger_style`](utils/logger_util/logger.py): apply a style to an existing logger
- Convenience functions: [`log_debug`, `log_info`, `log_warning`, `log_error`, `log_critical`](utils/logger_util/logger.py)

## Lifecycle (How It Works)
1. Create or fetch a logger
   - `get_logger("MyModule", verbose=True)` returns a standard `logging.Logger` with compact style applied and level=DEBUG when verbose.
   - Internally, a stream handler is ensured and styled via `apply_style`.
2. Optional file logging
   - When using `Logger(..., log_to_file=True)`, a file handler with NormalStyle is added (console style unaffected).
3. Style management
   - Switch styles at runtime with `set_logger_style(logger, NormalStyle())` or via a `Logger` instance’s `set_style`.

## Quick Start
```python
from utils.logger_util.logger import get_logger, set_logger_style
from utils.logger_util.logger_style import NormalStyle
from utils.logger_util.compact_style import CompactStyle

# Compact by default
logger = get_logger("MyModule", verbose=True)
logger.debug("Debug in compact style")

# Switch to normal (verbose) style at runtime
set_logger_style(logger, NormalStyle())
logger.info("Now in normal style")

# Switch back to compact explicitly (optional colors auto-detected)
set_logger_style(logger, CompactStyle())
```

## Examples
### API Usage (code)
```python
from utils.logger_util.logger import (
    get_logger, get_central_logger, set_logger_style,
    log_info, log_error,
)
from utils.logger_util.logger_style import NormalStyle
from utils.logger_util.compact_style import CompactStyle

# 1) Module logger (compact by default)
log = get_logger("Database", verbose=True)
log.debug("Connected")
log.info("Ready")

# 2) Child logger (inherits style/handlers)
root = get_logger("App")
child = get_logger("App.Worker")  # same as logging.getLogger("App.Worker")
child.info("Child inherits the root style")

# 3) Switch style at runtime
set_logger_style(root, NormalStyle())
root.info("Now using normal style")

# 4) Central logger + convenience functions
central = get_central_logger(verbose=True)
central.debug("Central diagnostics")
log_info("Quick info via central logger")
log_error("Quick error via central logger")

# 5) File logging (normal formatter for files)
from utils.logger_util.logger import Logger
logger_instance = Logger(name="MyService", verbose=True, log_to_file=True)
svc = logger_instance.get_logger()
svc.info("Also logged to logs/MyService_YYYYMMDD.log")
```

## CLI and Regeneration
- No CLI or regeneration steps are required for this module.
- Console style is controlled programmatically. CompactStyle color can be toggled via environment:
  - `LOGGER_COLOR=0` to disable ANSI colors in compact mode
  - `LOGGER_COLOR=1` (default) to enable colors when TTY

## Module File Layout
- [`utils/logger_util/logger.py`](utils/logger_util/logger.py) — Core logger orchestration and helpers
- [`utils/logger_util/logger_style.py`](utils/logger_util/logger_style.py) — LoggerStyle base + NormalStyle
- [`utils/logger_util/compact_style.py`](utils/logger_util/compact_style.py) — CompactStyle + apply_style
- [`utils/logger_util/__init__.py`](utils/logger_util/__init__.py) — Package exports
- [`utils/logger_util/init.yaml`](utils/logger_util/init.yaml) — Module metadata
- [`utils/logger_util/agent_instruction.json`](utils/logger_util/agent_instruction.json) — Module agent info

## Implementation Notes
- `get_logger(name)` returns a standard `logging.Logger`; no custom subclassing
- Stream handler is created on demand by `apply_style` and reused
- Child loggers inherit handlers from their parent; avoid adding duplicate handlers
- File handler always uses NormalStyle (full context), independent of console style
- CompactStyle:
  - Format: `HH:MM:SS L Name: message` with 1-letter levels (D/I/W/E/C)
  - Truncates logger name to a configurable width (default 18)
  - Optional ANSI colors; enabled only on TTY by default

## Troubleshooting
- Duplicate messages: Ensure you don’t attach multiple handlers to the same logger
- No color output: Set `LOGGER_COLOR=1` and run in a TTY; some terminals/CI strip ANSI
- Missing logs in files: Check write permissions for `./logs/`
- Too verbose/noisy: Use `verbose=False` or call `logger.setLevel("INFO")`

## Warnings
- Excessive DEBUG logging impacts performance; keep verbose off in production
- Avoid manual handler proliferation on child loggers; rely on inheritance unless necessary

## Related Files
- Logs directory: `./logs/` (created on demand)

## Versioning & Maintenance
- Backward-compatible public helpers: `get_logger`, `set_logger_style`, `get_central_logger`
- Keep README in sync with code when adding new styles or helpers