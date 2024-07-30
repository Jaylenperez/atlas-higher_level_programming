// Ensure the script runs after the DOM is fully loaded
$(document).ready(function () {
  // Attach a click event handler to the DIV with id="red_header"
  $('#red_header').click(function () {
    // Select the <header> element using jQuery and change its text color to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});
