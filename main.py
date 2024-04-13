from fastapi import FastAPI
from routes.users import user_router

import uvicorn

app = FastAPI()
app.include_router(user_router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1" , port=8000, reload=True)
