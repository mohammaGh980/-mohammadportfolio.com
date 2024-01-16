function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }
  //søkefelte
  var games = [
    { title: "Om Meg", description: "", url: "about.html" },
    { title: "kontakt meg", description: "", url: "contactme.html" },
    { title: "mine fag ", description: "alle min fag", url: "subject.html" },
    { title: " Konseptutv og porgrammering", description: "Konseptutvikling og porgramering fag ", url: "porgrammering.html" },
    { title: "prod og historieforteling", description: "prod og historieforteling", url: "prodoghistorieforteling.html" },
    { title: "teknologi", description: "teknologi fage", url: "teknologi.html" },
    { title: "Guess the color code ", description: "gusse the collor code.", url: "colorcode.html" },
  ];
  
  // Søk etter spill basert på input
  function searchGames() {
    // Hent søkeord fra inputfeltet og trim det
    var searchQuery = document.getElementById('searchInput').value.trim().toLowerCase();
  
    // Filtrer spill basert på søketeksten
    var searchResults = games.filter(function (game) {
      return game.title.toLowerCase().includes(searchQuery) || game.description.toLowerCase().includes(searchQuery);
    });
  
    // Vis søkeresultatene på siden
    displaySearchResults(searchResults);
  }
  
  // Vis søkeresultatene på siden
  function displaySearchResults(results) {
    var resultContainer = document.getElementById('searchResult');
  
    // Tøm resultContainer før man legger til nye resultater
    resultContainer.innerHTML = '';
  
    // Vis resultater
    results.forEach(function (result) {
      var resultElement = document.createElement('div');
      resultElement.innerHTML = `<a href="${result.url}">${result.title}</a>`;
      resultContainer.appendChild(resultElement);
    });
  }