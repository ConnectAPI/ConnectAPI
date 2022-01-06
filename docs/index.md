<p align="center">
  <a href="https://connectapi.io"><img src="https://blogs.mulesoft.com/wp-content/uploads/api-connect-devices-300x214.png" alt="ConnectAPI"></a>
</p>
<p align="center">
    <em>A way to build your backend with components.</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/asyncer/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/tiangolo/asyncer/workflows/Publish/badge.svg" alt="Publish">
</a>
</p>

---

**Documentation**: <a href="https://connectapi.io" target="_blank">https://connectapi.io</a>

**Source Code**: <a href="https://github.com/connectapi/connectapi" target="_blank">https://github.com/connectapi/connectapi</a>

---

**ConnectAPI** is a system built to help backend developers to write less and get more.

**ConnectAPI** allows you to run multiple APIs with no code at all, and manage them with nice and easy dashboard.

The main goal of **ConnectAPI** is to improve **developer experience** by helping you use open source services with **auto generated SDKs and documentation** for multiple languages and frameworks.

**ConnectAPI** also make it easy for other developers to use your service by providing a **service marketplace**, it also possible to **make money** on the marketplace by requiring a payment on your service.

## 🚨 Warning

This system is work in progress, it is not advisable to use it in production yet!.

## Can I Use It?

Yes 🎉 (but continue reading).

You can use this and evaluate the **idea and easy of use** I'm proposing. It will probably be useful to know if it works and is useful for you (I hope so).

But still, consider this lab material, expect it to change a bit. 🧪

If you do use it and want to write me your thoughts please contact me on **yehotada.sht@gmail.com**
## Requirements

As **ConnectAPI** is running on [Docker](https://www.docker.com/) it will require you to install it on your machine.

## Installation

<div class="termy">

```console
$ docker run -it --rm\
        -v /var/run/docker.sock:/var/run/docker.sock \
        -e MARKETPLACE_URL='https://market.boxs.ml' \
        connectapi install
2022-01-05 23:05:44.300 | INFO     | __main__:main:48 - Starting command 'install'

Enter http_port[80]:

Enter https_port[443]:

Enter dashboard_port[6489]:

Enter domain[localhost]: 

2022-01-05 23:06:02.559 | INFO     | __main__:setup_db:15 - setting up db...
2022-01-05 23:06:02.583 | WARNING  | continers:start_containers:26 - network all ready existing.
2022-01-05 23:06:02.585 | INFO     | continers:start_containers:29 - Starting gateway
2022-01-05 23:06:03.263 | INFO     | continers:start_containers:49 - Started 6d4dc62757
2022-01-05 23:06:03.265 | INFO     | continers:start_containers:52 - Starting dashboard...
2022-01-05 23:06:04.422 | INFO     | continers:start_containers:71 - Started abadcbe10c
2022-01-05 23:06:04.423 | INFO     | __main__:install_and_start_system:25 - Running dashboard on http://localhost:6489
```

</div>

## How to Use

Like you see on the last line of the output the system is running a dashboard on port 6489 by default,

Registering to the **Dashboard** as quick as possible is important, the **Dashboard** will make the first user to register a root user on the system.

After registering you can start searching on the **Marketplace** for services, once found you can view their docs, endpoints and examples. the installation is simple just click on the installation button.

After the installation the service will be added to your system tab and display monitoring info, and will allow you to config it to your needs.

### Developer Experience

Everything in **ConnectAPI** is designed to get the best **developer experience** possible.

Every service that upload to the **Marketplace** has to have [OpenAPI spec](https://www.openapis.org) file, on upload the **Marketplace** generate SDKs and documentations for the supported languages, and upload the SDKs to their package managers, so you can just install them and use the service without dealing with http requests.

Example code to show you how your code will look using our **ConnectAPI**
```python
from connectapi_core import Client # core sdk for python
from connectapi_demo import Demo  # Auto generated sdk for the demo service

Client.set_url("http://your.server.domain")
Client.set_token(
    token="<TOKEN FROM THE DASHBOARD>",
)
demo_service = Demo(client=Client())

r = demo_service.multiply_two_numbers(a=16, b=8)
print(r)

r = demo_service.sum_two_numbers(a=16, b=8)
print(r)

r = demo_service.random_int_from_range(a=-50, b=50)
print(r)

r = demo_service.random_string(n=10)
print(r)
```
## License
TODO: add licence
