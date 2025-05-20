from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        # self.image("image/sample.jpg", 10, 8, 33)
        self.image("https://farm9.staticflickr.com/8295/8007075227_dc958c1fe6_z_d.jpg", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="I", size=8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")