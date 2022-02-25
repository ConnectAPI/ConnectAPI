docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -v /opt:/opt:rw \
	 -e MARKETPLACE_URL='http://10.100.102.10:3596' \
	 --network host \
	 connectapihub/connectapi install
