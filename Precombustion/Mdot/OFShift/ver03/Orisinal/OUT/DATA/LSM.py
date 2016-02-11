import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    return 5.*x + 10.

#Pusedo measured data by random number
xdata = np.linspace(-10, 10, num=101)
np.random.seed(1234)
ydata = f(xdata) + 5.*np.random.randn(xdata.size)

#Least squares method with scipy.optimize
def fit_func(parameter,x,y):
    a = parameter[0]
    b = parameter[1]
    residual = y-(a*x+b)
    return residual

parameter0 = [0.,0.]
result = optimize.leastsq(fit_func,parameter0,args=(xdata,ydata))
print(result)
a_fit=result[0][0]
b_fit=result[0][1]

print(a_fit,b_fit)

#PLot
plt.figure(figsize=(8,5))
plt.plot(xdata,ydata,'bo', label='Exp.')
plt.plot(xdata,a_fit*xdata+b_fit,'k-', label='fitted line', linewidth=10, alpha=0.3)
plt.plot(xdata,f(xdata),'r-', label='mother line', linewidth=3)
plt.xlabel('Time')
plt.ylabel('Verocity')
plt.legend(loc='best',fancybox=True, shadow=True)
plt.grid(True)
plt.show()
