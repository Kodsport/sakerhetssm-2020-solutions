#!/usr/bin/env python3
print(u"""
   ___   ___  ____   
 .'   `.|_  ||_  _|  
/  .-.  \ | |_/ /    
| |   | | |  __'.    
\  `-'  /_| |  \ \_  
 `.___.'|____||____| 
                     
                     
Use my "miniraknare":
""")


banned = ["open"]

while True:
	expr = input()
	no = False
	for i in banned:
		if i in expr:
			no = True
	if no:
		print("invalid expression")
		continue
	print(eval(expr))
