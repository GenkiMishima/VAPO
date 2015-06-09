program main
implicit none
character*20 ParaName
integer i,j
double precision, dimension(4)::Pre,Temp,Gmm,Ml,Isp
open (50,file='Pressure.d')
open (51,file='Temprature.d')
open (52,file='Gamma.d')
open (53,file='Mole.d')
open (54,file='Isp.d')
do i = 1,22
read (50,'(A15, F9.4, F9.4, F9.4, F9.4)') ParaName,Pre(1),Pre(2),Pre(3),Pre(4)
print *,'Pre',Pre
read (51,'(F9.4, F9.4, F9.4, F9.4)') Temp(1),Temp(2),Temp(3),Temp(4)
print *,'Temp',Temp
read (52,'(F9.4, F9.4, F9.4, F9.4)') Gmm(1),Gmm(2),Gmm(3),Gmm(4)
print *,'Gamma',Gmm
read (53,'(F9.4, F9.4, F9.4, F9.4)') Ml(1),Ml(2),Ml(3),Ml(4)
print *,'Mole',Ml
read (54,'(A15, F9.4, F9.4, F9.4, F9.4)') ParaName,Isp(1),Isp(2),Isp(3),Isp(4)
print *,'Isp',Isp
end do
close (50)
close (51)
close (52)
close (53)
close (54)
open (50,file='ReadFile.d')
write(50,'(F9.4,a1, F9.4,a1, F9.4,a1, F9.4,a1, F9.4)') Pre(1),',',Temp(1),',',Gmm(1),',',Ml(1),',',Isp(1)
close(50)


end program main
