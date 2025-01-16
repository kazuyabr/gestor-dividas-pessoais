from logging.config import dictConfig
import logging
from ..config.settings import settings
import os

def setup_logging():
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "format": "%(asctime)s %(name)s %(levelname)s %(message)s"
            },
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "access_file": {
                "class": "logging.FileHandler",
                "filename": os.path.join(settings.log_dir, "access.log"),
                "formatter": "json" if settings.log_format == "json" else "standard"
            },
            "error_file": {
                "class": "logging.FileHandler",
                "filename": os.path.join(settings.log_dir, "error.log"),
                "formatter": "json" if settings.log_format == "json" else "standard"
            }
        },
        "loggers": {
            "access": {
                "handlers": ["access_file"],
                "level": "INFO"
            },
            "error": {
                "handlers": ["error_file"],
                "level": "ERROR"
            }
        }
    }
    
    os.makedirs(settings.log_dir, exist_ok=True)
    logging.config.dictConfig(log_config) 