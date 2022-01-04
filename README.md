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


### Quick start, how to run the system
1. run this command to install and run the system
    ```commandline
    docker run \
        --volume /var/run/docker.sock:/var/run/docker.sock \
        -e MARKETPLACE_URL="https://market.boxs.ml" \
        apiconnectsys/connectapi:latest install
    ```
    Once the Docker installation completes an HTTP url for the dashboard will be showen on the console, enter it to manage your system.
2. connect to the dashboard, choose a service and click install
3. go to your code and install the service sdk (provided from the dashboard)


### Quick start on how to add a service
1. write an HTTP service.
2. write an OpenAPI spec for the service and build a docker image.
3. go to the [marketplace](https://market.boxs.ml) and upload you'r service.
You now have a service on the ConnectAPI marketplace that anyone can use in their system. 😎


### How it works
Our system is built from three main parts:

1. The gateway is per client (you) and manages the incoming requests to the system.
2. The dashboard is also per client and allow you to command and control you'r system.
3. The marketplace is global and manages the services, every service you install on your system come from the marketplace.
