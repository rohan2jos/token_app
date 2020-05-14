function performGetRequest1(){
  var resultElement = document.getElementById('getResult1');
  resultElement.innerHTML = '';

  axios.get('http://jsonplaceholder.typicode.com/todos')
    .then(function (response) {
      resultElement.innerHTML = generateSuccessHTMLOutput(response);
    })
    .catch(function (error) {
      resultElement.innerHTML = generateErrorHTMLOutput(error);
    });
}

function generateSuccessHTMLOutput(response) {
  return  '<h4>Result:</h4>' +
          '<h5>Status:</h5>' +
          '<pre>' + response.status + ' ' + response.statusText + '</pre>' +
          '<h5>Data:</h5>' +
          '<pre>' + JSON.stringify(response.data, null, '\t') + '</pre>';
}

function generateErrorHTMLOutput(error) {
  return  '<h4>Result:</h4>' +
          '<h5>Message:</h5>' +
          '<pre>' + error.message + '</pre>' +
          '<h5>Status:</h5>' +
          '<pre>' + error.response.status + ' ' + error.response.statusText + '</pre>' +
          '<h5>Data:</h5>' +
          '<pre>' + JSON.stringify(error.response.data, null, '\t') + '</pre>';
}


function performGetRequest2(){
  var resultElement = document.getElementById('getResult2');
  var todoId = document.getElementById('todoId').value;
  resultElement.innerHTML = '';

  axios.get('http://jsonplaceholder.typicode.com/todos', {
    params: {
      id: todoId
    }
  })
    .then(function (response) {
      resultElement.innerHTML = generateSuccessHTMLOutput(response);
    })
    .catch(function (error) {
      resultElement.innerHTML = generateErrorHTMLOutput(error);
    });
}

document.getElementById('todoInputForm').addEventListener('submit', performPostRequest);

function performPostRequest(e) {
  var resultElement = document.getElementById('postResult');
  var fullName = document.getElementById('name').value;
  var email = document.getElementById('email').value;
  var phone = document.getElementById('phone').value;
  resultElement.innerHTML = '';

  axios.post('http://jsonplaceholder.typicode.com/todos', {
    name: fullName,
    email: email,
    phone: phone
  })
  .then(function(response) {
    resultElement.innerHTML = generateSuccessHTMLOutput(response);
  })
  .catch(function(error) {
    resultElement.innerHTML = generateErrorHTMLOutput(error);
  })
  e.preventDefault();
}

function clearOutput() {
    var resultElement = document.getElementById('getResult1');
    resultElement.innerHTML = '';
    var resultElement = document.getElementById('getResult2');
    resultElement.innerHTML = '';
    var resultElement = document.getElementById('postResult');
    resultElement.innerHTML = '';
}
