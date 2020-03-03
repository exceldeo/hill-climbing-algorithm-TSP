# nama:   Kresna Adhi Pramana - 05111840000072
#         excel deo cornelius - 05111840000117

import matplotlib.pyplot as plt
import networkx as nx

print('Weighted-Graph Model :')
G = nx.Graph()

G.add_edge('A', 'B', weight=9)
G.add_edge('A', 'C', weight=3)
G.add_edge('A', 'D', weight=2)
G.add_edge('A', 'E', weight=10)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'D', weight=7)
G.add_edge('B', 'E', weight=5)
G.add_edge('C', 'D', weight=4)
G.add_edge('C', 'E', weight=11)
G.add_edge('D', 'E', weight=6)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=800)
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()

# Initial Route
print('Initial Route :')
I = nx.DiGraph()

I.add_edges_from([('E', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D')])

pos = nx.spring_layout(I)

nx.draw_networkx_nodes(I, pos, node_size=800)
nx.draw_networkx_edges(I, pos, node_size=800,
                       arrowstyle='->', arrowsize=10, width=2)
nx.draw_networkx_labels(I, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()
print('Cost : 18')
print()

# Hill Climbing
print("--------------- Hill-Climbing ---------------")
cost = [[0, 9, 3, 2, 10], [9, 0, 8, 7, 5], [
    3, 8, 0, 4, 11], [2, 7, 4, 0, 6], [10, 5, 11, 6, 0]]
init = ['E', 'B', 'C', 'A', 'D']
new = init.copy()
temp = init.copy()
base = 18
i = 0
count = 0
loop = 1
itr = 1
MST = 100
init2 = []
while(loop):
    loop = 0
    print("Iteration : ", itr)

    while(i < 5):
        for j in range(i, 5):
            if(i == j):
                continue
            tempPath = init[i]
            init[i] = init[j]
            init[j] = tempPath

            for x in range(0, 4):
                count = count + cost[ord(init[x])-65][ord(init[x+1])-65]
#                 print(count)
            if MST > count:
                MST = count
                init2 = init
            print("Path : ", init, "Cost : ", count)
            # print("mst: ", MST)
            if(count < base):
                new = init
                base = count
                print("New Initial Route : ", new, "Cost : ", base)
                loop = 1

            count = 0
            init = temp.copy()

        i += 1

    print()
    init = new.copy()
    itr += 1
    i = 0

print("Path : ", init2, "MST : ", MST)
print("MST graph: ")
I = nx.DiGraph()

a = len(init2)
it = 0
while it < a - 1:
    ij = it + 1
    I.add_edges_from([(init2[it], init2[ij])])
    it += 1

pos = nx.spring_layout(I)

nx.draw_networkx_nodes(I, pos, node_size=800)
nx.draw_networkx_edges(I, pos, node_size=800,
                       arrowstyle='->', arrowsize=10, width=2)
nx.draw_networkx_labels(I, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()
