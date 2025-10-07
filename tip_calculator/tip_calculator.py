while True:
    try:
        bill_amount = float(input('Enter the total amount: '))
        break
    except ValueError:
        print('Incorrect value entered. Please enter numbers only.')

while True:
    try:
        tip_percentage = float(input('Enter the tip percentage: '))
        break
    except ValueError:
        print('Incorrect value entered. Please enter numbers only.')

tip = (tip_percentage / 100) * bill_amount
total = bill_amount + tip
print(
    f'Bill: {bill_amount:.2f}\n'
    f'Tip: {tip:.2f}\n'
    f'Total: {total:.2f}'
)
