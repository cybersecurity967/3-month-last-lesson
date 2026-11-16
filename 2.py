buyurtmalar = [
    {"mahsulot": "Kitob", "narx": 45000, "miqdor": 2},
    {"mahsulot": "Ruchka", "narx": 5000, "miqdor": 10},
    {"mahsulot": "Sumka", "narx": 180000, "miqdor": 1},
]

eng_qimmat_nom = ""
eng_qimmat_summa = 0

for b in buyurtmalar:
  qiymat = b["narx"] * b["miqdor"]
  print(f"{b['mahsulot']}: {qiymat} so‘m")
  if qiymat > eng_qimmat_summa:
    eng_qimmat_summa = qiymat
    eng_qimmat_nom = b["mahsulot"]

print(f"Eng qimmat buyurtma: {eng_qimmat_nom} — {eng_qimmat_summa} so‘m")