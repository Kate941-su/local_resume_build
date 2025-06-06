from fpdf import FPDF
from model.resume import ResumeData

class PDF(FPDF):

    def __init__(self, resume_data: ResumeData):
        self.resume_data = resume_data

    def header(self):
        # Rendering logo:
        self.image(self.resume_data.personal_info.image_path)
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