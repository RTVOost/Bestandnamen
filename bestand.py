import os 
map = input("welke map moet het worden?")
bestandlijst = os.listdir(map)
print(f"je hebt deze gekozen: {map}")
print(f"deze bestanden staan in de map: {bestandlijst}")

with open("foto_namen.txt", "wt") as f:
    for bestand in bestandlijst:
        f.write(f"{bestand}\n")

print(f"bestanden uit '{map}' zijn opgeslagen")
    
for index, oude_naam in enumerate(bestandlijst, start=1):
    _, extensie = os.path.splitext(oude_naam)

    nieuwe_naam = f"Foto_{index:02}{extensie}"

    oud_pad = os.path.join(map, oude_naam)
    nieuw_pad = os.path.join(map, nieuwe_naam)

    os.rename(oud_pad, nieuw_pad)

    print("alles is hetnoemd.")



