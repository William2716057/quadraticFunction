import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(a, b, c):
    #generate x values
    x =np.linspace(-10, 10, 400)
    #comput y values
    y = a * x**2 + b * x + c
    
    #create plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a}x^2 + {b}x + c')
    
    #add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Plot of the Quadratic Function {a}x^2 + {b}x + c')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    
    #show plot
    plt.show()
    
a = float(input("Enter a: ")) #1 
b = float(input("Enter b: ")) #-3
c = float(input("Enter c: ")) #2

plot_quadratic(a, b, c)