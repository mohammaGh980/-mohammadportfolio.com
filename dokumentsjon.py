import turtle  # Importerer biblioteket for å tegne

# Tegn en blå plate som bakgrunn
def tegn_plate():
    turtle.penup()  # Løft pennen så den ikke tegner
    turtle.goto(-200, 300)  # Start i toppen av platen
    turtle.pendown()  # Sett pennen ned for å tegne
    turtle.fillcolor("blue")  # Velg blå farge
    turtle.begin_fill()  # Start å fylle med blå farge
    for _ in range(2):  # Tegn en rektangulær plate
        turtle.forward(400)  # Gå fremover 400 pixler
        turtle.right(90)  # Snu 90 grader til høyre
        turtle.forward(600)  # Gå fremover 600 pixler
        turtle.right(90)  # Snu 90 grader igjen
    turtle.end_fill()  # Fullfør fyllingen

# Tegn en firkantet enhet med tekst
def tegn_enhet(x, y, bredde, høyde, farge, tekst):
    turtle.penup()  # Løft pennen
    turtle.goto(x, y)  # Flytt til startposisjonen
    turtle.pendown()  # Sett pennen ned
    turtle.fillcolor(farge)  # Velg fyllfarge
    turtle.begin_fill()  # Start fyllingen
    for _ in range(2):  # Tegn en rektangulær enhet
        turtle.forward(bredde)  # Gå fremover
        turtle.right(90)  # Snu 90 grader
        turtle.forward(høyde)  # Gå fremover
        turtle.right(90)  # Snu igjen
    turtle.end_fill()  # Fullfør fyllingen
    turtle.penup()  # Løft pennen for å skrive tekst
    turtle.goto(x + bredde / 2, y - høyde - 10)  # Plasser teksten under enheten
    turtle.write(tekst, align="center", font=("Arial", 10, "bold"))  # Skriv tekst

# Tegn en rund enhet (sirkel) med tekst
def tegn_sirkel(x, y, radius, farge, tekst):
    turtle.penup()  # Løft pennen
    turtle.goto(x, y - radius)  # Flytt til toppen av sirkelen
    turtle.pendown()  # Sett pennen ned
    turtle.fillcolor(farge)  # Velg fyllfarge
    turtle.begin_fill()  # Start fyllingen
    turtle.circle(radius)  # Tegn en sirkel
    turtle.end_fill()  # Fullfør fyllingen
    turtle.penup()  # Løft pennen for å skrive tekst
    turtle.goto(x, y - radius - 20)  # Plasser teksten under sirkelen
    turtle.write(tekst, align="center", font=("Arial", 10, "bold"))  # Skriv tekst

# Tegn en kabel mellom to punkter
def tegn_kabel(fra_x, fra_y, til_x, til_y, farge="black"):
    turtle.penup()  # Løft pennen
    turtle.goto(fra_x, fra_y)  # Flytt til startpunktet
    turtle.pendown()  # Sett pennen ned for å tegne
    turtle.pensize(2)  # Sett tykkelsen på kabelen
    turtle.pencolor(farge)  # Velg fargen på kabelen
    turtle.goto(til_x, til_y)  # Tegn en rett linje til sluttpunktet
    turtle.penup()  # Løft pennen

# Tegn hele diagrammet
def tegn_diagram():
    tegn_plate()  # Tegn bakgrunnsplaten

    # Tegn enhetene
    tegn_enhet(-150, 150, 100, 50, "white", "USG")  # Tegn USG (Gateway)
    tegn_enhet(-30, 150, 150, 50, "gray", "Switch\nUS-8-60W")  # Tegn Switch
    tegn_sirkel(120, 250, 40, "white", "AP AC Pro")  # Tegn Access Point
    tegn_enhet(-70, -60, 100, 20, "black", "")  # Øvre strømkabel
    tegn_enhet(-70, -90, 100, 20, "black", "Strømkabel")  # Nedre strømkabel
    tegn_enhet(-180, -230, 100, 50, "white", "Kabelskytter")  # Tegn Kabelskytter

    # Tegn kabler mellom enhetene
    tegn_kabel(-150, 150, -30, 150)  # Koble USG til Switch
    tegn_kabel(-30, 150, 120, 250)  # Koble Switch til Access Point
    tegn_kabel(-150, 150, -70, -60)  # Koble USG til øvre strømkabel
    tegn_kabel(-30, 150, -70, -90)  # Koble Switch til nedre strømkabel
    tegn_kabel(-180, -230, -70, -60)  # Koble Kabelskytter til øvre strømkabel
    tegn_kabel(-180, -230, -70, -90)  # Koble Kabelskytter til nedre strømkabel

    turtle.done()  # Fullfør tegningen

# Kjør diagrammet
tegn_diagram()
