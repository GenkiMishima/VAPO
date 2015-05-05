program main
implicit none
integer i,j
double precision k,R,T
double precision c,Cf,isp

k=1.1864d0
R=302.344d0
T=2318.98d0
Cf=1.6376d0

c=dsqrt(k*R*T)/(k*dsqrt((2d0/(k+1))**((k+1)/(k-1))))
isp=c*Cf/9.8d0
print *,c,isp



end program main
