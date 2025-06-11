from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from vibecoding.logging import get_logger


def test_get_logger_creates_json_log(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    logger = get_logger("test")
    logger.info("hello")
    for handler in logger.handlers:
        handler.flush()

    log_file = Path("logs") / f"{date.today().isoformat()}.log"
    assert log_file.exists()
    line = log_file.read_text().splitlines()[0]
    entry = json.loads(line)
    assert entry["message"] == "hello"
    assert entry["level"] == "INFO"
    assert entry["name"] == "test"


def test_get_logger_idempotent(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    logger1 = get_logger("test")
    handlers = list(logger1.handlers)
    logger2 = get_logger("test")
    assert logger1 is logger2
    assert logger2.handlers == handlers
