RHO:7.93*10^-3; /*[g/mm3]*/
t:3$/*[mm]*/
D:210$/*[mm]*/
Dt:D+t$
H:210$/*[mm]*/
Volume_per:3.141592/4*H*((D+t)^2-D^2);/*[mm3]*/
Mass_per:RHO*Volume_per;/*[g]*/
4/3*3.141592*(D/2*D/10*D/2);
/*Volume_bot:4/3*3.141592*((D+t)^3-D^3);*/
Volume_bot:4/3*3.141592*(Dt/2*Dt/10*Dt/2-D/2*D/10*D/2);
Mass_bot:RHO*Volume_bot;/*[g]*/
Mass:Mass_bot+Mass_per+7150;/*[g]*/
