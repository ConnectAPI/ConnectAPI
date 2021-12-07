# ConnectAPI
Build your backend with components


## What do we do?
Our goal is to create a system that allows you to set up your backend with a few click's.


### installation
```
$> docker run -it --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --entrypoint="install" \
    apiconnect/apiconnect:latest
```
Once the Docker installation completes, go to http://localhost to access the system dashboard from your browser. Please note that on non-Linux native hosts, the server might take a few minutes to start after installation completes.


### How it works (from the side of a service writer)?
1. write a nice service that can detect animals in photos.
2. write an OpenAPI spec for the service and build a docker image.
3. upload the docker image and the spec to the marketplace.
You now have a service on the ConnectAPI marketplace and anyone can use it in thire system.

### How it works (from the side of an app developer)?
1. Run our docker image on your machine.
2. Open the dashboard (click on the link).
3. Search for needed services (file storage, users, etc)
4. Click install
5. That it! Now the service is running on your system.
6. To access the service you need to access the gateway with a specific URL prefix (HTTP://<gateway_url>/<service_name>)
OR use the dedicated auto-generated library.
