import sys
import json
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Add current dir to sys.path
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

from ai_engine import RecallAIEngine

app = FastAPI(title="VLearn Recall AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = RecallAIEngine()

class QueryRequest(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
def get_home():
    html_file = current_dir / "index.html"
    if html_file.exists():
        with open(html_file, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>VLearn Recall Backend Running</h1>"

@app.post("/api/recall")
def recall_endpoint(req: QueryRequest):
    query_text = req.query.strip()
    if not query_text:
        return JSONResponse(status_code=400, content={"error": "Empty query"})
    
    result = engine.process_query(query_text)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
