connect = True
while connect == True:
    try:
        number = float(input("Kerekli sonni kiriting: "))
        prosent = float(input("Foyizni kiriting: "))
        finish = number / 100 * prosent
        print(finish)
    except ValueError:
        print("Siz string kirityapsiz. Kerakli amalni kiriting")