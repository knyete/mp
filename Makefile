# mp
# Makefile


PHONY: create-virtualenv pip-install clean docs help
DEV=/dev/ttyUSB0

create-virtualenv:
	mkvirtualenv -p python3 $(NAME)

pip-install:
	pip install -r requirements.txt

clean:
	../dev-scp/clean.sh && rm -rf tmp/index.html tmp/docs.zip

docs:
	rst2html README.rst > tmp/index.html && zip tmp/docs.zip tmp/index.html

shell:
	picocom $(DEV) -b 115200


help:
	@echo "    create-virtualenv:"
	@echo "        Creates virtualenv."
	@echo "    pip-install:"
	@echo "        Install common and development requirements."
	@echo "    clean:"
	@echo "        Remove useless and autogenerated files."
	@echo "    docs:"
	@echo "        Build docs."
	@echo "    shell:"
	@echo "        Connect to device REPL."
