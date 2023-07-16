// main.js
document.addEventListener('DOMContentLoaded', function() {
    // Make an AJAX request to fetch the dog breeds
    axios.get('/get_dog_breeds')
        .then(function(response) {
            // Handle the successful response
            var breeds = response.data.breeds;

            // Iterate over the breeds and add them to the list
            for (var i = 0; i < breeds.length; i++) {
                var listItem = document.createElement('li');
                listItem.textContent = breeds[i];
                document.getElementById('breed-list').appendChild(listItem);
            }
        })
        .catch(function(error) {
            // Handle the error
            console.log('Error occurred while fetching dog breeds.', error);
        });
});
