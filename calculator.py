while True:
    begin = input("Welcome to the pay calculator. Type 'start' to begin or 'quit' to quit.")
    if begin == "quit":
        break
    elif begin == "start":
        hoursWorked = int(input("How many hours have you worked?"))
        hourlyPay = int(input("What is your hourly pay?"))
        if hoursWorked > 40:  
            overtimePay = (hoursWorked - 40) * (hourlyPay * 1.5)
            regularPay = 40 * hourlyPay
            totalPay = overtimePay + regularPay
            print(f"You're being paid {totalPay}!")
        elif hoursWorked <= 40:
            totalPay = hoursWorked * hourlyPay
            print(f"You're being paid {totalPay}!")
    else:
        print("Listen to me.")
