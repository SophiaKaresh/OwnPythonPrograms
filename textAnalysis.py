import string

def textAnalysis():
    print("Napiš libovolný text pro analýzu. Pro ukončení napiš prázdný řádek a stiskni Enter.")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    input_text = " ".join(lines)  # spojíme všechny řádky do jednoho textu


    text_clean = input_text.lower()  # malá písmena, ignorujeme velikost
    for znak in string.punctuation + "…":  # interpunkce + tři tečky
        text_clean = text_clean.replace(znak, "")
    text_clean = text_clean.replace(" ", "")


    number_of_symbols = len(text_clean)
    number_of_words = len(input_text.split())

 
    if text_clean:
        most_common_letter = max(set(text_clean), key=text_clean.count)
        least_frequent_letter = min(set(text_clean), key=text_clean.count)
    else:
        most_common_letter = least_frequent_letter = None

    print(f"""
Tvoje věta je: {input_text}

Celkový součet znaků bez mezer a interpunkce: {number_of_symbols}

Celkový počet slov: {number_of_words}

Nejčastější písmeno: {most_common_letter}

Nejméně časté písmeno: {least_frequent_letter}

Dííky, že jsi využil náš analyzátor textu! :)
""")

textAnalysis()

