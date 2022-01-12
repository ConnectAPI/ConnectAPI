docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -e MARKETPLACE_URL='https://market.boxs.ml' \
	 connectapi_install uninstall
