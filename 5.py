tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

barchasida = tadbir_1 & tadbir_2 & tadbir_3

faqat_1 = tadbir_1 - (tadbir_2 | tadbir_3)
faqat_2 = tadbir_2 - (tadbir_1 | tadbir_3)
faqat_3 = tadbir_3 - (tadbir_1 | tadbir_2)
faqat_bittasida = faqat_1 | faqat_2 | faqat_3

kamida_ikkitasida = (
    (tadbir_1 & tadbir_2) | (tadbir_1 & tadbir_3) | (tadbir_2 & tadbir_3)
)

print(f"Barcha tadbirlarda: {', '.join(barchasida)}")
print(f"Faqat bitta tadbirda: {', '.join(faqat_bittasida)}")
print(f"Kamida ikkitasida: {', '.join(kamida_ikkitasida)}")