from pathlib import Path

Bpath=Path(__file__)
print(f"Bpath : {Bpath}")

Bpath2=Path(__file__).resolve().parent
print(f"Bpath2 : {Bpath2}")