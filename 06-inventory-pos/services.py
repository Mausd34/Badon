"""Inventory/POS business logic."""

def checkout(cart: list[dict], stock: dict[str,int]) -> dict:
    total = 0.0
    updated = stock.copy()
    for item in cart:
        sku, qty, price = item["sku"], int(item["qty"]), float(item["price"])
        if updated.get(sku, 0) < qty:
            raise ValueError(f"Insufficient stock for {sku}")
        updated[sku] -= qty
        total += qty * price
    return {"total": round(total, 2), "stock": updated}
