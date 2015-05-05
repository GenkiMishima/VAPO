program spherical_heat_transfer
!TEMPLATE{{{
implicit none
integer i,j,step
integer,parameter :: n=1e3
integer,parameter :: raw_data=2407
integer,parameter :: out_time=1e1
double precision,dimension(0:n)::T,Tn,dent,RHS
double precision,dimension(0:n)::ri
double precision,dimension(14,raw_data)::O2
double precision dr,dt,k,kj,kk,rho,c,rj,rk,alpha,time,ent,x,ans
double precision tmp(5)
double precision,parameter :: rw=1d-3
double precision,parameter :: r=rw+8.74d-4
double precision,parameter :: p=3.3d6
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

   tmp(1)=r/dble(n)
   time=0d0
   ent=0d0
   T=1d3
   T(0:5e2)=90d0
   !do step=1,out_time*1e2
   do step=1,2
      T(0)=T(1)
      T(n)=8d2
      do j=1,raw_data
         rho=0.5d0*(O2(j, 3)+O2(j-1, 3))
         c  =0.5d0*(O2(j, 9)+O2(j-1, 9))
         k  =0.5d0*(O2(j,13)+O2(j-1,13))
         alpha=k/(rho*c)
         dt=min(dt,dr**2/(2d0*abs(alpha))*CFL)
         dt=1d-7
      end do
      do i=1,n-1
         do j=1,raw_data
            if(O2(j,1)>=T(i))then
               rho=O2(j, 3)
               c  =O2(j, 9)
               kj =0.5d0*(O2(j,13)+O2(j+1,13))
               kk =0.5d0*(O2(j,13)+O2(j-1,13))
            exit
            end if
         end do
         rj=0.5d0*(ri(i+1)+ri(i))
         rk=0.5d0*(ri(i-1)+ri(i))
         tmp(1)=rj**2*kj*(T(i+1)-T(i  ))/dr
         tmp(2)=rk**2*kk*(T(i  )-T(i-1))/dr
         tmp(3)=1d0/(rho*c*ri(i)**2)
         if(T(i)<144d0)then
            tmp(5)=tmp(3)*(tmp(1)-tmp(2))
            !!RUNGE_KUTTA
            !x=abs(i)*dt
            !call RK4(x,tmp(5),dt,ans)
            !Tn(i)=ans
            Tn(i)=dt*tmp(5)
         elseif(T(i)>=144d0)then
            tmp(5)=tmp(3)*(tmp(1)-tmp(2))
            !!RUNGE_KUTTA
            !x=abs(i)*dt
            !call RK4(x,tmp(5),dt,ans)
            !Tn(i)=ans
            Tn(i)=dt*tmp(5)
            dent(i)=Tn(i)+dent(i)
         elseif(dent(i)>=110d0)then
            tmp(4)=0d0
            tmp(5)=tmp(3)*(tmp(1)-tmp(2))+tmp(4)/(rho*c)+T(i)
            !eular
            Tn(i)=dt*tmp(5)
            !RUNGE_KUTTA
            !x=abs(i)*dt
            !call RK4(x,tmp(5),dt,ans)
            !Tn(i)=ans
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
