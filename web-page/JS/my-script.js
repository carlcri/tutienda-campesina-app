'use strict'

$(document).ready(function(){
    console.log('Jquery ha cargado. Feliz');
    // var aux = $('#clientForm').eq(0);
    // console.log(aux);
    // console.log(aux.html());

    var counter=0;

    $('#searchClientButton').click(function(e){ 
        e.preventDefault();
        counter++;
        console.log(counter);

        let client_id = $('#clientId').val();
        client_id = parseInt(client_id)
        console.log(`client_id: ${client_id} and type: ${typeof(client_id)}`);

        if(isNaN(client_id)){
            console.log('Debe ingresar un numero valido');
            return;
        }

        const api_URL = `http://localhost/api/client/${client_id}`;
        fetch(api_URL)
        .then(function(data){
            return data.json();
        })
        .then(function(client){
            console.log(client);
            console.log(client.DOB);
            console.log(client.address);
            console.log(client.lastName);
        })  
    });
})

// var usuarios = []
// var usuarios_lista = document.querySelector('#usuarios-lista');
// console.log(usuarios_lista.innerHTML)


// fetch('https://reqres.in/api/users?page=2', {
//      headers: {
//           'x-api-key': 'reqres-free-v1' 
//      }
// })
//      .then(function(data) {
//           return data.json();  // Convierte la respuesta a JSON
//      })
//      .then(function(users) {
//           usuarios = users.data;  // Accede a la propiedad 'data'

//           usuarios.forEach(function(element){
//                let elemento_lista = document.createElement('li');
//                elemento_lista.append(`${element.id}: ${element.first_name} ${element.email}`);
//                usuarios_lista.append(elemento_lista);
//           })
// });


// fetch('https://reqres.in/api/users/4', {
//      headers: {
//           'x-api-key': 'reqres-free-v1' 
//      }
// })
//      .then(function(data) {
//           return data.json();  // Convierte la respuesta a JSON
//      })
//      .then(function(user){
//           let usuario = []
//           usuario = user.data;
//           console.log(usuario);
//           console.log(usuario.first_name, usuario.email, usuario.id)
//      })


 
// fetch('http://localhost/api/client/10')
//        .then(function(data){
//             return data.json();
//      })
//      .then(function(client){
//          console.log(client);
//           console.log(client.DOB);
//           console.log(client.address);
//           console.log(client.lastName);
//      })     

