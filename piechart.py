import matplotlib.pyplot as plt
def drawPieChart(react):
    fig1,ax1 = plt.subplots()
    r = {k:v for k,v in react.items() if v}
    color = ['#DA33FF','#FF3333','#BDFF33','#FF9033','#3334FF','#9BFF33','#102C1D']
    ax1.pie(r.values(),labels=r.keys(),colors=color,autopct='%1.0f%%',pctdistance=1.1,labeldistance=1.2,shadow=True)
    ax1.axis('equal')
    plt.title("Facebook Reactions")
    plt.show()
    plt.savefig('piechart.png')
