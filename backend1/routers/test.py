from fastapi import APIRouter, Depends
from backend1.auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/backend1",
)

@router.get("/hello_world")
async def hello_world():
    return {"message": "Hello World"}


@router.get("/test_authentication", dependencies=[Depends(JWTBearer())])
async def test_authentication():
    return {"message": "Authentication successfull"}
