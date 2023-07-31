class IceCreamShop:
    def __init__(self, vainilla, durazno, maracuya):
        self.vainilla = vainilla
        self.durazno = durazno
        self.maracuya = maracuya

    def expiration(self, current_day):
        if currentDay <= 29:
            if self.durazno > 0:
                return f"The product about to expire is: Durazno (remaining {self.durazno} units)"
            else:
                return "Durazno ice creams are sold out in the inventory."
        else:
            if self.vainilla > 0 and self.durazno > 0:
                return f"The products that will expire are: Vainilla and Durazno (remaining {self.vainilla} units of Vainilla and {self.durazno} units of Durazno)"
            elif self.vainilla > 0:
                return f"The product about to expire is: Vainilla (remaining {self.vainilla} units)"
            elif self.durazno > 0:
                return f"The product about to expire is: Durazno (remaining {self.durazno} units)"
            else:
                return "Durazno ice creams are sold out in the inventory."

vainilla_actual = int(input(">>>>Enter the quantity of Vainilla ice creams currently available.<<<< "))
durazno_actual = int(input(">>>>Enter the quantity of Durazno ice creams currently available.<<<< "))
maracuya_actual = int(input(">>>>Enter the quantity of Maracuyá ice creams currently available.<<<< "))

currentDay = int(input("Enter the current day to check for expiration date (numeric value): "))
if currentDay < 1 or currentDay > 30:
    print("Please enter a valid day (1 to 30).")
else:
    icecreamshop = IceCreamShop(vainilla_actual, durazno_actual, maracuya_actual)
    result = icecreamshop.expiration(currentDay)
    print(result)
