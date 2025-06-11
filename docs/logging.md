# Logging utility

The `vibecoding.logging.get_logger` function provides a preconfigured logger.
It formats messages as JSON and writes them to the `logs/` directory, one file
per day. The same JSON lines are also printed to standard output.

## Usage

```python
from vibecoding.logging import get_logger

logger = get_logger(__name__)
logger.info("Application started")
```
