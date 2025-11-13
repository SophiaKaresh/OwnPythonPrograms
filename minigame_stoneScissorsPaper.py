import random

def stoneScissorsPaper():
    player_won = "\n--> Vyhráváš!! :)"
    computer_won = "\n--> Vyhrává počítač!"

    # smyčka, dokud hráč nezadá správný tah
    while True:
        players_turn = input("Zadej svůj tah (kámen, nůžky, papír): ").lower()
        # odstraníme diakritiku pro zjednodušení
        players_turn = players_turn.replace("á","a").replace("ů","u").replace("ž","z").replace("í","i")

        if players_turn not in ["kamen","nuzky","papir"]:
            print("\nNezadal si ani jedno z kámen, nůžky, papír. Zkus to znovu.\n")
            continue  
        else:
            break 

    print(f"\nTy jsi zvolil: {players_turn}")

    computers_turn = random.choice(["kamen","nuzky","papir"])
    print(f"Počítač zvolil: {computers_turn}")

    if players_turn == computers_turn:
        print("Remízaa!")
    
    elif (players_turn == "kamen" and computers_turn == "nuzky") or \
         (players_turn == "nuzky" and computers_turn == "papir") or \
         (players_turn == "papir" and computers_turn == "kamen"):
        print(player_won)
    
    else:
        print(computer_won)

stoneScissorsPaper()
