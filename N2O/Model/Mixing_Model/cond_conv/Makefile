main: main.f90
	ifort -xHOST -O3 -static -parallel $^
clean:remove
	rm -rf Output/* a.out out.png *.d
remove:
