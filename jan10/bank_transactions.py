min_bal = 500
amt = int(input("Enter the amount to withdraw : "))
balance = 10000
if amt<balance:
    print("Your aavailable balance is ",balance-amt)
elif amt>balance:
    print("Insufficient balance")
elif balance <500:
    print("your account balance is ",balance," Please  keep your account balance above Rs.500 to avoid unwanted charges.")
