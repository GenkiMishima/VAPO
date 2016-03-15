#COMP         := ifort 
COMP         := gfortran

#OPTIM        := -Wall -pedantic -std=f95 -fbounds-check -O -Wuninitialized -ffpe-trap=invalid,zero,overflow
#OPTIM        := -Wall -fbounds-check -O -Wuninitialized
#OPTIM        := -fast -parallel
OPTIM        := -O3 -w
DEBUG        := -g -fbacktrace -ffpe-trap=zero

FLAGS        := $(OPTIM)
#FLAGS        := $(DEBUG)

PARALLEL     :=
#PARALLEL     := -openmp

COMP         :=$(COMP) $(FLAGS) $(PARALLEL)
