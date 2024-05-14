from fastapi import FastAPI
import json, os
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def test():
    return {"message": "OK"}
