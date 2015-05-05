module prmtr
implicit none
integer,parameter:: ni = 100
integer,parameter:: nj = 30
integer,parameter:: dime = 2
double precision,parameter:: m = 16.d0
double precision,parameter:: pi = 3.14159265d0
double precision,parameter:: kb = 1.3806488d-23
double precision,parameter:: T = 3d2
double precision,parameter:: nu = 1.512d-5
double precision,parameter:: dt = 1d-8
end module prmtr
module variable
use prmtr
implicit none
double precision rho,u,v,Vel,t_now,tmp(1:5)
double precision,dimension(1:8):: Par
double precision,dimension(1:8,1:2):: ev
double precision,dimension(ni+1,nj+1):: lambda
double precision,dimension(1:3,ni+1,nj+1):: w
double precision,dimension(ni+1,nj+1,0:8):: f,df,Nf
character*20 tmpstring
end module variable
program main
use prmtr
use variable
implicit none
!Set_variable{{{
integer i,j,num,time

!}}}

!Call_set_IC
w(1,:,:)=1.2d0
w(2,:,:)=1d1
w(3,:,:)=0d0

ev(0,1) = 0d0
ev(0,2) = 0d0
ev(1,1) = 1d0
ev(1,2) = 0d0
ev(2,1) = 1d0
ev(2,2) = 1d0
ev(3,1) = 0d0
ev(3,2) = 1d0
ev(4,1) =-1d0
ev(4,2) = 1d0
ev(5,1) =-1d0
ev(5,2) = 0d0
ev(6,1) =-1d0
ev(6,2) =-1d0
ev(7,1) = 0d0
ev(7,2) =-1d0
ev(8,1) = 1d0
ev(8,2) =-1d0

lambda(:,:) = 5d-1+3d0*nu/(w(2,:,:)**2+w(3,:,:)**2*dt)

Par(0) = 4d0/9d0 
do i = 1,num
   if (mod(i,2)==0)then
      Par(i) = 1d0/36d0
   else
      Par(i) = 1d0/9d0
   end if
end do

t_now=0d0
do time=1,100
   t_now=dt+t_now
   !Call_set_BC
   do i=0,ni+1
      f(i, 0,:)=0d0!-f(i, 0)
      f(i, 0,:)=0d0!-f(i, 0)
      f(i, 0,:)=0d0!-f(i, 0)
      f(i,31,:)=0d0!-f(i,31)
      f(i,31,:)=0d0!-f(i,31)
      f(i,31,:)=0d0!-f(i,31)
   end do
   do j=0,nj+1
      call MBD(1d1,0d0,0d0,dime,tmp(1))
      f(  0,j,:)=tmp(1)!-df(  0,j,8)
      f(  0,j,:)=tmp(1)!-df(  0,j,1)
      f(  0,j,:)=tmp(1)!-df(  0,j,2)
      f(101,j,:)=f(100,j,:)! df(101,j,3)
      f(101,j,:)=f(100,j,:)! df(101,j,6)
      f(101,j,:)=f(100,j,:)! df(101,j,8)
   end do
   !Call_set_Particle
   do j = 1,nj
      do i = 1,ni
      rho = w(1,i,j)
        u = w(2,i,j)
        v = w(3,i,j)
      Vel = u**2+v**2
         do num = 0,8
            tmp(1) = ev(num,1)*u+ev(num,2)*v
            df(i,j,num)=Par(num)*rho*(1d0+3d0*tmp(1)+9d0/2d0*tmp(1)**2-3d0/2d0*Vel)
         end do
      end do
   end do
   !Call_set_BGK
   do j = 1,nj
      do i = 1,ni
         do num = 0,8
            Nf(i,j,num)=f(i,j,num)-1d0/lambda(i,j)*(f(i,j,num)-df(i,j,num))
         end do
      end do
   end do
!Call_set_NValue
   do j = 1,nj
      do i = 1,ni
         tmp = 0d0
         do num = 0,8
            tmp(1) = Nf(i,j,num) + tmp(1)
            tmp(2) = Nf(i,j,num)*ev(num,1) + tmp(2)
            tmp(3) = Nf(i,j,num)*ev(num,2) + tmp(3)
         end do
         w(1,i,j) = tmp(1)
         w(2,i,j) = tmp(2)/w(1,i,j)
         w(3,i,j) = tmp(3)/w(1,i,j)
         lambda(i,j) = 5d-1+3d0*nu/(w(2,i,j)**2+w(3,i,j)**2*dt)
      end do
   end do
!Call_set_Judge
   !if(time==1.or.(mod(time,out_time)== 0).or.temp_int==1) then
      write(tmpstring,'(i3.3)') int(time)
      open(10, file='data/density_'//trim(tmpstring)//'.d')
      open(11, file='data/U_Velocity_'//trim(tmpstring)//'.d')
      open(12, file='data/V_Velocity_'//trim(tmpstring)//'.d')
!      !$omp parallel do private(i)
      do j=1,nj
         do i=1,ni
            write(10, *) w(1,i,j)
            write(11, *) w(2,i,j)
            write(12, *) w(3,i,j)
         enddo
      enddo
!      !$omp end parallel do
      close(10)
      close(11)
      close(12)
   !end if
end do
end program main
subroutine MBD(u,v,w,d,ans)
use prmtr
implicit none
integer,intent(in)::d
double precision,intent( in)::u,v,w
double precision,intent(out)::ans
ans = (m/(2d0*pi*kb*T))**(dble(d)/3)*exp(-m*(u**2+v**2+w**2)/(2d0*kb*T))
end subroutine MBD
