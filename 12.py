import math


def dist(t1, g1, t2, g2):
    t1 = math.radians(t1)
    g1 = math.radians(g1)
    t2 = math.radians(t2)
    g2 = math.radians(g2)
    dis = 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    return dis


print(dist(1, 1, 45,67))
