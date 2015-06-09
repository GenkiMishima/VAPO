OUTPUT  :=Mycompile
FAST    :=-parallel -fast
DEBUG   :=-check -traceback
COMP    :=gfortran

#COMP :=$(COMP) $(DEBUG)
#COMP :=$(COMP) $(FAST)
COMP :=$(COMP) 
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
