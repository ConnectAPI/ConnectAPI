# ConnectAPI
Build your backend with components


## What do we do?
Our goal is to create a system that allows you to set up your backend with a few clicks.


### installation
```
$> docker run -it --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --entrypoint="install" \
    apiconnect/apiconnect:latest
```
Once the Docker installation completes, go to http://localhost to access the system dashboard from your browser. Please note that on non-Linux native hosts, the server might take a few minutes to start after installation completes.


### How it works (from the side of a service writer)?
1. write a service that can detect animals in photos.
2. write an OpenAPI spec for the service and build a docker image.
3. upload the docker image and the spec to the marketplace.
You now have a service on the ConnectAPI marketplace that anyone can use in their system.

### How it works (from the side of an app developer)?
1. Run our docker image on your machine.
2. Open the dashboard (click on the link).
3. Search for needed services
4. Click install
5. That it! Now the service is running on your system.
6. To access the service you need to access the gateway with a specific URL prefix (HTTP://<gateway_url>/<service_name>)
OR use the dedicated auto-generated library.


#### User story
1. Backend developer creates some API and OpenAPI spec for the API and uploads docker image of the API to docker hub
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
