$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', ({ name }, status) => {
  if (status === 'success') {
    $('#character').text(name);
  }
});
