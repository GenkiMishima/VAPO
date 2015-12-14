/*Combustion Chamber*/
RHO:7.93*10^-3$ /*[g/mm3] Stenless*/
t:3$/*[mm] Thickness*/
D:210$/*[mm] Diameter*/
Dt:D+t$
H:210$/*[mm] Height*/
Bot_A:Dt/2;
Bot_B:Dt/10;
Bot_C:Dt/2;
Volume_per:3.141592/4*H*((D+t)^2-D^2);/*[mm3]*/
Mass_per:RHO*Volume_per;/*[g]*/
4/3*3.141592*(D/2*D/10*D/2);
/*Volume_bot:4/3*3.141592*((D+t)^3-D^3);*/
Volume_bot:4/3*3.141592*(Dt/2*Dt/10*Dt/2-D/2*D/10*D/2);
Mass_bot:RHO*Volume_bot;/*[g]*/
Mass_CC:Mass_bot+Mass_per;

/*Mixing Chamber*/
Mass_MC:Mass_per;

/*Graphite Baffle Plate*/

/*Graphite Nozzle*/

/*Grain*/
Mass_Grain:7150.0$/*[g]*/
Mass:Mass_CC+Mass_MC+Mass_Grain;/*[g]*/
