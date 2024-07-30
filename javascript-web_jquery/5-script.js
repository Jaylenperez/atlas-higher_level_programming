// Ensure the script runs only after the DOM is fully loaded
$(document).ready(function () {
  // Attach a click event handler to the DIV with id 'add_item'
  $('#add_item').click(function () {
    // Create a new <li> element with the text 'Item'
    const newItem = $('<li>Item</li>');
    // Append the new <li> element to the UL with class 'my_list'
    $('ul.my_list').append(newItem);
  });
});
