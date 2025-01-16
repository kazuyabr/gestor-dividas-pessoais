from logging.config import dictConfig
import logging
from ..config.settings import settings
import os

def setup_logging():
    # Garante que o diretório de logs existe
    os.makedirs(settings.log_dir, exist_ok=True)
    
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "format": "%(asctime)s %(name)s %(levelname)s %(message)s"
            },
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard" if settings.log_format == "standard" else "json",
                "level": settings.log_level,
            },
            "access_file": {
                "class": "logging.FileHandler",
                "filename": f"{settings.log_dir}/access.log",
                "formatter": "standard" if settings.log_format == "standard" else "json",
                "level": settings.log_level,
            },
            "error_file": {
                "class": "logging.FileHandler",
                "filename": f"{settings.log_dir}/error.log",
                "formatter": "standard" if settings.log_format == "standard" else "json",
                "level": "ERROR",
            }
        },
        "loggers": {
            "access": {
                "handlers": ["console", "access_file"] if settings.enable_access_logs else ["console"],
                "level": settings.log_level,
                "propagate": True
            },
            "error": {
                "handlers": ["console", "error_file"] if settings.enable_error_logs else ["console"],
                "level": "ERROR",
                "propagate": True
            }
        },
        "root": {
            "level": settings.log_level,
            "handlers": ["console"]
        }
    }
    dictConfig(log_config) 