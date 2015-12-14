module precision_mod
integer,parameter :: d8 = selected_real_kind(8)
end module precision_mod

program main
use precision_mod
implicit none
real(d8)::mean
real(d8)::std

mean = 6
std = 5
call gauss( mean, std)
end program main

subroutine gauss( mean, std )
use precision_mod
implicit none
real(d8)::x
real(d8)::mean
real(d8)::std
intent(in)::mean,std

integer :: i
integer :: n=100
real(d8)::f
real(d8),parameter::pi=4*atan(1.0)

open (66,file='output.d')
do i=1,n
x=rand(0)
f = 1 / sqrt(2*pi*std**2) * exp (-( (x-mean)**2 / (2*std**2 ) ))
print*,f
write(66,*) f
end do 
close(66)
end subroutine gauss
