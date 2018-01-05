from matplotlib import pyplot as pl,animation as anm
fig = pl.figure()
ax1 = fig.add_subplot(1,1,1)

def refreshInputData(i):
    print('Refreshing data...')
    graphData = open('graph_data.txt','r').read()
    lines = graphData.split('\n')
    xValues = []
    yValues = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xValues.append(x)
            yValues.append(y)
    ax1.clear()
    ax1.plot(xValues, yValues)

ani = anm.FuncAnimation(fig, refreshInputData, interval=1000)
pl.show()