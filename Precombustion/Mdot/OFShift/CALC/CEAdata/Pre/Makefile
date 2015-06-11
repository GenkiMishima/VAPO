OUTPUT  :=PreRead
FAST    :=-parallel -fast
DEBUG   :=-check -traceback
COMP    :=ifort

#COMP :=$(COMP) $(DEBUG)
COMP :=$(COMP) $(FAST)
HEAD = 
SUB  = 

all:$(OUTPUT)

$(OUTPUT): $(OUTPUT).f90 $(HEAD) $(SUB)
	$(COMP) $^ -o $@
clean:remove
	rm -rf $(OUTPUT)
remove:
cleandata:remove
	rm -rf $(OUTPUT) *.d
remove:

