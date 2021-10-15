
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.encoders import jsonable_encoder

app = FastAPI()

from chatbot_graph import chat_bot
from pkg.api import E, DictMsg

class ReqAskGraphParams(BaseModel):
    content: str

@app.get("/")
def read_root():
    return {"version": "qa_medical_20210412"}

@app.post("/ask_graph/")
async def ask_graph(content: str):
    data, err = chat_bot.chat_main(content)
    if err != E.SUCCESS:
        return {"code": err, "content": DictMsg.get(err) or ''}
    elif data:
        return {"code": err, "content": data}
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)