cost = int(input('what is cost '))
tax = cost * 0.05
tip = cost * 0.18
total = cost + tax + tip
print('tip is $%.2f tax is $%.2f total $%.2f' % (tip, tax, total))
