set terminal png
set key below
set output "out.png"
set grid
set xlabel "x"
set ylabel "temp"
set yrange [0:1100]
p 'Output/O2_out000.d'w l title'time:0d0','Output/O2_out001.d'w l title'time:2d-4','Output/O2_out002.d'w l title'time:4d-4','Output/O2_out003.d'w l title'time:6d-4','Output/O2_out004.d'w l title'time:8d-4','Output/O2_out005.d'w l title'time:1d-3','Output/O2_out006.d'w l title'time:1.2d-3','Output/O2_out007.d'w l title'time:1.4d-3','Output/O2_out008.d'w l title'time:1.6d-3','Output/O2_out009.d'w l title'time:1.8d-3','Output/O2_out010.d'w l
