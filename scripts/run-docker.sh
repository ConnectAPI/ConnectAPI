docker run -it --rm \
	 -v /var/run/docker.sock:/var/run/docker.sock \
	 -v /home/magshimim/Documents/projects/ConnectAPI/data:/local \
	 -e MARKETPLACE_URL='https://market.boxs.ml' \
	 -e DEBUG="yes" \
	 connectapi_install install
