docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -v /opt:/var/lib \
	 -e MARKETPLACE_URL='https://market.boxs.ml' \
	 -e PRUNE='yes' \
	 connectapi_install uninstall
