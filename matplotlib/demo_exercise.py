import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

years = [2019, 2020, 2021, 2022, 2023, 2024]
python_salary = [65000, 68000, 72000, 78000, 85000, 92000]
javascript_salary = [62000, 64000, 67000, 71000, 76000, 80000]
csharp_salary = [64000, 66000, 69000, 73000, 78000, 84000]

plt.figure(figsize=(10,6))
plt.plot(years, python_salary, label='python devs',linestyle='--',marker='o', color='k')
plt.plot(years,javascript_salary, label='js devs',linestyle='-.',marker='.', color='b')
plt.plot(years,csharp_salary, label='csharp devs', color='r',marker='.')
plt.title('Median salary by Salary')
plt.xlabel('year')
plt.ylabel('salary (USD)')
plt.legend()
plt.show()