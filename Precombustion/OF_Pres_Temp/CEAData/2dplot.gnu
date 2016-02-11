set terminal postscript eps enhanced color
set output "OF_T.eps"
set xlabel "O/F"
set ylabel "Temperature[K]"

plot "Ideal_0400.d" using 2:3 with linespoints title "0.4MPaA",\
     "Ideal_0600.d" using 2:3 with linespoints title "0.6MPaA"
