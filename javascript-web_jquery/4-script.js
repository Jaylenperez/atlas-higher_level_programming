// Ensure the script runs only after the DOM is fully loaded
$(document).ready(function () {
  // Attach a click event handler to the DIV with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Check the current class of the <header> element
    if ($('header').hasClass('red')) {
      // If the class is 'red', remove it and add 'green'
      $('header').removeClass('red').addClass('green');
    } else {
      // If the class is not 'red', remove 'green' and add 'red'
      $('header').removeClass('green').addClass('red');
    }
  });
});
