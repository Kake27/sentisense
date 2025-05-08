from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import analyse, clustering, getcsv, graphs, solutions, status

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

app.include_router(analyse.router)
app.include_router(getcsv.router)
app.include_router(solutions.router)
app.include_router(graphs.router)
app.include_router(clustering.router)
app.include_router(status.router)

@app.get("/")
async def root():
    return {"message": "Server Running"}
