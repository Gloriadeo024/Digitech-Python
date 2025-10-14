mpesa_input = input("Enter the amount you want to withdraw: ")
mpesa_amount = int(mpesa_input)
def mpesa_withdraw(amount):
    if amount < 100:
        return "Minimum amount to withdraw is 100"
    elif amount > 70000:
        return "Maximum amount to withdraw is 70000"
    else:
        return f"You have successfully withdrawn {amount} Ksh"
result = mpesa_withdraw(mpesa_amount)
print(result)
