import json

with open("sozlamalar.json", "r", encoding="utf-8") as fayl:
  sozlamalar = json.load(fayl)

mavzu = input("Mavzu (light/dark): ").strip().lower()
bildirishnoma = input("Bildirishnoma (ha/yo‘q): ").strip().lower()

if mavzu in ("light", "dark"):
  sozlamalar["mavzu"] = mavzu

sozlamalar["bildirishnoma"] = bildirishnoma == "ha"

with open("sozlamalar.json", "w", encoding="utf-8") as fayl:
  json.dump(sozlamalar, fayl, indent=2, ensure_ascii=False)

print("Sozlamalar muvaffaqiyatli yangilandi.")