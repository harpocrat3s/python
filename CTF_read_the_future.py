import sys
import socket
import time

hostname = "164.90.147.2"
port = 1234
nos = [14]
data = ''

def netcat(hn,p,content):

	global nos
	ind = 0

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((hn,p))
	time.sleep(0.5)

	global data

	while 'TS{' not in data:
		try:
			data = sock.recv(1024).decode()
			while 'Sorry' not in data:
				if len(nos) == 0 or ind > len(nos)-1:
					print("sending:",content)
					sock.sendall(content)
				else:
					print("Sending:",str(nos[ind]).encode())
					sock.sendall(str(nos[ind]).encode())
					ind = ind + 1
				time.sleep(0.75)
				data = sock.recv(1024).decode()
				print(nos)
				print(data)
				if 'Sorry' in data:
					no = [int(i) for i in data.split() if i.isdigit()][0]
					print(no)
					
					nos.append(no)
					sock.close()
					break

			
			if 'Sorry' in data:
				ind = 0
				sock.connect((hn,p))
				time.sleep(0.75)
			if 'TS{' in data:
				break
		except:
			netcat(hn,p,content)

	
content = "1234"

netcat(hostname, port, content.encode())
