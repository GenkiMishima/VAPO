include ../Makefile.inc
OUTPUT  :=Mycompile
HEAD = 
SUB  = 

all:$(OUTPUT)

$(OUTPUT): $(OUTPUT).f $(HEAD) $(SUB)
	$(COMP) $^ -o $@
clean:remove
	rm -rf $(OUTPUT)
remove:





#compiler=ifort
#
#main: a.out
#
#a.out: cea2.f
#	 $(compiler) $^
#clean:remove
#	rm -rf a.out
#remove:
