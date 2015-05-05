program spherical_heat_transfer
!TEMPLATE{{{
implicit none
integer i,j,step,num_sur,check
integer,parameter :: n=1e3
integer,parameter :: raw_data=2407
integer,parameter :: out_time=3e4
double precision,dimension(0:n)::T,Tn,dent
double precision,dimension(0:n)::ri
double precision,dimension(14,raw_data)::O2
double precision dr,k,rho,c,rj,rk,alpha,time,ent,kj,kk,mu,mu_f,Re,HH
double precision tmp(5)
double precision,parameter :: rl=1d-3
double precision,parameter :: rg=8.3d-4
double precision,parameter :: r=rl+rg
double precision,parameter :: dt=1d-8
!double precision,parameter :: r=rl
double precision,parameter :: p=3.3d6
double precision,parameter :: pr=7d-1
!double precision,parameter :: Re=11327.32
double precision,parameter :: CFL=0.5d0
character *20 tmpstring
!}}}
!READ{{{
   open(44,file='Input/O2_data.d')
      do j=1,raw_data-1
         read(44,*) (O2(i,j),i=1,13)
      end do
   close(44)
   dr=r/dble(n)
   do i=0,n
      ri(i)=dr*dble(i)
   end do
!}}}
   num_sur=int(dble(n)*rl/r)
   time=0d0
   dent=0d0
   T=9d1
   T(num_sur:n)=8d2
   check=0
   do j=1,raw_data
      if(O2(1,j)>=T(num_sur).and.check==0)then
         mu=O2(12,j)*1d-6
         k =O2(13,j)
         check=1
      elseif(O2(1,j)>=T(n))then
         mu_f=O2(12,j)*1d-6
      exit
      end if
   end do
   HH=2d0*k/rl
   print *, k,mu,rl,HH
   
   open(45,file='Output/O2_out000.d')
   do i=1,n-1
      write(45,*) ri(i),T(i)
   end do
   close(45)
   do step=1,out_time*1e1
      T(0)=T(1)
      T(n)=T(n-1)
      do i=1,n-1
         do j=1,raw_data
            if(O2(j,1)>=T(i))then
               rho=O2( 3,j)
               c  =O2( 9,j)
               mu =O2(12,j)*1d-6
               k  =O2(13,j)
            exit
            end if
         end do
         rj=0.5d0*(ri(i+1)+ri(i))
         rk=0.5d0*(ri(i-1)+ri(i))
         alpha=1d0/(rho*c)
         tmp(1)=rj**2*k*(T(i+1)-T(i  ))/dr
         tmp(2)=rk**2*k*(T(i  )-T(i-1))/dr
         !if(T(i).lt.144d0.or.dent(i).ge.110d0)then
         if((T(i).lt.144d0).or.(i.ge.num_sur))then
            Tn(i)=dt*alpha/(dr*ri(i)**2)*(tmp(1)-tmp(2))+T(i)
            !tmp(3)=alpha/(dr*ri(i)**2)*(tmp(1)-tmp(2))
            !call RK4(ri(i),tmp(3),dt,Tn(i))
         elseif(dent(i).ge.110d0)then
         !elseif(dent(i).eq.110d0)then
            Re = (2d0*ri(i)*rho)/mu
            tmp(4)=2d0+(4d-1*Re**5d-1+6d-2*Re**6.6d-1)*Pr**4d-1*(mu_f/mu)**0.25
            !print *,i,tmp(4)/(2d0*ri(i))*k
            tmp(4)=tmp(4)*k/(2d0*ri(i))*(T(n)-T(i))
            !print *,i,tmp(4)
            !call exit
            tmp(4)=tmp(4)/c
            !Tn(i)=T(i)-tmp(4)
            num_sur=i
         elseif(T(i).ge.144d0)then
            tmp(3)=dt*alpha/(dr*ri(i)**2)*(tmp(1)-tmp(2))
            !call RK4(ri(i),tmp(3),dt,tmp(4))
            dent(i)=tmp(3)+dent(i)
            !temp(i)=1d0
         end if
      end do
      T=Tn
      if(mod(step,out_time)==0)then
         write(tmpstring,'(i3.3)') int(step/out_time)
         open(45,file='Output/O2_out'//trim(tmpstring)//'.d')
         do i=1,n-1
            write(45,*) ri(i),T(i)
         end do
         close(45)
         print *,time
      end if
      if(T(1)>300d0)exit

      time=dt+time
   end do
   print *,time,step,T(1)
end program spherical_heat_transfer
subroutine RK4(x,y,h,ans)
implicit none
double precision k1,k2,k3,k4
double precision,intent( in):: x,y,h
double precision,intent(out):: ans

!x_n = x+h

k1  = f(x        ,y           )
k2  = f(x+0.5d0*h,y+0.5d0*h*k1)
k3  = f(x+0.5d0*h,y+0.5d0*h*k2)
k4  = f(x+      h,y+      h*k3)
ans = y+h/6d0*(k1+2d0*k2+2d0*k3+k4)


contains
double precision function f(x,y)
double precision x,y
f=y
end function f

end subroutine RK4
