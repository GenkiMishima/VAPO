program main
implicit none
integer i,j
double precision a,b,c,d
double precision ox,fu,mixture_rate,isp
double precision temp(10)
double precision,parameter::ch4=1.00794d0*4d0+12.0107d0
double precision,parameter::o2=15.9994d0*2d0
double precision,parameter::N2O=14.0067d0*2d0+15.9994d0


character*30 word(10)

open(44,file='raw.d')
open(55,file='compile.d')
do i=1,2000
   read(44,*) word(1)
   fu=0d0
   ox=0d0
   if(word(1).eq.'REACTANT')then
      read(44,*)
      do j=1,3
      read(44,*) word(1),word(2),a
         if(word(1).eq.'FUEL') then
            if(word(2).eq.'CH4') then
               temp(1)=ch4 
            end if
            a=a*temp(1)
            !print *,a
          
            fu=fu+a
         else if(word(1).eq.'OXIDANT') then
            if(word(2).eq.'N2O') then
               temp(1)=N2O
            else if(word(2).eq.'O2') then
               temp(1)=O2
            end if
            a=a*temp(1)
            !print *,a
            ox=ox+a
         end if
      end do 
      mixture_rate=ox/fu
      !print *,mixture_rate
   else if(word(1).eq.'PERFORMANCE')then
      !print *, 'ok'
      a=0d0
      read(44,*)
      read(44,'(A,e15.7e3)') word(1),a
      read(44,*) word(1),word(2),a,b,c,d
      read(44,*) word(1),a
      read(44,*) word(1),word(2),a
      read(44,*) word(1),word(2),a,b,isp,d
      write(55,*),mixture_rate, isp/9.80665d0
      !print *, a,b,isp
      !if(word(1).eq.'PERFORMANCE')then
   end if
   !print *, mixture_rate,isp
   
end do


close(44)
close(55)



end program main
