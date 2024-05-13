const text = "Welcome to my portfolio";
const animatedTextElement = document.getElementById("animatedText");

function animateText() {
  let i = 0;

  function addNextLetter() {
    if (i < text.length) {
      animatedTextElement.textContent += text.charAt(i);
      i++;
      setTimeout(addNextLetter, 100);
    } else {
      setTimeout(deleteText, 2000); // Vent før du sletter teksten
    }
  }

  function deleteText() {
    const currentText = animatedTextElement.textContent;
    if (currentText.length > 0) {
      animatedTextElement.textContent = currentText.slice(0, -1);
      setTimeout(deleteText, 50);
    } else {
      animateText(); // Start skriveprosessen på nytt
    }
  }

  addNextLetter();
}

animateText();



function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}