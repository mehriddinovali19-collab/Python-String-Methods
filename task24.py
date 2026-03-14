email = input('email kiriting: ')

if not email.startswith("@") and email.endswith(".com"):
    print("email qabul qilindi")
else:
    print("emailda xatolik bor!")