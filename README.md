# ConnectAPI
Build your backend with components


## What do we do?
Our goal is to create a system that allows you to set up your backend with a few click's


## How it works (from the side of a service writer)?
1. You write a nice service that can detect animals in photos.
2. You write an OpenAPI spec for the service and build a docker image of it.
3. You upload the docker image and the spec to the marketplace.


## How it works (from the side of an app developer)?
1. Run our docker image on your machine. (gateway)
2. Open the dashboard (click on the link).
3. Search for needed services (file storage, users, etc)
4. Click install
5. That it! Now the service is running on your system.
6. To access the service you need to access the gateway with a specific URL prefix (HTTP://<gateway_url>/<service_name>)
OR use the dedicated auto-generated library.
