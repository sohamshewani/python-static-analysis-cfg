all: build test

build:
	make -C src

src:
	cd src && python3 -m pip install -r requirements.txt

test:
	make -C tests

clean:
	make -C src clean
	make -C tests clean
