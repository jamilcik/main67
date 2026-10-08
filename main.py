class Park:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.atraksionlar = []

    def atraksion_qoshish(self, atraksion):
        self.atraksionlar.append(atraksion)

    def malumot(self):
        print("Park nomi:", self.nomi)
        print("Manzil:", self.manzil)
        print("Atraksionlar:", self.atraksionlar)


# O'zgaruvchi yaratamiz
park = Park("Navro'z Bog'i", "Toshkent")

# Atraksionlar qo'shamiz
park.atraksion_qoshish("Aylana charx")
park.atraksion_qoshish("Amerikacha tepaliklar")
park.atraksion_qoshish("Avtodrom")

# Ma'lumotlarni ekranga chiqaramiz
park.malumot()
