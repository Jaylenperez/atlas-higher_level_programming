// Ensure the script runs only after the DOM is fully loaded
$(document).ready(function () {
  // Fetch data from the provided URL
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    // Iterate over each movie in the response
    data.results.forEach(function (movie) {
      // Create a new <li> element with the movie title
      const listItem = $('<li></li>').text(movie.title);
      // Append the new <li> element to the UL with id 'list_movies'
      $('#list_movies').append(listItem);
    });
  });
});
