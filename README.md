# ConnectAPI
Build your backend with components

### Full system overview
| Service           | Description                                                                            | repo                                        |
|-------------------|:---------------------------------------------------------------------------------------|---------------------------------------------|
| **Marketplace**   | Provide API and website to upload, download and search services.                       | https://github.com/ConnectAPI/MarketPlace   |
| **Gateway**       | The only entry point to the system, responsible for auth, validation and rate limit's. | https://github.com/ConnectAPI/Gateway       |
| **Dashboard**     | Provide easy interface for managing and monitoring the system.                         | https://github.com/ConnectAPI/Dashboard     |
| **SDK Generator** | Generate SDK from OpenAPI spec.                                                        | https://github.com/ConnectAPI/SDKGeneragtor |

### What we want?
Our goal is to create a system that allows you to set up your backend with a few clicks.

### installation
```commandline
$> docker run \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    -e MARKETPLACE_URL="https://market.boxs.ml"
    apiconnectsys/connectapi:latest install
```
Once the Docker installation completes an HTTP url for the dashboard will be showen on the console, enter it to manage your system.


### How it works (from the side of a service writer)?
1. write a HTTP service.
2. write an OpenAPI spec for the service and build a docker image.
3. upload the docker image and the spec to the marketplace. 
You now have a service on the ConnectAPI marketplace that anyone can use in their system. 😎

### How it works (from the side of an app developer)?
1. Run our docker image on your machine.
2. Open the dashboard (click on the link 🖱).
3. Search for needed services 🔎.
4. Click install 📲.
5. That it! Now the service is running on your system 🙌.
6. To access the service just access the gateway with a specific URL prefix (HTTP://<gateway_url>/<service_name>)  
OR use the dedicated auto-generated library. (**recommanded**)
   

### User story
1. Backend developer creates API, OpenAPI spec for that API, and uploads the API docker image to docker hub
2. He goes to the ConnectAPI marketplace and register (email and password for now)
3. He clicks on the "Create Service" button
4. He choose the service name (if not taken)
5. He writes some service description
6. He enters the docker image name of his service (if not exist yet)
7. He adds the OpenAPI spec (validate schema)
8. He clicks on the submit button
9. Another developer installs the ConnectAPI system on his machine (docker run)
10. The container output is an HTTP link for the dashboard
11. He opens the link to the dashboard and set his password
12. He browse the marketplace or use the search and choose a service to install
13. The service is added to the system services and starts running
14. He visit the system tab at the dashboard and get full monitoring info about his installed services


### uninstall
```commandline
$> docker run \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    apiconnectsys/connectapi:latest uninstall
```