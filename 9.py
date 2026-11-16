def bolish(a, b):
  assert isinstance(a, (int, float)) and isinstance(
      b, (int, float)
  ), "Qiymatlar son bo'lishi kerak"
  assert b != 0, "Nolga bo'lish mumkin emas"
  return a / b


try:
  son1 = float(input("Birinchi son: "))
  son2 = float(input("Ikkinchi son: "))
  natija = bolish(son1, son2)
  print("Natija:", natija)
except ValueError:
  print("Xatolik: Iltimos, faqat son kiriting.")
except (ZeroDivisionError, AssertionError):
  print("Xatolik: Nolga bo'lish mumkin emas.")

print("Dastur ishlashda davom etmoqda.")