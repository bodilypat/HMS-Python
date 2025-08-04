# run.py

import uvicorn
from app.config.setting import settings

if __name__=='__main__":
	nvicorn.run(
		"app.main:app",
		host=settings.APP_HOST,
		port=settings.APP_PORT,
		reload=settings.APP_ENV == "development",
		log_level="Info"
	)
	