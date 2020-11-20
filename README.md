# How to run django, DB and a frontend framework in docker containers using docker-compose

## 1. Install VSCode extensions
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---

## 2. Create VS Code Dev container/s
- devcontainer.json specifies:
  -  which files to use to build the container
  -  which service it should attach to
  -  what VS Code plugins to download
  -  Project settings (interpreter path, linting and formatting, etc.)

### a) Create Dev containers from template
- run a command in vscode (```ctrl+shift+p```) 
  - ```>Remote-Containers: Add development container configuration files```
  - Select "Python 3 & PostgresSQL"

### b) Create devcontainer for each service
- for each service create a directory (with a Dockerfile)
  - example file hierarchy:
    ```
    📁container1-src
      📄 Dockerfile
      📄.devcontainer.json
      📄hello.go
    📁container2-src
      📄.devcontainer.json
      📄hello.js
    📄docker-compose.yml
    ```
- create a docker-compose.yml
  - ```yml
    version: '3'
    services:
      container-1:
        build: ./container-1-src
        volumes:
          - ./container-1-src:/workspace
        ...
      container-2:
        image: ubuntu:bionic
        volumes:
          - ./container-2-src:/workspace
        ...
    ```
- for each container/srvice create a .devcontainer.json file
  - ```json
    {
    "name": "Container X",
    "dockerComposeFile": ["../docker-compose.yml"],
    "service": "container-X",
    "workspaceFolder": "/workspace",
    "extensions": [.........],
    "shutdownAction": "none"
    }
    ```
- TODO: Add description about Dockerfile and docker-compose

- Test:
  - ```$docker-compose up``` or ```>Docker: Compose Up```
  - ```>Remote-Containers: Attach Shell```
  - ```>Remote-Containers: Attach Visual Studio Code```
    - doeesn't install VS Code server and set up workspace
  - ```>Remote-Containers: Open Folder in Container```
    - will install VS Code server and set up workspace according to .devcontainer.json in given folder

---

## 3. Django backend
### 3.1 Create Django project
- Change to the root of your project directory.
- ```$ll``` 
  ```
  README.md
  backend
  db
  docker-compose.yml
  frontend
  ```
- Build backend container
  - ```$docker-compose build backend```
- Create the Django project in docker:
  - ```$sudo docker-compose run backend django-admin startproject backend /app/backend```
    - This instructs Compose to execute the django-admin startproject command in the container.
- If you are running Docker on Linux, the files django-admin created are owned by root. This happens because the container runs as the root user. Change the ownership of the new files.
  - ```$sudo chown -R $USER:$USER .```
- Test:
  - ```$docker-compose up```
  - [visit here](http://localhost:8000/)

### 3.2 Set up postgres db and connect to django
- Edit the backend/settings.py file, replace the DATABASES = ... with:
  - ```python
    # settings.py
      
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
    ```
- ```$docker-compose up```
- attach shell to backend and run ```$python manage.py createsuperuser```

### 3.3 create API using django rest framework
- attach shell to backend and create a new django app called api 
  - ```$python manage.py startapp api```
- in backend/settings.py add 
  - ```python
    # settings.py
    INSTALLED_APPS = [
      ...
      "rest_framework",
      "api",
    ]
    ```
- in api/models.py create your models
  - "db tables, bud defined using python classes instead of sql"
- make migrations and migrate after creating or altering any model
  - ```$python manage.py makemigrations api```
  - ```$python manage.py migrate```
- create model serializers in api/serializers.py
  - "class that can convert db entries to json and vice versa"
- in api/viewsets.py create your viewsets (CRUD endpoints)
  - "selection of db entries from one or more tables"

- in backend/urls.py add 
  ```python
  # urls.py
  urlpatterns = [
    ...
    path("", include("api.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  ]
  ```
  - will allow to access other django apps within the project
- restart container to access endpoints

---

## Useful links
- **VS Code Remote Containers**
  - [developing inside a container](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container)
  - [devcontainer.json reference](https://code.visualstudio.com/docs/remote/devcontainerjson-reference#_devcontainerjson-properties)
  - [devcontainer for each service](https://github.com/microsoft/vscode-remote-release/issues/254)
  - [attaching vscode to container](https://code.visualstudio.com/docs/remote/attach-container)
  - [djangoCon containerized dev env](https://www.youtube.com/watch?v=hwHRI59iGlw)
- **Docker**
  - [run django in docker](https://docs.docker.com/compose/django/)


---
### Hint
- ```$ ...``` - cmd line command 
- ```> ...``` - vscode command