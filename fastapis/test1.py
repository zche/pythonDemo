from fastapi import FastAPI
import asyncio
import uvicorn 
from pydantic import BaseModel
from fastapi import FastAPI, File, Form, UploadFile
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED
from starlette.responses import JSONResponse,FileResponse
import time
import os
import tempfile
app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/async")
async def read_root():
    print('Started')
    await asyncio.sleep(5)
    print('Finished')
    return {"Hello": "World"}

@app.post("/train")
async def train(trainfile:str, imageName:str, imageVersion:str = Form('rasa_entity_baojie')):
    print(trainfile)
    print(imageName)
    print(imageVersion)
    fileTrain = File(trainfile)
    trainFilePath = os.path.join(tempfile.gettempdir(), "{fileName}.xlsx".format(fileName=str(time.time()).replace('.','')))
    with open(trainFilePath, "wb") as fileWrite:
        fileWrite.write(trainfile)
    return JSONResponse({"result":1,"message":"训练模型成功"})
uvicorn.run(app, host='0.0.0.0', port=8010,log_level="info")