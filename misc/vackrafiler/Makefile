
run:
	docker build -t vackrafiler-img .
	docker run -d -p 2222:22 --name vackrafiler -i vackrafiler-img

stop:
	docker stop vackrafiler
	docker container rm vackrafiler
