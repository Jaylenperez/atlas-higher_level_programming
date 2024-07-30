// Ensure the script runs only after the DOM is fully loaded
$(document).ready(function () {
  // Attach a click event handler to the DIV with id 'red_header'
  $('#red_header').click(function () {
    // Add the class 'red' to the <header> element when the DIV is clicked
    $('header').addClass('red');
  });
});
