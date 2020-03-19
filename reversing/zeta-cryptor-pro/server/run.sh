#!/bin/sh
/bin/nsjail -Ml --port 1337 --proc_rw --keep_caps --user nobody --group nogroup -R /home/zetacryptorpro/ -R /usr/local/lib -R /bin/nsjail -R /usr/bin/python3 -R /lib -R /usr/lib -R /lib/x86_64-linux-gnu/ -R /lib64 -R /dev/urandom -T /tmp/ --cwd /home/zetacryptorpro -- /usr/bin/python3 server.py
