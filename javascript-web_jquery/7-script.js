// Ensure the script runs only after the DOM is fully loaded
$(document).ready(function () {
  // Fetch data from the provided URL
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    // Update the text of the DIV with id 'character' to the character's name
    $('#character').text(data.name);
  });
});
