"""Logging utilities for VibeCoding."""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Final


_LOG_DIR: Final[Path] = Path("logs")


class JSONFormatter(logging.Formatter):
    """Format log records as JSON strings."""

    def format(self, record: logging.LogRecord) -> str:  # type: ignore[override]
        log_dict = {
            "timestamp": datetime.fromtimestamp(record.created, UTC).isoformat(),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_dict["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_dict)


def get_logger(name: str) -> logging.Logger:
    """Return a logger with JSON formatting and daily file rotation."""

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)
    _LOG_DIR.mkdir(exist_ok=True)
    log_file = _LOG_DIR / f"{datetime.now(UTC).date().isoformat()}.log"

    formatter = JSONFormatter()

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.propagate = False
    return logger
