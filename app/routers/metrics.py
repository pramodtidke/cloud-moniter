from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Metric
from app.schemas import MetricCreate, MetricResponse

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.post("/", response_model=MetricResponse)
def create_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    db_metric = Metric(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

@router.get("/", response_model=List[MetricResponse])
def get_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Metric).offset(skip).limit(limit).all()

@router.get("/{service_name}", response_model=List[MetricResponse])
def get_metrics_by_service(service_name: str, db: Session = Depends(get_db)):
    metrics = db.query(Metric).filter(Metric.service_name == service_name).all()
    if not metrics:
        raise HTTPException(status_code=404, detail="No metrics found for this service")
    return metrics