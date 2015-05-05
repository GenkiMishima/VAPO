set grid
set xlabel "MIXTURE_RATIO" font 'Arial,17'
set ylabel "Isp" font 'Arial,17'
set xrange [0:15]
set yrange [200:320]
set terminal png
set key inside t r
set output "Isp.png"
p './O2/compile.d'w lp title "O2",'./N2O/compile.d'w lp title "N2O",'./MIXED_1_9/compile.d'w lp title "[N2O:O2] 1:9",'./MIXED_1_5/compile.d'w lp title "1:5",'./MIXED_1_2/compile.d'w lp title "1:2"
