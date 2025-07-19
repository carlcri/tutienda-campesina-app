# Selectores

Antes de empezar, para no contactar un CDN externo, guardar el codigo JS del script de la version 3.3.1 de Jquery. SImplemente dando click, y guardandola en la carpeta `JS`. haciendo las respectimas modificacione en el `html`:

```js
<body>
    <h1>Aprendiendo JQuery</h1>
    <p>Ejercicios</p>
    <!--scripts-->
    <script src="./JS/jquery-3.3.1.min.js"></script> 👈
    <script src="./JS/91_integrar.js"></script>
</body>
```

Ahora en nuestro JS:

```js
$(document).ready(function(){
    console.log('Jquery ha cargado. Feliz')
})
```
El signo de dolar `$` siempre se refiere a `jQuery`, tambien se podria remplazar directamente con `Jquery` y tambien funcionaria:

```js
jQuery(document).ready(function(){
    console.log('jQuery está presente con el nombre completo')
})
```

### Selector de ID

Crea una serie de etiquetas dentro del html, y luego seleccionalas usando los selectores, para mostrar que hay dentro de cada una.

```js
$(document).ready(function(){
    var div_red = $('#red');
    console.log(div_red);
    console.log(div_red[0].innerHTML);
})
```

Ahora cambia el color de background, usando el metodo `css`

```js
$('#red').css('background', 'red');
```

Escoge otra etiqueta y cambia el background, y el color de fuente al mismo tiempo:
Esto es encadenando la llamada a los metodos
```js
    var div_yellow = $('#yellow').css('background', 'yellow')
                                 .css('color', 'red');
```

Es mas no se necesita declarar la variable.

### Selectores de Clases

Modificando el HTML:

```html
    <div id="yellow" class="zebra">I am yellow and zebra</div>
    <div id="red" class="zebra">I am red and zebra</div>
    <div class="zebra">I am a zebra</div>
```

y en el .js con su respectivo selector de clase:

```js
    var clase_zebra = $('.zebra');
    console.log(clase_zebra)
```

El resultado:

![](https://imgur.com/M37QbtS.png)

Como era de esperarse es un arreglo de 3 elementos, el primero `yellow.zebra`, el segundo `red.zebra`, y el tercero `.zebra`. ¿TIene sentido?

Si queremos acceder al primer elemento del arreglo, lo podemos hacer de dos formas, una de ellas con el metodo `eq`:

```js
    console.log(clase_zebra[0]);
    console.log(clase_zebra.eq(0))
```


#### Ejercicio

Darle un estilo CSS a la clase zebra.

```js
    clase_zebra.css('background', 'green')
               .css('color', 'brown');
```





