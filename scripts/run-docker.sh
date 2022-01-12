docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -v /opt:/var/lib:rw \
	 -e MARKETPLACE_URL='https://market.boxs.ml' \
	 --network host \
	 connectapi_install install
