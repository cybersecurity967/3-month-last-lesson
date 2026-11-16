import matplotlib.pyplot as plt

oylar = ["Yan", "Fev", "Mar", "Apr", "May", "Iyun"]
daromad = [12, 15, 11, 19, 22, 18]

kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
savdo = [35, 20, 45]

buyurtma_qiymatlari = [50, 75, 80, 120, 150, 150, 180, 220, 250, 300]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(oylar, daromad, marker="o", color="royalblue", linewidth=2)
axes[0].set_title("Oylik daromad dinamikasi")
axes[0].set_xlabel("Oylar")
axes[0].set_ylabel("Daromad (mln so'm)")
axes[0].grid(True, linestyle="--", alpha=0.5)

axes[1].bar(kategoriyalar, savdo, color=["teal", "coral", "goldenrod"])
axes[1].set_title("Kategoriyalar savdosi")
axes[1].set_xlabel("Kategoriyalar")
axes[1].set_ylabel("Sotilgan soni (dona)")

axes[2].hist(buyurtma_qiymatlari, bins=5, color="slateblue", edgecolor="black")
axes[2].set_title("Buyurtma qiymatlari taqsimoti")
axes[2].set_xlabel("Buyurtma qiymati (ming so‘m)")
axes[2].set_ylabel("Buyurtmalar soni")

plt.tight_layout()
plt.show()