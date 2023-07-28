import random

i = 0
file = open("transaction.txt", "w")
while i <=500:
    amount = round(random.uniform(1.00, 1500.00), 2)

    transTypeDecider = random.randint(0, 1)
    if transTypeDecider == 0:
        transType = "Incoming"
    elif transTypeDecider == 1:
        transType = "Outgoing"

    dayNumber = random.randint(1, 31)
    if dayNumber < 10:
        dayNumber = "0" + f"{dayNumber}"
        dayNumber = str(dayNumber)
    else:
        dayNumber = str(dayNumber)

    accountNumber = str(random.randint(1, 25))

    finalString = f"({amount:.2f}, \'{transType}\', \'2021-12-{dayNumber}\', {accountNumber}),\n"
    file.write(finalString)
    i = i + 1
file.close()