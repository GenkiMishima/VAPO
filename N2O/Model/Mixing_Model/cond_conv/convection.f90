subroutine convection(mu,mu_w,Nu)
implicit none
double precision,parameter:: Re = 3.5d2
double precision,parameter:: Pr = 7.d-1
double precision,intent( in)::mu/mu_w
double precision,intent(out)::Nu

Nu = 2d0+(4d-1*Re**0.5+6d-2*Re**(2d0/3d0))*Pr**0.4*(mu/mu_w)**0.25
end subroutine convection
