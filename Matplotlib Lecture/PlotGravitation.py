import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitation force in Newtons')
    plt.title('Gravitation force vs distance')
    plt.show()

def generateForce():
    r = range (100, 900, 30)
    F = []
    G = 6.674*(10**-11)
    #2 vat the
    m1 = 100
    m2 = 50
    for dist in r:
        force = G * (m1 * m2) / (dist ** 2)
        F.append(force)

    draw_graph(r, F)

generateForce()