from fastapi import FastAPI
from app.database import engine, Base
from app.routers import metrics, alerts, health

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cloud Infrastructure Monitor",
    description="Real-time monitoring and alerting system for cloud infrastructure",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(metrics.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "Cloud Monitor API is running", "docs": "/docs"}