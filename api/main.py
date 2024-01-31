# Import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api.routes as routes
from api.config import settings

origins = [
    "*", # Allow all origins
]

app = FastAPI(
    title=settings.swagger_title, description = settings.swagger_description,
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.default_router, include_in_schema=False)
app.include_router(routes.mongo_router, tags=["Mongo management"],
                   prefix="/mongo")
app.include_router(routes.stats_router, tags=["Statistics"], prefix="/stats")
app.include_router(routes.minio_router, tags=["MinIO Operations"], prefix="/minio")
