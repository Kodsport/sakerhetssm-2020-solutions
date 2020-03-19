build:
	mkdir -p public 
	cp client.py server.py lib.py public
	cp pub_secret.py public/secret.py
	zip chall.zip public/*

	mkdir -p docker-server/files
	cp server.py lib.py secret.py docker-server/files

	mkdir -p docker-client/files
	cp client.py lib.py secret.py docker-client/files


clean:
	rm -r public
	rm docker-server/files/server.py docker-server/files/lib.py docker-server/files/secret.py
	rm docker-client/files/client.py docker-client/files/lib.py docker-client/files/secret.py
	rm chall.zip
