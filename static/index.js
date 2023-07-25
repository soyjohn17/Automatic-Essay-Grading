document.addEventListener('DOMContentLoaded', function() {
    // Get references to the text box and the clear button
    const textBox = document.getElementById('essay');
    const clearButton = document.getElementById('clearButton');

    // Add click event listener to the clear button
    clearButton.addEventListener('click', function() {
        // Clear the contents of the text box
        textBox.value = '';
    });
});