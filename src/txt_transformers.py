from utils import to_mnx, clean_str

raw = [
    {"name": "    ana    ", "active": True, "cash": "120.50"},
    {"name": "LUIS", "active": False, "cash": "0"},
    {"name": "    MaRiA    ", "active": True, "cash": "99.99"}
]

def clean(row: dict) -> dict:
    return {
        "name": clean_str(row["name"]),
        "active": bool(row["active"]),
        "cash_mnx": to_mnx(row["cash"])
    }

# list comprehesion
clean_list = [clean(r) for r in raw if row["active"] == True]

print(f"\n\n lista original: \n{raw}")
print(f"\n\n lista normalizada: \n{clean_list}")