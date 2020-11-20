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