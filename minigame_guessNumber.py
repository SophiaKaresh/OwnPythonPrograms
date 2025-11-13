##Minihra uhádni číslo! 

def guessNumber():
    import random
    random_number= random.randint(1,50)
    number_of_attempts = 0
    while True:
        try:
            input_guess = int(input("\nHádej náhodné číslo od 1-50!:) : "))
        except ValueError:
            print("Zadej celé číslo.")
            continue
        
        number_of_attempts += 1

        if input_guess == random_number:
            print(f"\nAnoooo! Uhodnul si! Náhodné číslo je {random_number}\nPočet pokusů byl: {number_of_attempts}")
            break
        elif input_guess > random_number:
            print("\nAjaj, tohle číslo to není. Ale dám ti menší hint! Tvoje číslo je větší než to, které vygeneroval počítač.")
        elif input_guess < random_number:
            print("\nToto číslo není správné. Malý hint jako bonus ode mě  - vygenerované číslo počítačem je větší než to co jsi napsal.")


        if number_of_attempts == 10:
            print(f"\nBohužel bylo jen 10 pokusů a ty si vyčerpal:( Nevadí! Příště to vyjde!\nSprávné číslo bylo: {random_number}")
            break
guessNumber()
