from matplotlib import colors, pyplot as plt
legenda = ['12-17', '18-19', '20-29', '30-39', '40-49', '50-59', '60-64', '65-69', '70-74','75-79', '80+']

valores = [0, 34060, 365567, 479944, 728411, 774344, 350496, 309785, 216826, 144659, 132884 ]

back = plt.axes()

back.set_facecolor('orange')

plt.bar(legenda,valores, color='purple',)

for i, v in enumerate(valores):
    plt.text(x=i-0.2,
             y = v,
             s=f'{v}')

plt.show()
