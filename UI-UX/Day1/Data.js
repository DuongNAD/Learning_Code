
const BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZTU5NzY0OTIyMGVmMjU2ZWI3YTNlNDAzNmM5N2QwZCIsIm5iZiI6MTYyNjA3ODM3MC4wNzUsInN1YiI6IjYwZWJmY2EyOTgyNGM4MDA1ZmYzZTdiNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zHDTNuMcM_YJLRGw_TlCu5LCJXqKmxtQ4Jy-AS1Wov4';

const API_URL = 'https://api.themoviedb.org/3/person/popular?language=en-US&page=1 ';

fetch(API_URL, {
  method: 'GET',
  headers: {
    Authorization: `Bearer ${BEARER_TOKEN}`,
    'Content-Type': 'application/json;charset=utf-8'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log('API Data:', data);

    if (data.results) {
      displayPeople(data.results);
    } else {
      console.log('No results found.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });

function displayPeople(people) {

  const container = document.getElementById('people-list');
  container.innerHTML = '';

  people.forEach(person => {
    const personDiv = document.createElement('div');
    personDiv.classList.add('person-item');

    const nameEl = document.createElement('h3');
    nameEl.textContent = person.name;

    const imgEl = document.createElement('img');
    if (person.profile_path) {

      imgEl.src = `https://image.tmdb.org/t/p/w200${person.profile_path}`;
      imgEl.alt = person.name;
    } else {
      imgEl.src = 'https://via.placeholder.com/200x300?text=No+Image';
      imgEl.alt = 'No Image';
    }

    personDiv.appendChild(imgEl);
    personDiv.appendChild(nameEl);

    container.appendChild(personDiv);
  });
}
