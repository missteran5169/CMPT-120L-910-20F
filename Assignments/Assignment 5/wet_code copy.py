# We're looking to find out how much money we have after a day with friends on Saturday. 
# Our code does the trick but we learned about keeping out code DRY recently and want to make it more efficent by making it DRY.
# I want you to accomplish this by making functions where you see repeated code. 
# Some things to note. When we have a positive number that gets split up and 85% goes into checking and 15% goes into savings. 
# All negative numbers gets taken out of the checking account.


def saturdays_bank_transactions(transations) -> (float, float):
    savings = 1096.25
    checking = 1590.80

if __name__ == "__main__":
    transations = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transations)

a == 0
b == -1
if transations[0:] > a:
    checking += (transations[0] * 0.85)
    savings += (transations[0] * 0.15) 
    return checking
else:
    return savings

print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\n", "Your new savings balance is:", '${:.2f}'.format(round(new_balance[1], 2)))