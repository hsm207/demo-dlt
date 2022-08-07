from fastapi import FastAPI
from pydantic import BaseModel
from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          pipeline)


class Message(BaseModel):
    text: str


app = FastAPI()
classifier = {}


@app.on_event("startup")
async def init_model():
    tokenizer = AutoTokenizer.from_pretrained(
        "finiteautomata/bertweet-base-sentiment-analysis"
    )
    model = AutoModelForSequenceClassification.from_pretrained(
        "finiteautomata/bertweet-base-sentiment-analysis"
    )
    classifier["model"] = pipeline(
        task="text-classification", model=model, tokenizer=tokenizer
    )


@app.get("/", status_code=200)
def read_root():
    return "Hello from the model server!"


@app.post("/predict/")
async def classify_text(msg: Message):
    text = msg.text
    model = classifier["model"]
    result = model(text)
    
    return result[0]
