def currencyConversion():
    course = {"EUR": 25.3, "USD": 23.8, "GBP": 29.4, "CZK": 1}
    print("Dobrý den, děkujeme, že využíváte náš převodník měn.\nAktuální kurzy jsou: {course}")
    
    alternative_inputs = {
        "EURO": "EUR", "EURA": "EUR",
        "DOLARY": "USD", "DOLÁKY": "USD", "AMERICKÝ DOLARY": "USD",
        "LIBRA": "GBP", "LIBRÁKY": "GBP", "BRITSKÁ LIBRA": "GBP",
        "KORUNY": "CZK", "KORUNA": "CZK", "KČ": "CZK"
    }

    input_amount = float(input("\nZadejte částku k převodu: "))
    input_from = input("\nVyberte z jaké měny chcete převádět (CZK, EUR, USD, GBP): ").upper()
    input_to = input("\nNa jakou měnu si přejete převést (CZK, EUR, USD, GBP): ").upper()

    input_from = alternative_inputs.get(input_from, input_from)
    input_to = alternative_inputs.get(input_to, input_to)

    if input_from not in course or input_to not in course:
        print("\nJe nám líto...Tento druh měny zatím neumíme :( ")
        return

   
    czk = input_amount * course[input_from]
    result = czk / course[input_to]

    print(f"{input_amount} {input_from} = {result:.2f} {input_to}")

currencyConversion()
