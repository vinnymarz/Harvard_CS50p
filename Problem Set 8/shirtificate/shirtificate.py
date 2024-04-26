from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", size = 50)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        # Use .epw to center image to page
        self._pdf.image("shirtificate.png", w=self._pdf.epw)

        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font("helvetica", "B", size = 25)
        # Use length of object to center x
        text_width = self._pdf.get_string_width(f"{name} took CS50")
        x_centered = (self._pdf.w - text_width) / 2
        self._pdf.text(x=x_centered, y=140, text=f"{name} took CS50")

    def save(self, filename):
        self._pdf.output(filename)


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
