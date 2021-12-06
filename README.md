# ConnectAPI
Build your backend with components


## What we do?
Our goal is to create a system that allow you to setup your backend with few click's


## How it works (from the side of a service writer)?
1. You write nice service that can detect animals in photos.
2. You write an openapi spec for the service and build a docker image of it.
3. You upload the docker image and the spec to the marketplace.


## How it works (from the side of an app developer)?
1. Run our docker image on your machin. (gateway)
2. Open the dashboard (click on the link).
3. Search for needed services (file storage, users, etc...)
4. Click install
5. That it, now you have thet service running on your system.
6. To access the service you need to access the gateway with specific url prefix (http://<gateway_url>/<service_name>)
