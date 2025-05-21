import os
from fpdf import FPDF
from PIL import Image

def jpgs_naar_pdf(source_map, output_pad):
    pdf = FPDF(unit="pt")  

   
    bestanden = sorted([
        f for f in os.listdir(source_map)
        if f.lower().endswith('.jpg')
    ])

    if not bestanden:
        print("Geen JPG-bestanden gevonden.")
        return

    for bestand in bestanden:
        pad = os.path.join(source_map, bestand)
        image = Image.open(pad)
        breedte, hoogte = image.size

        
        pdf.add_page(format=(breedte, hoogte))
        pdf.image(pad, x=0, y=0, w=breedte, h=hoogte)

    pdf.output(output_pad)
    print(f"PDF opgeslagen als: {output_pad}")


if __name__ == "__main__":
    source = input("Geef het pad naar de map met JPG-afbeeldingen: ").strip('"')
    output = input("Geef het pad + bestandsnaam voor de PDF (bijv. output.pdf): ").strip('"')
    jpgs_naar_pdf(source, output)