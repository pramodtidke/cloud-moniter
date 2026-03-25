THRESHOLDS = {
    "cpu": {"medium": 70, "high": 85, "critical": 95},
    "memory": {"medium": 75, "high": 88, "critical": 95},
    "disk": {"medium": 80, "high": 90, "critical": 95},
}

def check_threshold(metric_type: str, value: float, service_name: str):
    thresholds = THRESHOLDS.get(metric_type)
    if not thresholds:
        return None

    severity = None
    if value >= thresholds["critical"]:
        severity = "critical"
    elif value >= thresholds["high"]:
        severity = "high"
    elif value >= thresholds["medium"]:
        severity = "medium"

    if severity:
        return {
            "service_name": service_name,
            "alert_type": f"{metric_type}_threshold",
            "message": f"{metric_type.upper()} usage is {value}% on {service_name}",
            "severity": severity,
        }
    return None