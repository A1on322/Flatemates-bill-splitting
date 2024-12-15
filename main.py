from Flat import Bill, Flatmate
from report import PdfReport

amount, period = int(input('Enter amount of the bill: ')), input('Enter period of the bill like \'January 2024\': ')
bill = Bill(amount, period)

flatmates = {}
for i in range(int(input('Enter number of flatemates: '))):
    name = input(f'Enter name of the flatemate #{i+1}: ')
    n_days = int(input(f'Enter number of days {name} stayed in the house: '))
    flatmates['flatmate' + str(i+1)] = Flatmate(name, n_days)

new_pdf = PdfReport(bill.period + '.pdf')
new_pdf.generate_pdf(*flatmates.values(),bill = bill)