def assign_severity(count):
    if count >= 5:
        return "High"
    elif count >= 3:
        return "Medium"
    else:
        return "Low"
