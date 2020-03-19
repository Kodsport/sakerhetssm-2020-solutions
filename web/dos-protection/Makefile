run:
	docker build -t web-spoofing-img .
	docker run -d -p 9696:6969 --name web-spoofing -i web-spoofing-img

stop:
	docker stop web-spoofing
	docker container rm web-spoofing