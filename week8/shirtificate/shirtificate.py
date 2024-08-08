from fpdf import FPDF


name=input('Name: ')
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica",'', 43)
pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.image("shirtificate.png",h=pdf.epw, w=pdf.epw)
pdf.set_font_size(26)
pdf.set_text_color(255,255,255)
pdf.text(x=55, y=140, text=f'{name} took CS50')



pdf.output("shirtificate.pdf")
