server {
    listen 80;
    server_name datapoint.meetingpointuae.com;

    location /media {
        alias /usr/share/nginx/media/;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}

server {
    listen 80 default_server;
    return 444;
}