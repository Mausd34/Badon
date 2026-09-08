"""Simple, explainable fraud-risk scoring API logic."""

def risk_score(amount: float, velocity: int, foreign: bool = False, new_device: bool = False) -> dict:
    score = 0
    reasons = []
    if amount >= 1000: score += 30; reasons.append("high transaction amount")
    if velocity >= 5: score += 30; reasons.append("high transaction velocity")
    if foreign: score += 20; reasons.append("foreign transaction")
    if new_device: score += 20; reasons.append("new device")
    return {"risk_score": min(score,100), "is_high_risk": score >= 60, "reasons": reasons}
