import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
with open('oddExperiment.txt') as f :
    lines = f.readlines()
for i in range(22) :
    lines[i] = lines[i].split(" ")

x = []
y = []
for i in range(1, 22) :
    x.append(int(lines[i][1].strip()))
    y.append(float(lines[i][0].strip()))
plt.scatter(x, y, label = "Data")
po1 = np.polyfit(x, y, deg = 1)
po2= np.polyfit(x, y, deg = 2)
x_1 = np.arange(x[0],x[20],0.01)
y_1 = po1[0]*x_1+po1[1]
y_2 = po2[0]*x_1**2+po2[1]*x_1+po2[2]
x_2 = np.arange(x[0],x[20]+1)
y_3 = po1[0]*x_2+po1[1]
y_4 = po2[0]*x_2**2+po2[1]*x_2+po2[2]

Suma = 0
Sumb = 0
for i in range(len(x)) :
    Suma = Suma + (y[i]-y_3[i])**2
    Sumb = Sumb + (y[i]-y_4[i])**2
avg1 = round((Suma/len(x)),5)
avg2 = round((Sumb/len(x)),5)

plt.plot(x_1, y_1, label = f"Fit of degree 1,LSE = {avg1}", color = "red")
plt.plot(x_1, y_2, label = f"Fit of degree 2,LSE = {avg2}", color = "purple")
plt.title('oddExperiment Data')
plt.legend()
plt.show()
plt.savefig("lab12_plus.png")