$.get('https://swapi-api.alx-tools.com/api/films/?format=json', ({ results }, status) => {
  if (status === 'success') {
    results.forEach(({ title }) => {
      $('UL#list_movies').append($('<li></li>').text(title));
    });
  }
});
