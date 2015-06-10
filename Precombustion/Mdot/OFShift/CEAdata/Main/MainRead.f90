program main
implicit none
character*20 ParaName
character(len=20) :: MoleName(15),val(4)
integer i,j
double precision, dimension(4)::Pre,Temp,Gmm,Ml,Isp
double precision, dimension(15,1:4)::Frac
open (50,file='Pressure.d')
open (51,file='Temprature.d')
open (52,file='Gamma.d')
open (53,file='Mole.d')
open (54,file='Isp.d')
read (50,'(A15, F9.4, F9.4, F9.4, F9.4)') ParaName,Pre(1),Pre(2),Pre(3),Pre(4)
read (51,'(F9.4, F9.4, F9.4, F9.4)') Temp(1),Temp(2),Temp(3),Temp(4)
read (52,'(F9.4, F9.4, F9.4, F9.4)') Gmm(1),Gmm(2),Gmm(3),Gmm(4)
read (53,'(F9.4, F9.4, F9.4, F9.4)') Ml(1),Ml(2),Ml(3),Ml(4)
read (54,'(A16, F9.4, F9.4, F9.4, F9.4)') ParaName,Isp(1),Isp(2),Isp(3),Isp(4)
close (50)
close (51)
close (52)
close (53)
close (54)

open (54,file='FracCount.d')
read(54,*) j
close (54)
open (54,file='Frac.d')
do i=1,j
!read(54,'(A18,F8.5,F8.5,F8.5,F8.5)')MoleName(i),Frac(i,1),Frac(i,2),Frac(i,3),Frac(i,4) 
read(54,'(A17,A9,A9,A9,A9)')MoleName(i),val(1),val(2),val(3),val(4)
read(val(:),*) Frac(i,:)

!Frac(i,:)=dble(val(:))
end do
close (54)
open (50,file='CH4.d')
write(50,*)
close(50)
open (50,file='CO2.d')
write(50,*)
close(50)
open (50,file='CO.d')
write(50,*)
close(50)
open (50,file='H.d')
write(50,*)
close(50)
open (50,file='H2.d')
write(50,*)
close(50)
open (50,file='H2O.d')
write(50,*)
close(50)
open (50,file='OH.d')
write(50,*)
close(50)
do i=1,j
  if(MoleName(i).eq.' CH4 ') then
    !open (50,file='MF_'//trim(i)//'.d',position='append')
    open (50,file='CH4.d',position='append')
    write(50,'(4es15.7)')Frac(i,1:4)
    close(50)
  elseif(MoleName(i).eq.' *CO2 ') then
    !open (50,file='MF_'//trim(i)//'.d',position='append')
    open (50,file='CO2.d',position='append')
    write(50,'(4es15.7)')Frac(i,1:4)
    close(50)
  elseif(MoleName(i).eq.' *CO ') then
    !open (50,file='MF_'//trim(i)//'.d',position='append')
    open (50,file='CO.d',position='append')
    write(50,'(4es15.7)')Frac(i,1:4)
    close(50)
  elseif(MoleName(i).eq.' *H ') then
    !open (50,file='MF_'//trim(i)//'.d',position='append')
    open (50,file='H.d',position='append')
    write(50,'(4es15.7)')Frac(i,1:4)
    close(50)
  elseif(MoleName(i).eq.' *H2 ') then
    !open (50,file='MF_'//trim(i)//'.d',position='append')
    open (50,file='H2.d',position='append')
    write(50,'(4es15.7)')Frac(i,1:4)
    close(50)
  elseif(MoleName(i).eq.' *H2O ') then
    !open (50,file='MF_'//trim(i)//'.d',position='append')
    open (50,file='H2O.d',position='append')
    write(50,'(4es15.7)')Frac(i,1:4)
    close(50)
  elseif(MoleName(i).eq.' *OH ') then
    !open (50,file='MF_'//trim(i)//'.d',position='append')
    open (50,file='OH.d',position='append')
    write(50,'(4es15.7)')Frac(i,1:4)
    close(50)
  end if
end do


open (50,file='ReadFile.d')
write(50,'(F9.4,a1, F9.4,a1, F9.4,a1, F9.4,a1, F9.4)') Pre(1),',',Temp(1),',',Gmm(1),',',Ml(1),',',Isp(2)
close(50)


end program main
