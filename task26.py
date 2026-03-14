username = input("Username kiriting: ")

# '-' ni olib tashlab, faqat harf va raqamligini tekshiramiz
result = username.replace("-", "").isalnum()

print(result)