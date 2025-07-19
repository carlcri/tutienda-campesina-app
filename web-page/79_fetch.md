# 79 Fetch

 ``Fetch`` traduce "obtener" o "recuperar". La función fetch() se utiliza para realizar solicitudes HTTP y obtener recursos, como datos de una API o archivos.


- "Obtener datos de una API" (fetch data from an API).
- "Recuperar información de un servidor" (fetch information from a server). Sugiere la acción de "ir a buscar" y traer algo desde una fuente externa, como un servidor.

Consumiremos datos desde una API de prueba: https://reqres.in 

## Primer Ejemplo

### ¿Cómo funciona?

```js
var usuarios = []

fetch('https://reqres.in/api/users?page=1')
     .then(data => data.json())
     .then(data => {
          usuarios = data;
          console.log(usuarios);
     })
```

- fetch() realiza la solicitud HTTP a la API de ReqRes.
- El primer .then() convierte la respuesta a JSON.
- El segundo .then() guarda la respuesta en la variable usuarios y la imprime en la consola: Aquí se asigna todo el objeto JSON que recibiste a la variable usuarios. Esto incluye información como la página actual, el número de usuarios por página, el total de usuarios, las páginas totales y, lo más importante, el array ``data`` que contiene los usuarios.

![image](https://i.imgur.com/m1txfX3.png)

#### Puliendo el Codigo

En realidad solo nos interesa el array `data` que es el que contiene los usuarios.

```js
fetch('https://reqres.in/api/users?page=1')
     .then(data => data.json())
     .then(data => {👈
          usuarios = data.data;👈
          console.log(usuarios);
})
```

El profesor uso:

```js
fetch('https://reqres.in/api/users?page=1')
     .then(data => data.json())
     .then(users => {👈
          usuarios = users.data;👈
          console.log(usuarios);
})
```

Casi iguales pero con una sutil diferencia, que veremos si lo escribimos como funciones de callback:

```js
fetch('https://reqres.in/api/users?page=1')
     .then(function(data) {
          return data.json();  // Convierte la respuesta a JSON
     })
     .then(function(users) {
          usuarios = users.data;  // Accede a la propiedad 'data'
          console.log(usuarios);  // Imprime el arreglo de usuarios
     });
```

¿Ya entendiste un poco mejor? 😊

#### ¿Cual de estos console.logs crees que van a imprimir la longitud correcta del Array?

```js
fetch('https://reqres.in/api/users?page=1')
     .then(function(data) {
          return data.json();  // Convierte la respuesta a JSON
     })
     .then(function(users) {
          usuarios = users.data;  // Accede a la propiedad 'data'
          console.log(usuarios);  // Imprime el arreglo de usuarios
          console.log(usuarios.length); 👈
});

console.log(usuarios.length); 👈
```
La que esta dentro del fetch imprime *6* y la de fuera imprime *0*. ¿Que es lo que pasa?

Las operaciones dentro del bloque ``then`` suceden de forma asíncrona, lo que significa que el código fuera del then, *se ejecuta antes de que la solicitud fetch termine* y de que la variable usuarios sea asignada.

### Ejercicio

Imprimir en consola solo los *emails*:

```js
fetch('https://reqres.in/api/users?page=1')
     .then(function(data) {
          return data.json();  
     })
     .then(function(users) {
          usuarios = users.data;  
          console.log(usuarios);  
          console.log(usuarios.length);

          usuarios.forEach(function(element){ 
               console.log(element.email); 👈
          })
});
```

### Ejercicio 2

Añadir los usuarios obtenidos mediante la peticion asincrona al documento html, para poderlos visualizar dentro de una lista. Se debe visualizar el primer nombre, y el correo.

```js

fetch('https://reqres.in/api/users?page=1')
     .then(function(data) {
          return data.json();  // Convierte la respuesta a JSON
     })
     .then(function(users) {
          usuarios = users.data;  // Accede a la propiedad 'data'

          usuarios.forEach(function(element){
               let elemento_lista = document.createElement('li');
               elemento_lista.append(`${element.id}: ${element.first_name} ${element.email}`);
               usuarios_lista.append(elemento_lista); 👈
          })
});
```

El instructo uso *appendChild* el cual tiene una sutil diferencia con *append*

## Cuanto tarda la peticion en hacerse

Dentro de la consola en la parte de red, podemos darnos una idea cuanto tardan estas peticiones:

![image](https://i.imgur.com/zzsVKLU.png)

En la siguiente seccion, y aprovechando los tiempos de carga, mostrar un mensaje de cargando, que luego desaparecera una vez carguen los datos.


## Solucionando un error.

Nuevamente despues de retomar el trabajo en junio del 2025. Se noto que no estaba cargando la informacion de los usuarios. E investigando el servicio *reqres*, hay un error de:

`
     error: "Missing API key.",
`

Ahora para acceder a dicho servicio de necesita dicha clave, que la obtenemos de la pagina de *reqres*, donde indica:

![image](https://imgur.com/pRmi6ax.png)

Esta API key la agregamos a nuestro **fetch** un segundo argumento, de la siguiente manera:

```js
fetch('https://reqres.in/api/users?page=3', {
     headers: {
          'x-api-key': 'reqres-free-v1' 
     }
})
```
Es mas, si queremos usar INSOMNIA, añadir el *header*:

![image](https://imgur.com/ws3dBid.png)
