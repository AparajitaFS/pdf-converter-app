from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100) #gray color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) # ln is new line
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    #add breakline
    pdf.ln(265)
    # Set the footer
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    # Adding multiple pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# pdf.set_font(family="Times", style="B", size=10)
# pdf.cell(w=0, h=12, txt="Hi there", align="L", ln=1, border=1)

pdf.output("output.pdf")