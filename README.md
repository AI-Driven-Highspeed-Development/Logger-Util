# ADHD Logger Utility

A simple, powerful logging solution that helps you track what's happening in your ADHD project. Get clear, organized logs without the complexity - just drop it in and start logging.

## Why Use This Logger?

- **Zero Setup Hassle**: Works immediately with sensible defaults
- **Stay Organized**: Keep logs from different parts of your app clearly separated
- **Debug Faster**: Quick verbose mode when you need to troubleshoot
- **Save Everything**: Automatically save logs to files when needed
- **Works Everywhere**: Use the same logger across your entire project
- **Flexible Output**: Log to console, files, or anywhere you need

## Getting Started in 30 Seconds

### Just Want to Log Something?

```python
from utils.logger import get_logger

logger = get_logger("MyModule")
logger.info("Hello, this works!")
logger.error("Something went wrong")
```

### Need More Detail While Debugging?

```python
from utils.logger import get_logger

# Turn on verbose mode - shows everything including debug messages
logger = get_logger("MyModule", verbose=True)
logger.debug("Now you'll see debug messages too")
```

### Want to Save Logs to a File?

```python
from utils.logger import LoggerFactory

logger = LoggerFactory.create_module_logger("MyModule", 
                                          verbose=True, 
                                          log_to_file=True)
logger.info("This will appear in console AND be saved to a file")
```

## Common Use Cases

### For New Components/Classes

When building a new part of your application:

```python
from utils.logger import LoggerFactory

class MyNewFeature:
    def __init__(self, debug_mode=False):
        self.logger = LoggerFactory.create_module_logger("MyNewFeature", 
                                                       verbose=debug_mode)
        self.logger.info("MyNewFeature is ready to go")
    
    def do_something(self):
        self.logger.debug("Starting to do something...")
        try:
            # Your code here
            self.logger.info("Task completed successfully")
        except Exception as e:
            self.logger.error(f"Oops, something failed: {e}")
```

### For Development vs Production

Development (see everything):
```python
logger = get_logger("MyApp", verbose=True)  # Shows debug messages
```

Production (important messages only):
```python
logger = get_logger("MyApp")  # Shows info, warning, error messages
```

### For Different Parts of Your App

```python
# Database operations
db_logger = get_logger("Database")
db_logger.info("Connected to database")

# API calls
api_logger = get_logger("APIClient") 
api_logger.debug("Making request to external service")

# File processing
file_logger = get_logger("FileProcessor")
file_logger.warning("Large file detected, processing may take time")
```

## What Gets Logged Where

### Console Output (Always On)
Clean, readable messages perfect for development:
```
2024-01-15 10:30:45 [MyModule] INFO: User logged in successfully
2024-01-15 10:30:46 [MyModule] ERROR: Failed to load user preferences
```

### File Output (When Enabled)
Detailed logs saved to `logs/` folder with technical details:
```
2024-01-15 10:30:45,123 - MyModule - INFO - user_manager.py:42 - login() - User logged in successfully
```

## Configuration Made Simple

### Log Levels (What Gets Shown)

- **DEBUG**: Everything - use when debugging (verbose=True)
- **INFO**: Normal operations - daily use
- **WARNING**: Potential problems - things to watch
- **ERROR**: Actual problems - needs attention
- **CRITICAL**: Serious failures - immediate action required

### Quick Settings

```python
# Most common: basic logging
logger = get_logger("MyModule")

# Development: see everything + save to file
logger = LoggerFactory.create_module_logger("MyModule", 
                                          verbose=True, 
                                          log_to_file=True)

# Custom file location
logger_instance = Logger(
    name="MyApp",
    verbose=True,
    log_to_file=True,
    log_file_path="my_custom_logs/app.log"
)
```

## Integration Examples

### Works Great with ConfigManager

```python
from managers.config_manager import ConfigManager

# ConfigManager automatically uses the logger
cm = ConfigManager(verbose=True)  # Will log in debug mode
```

### Adding to Existing Code

Replace print statements:
```python
# Instead of this:
print("Processing file:", filename)

# Do this:
logger = get_logger("FileProcessor")
logger.info(f"Processing file: {filename}")
```

## When Things Go Wrong

### Enable Debug Mode
```python
logger = get_logger("MyModule", verbose=True)
logger.debug("This will help you see what's happening")
```

### Check Your Log Files
Look in the `logs/` folder for detailed information.

### Test the Logger
```bash
cd utils/logger
python logger.py  # Shows example output
```

## Tips for Better Logging

1. **Give your loggers clear names**: Use your module/class name
2. **Use the right level**: INFO for normal stuff, ERROR for problems
3. **Add helpful details**: Include variables and context in messages
4. **Enable verbose mode when debugging**: You'll see much more detail
5. **Check log files**: Sometimes console messages get lost, files don't

## That's It!

The logger handles all the technical stuff automatically. Just create a logger, call the methods, and focus on building your application. Your logs will be consistent, organized, and helpful.
