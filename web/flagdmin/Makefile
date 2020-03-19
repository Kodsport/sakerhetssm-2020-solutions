run:
	docker build -t web-nosqli-img .
	docker run -d -p 6969:6969 --name web-nosqli -i web-nosqli-img

stop:
	docker stop web-nosqli
	docker container rm web-nosqli
	