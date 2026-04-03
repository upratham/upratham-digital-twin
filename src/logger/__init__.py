import logging
from pathlib import Path

_LOGGER = None

def get_logger(name: str = "app") -> logging.Logger:
    global _LOGGER
    if _LOGGER is not None:
        return logging.getLogger(name)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "app.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    _LOGGER = logging.getLogger(name)
    return _LOGGER