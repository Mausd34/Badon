"""Deterministic customer-support assistant suitable for demo/testing."""
FAQ = {
 "refund": "Refund requests are reviewed within 3-5 business days.",
 "password": "Use the password reset flow from the login page.",
 "order": "Please provide your order ID so support can check the status.",
 "hello": "Hello! How can I help you today?",
}

def reply(message: str) -> dict:
    text = (message or "").lower()
    for key, answer in FAQ.items():
        if key in text:
            return {"answer": answer, "intent": key, "confidence": 0.9}
    return {"answer": "I can help with orders, refunds, and password issues. Please describe your problem.", "intent": "fallback", "confidence": 0.5}
