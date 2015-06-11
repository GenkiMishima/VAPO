COMP         := ifort 
#COMP         := gfortran

OPTIM        := -fast -parallel
DEBUG        := -check -traceback

FLAGS        := $(OPTIM)
#FLAGS        := $(DEBUG)

#PARALLEL     :=
PARALLEL     := -openmp

COMP         :=$(COMP) $(OPTIM) $(PARALLEL)
