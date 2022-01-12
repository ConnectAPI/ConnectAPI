# Uninstalling the system

If you want to move to our cloud or just not using the system any more run this commad to uninstall the system.

```console
$ docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -v /opt:/var/lib:rw \
	 connectapihub/connectapi uninstall
```

To remove all the data of the system just add ```-e PRUNE="yes" \``` to the command above.