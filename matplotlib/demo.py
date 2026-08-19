import matplotlib.pyplot as plt

print(plt.style.available)

plt.style.use('seaborn-v0_8')

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496, 42000, 46572, 49320,53200,
         56000,62316,64928,67317,68748,73752]

plt.plot(ages_x, dev_y,color='#444444',linestyle='--',marker='o',label = 'All Devs')

py_dev_y = [48496, 52000, 56572, 59320,63200,
         66000,72316,74928,77317,78748,83752]
plt.plot(ages_x + 0.25, py_dev_y, '.b-.',label = 'Python Developers',linewidth=3)

plt.xlabel('Ages')
plt.ylabel('Salary (USD)')
plt.title('Median salary (USD) by Age')
plt.grid()
plt.legend()
plt.show()