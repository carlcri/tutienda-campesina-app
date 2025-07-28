# tutienda-campesina-app
tienda campesina 

Cambio 1


```mermaid
graph TD
    A[fetch(api_URL)] --> B{Server Responds};
    B -- Status 200-299 --> C{response.ok is true};
    C --> D[return response.json()];
    D -- Parsed Client Data --> E[Second .then(client => ...)];

    B -- Status 4xx or 5xx --> F{response.ok is false};
    F --> G[return response.json()];
    G -- Parsed Error Data --> H[Nested .then(errorData => ...)];
    H --> I[throw new Error(...)];
    I --> J[Outer .catch(error => ...)];


graph TD
    A[fetch(api_URL)] --> B{Server Responds};
    B -- Status 200-299 --> C{response.ok is true};
    C --> D[return response.json()];
    D -- Parsed Client Data --> E[Second .then(client => ...)];

    B -- Status 4xx or 5xx --> F{response.ok is false};
    F --> G[return response.json()];
    G -- Parsed Error Data --> H[Nested .then(errorData => ...)];
    H --> I[throw new Error(...)];
    I --> J[Outer .catch(error => ...)];






curl -X 'PATCH' \
  'http://localhost:8000/student/4' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-binary '{
  "name": "soy la comadreja"
}'



curl -X 'PATCH' \
  'http://localhost:8000/student/19' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "lastName": "baab",
  "governmentId": "string"
}'
