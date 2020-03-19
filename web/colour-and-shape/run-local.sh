#!/bin/sh
docker run -it --rm -p31337:80 -v $(pwd)/src:/var/www/html colours-and-shapes
