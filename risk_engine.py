def calculate_risk(total_alerts):
    if total_alerts >= 10:
        return "HIGH"
    elif total_alerts >= 5:
        return "MEDIUM"
    else:
        return "LOW"
