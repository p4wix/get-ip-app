from flask import Flask, request
from requests import get
from flask_accept import accept
from socket import gethostname, gethostbyname


app = Flask(__name__)

# List of acceptable headers
# curl localhost:5000 -H "Accept: text/xml"
# https://pypi.org/project/flask_accept/


@app.route('/')
@accept("text/html", "text/xml", "text/yaml", "text/txt")
def index():
	# ip = get('https://api.ipify.org').content.decode('utf8')
	ip = get_ip()
	to_add = check_file(ip)
	if not to_add:
		add_to_file(ip)
	list_of_ip = display_list_of_ip()
	# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
	return "Your ip: {}, visited by {}".format(ip, ' '.join(list_of_ip))


def get_ip():
	hostname = gethostname()
	ip = gethostbyname(hostname)
	return ip


def check_file(current_ip):
	with open('ip_list.txt', "r") as f:
		for line in f:
			if current_ip + ';\n' == line:
				return True
		return False


def add_to_file(current_ip):
	with open('ip_list.txt', "a") as f:
		f.write(f'{current_ip};\n')


def display_list_of_ip():
	tab = []
	with open('ip_list.txt', "r") as f:
		for line in f:
			tab.append(line)
	return tab


if __name__ == '__main__':
	app.run(host='0.0.0.0')
