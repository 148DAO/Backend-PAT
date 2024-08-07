# Backend-PAT

### 1. Docker and docker-compose
- install docker and docker-compose globally on terminal

Docker installations
- Ubuntu: https://docs.docker.com/engine/install/ubuntu/
- Debian: https://docs.docker.com/engine/install/debian/
- Windows: https://docs.docker.com/desktop/install/windows-install/
- Mac: https://docs.docker.com/desktop/install/mac-install/

To install docker-compose on Ubuntu, run the following commands:
- `sudo curl -L "https://github.com/docker/compose/releases/download/v2.17.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
- `sudo chmod +x /usr/local/bin/docker-compose`
- `docker-compose --version` To verify that it's installed
- Run bellow commands to ensure that you don't have docker permissions problems
    1. sudo usermod -a -G docker $USER
    2. newgrp docker
    3. chmod 777 /var/run/docker.sock

For Windows: The easiest and recommended way to get Docker Compose is to install Docker Desktop. Docker Desktop includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites. From the link provided above.


### 2. Install poery for dependencies management
For linux, command: `pip poetry install`

After installing poetry, navigate to root foler backend-pat/ and run command `poetry install` to install all packages required for this app to work

### 3. Ask for `.env` files from one of the team member, because docker will throw error when building the container

### 4. Commands to run the FastAPI app with it's MySQL database
First build the container: `docker-compose build` <br>
Run container with applications: `docker-compose up`<br>
To stop the container: `docker-compose down`<br>

#### VSCode Tips
1. To remove delete branches on VSCode: `git fetch --prune && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs -r git branch -d
`


#### COMMON PROBLEMS SOLVING: FOR LINUX

1.  listen tcp4 0.0.0.0:3306: bind: address already in use
    - `sudo systemctl stop mysql` => when it's specifically wanting to kill mysql port 
    - For any port try this: `sudo fuser -k <port>/tcp`



