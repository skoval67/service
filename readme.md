Для смены версии docker-образа сервиса при деплое, положить новую версию образа на hub.docker.com

docker push repo/reponame:tagname

указать имя образа repo/reponame:tagname в переменной app_docker_image в файле roles/app_deploy/vars/main.yml
