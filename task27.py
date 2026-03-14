tugash = input("faly turni kiriting: ")
if tugash.endswith('.pdf'):
    print("True")
elif tugash.endswith('.txt'):
     print("True")
elif tugash.endswith('.docx'):
     print("True")
else:
     print("False")