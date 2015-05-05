set terminal png
set key below
set output "out.png"
set grid
set xlabel "x"
set ylabel "temp"
set yrange [0:1000]
p 'Output/O2_out001.d'w l,'Output/O2_out002.d'w l,'Output/O2_out003.d'w l,'Output/O2_out004.d'w l,'Output/O2_out005.d'w l,'Output/O2_out006.d'w l,'Output/O2_out007.d'w l,'Output/O2_out008.d'w l,'Output/O2_out009.d'w l,'Output/O2_out010.d'w l
