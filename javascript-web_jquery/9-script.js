// Ensure the script runs only after the DOM is fully loaded
$(document).ready(function () {
  // Fetch data from the provided URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Update the text of the DIV with id 'hello' to the translation of 'hello'
    $('#hello').text(data.hello);
  });
});
