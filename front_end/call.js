function search(){
      fetch(url)
        .then((resp) => resp.json()) // Transform the data into json
        .then(function(data) {
    // Create and append the li's to the ul
        console.log(data);
    })
  })
}
