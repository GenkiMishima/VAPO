program main
implicit none
integer i,j
integer,parameter::n=10
double precision,parameter::T0=273.15d0
double precision,parameter::R0=8.314d0

double precision,dimension(n):: LV,SV,FL,T,x,Nox
double precision tau,pi,y,H,k1,k2,T1,T2,SVs,p1,p2,Mol,rho,R,x0,p,p0

!open(55,file='showa_raw.d')
!do i=1,n
!read(55,*) LV(i),SV(i),FL(i),T(i),x(i),Nox(i)
!end do
!close(55)
!
!x=x/1d2-1d-10
!
!T2=T0+25d0
!p2=rho*R/Mol*T2
!open(55,file='showa_are.d')
!open(56,file='arrhenius_pressure.d')
!do i=1,n
!SVs=SV(i)/3600d0
!T1=T(i)+T0
!p1=rho*R/Mol*T1
!!k=(T1/T2)*SVs*(2d0*log(1d0/(1d0-x(i)))-x(i))
!k1=(T1/T2)*SVs*(x(i)-0.5d0*x(i)**2)
!write(56,*)k1,k2
!end do
!!close(55)
!close(56)

Mol = 44.0128d-3
R=R0/Mol
x0=0.9999999d0
rho = 48d0
p0=89d0*R/Mol*298.15d0
open(55,file='sv_pressure.d')
do i=1,100
p=0.101325d6*5d1*(1+dble(i)*1d-2)
t1=p/(rho*R)
!k=2580.4d0*exp(-735.7469d0*32d0/p)
SVs=2580.4d0*exp(-735.7469d0*rho/p)*(298.15d0/(p/(rho*R)))/(x0-0.5d0*x0**2)
write(55,*)p,SVs,t1,36630d0*3600d0
enddo
close(55)
end program main

