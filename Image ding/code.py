import os
from PIL import Image

# Ondersteunde extensies
AFBEELDING_EXTENSIES = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']

def is_afbeelding(bestandsnaam):
    _, ext = os.path.splitext(bestandsnaam)
    return ext.lower() in AFBEELDING_EXTENSIES

def resize_afbeelding(input_pad, output_pad, max_formaat):
    with Image.open(input_pad) as img:
        img.thumbnail((max_formaat, max_formaat))
        img.save(output_pad)

def main():
    bronmap = input("Geef het pad naar de bronmap met afbeeldingen: ").strip('"')
    doelmap = input("Geef het pad naar de doelmap: ").strip('"')
    max_formaat = int(input("Wat is de maximale grootte (in pixels, max 2000)? "))

    if max_formaat > 2000:
        print("Maximale grootte mag niet groter zijn dan 2000 pixels.")
        return

    if not os.path.exists(doelmap):
        os.makedirs(doelmap)

    bestanden = os.listdir(bronmap)
    totaal = 0
    overgeslagen = 0

    print(f"\nAantal gevonden bestanden in '{bronmap}': {len(bestanden)}\n")

    for bestand in bestanden:
        bron_bestand = os.path.join(bronmap, bestand)

        if not is_afbeelding(bestand):
            print(f"[OVERGESLAGEN] '{bestand}' is geen afbeelding.")
            overgeslagen += 1
            continue

        doel_bestand = os.path.join(doelmap, bestand)
        try:
            resize_afbeelding(bron_bestand, doel_bestand, max_formaat)
            print(f"[AANGEPAST] '{bestand}' opgeslagen.")
            totaal += 1
        except Exception as e:
            print(f"[FOUT] '{bestand}' kon niet worden aangepast. ({e})")

    print(f"\nKlaar! {totaal} afbeelding(en) aangepast en opgeslagen in '{doelmap}'.")
    print(f"{overgeslagen} bestand(en) overgeslagen.\n")

if __name__ == "__main__":
    main()
