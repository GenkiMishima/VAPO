program main
implicit none
integer i,j
integer,parameter::n=10
double precision,dimension(n)::LV,SV,FL,Tem,x,nox

open(55,file='showa_raw.d')
do i=1,n
read(55,*) LV(i),SV(i),FL(i),Tem(i),x(i),nox(i)
end do
close(55)



!do i=1,n
!print *, LV(i),SV(i),FL(i),Tem(i),x(i),nox(i)
!end do
end program main
