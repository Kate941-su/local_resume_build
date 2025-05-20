from pdf.test import PDF
from model.resume import Resume
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# pdf = PDF()
# pdf.add_page()
# pdf.set_font("Times", size=12)
# for i in range(1, 41):
#     pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
# pdf.output("test.pdf")

with open("sample.yaml", "r") as file:
    config = yaml.safe_load(file)
print(config)