init:
	sudo apt-get install python3-pygame	
	pip3 install -r requirements.txt
test:
	nosetests tests
