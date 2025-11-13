##Zjištění dne v týdnu
def dayOfWeek ():
    import datetime 
    input_date = input("Zadejte datum ve formátu RRRR-MM-DD: ")
    day = datetime.datetime.strptime(input_date, "%Y-%m-%d").weekday()

    days = {0:"Pondělí",1:"Úterý",2:"Středa",3:"Čtvrtek",4:"Pátek",5:"Sobota",6:"Neděle"}

    print(f"Zadané datum bylo: {input_date} \nTento den je {days[day]}")
dayOfWeek()
