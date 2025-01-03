import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Object of PdfReport that will hold filename attribute and generate() method which will
    generate pdf file containing information about flatmates and their amount to pay
    """
    def __init__(self,filename):
        self.filename = filename

    def generate_pdf(self, *flatemates, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image('./files/house.png',w=30,h=30)

        #Title
        pdf.set_font(family='Times', size = 36, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates bill', align='C', ln=1)

        #Header - info
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=50, h=50, align='R')
        pdf.cell(w=260, h=50, txt='Period',align='L')
        pdf.cell(w=0, h=50, txt='Total bill',align='L', ln=1)
        pdf.set_font(family='Times', size=16, style='U')
        pdf.cell(w=50, h=150, align='R')
        pdf.cell(w=260, h=25, txt=bill.period, align='')
        pdf.cell(w=0, h=25, txt=f'{bill.amount}$', align='', ln=1)
        pdf.cell(w=0, h=125, align='R', ln=1)

        #Body - header
        pdf.set_font(family='Times', size=36, style='B')
        pdf.cell(w=0, h=80, txt='Bill summary', align='C', ln=1)

        #Body - main | table columns
        pdf.set_font(family='Times', size=18,style='B')
        pdf.cell(w=25, h=25, align='R')
        pdf.cell(w=140, h=25, txt='Name', border=1, align='C')
        pdf.cell(w=200, h=25, txt='Amount of days', border=1, align='C')
        pdf.cell(w=140, h=25, txt='Total', border=1, align='C', ln=1)

        #Body - table rows
        pdf.set_font(family='Times', size=16)
        for flatemate in flatemates:
            indx = flatemates.index(flatemate)
            total_to_pay = flatemate.pay(bill, *flatemates[:indx] + flatemates[indx + 1:])
            pdf.cell(w=25, h=25, align='R')
            pdf.cell(w=140, h=25, txt= flatemate.name, border=1, align='C')
            pdf.cell(w=200, h=25, txt= str(flatemate.days_in_house), border=1, align='C')
            pdf.cell(w=140, h=25, txt=f'${total_to_pay:.2f}', border=1, align='C',ln=1)

        pdf.output(f'reports/{self.filename}')
        webbrowser.open('file://' + os.path.realpath(f'reports/{self.filename}'))
