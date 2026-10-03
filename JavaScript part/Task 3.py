const API_URL = 'https://fer-api.coderslab.pl/v1/be-exam/movies';

// Načtení dat z API
fetch(API_URL)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(movies => {
    // Zobrazení odpovědi v konzoli pro kontrolu struktury objektů
    console.log('Načtená data:', movies);

    // Vytvoření hlavního seznamu <ul> nebo nalezení existujícího containeru
    const ul = document.createElement('ul');

    // Procházení pole filmů pomocí cyklu
    movies.forEach(movie => {
      // Vytvoření prvků pro každý film
      const li = document.createElement('li');
      const h2 = document.createElement('h2');
      const h3 = document.createElement('h3');

      // Vložení textu (podle struktury objektu: title a year)
      h2.innerText = movie.title;
      h3.innerText = movie.year;

      // Sestavení struktury
      li.appendChild(h2);
      li.appendChild(h3);
      ul.appendChild(li);
    });

    // Vložení seznamu do těla dokumentu (body)
    document.body.appendChild(ul);
  })
  .catch(error => {
    console.error('Chyba při načítání dat:', error);
  });