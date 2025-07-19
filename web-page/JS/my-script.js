'use strict'

console.log('Nueva Implementacion');

var usuarios = []
var usuarios_lista = document.querySelector('#usuarios-lista');
console.log(usuarios_lista.innerHTML)


fetch('https://reqres.in/api/users?page=2', {
     headers: {
          'x-api-key': 'reqres-free-v1' 
     }
})
     .then(function(data) {
          return data.json();  // Convierte la respuesta a JSON
     })
     .then(function(users) {
          usuarios = users.data;  // Accede a la propiedad 'data'

          usuarios.forEach(function(element){
               let elemento_lista = document.createElement('li');
               elemento_lista.append(`${element.id}: ${element.first_name} ${element.email}`);
               usuarios_lista.append(elemento_lista);
          })
});


fetch('https://reqres.in/api/users/4', {
     headers: {
          'x-api-key': 'reqres-free-v1' 
     }
})
     .then(function(data) {
          return data.json();  // Convierte la respuesta a JSON
     })
     .then(function(user){
          let usuario = []
          usuario = user.data;
          console.log(usuario);
          console.log(usuario.first_name, usuario.email, usuario.id)
     })


 
fetch('http://localhost/api/client/10')
       .then(function(data){
            return data.json();
     })
     .then(function(client){
         console.log(client);
          console.log(client.DOB);
          console.log(client.address);
     })     


// fetch('http://localhost:8000/client/5')
//        .then(function(data){
//             return data.json();
//      })
//      .then(function(client){
//          console.log(client);
//           console.log(client.DOB);
//           console.log(client.address);
//      }) 

