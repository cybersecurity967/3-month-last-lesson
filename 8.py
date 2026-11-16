fayllar = [
    "Hisobot 2026.pdf",
    "profil rasmi.jpg",
    "video.mp4",
    "jadval.xlsx",
    "diagramma.png",
]
ruxsat_etilgan = (".pdf", ".jpg", ".png")

yaroqli = []
yaroqsiz = []

for fayl in fayllar:
  if fayl.lower().endswith(ruxsat_etilgan):
    yaroqli.append(fayl.replace(" ", "_"))
  else:
    yaroqsiz.append(fayl)

print("Yaroqli:")
for f in yaroqli:
  print(f)

print("\nYaroqsiz:")
for f in yaroqsiz:
  print(f)