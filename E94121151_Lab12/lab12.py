import numpy as np
import matplotlib.pyplot as plt
with open('Temperature.txt') as f :
    lines = f.readlines()
for i in range(1, 10) :
    lines[i] = lines[i].split(",")
    for j in range(len(lines[i])-1) :
        lines[i][j+1] = float(lines[i][j+1].strip())
    lines[i].remove(lines[i][0])
nums = np.linspace(1, 12, 12)
years = np.array(range(2013, 2022))
fig = plt.subplot(121)
for i in range(1,10) :
    fig.plot(nums, lines[i], label = years[i-1])
plt.title("Tainan Monthly Mean Temperature From 2013 To 2021")
plt.xlabel("Month")
fig.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.ylabel("Temperature in Degree C")
plt.ylim([15, 31]) 
plt.legend(loc = "lower center")

summ = 0
avg = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(12) :
    for j in range(1,10) :
        summ = summ + lines[j][i]
    avg[i] = round(summ/9, 2)
    summ = 0
suma = int(sum(avg)/12*100)*0.01
fig = plt.subplot(122)
fig.plot(nums, avg)
fig.scatter(nums, avg, color = "red")
for i, label in enumerate(avg):
    plt.text(nums[i], avg[i], label)
fig.axhline(y=suma, color = "red", label = "Mean of 9 Years", linestyle ="--" )
plt.text(1, suma, suma)
plt.title("Tainan Monthly Mean Temperature Of 2013 To 2021")
plt.xlabel("Month")
fig.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.ylabel("Temperature in Degree C")
plt.ylim([16,32])
plt.legend()
plt.show()
fig = plt.figure(figsize=(15,6))
fig.savefig('lab12_03.png')