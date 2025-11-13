import random
import string
def passwordGenerator():
    password_length = int(input("Zadej délku hesla: "))
    symbols = string.ascii_letters + string.digits + string.punctuation
    password ="".join(random.choice(symbols) for i in range(password_length))
    print("Bylo vybíráno z těchto znaků:\n", symbols)
    print("Požadovaná délka hesla byla: ", password_length)
    print("Vygenerované heslo:",password)
passwordGenerator()
