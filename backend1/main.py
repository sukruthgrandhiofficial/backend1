import uvicorn
from fastapi import FastAPI
from backend1.routers.users import router as users_router
from backend1.routers.test import router as test_router

from backend1.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    openapi_url="/backend1/openapi.json",
    docs_url="/backend1/docs"
)

app.include_router(users_router)
app.include_router(test_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

