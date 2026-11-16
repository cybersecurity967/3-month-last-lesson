import math


def masofa_hisobla(nuqta1, nuqta2):
  x1, y1 = nuqta1
  x2, y2 = nuqta2
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


shaharlar = {"A": (0, 0), "B": (3, 4), "C": (6, 0)}
nomlar = list(shaharlar.keys())

eng_uzoq_juftlik = ""
maks_masofa = 0

for i in range(len(nomlar)):
  for j in range(i + 1, len(nomlar)):
    s1, s2 = nomlar[i], nomlar[j]
    d = masofa_hisobla(shaharlar[s1], shaharlar[s2])
    print(f"{s1} va {s2}: {d:.1f}")
    if d > maks_masofa:
      maks_masofa = d
      eng_uzoq_juftlik = f"{s1} — {s2}"

print(f"Eng uzoq yo‘nalish: {eng_uzoq_juftlik} ({maks_masofa:.1f})")