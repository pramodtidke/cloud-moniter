import psutil
import httpx
from datetime import datetime

def collect_system_metrics(service_name: str = "local"):
    return [
        {"service_name": service_name, "metric_type": "cpu", "value": psutil.cpu_percent(interval=1), "unit": "%"},
        {"service_name": service_name, "metric_type": "memory", "value": psutil.virtual_memory().percent, "unit": "%"},
        {"service_name": service_name, "metric_type": "disk", "value": psutil.disk_usage('/').percent, "unit": "%"},
    ]

async def check_service_health(url: str):
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            return {"status": "up", "response_time": response.elapsed.total_seconds() * 1000}
    except Exception as e:
        return {"status": "down", "error": str(e)}