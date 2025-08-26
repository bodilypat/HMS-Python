# backend/app/__init__.py

"""
    App Initialization for the Hotel Management System backend.
    Includes versioning and root logger setup.
"""
 import logging
 __version__ = "0.1.0"
 
 # Configure root logger
 logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    # App-level logger
    logger=logging.getLogger(__name__)
    logger.info("Hotel Management System backend initialized.")
    