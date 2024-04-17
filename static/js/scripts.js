document.getElementById("textForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    
    var text1 = document.getElementById("text1").value;
    var text2 = document.getElementById("text2").value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'text1': text1,
            'text2': text2
        })
    })
    .then(response => response.json())
    .then(data => {

        var resultElement = document.getElementById("result");
        resultElement.innerHTML = "<h2 style='color:white;' background-color='color:white'>Results:</h2>" +
        "<h3 style='color:white;'>Text 1: </h3>" + "<p style='background-color:white;'>" + data.text1 + "</p>" + 
        "<h3 style='color:white;'>Text 2: </h3>" + "<p style='background-color:white;'>" + data.text2 + "</p>" +
        "<h2 style='color:white;'>Similarity Score: " + data.similarity_score + "</h2>";
        
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
