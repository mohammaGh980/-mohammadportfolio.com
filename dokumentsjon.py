import turtle

def tegn_plate():
    """Tegn en blå stående plate."""
    turtle.penup()
    turtle.goto(-200, 300)  # Start øverst
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(400)  # Bredde på platen
        turtle.right(90)
        turtle.forward(600)  # Høyde på platen
        turtle.right(90)
    turtle.end_fill()

def tegn_enhet(x, y, bredde, høyde, farge, tekst):
    """Tegn en firkantet enhet med tekst under."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(farge)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(bredde)
        turtle.right(90)
        turtle.forward(høyde)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x + bredde / 2, y - høyde - 10)  # Flytt tekst under enheten
    turtle.write(tekst, align="center", font=("Arial", 10, "bold"))

def tegn_sirkel(x, y, radius, farge, tekst):
    """Tegn en sirkulær enhet med tekst under."""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(farge)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y - radius - 20)
    turtle.write(tekst, align="center", font=("Arial", 10, "bold"))

def tegn_kabel(fra_x, fra_y, til_x, til_y, buet=False, farge="black"):
    """Tegn en kabel mellom to punkter, med mulighet for buede linjer."""
    turtle.penup()
    turtle.goto(fra_x, fra_y)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor(farge)
    if buet:
        mid_x = (fra_x + til_x) / 2
        mid_y = (fra_y + til_y) / 2 + 50  # Lag en bue
        turtle.goto(mid_x, mid_y)
    turtle.goto(til_x, til_y)
    turtle.penup()

def tegn_diagram():
    # Tegn bakgrunnsplaten
    tegn_plate()

    # Plasser enheter
    tegn_enhet(-150, 150, 100, 50, "white", "USG")  # UniFi Security Gateway
    tegn_enhet(-30, 150, 150, 50, "gray", "Switch\nUS-8-60W")  # Switch
    tegn_sirkel(120, 250, 40, "white", "AP AC Pro")  # Access Point
    tegn_enhet(-70, -60, 100, 20, "black", "")  
    tegn_enhet(-70, -90, 100, 20, "black", "Strømkabel")  
    tegn_enhet(-180, -230, 100, 50, "white", "Kabelskytter")  # Kabelskytter

    # Koble sammen enhetene med kabler
    tegn_kabel(-150, 150, -30, 150)  # Koble USG til switchen
    tegn_kabel(-30, 150, 120, 250)  # Koble switchen til Access Point
    tegn_kabel(120, 250, -180, -230)  # Koble Access Point til Kabelskytter
    tegn_kabel(-150, 150, -70, -60)  # Strømkabel til USG
    tegn_kabel(-30, 150, -70, -90)   # Strømkabel til Switchen

    # Avslutt tegning
    turtle.done()

# Kjør funksjonen for å tegne diagrammet
tegn_diagram()
