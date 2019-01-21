monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12
while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance    
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)

