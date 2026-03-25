from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MetricCreate(BaseModel):
    service_name: str
    metric_type: str
    value: float
    unit: str

class MetricResponse(MetricCreate):
    id: int
    timestamp: datetime
    class Config:
        from_attributes = True

class AlertCreate(BaseModel):
    service_name: str
    alert_type: str
    message: str
    severity: str

class AlertResponse(AlertCreate):
    id: int
    is_resolved: bool
    created_at: datetime
    resolved_at: Optional[datetime]
    class Config:
        from_attributes = True

class ServiceCreate(BaseModel):
    name: str
    url: str

class ServiceResponse(ServiceCreate):
    id: int
    is_active: bool
    created_at: datetime
    class Config:
        from_attributes = True