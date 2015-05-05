program main
use prmtr
use vari
implicit none
do time = t_init, t_end
   call set_dt
   call set_BC
   call set_Cnd
   call set_Cnv
   call set_Flx
   call set_NxtT
   call set_Out
end do
end program main
