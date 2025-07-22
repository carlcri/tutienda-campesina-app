FROM ubuntu/apache2

# Enable the necessary Apache modules during the build process
RUN a2enmod proxy proxy_http

COPY ["./my-apache-proxy.conf", "/etc/apache2/sites-available/000-default.conf"]

EXPOSE 80

# Command to run Apache in the foreground when the container starts
CMD ["apache2ctl", "-D", "FOREGROUND"]

