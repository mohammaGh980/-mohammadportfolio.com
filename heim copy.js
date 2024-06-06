// Teksten som skal animeres
const text = "Welcome to my portfolio";

// Henter HTML-elementet der teksten skal vises
const animatedTextElement = document.getElementById("animatedText");

// Funksjon for å animere tekst
function animateText() {
  let i = 0;

  // Funksjon for å legge til neste bokstav
  function addNextLetter() {
    if (i < text.length) {
      // Legger til neste bokstav i teksten
      animatedTextElement.textContent += text.charAt(i);
      i++;
      // Kaller funksjonen igjen etter 100ms
      setTimeout(addNextLetter, 100);
    } else {
      // Vent før du sletter teksten
      setTimeout(deleteText, 2000);
    }
  }

  // Funksjon for å slette teksten
  function deleteText() {
    const currentText = animatedTextElement.textContent;
    if (currentText.length > 0) {
      // Fjerner siste bokstav
      animatedTextElement.textContent = currentText.slice(0, -1);
      // Kaller funksjonen igjen etter 50ms
      setTimeout(deleteText, 50);
    } else {
      // Start skriveprosessen på nytt
      animateText();
    }
  }

  // Start animasjonen ved å legge til neste bokstav
  addNextLetter();
}

// Kaller funksjonen for å starte animasjonen
animateText();

// side bar :Funksjoner for å åpne og lukke sidebaren

// Åpner sidebaren
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

// Lukker sidebaren
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

// Funksjon for å oppdatere den digitale klokken
function updateClock() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  const currentTime = `${hours}:${minutes}:${seconds}`;
  // Oppdaterer klokkens innhold i HTML
  document.getElementById('clock').textContent = currentTime;
}

// Oppdater klokken hvert sekund
setInterval(updateClock, 1000);
// Initial kall for å vise klokken umiddelbart
updateClock();
