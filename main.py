import random

def wichteln_teilnehmer_aus_liste():
    teilnehmer = [
        "Florian",
        "Markus",
        "Claudia",
        "Jenny",
        "Jue",
        "Christian",
        "Rosi",
        "Heike",
        "Helmut",
        "Günther",
        # Füge hier weitere Teilnehmer hinzu
    ]
    return teilnehmer

def wichteln_paarungen_erstellen(teilnehmer):
    paare = list(zip(teilnehmer, teilnehmer[1:] + [teilnehmer[0]]))
    random.shuffle(paare)
    return paare

def wichteln_paarungen_in_textdatei_speichern(paare, dateiname='wichtel_paarungen.txt'):
    with open(dateiname, 'w') as file:
        for schenker, beschenkter in paare:
            file.write(f"{schenker} beschenkt {beschenkter}\n")

if __name__ == "__main__":
    print("Willkommen beim Wichteln Programm!")

    teilnehmer = wichteln_teilnehmer_aus_liste()

    if len(teilnehmer) < 2:
        print("Es müssen mindestens zwei Teilnehmer vorhanden sein.")
    else:
        paarungen = wichteln_paarungen_erstellen(teilnehmer)
        wichteln_paarungen_in_textdatei_speichern(paarungen)
        print("Die Paarungen wurden erfolgreich erstellt und in 'wichtel_paarungen.txt' gespeichert.")
