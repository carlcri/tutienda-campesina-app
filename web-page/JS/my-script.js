'use strict'

$(document).ready(function(){
    console.log('Jquery ha cargado exitosamente');
    var error_message = '';

    $('#searchClientButton').click(function(e){ 
        e.preventDefault();

        let client_id = $('#clientId').val();
        client_id = parseInt(client_id)
        console.log(`client_id: ${client_id} and type: ${typeof(client_id)}`);

        if(isNaN(client_id)){
            console.log('Debe ingresar un numero valido');
            
            return;
        }

        const api_URL = `http://localhost/api/client/${client_id}`;
        fetch(api_URL)
        .then(function(response){
            console.log(`ok: ${response.ok} | status code: ${response.status}`)

            if(!response.ok){
                return response.json().then(function(apiErrorResponse){
//                    console.log(apiErrorResponse);
                    error_message = `status_code:${response.status} | details: ${apiErrorResponse.detail.message}`    
                    let error = new Error(error_message);
                    error.status_code = response.status;
                    error.details = apiErrorResponse.detail.message; 
                    throw error;
                })
            }

            return response.json();
        })
        .then(function(client){
            console.log(`cliente con id:${client.id} encontrado`);
            $('#result-container').show();
            $('.message').show();
            $('#error-message').hide();
//            $('#clientForm').hide();
            $('#initial-message').hide();


            $('#client-id-display').html(client.id);
            $('#client-name-display').html(client.name);
            $('#client-lastname-display').html(client.lastName);
            $('#client-dob-display').html(client.DOB);            

        })
        .catch(function(error){
            //<p id="error-message" class="message"></p>
            console.log('hola error catch...');  
            console.log(error_message);
            console.log(error.status_code, error.details);

            $('#result-container').show();
            $('.message').show();
            $('#client-details').hide();
//            $('#clientForm').hide();

            $('#error-message').html(`<p>${error_message}</p>`);

        })  
    });
})
