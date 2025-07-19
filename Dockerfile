# Usa una imagen base de NGINX ligera y estable
FROM nginx:stable-alpine

# Copia tu archivo de configuración de NGINX personalizado
# El primer '.' se refiere al directorio actual (nginx-proxy)
# El segundo '.' se refiere al directorio de destino dentro del contenedor (/etc/nginx/nginx.conf)
COPY nginx.conf /etc/nginx/nginx.conf

# Copia los archivos de tu frontend al directorio de NGINX donde sirve archivos estáticos
# '../web-page' significa "sube un nivel (a tutienda-campesina-app) y luego entra en 'web-page'"
# '/usr/share/nginx/html' es la ubicación por defecto de NGINX para archivos web
COPY ../web-page /usr/share/nginx/html

# Expone el puerto 80 del contenedor
EXPOSE 80

# Comando para iniciar NGINX en primer plano (necesario para Docker)
CMD ["nginx", "-g", "daemon off;"]
