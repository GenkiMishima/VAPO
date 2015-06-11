include ../Makefile.inc
OUTPUT  :=Mycompile

COMP :=$(COMP) $(FLAGS)

all:$(OUTPUT)

$(OUTPUT): $(OUTPUT).f $(HEAD) $(SUB)
	$(COMP) $^ -o $@
clean:remove
	rm -rf $(OUTPUT)
remove:
