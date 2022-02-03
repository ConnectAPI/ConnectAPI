# Uninstalling the system

If you want to move to our cloud or just not using the system any more run this commad to uninstall the system.

```shell
docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -v /opt:/var/lib:rw \
	 -e PRUNE="no" \
	 connectapihub/connectapi uninstall
```

To remove all the data of the system just change the PRUNE value to "yse".