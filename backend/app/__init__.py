# backend/app/__init__.py
 import logging
 __version__ = "0.1.0"
 
 # Set up a root logger(optional)
 logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logger=logging.getLogger(__name__)
    logger.info("Hotel Management System backend initialized.")
    