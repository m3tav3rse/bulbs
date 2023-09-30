PORT := /dev/ttyUSB0

flash:
	ampy -p $(PORT) put lib/
	ampy -p $(PORT) put mod/
	ampy -p $(PORT) put boot.py
	ampy -p $(PORT) put main.py

config:
	ampy -p $(PORT) put conf.json

run:
	ampy -p $(PORT) run main.py

ifconfig:
	ampy -p $(PORT) run scripts/ifconfig.py

test:
	pytest -v

setup:
	pip install -r requirements.txt

clean:
	ampy -p $(PORT) rmdir lib/
	ampy -p $(PORT) rmdir mod/
	ampy -p $(PORT) rm boot.py
	ampy -p $(PORT) rm main.py
	rm -rf */__pycache__ .pytest_cache

