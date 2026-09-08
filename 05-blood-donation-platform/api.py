"""Blood donor matching helpers."""

def find_matches(donors: list[dict], blood_group: str, city: str = "") -> list[dict]:
    group = blood_group.upper().strip()
    city = city.lower().strip()
    return [d for d in donors if d.get("blood_group","").upper() == group and (not city or city in d.get("city","").lower()) and d.get("available", True)]
