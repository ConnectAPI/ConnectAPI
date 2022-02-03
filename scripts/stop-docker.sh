docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -v /opt:/opt:rw \
	 -e MARKETPLACE_URL='https://market.boxs.ml' \
	 -e PRUNE="no" \
	 connectapihub/connectapi uninstall
