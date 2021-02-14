import networkx as nx
import json
import math
graph = nx.Graph()
stationsL = {"lonsdale quay (seabus)":(8,18), "waterfront":(7,17), "Burrnard station":(5,17), "Granville Station":(6,14) ,"Stadium–Chinatown Station":(8,13) ,"Main Street–Science World Station":(9,12) ,
                      "Commercial–Broadway Station":(11,11) ,"Nanaimo Station":(12,10) ,"29th Ave Station":(13,9) ,"Joyce–Collingwood Station":(14,8) ,"Patterson Station":(15,7), "Metrotown Station":(16,6), "Royal Oak Station":(17,5),
                      "Edmonds Station":(18,4), "22nd Street Station":(19,3), "New Westminster Station":(20,4), "Columbia Station":(21,4), "Scott Road Station":(22,4), "Gateway Station":(23,3), "Surrey Central Station":(23,2),
                      "King George Station":(23,1), "Lougheed Town Centre Station":(21,7), "Burquitlam Station":(22,8), "Moody Centre Station":(23,9), "Inlet Centre Station":(24,9), "Coquitlam Central Station":(25,9),
                      "Lincoln Station":(25,10), "Lafarge Lake–Douglas Station":(25,11), "Sapperton Station":(21,5), "Braid Station":(21,6), "Production Way–University Station":(20,7), "Lake City Way Station":(19,7), "Sperling–Burnaby Lake Station":(18,7),
                      "Holdom Station":(17,7),"Brentwood Town Centre Station":(16,7), "Gilmore Station":(15,7), "Rupert Station":(14,7), "Renfrew Station":(13,7), "VCC–Clark Station":(12,7), "vancover city center station":(5,14),
                      "yaletown-roundhouse station":(5,13), "olympic village station":(6,11), "Broadway–City Hall Station":(6,10), "King Edward Station":(6,9), "Oakridge–41st Ave Station":(6,8), "Langara–49th Ave Station":(6,7),
                      "Trinity Western University":(26,9),"Marine Drive Station":(6,5), "Bridgeport Station":(5,4), "Templeton Station":(3,4), "Sea Island Centre Station":(2,4),"YVR–Airport Station":(1,4), "Aberdeen Station":(4,3), "Lansdowne Station":(4,2), "Richmond–Brighouse Station":(4,1)}
stations = (["lonsdale quay (seabus)", "waterfront", "Burrnard station", "Granville Station" ,"Stadium–Chinatown Station" ,"Main Street–Science World Station" ,
                      "Commercial–Broadway Station" ,"Nanaimo Station" ,"29th Ave Station" ,"Joyce–Collingwood Station" ,"Patterson Station", "Metrotown Station", "Royal Oak Station",
                      "Edmonds Station", "22nd Street Station", "New Westminster Station", "Columbia Station", "Scott Road Station", "Gateway Station", "Surrey Central Station",
                      "King George Station", "Lougheed Town Centre Station", "Burquitlam Station", "Moody Centre Station", "Inlet Centre Station", "Coquitlam Central Station",
                      "Lincoln Station", "Lafarge Lake–Douglas Station", "Sapperton Station", "Braid Station", "Production Way–University Station", "Lake City Way Station", "Sperling–Burnaby Lake Station",
                      "Holdom Station", "Brentwood Town Centre Station", "Gilmore Station", "Rupert Station", "Renfrew Station", "VCC–Clark Station", "vancover city center station",
                      "yaletown-roundhouse station", "olympic village station", "Broadway–City Hall Station", "King Edward Station", "Oakridge–41st Ave Station", "Langara–49th Ave Station",
                      "Trinity Western University", "Marine Drive Station", "Bridgeport Station", "Templeton Station", "Sea Island Centre Station", "YVR–Airport Station", "Aberdeen Station", "Lansdowne Station", "Richmond–Brighouse Station"])
graph.add_nodes_from(stations)
graph.add_edges_from([("lonsdale quay (seabus)" , "waterfront" , {'weight': 13}),
               ("waterfront" , "Burrnard station" , {'weight': 2}),
               ("Burrnard station" , "Granville Station" , {'weight': 1}),
               ("Granville Station" , "Stadium–Chinatown Station" , {'weight': 1}),
               ("Stadium–Chinatown Station" , "Main Street–Science World Station" , {'weight': 2}),
               ("Main Street–Science World Station" , "Commercial–Broadway Station" , {'weight': 3}),
               ("Commercial–Broadway Station" , "Nanaimo Station" , {'weight': 2}),
               ("Nanaimo Station" , "29th Ave Station" , {'weight': 1}),
               ("29th Ave Station", "Joyce–Collingwood Station" , {'weight': 2}),
               ("Joyce–Collingwood Station" , "Patterson Station" , {'weight': 2}),
               ("Patterson Station" , "Metrotown Station" , {'weight': 2}),
               ("Metrotown Station" , "Royal Oak Station" , {'weight': 2}),
               ("Royal Oak Station" , "Edmonds Station" , {'weight': 3}),
               ("Edmonds Station" , "22nd Street Station" , {'weight': 2}),
               ("22nd Street Station" , "New Westminster Station" , {'weight': 2}),
               ("New Westminster Station" , "Columbia Station" , {'weight': 2}),
               ("Columbia Station" , "Scott Road Station" , {'weight': 3}),
               ("Scott Road Station" , "Gateway Station" , {'weight': 3}),
               ("Gateway Station" , "Surrey Central Station" , {'weight': 2}),
               ("Surrey Central Station" , "King George Station" , {'weight': 3}),
               ("Lougheed Town Centre Station" , "Burquitlam Station" , {'weight': 3}),
               ("Burquitlam Station" , "Moody Centre Station" , {'weight': 5}),
               ("Moody Centre Station" , "Inlet Centre Station" , {'weight': 2}),
               ("Inlet Centre Station" , "Coquitlam Central Station" , {'weight': 2}),
               ("Coquitlam Central Station" , "Lincoln Station" , {'weight': 1}),
               ("Lincoln Station" , "Lafarge Lake–Douglas Station" , {'weight': 1}),
               ("Columbia Station" , "Sapperton Station" , {'weight': 4}),
               ("Sapperton Station" , "Braid Station" , {'weight': 2}),
               ("Braid Station" , "Lougheed Town Centre Station" , {'weight': 3}),
               ("Lougheed Town Centre Station" , "Production Way–University Station" , {'weight': 2}),
               ("Production Way–University Station" , "Lake City Way Station" , {'weight': 3}),
               ("Lake City Way Station" , "Sperling–Burnaby Lake Station" , {'weight': 2}),
               ("Sperling–Burnaby Lake Station" , "Holdom Station" , {'weight': 2}),
               ("Holdom Station" , "Brentwood Town Centre Station" , {'weight': 2}),
               ("Brentwood Town Centre Station" , "Gilmore Station" , {'weight': 2}),
               ("Gilmore Station" , "Rupert Station" , {'weight': 2}),
               ("Rupert Station" , "Renfrew Station" , {'weight': 1}),
               ("Renfrew Station" , "Commercial–Broadway Station" , {'weight': 2}),
               ("Commercial–Broadway Station" , "VCC–Clark Station" , {'weight': 2}),
               ("waterfront" , "vancover city center station" , {'weight': 2}),
               ("vancover city center station" , "yaletown-roundhouse station" , {'weight': 2}),
               ("yaletown-roundhouse station" , "olympic village station" , {'weight': 2}),
               ("olympic village station" , "Broadway–City Hall Station" , {'weight': 2}),
               ("Broadway–City Hall Station" , "King Edward Station" , {'weight': 3}),
               ("King Edward Station" , "Oakridge–41st Ave Station" , {'weight': 3}),
               ("Oakridge–41st Ave Station" , "Langara–49th Ave Station" , {'weight': 1}),
               ("Langara–49th Ave Station" , "Marine Drive Station" , {'weight': 2}),
               ("Marine Drive Station" , "Bridgeport Station" , {'weight': 3}),
               ("Bridgeport Station" , "Templeton Station" , {'weight': 3}),
               ("Templeton Station" , "Sea Island Centre Station" , {'weight': 1}),
               ("Sea Island Centre Station" , "YVR–Airport Station" , {'weight': 2}),
               ("Bridgeport Station" , "Aberdeen Station" , {'weight': 2}),
               ("Aberdeen Station" , "Lansdowne Station" , {'weight': 2}),
               ("Lansdowne Station" , "Richmond–Brighouse Station" , {'weight': 4}),
               ("Surrey Central Station","Trinity Western University",{'weight':63})])

#returns path 
def breadthFirst(nodeS, nodeE, graph):
    pathBuild = nx.DiGraph()
    pathBuild.add_nodes_from(graph.nodes)
    path= []
    print("start")
    waight = 0
    frontier = []
    frontier.append(nodeS)
    node = nodeS
    visited = [node]
    count = 0
    while not len(frontier) == 0:
        count = count +1
        #print(node)
        #print(node == nodeE)
        #print(nodeE)
        if node == nodeE:
            #print(node)
            while not node == nodeS:
                #print(node)
                path.insert(0, node)
                for i in pathBuild.successors(node):
                    waight += graph.get_edge_data(i , node)['weight']

                    node = i        
                #print(node)
            path.insert(0, node)
            return (', '.join(path) +" "+ str(waight))
        node = frontier.pop(0)
        
        #print("\n node")
        #print(node)
        for i in graph.neighbors(node):
            #print(i)
            
            if not (i in visited):
                #print(graph.get_edge_data(i,node))
                #print(node + ", " + i + "\n")
                pathBuild.add_edge(i, node)
                #print(pathBuild.edges)
                frontier.append(i)
                visited.append(i)
                #print(frontier)
def depthFirst(nodeS, nodeE, graph):
       
    pathBuild = nx.DiGraph()
    pathBuild.add_nodes_from(graph.nodes)
    path= []
    print("start")
    visited = []
    waight = 0
    frontier = []
    frontier.append(nodeS)
    node = nodeS
    #count = 0
    while not len(frontier) == 0:
        node = frontier.pop()
        if node == nodeE:
            #print(node)
            while not node == nodeS:
                #print(node)
                path.insert(0, node)
                for i in pathBuild.successors(node):
                    waight += graph.get_edge_data(i , node)['weight']
                    node = i        
                print(waight)
            path.insert(0, node)
            return (', '.join(path) +" "+ str(waight))

        if not (node in visited):
            visited.append(node)
            for i in graph.neighbors(node):
                if not (i in visited):
                    pathBuild.add_edge(i, node)
                    print(i +", "+ node)
                    frontier.append(i)
            #print(frontier)

def newdepthFirst(nodeS, nodeE, graph):

    pathBuild = nx.DiGraph()
    pathBuild.add_nodes_from(graph.nodes)
    
    print("start")
    visited = []
    
    frontier = []
    frontier.append(nodeS)
    node = nodeS
    best = float('inf')
    bestPath = []
    while not len(frontier) == 0:
        
        if node == nodeE:
            path = []
            waight = 0
            #print(node)
            while not node == nodeS:
                #print(node)
                path.insert(0, node)
                for i in pathBuild.successors(node):
                    waight += graph.get_edge_data(i , node)['weight']
                    print(waight)
                    node = i

            path.insert(0, node)
            if waight < best:
                best = waight
                bestPath = path
                
        
        node = frontier.pop()
        if not (node in visited):
            visited.append(node)
            for i in graph.neighbors(node):
                if not (i in visited):
                    pathBuild.add_edge(i, node)
                    #print(i +", "+ node)
                    frontier.append(i)
            #print(frontier)

    #print(node)
    
    return(', '.join(bestPath) +" "+ str(best))

def dijkstra(nodeS, nodeE, graph):
    pathBuild = nx.DiGraph()
    pathBuild.add_nodes_from(graph.nodes)
    frontier = []
    dist = {nodeE: 0, "temp": float('inf')}
    for node in graph.nodes:
        if not (node == nodeE):
            dist[node] = float('inf')
        frontier.append(node)
    
    while len(frontier)>0:
        node = "temp"
        #print(frontier)
        for i in frontier:
            if dist[i] < dist[node]:
                node = i
        #print(node)
        #print(dist[node])
        frontier.remove(node)

        for n in graph.neighbors(node):
            alt = dist[node] + graph.get_edge_data(node , n)['weight']
            if alt < dist[n]:
                dist[n] = alt
                pathBuild.add_edge(n, node)

    path = []
    waight = 0
    best = float('inf')
    #print(node)
    node = nodeS
    while not node == nodeE:
        #print(node)
        path.insert(0, node)
        for i in pathBuild.successors(node):
            waight += graph.get_edge_data(i , node)['weight']
            #print(waight)
            node = i

    path.insert(0, node)
    if waight < best:
        best = waight
        bestPath = path
    final = []
    while len(bestPath)> 0:
        final.append(bestPath.pop())
    
        
    
    return(', '.join(final) +" "+ str(best))
   

def aStar(nodeS, nodeE, graph):
    pathBuild = nx.DiGraph()
    pathBuild.add_nodes_from(graph.nodes)
    frontier = [nodeS]
    visited = []
    pathlen = []
    gDist = {nodeS: 0}
    #print(gDist[nodeS])
    #print(stationsL[nodeS])
    fDist = {nodeS: (gDist[nodeS] + abs(stationsL[nodeS][0]-stationsL[nodeE][0])+ abs(stationsL[nodeS][1]-stationsL[nodeE][1])),'temp':float('inf') } 
    for i in graph.nodes:
        if not (i == nodeS):
            gDist[i] = float('inf')
    while len(frontier)>0:
        #print(frontier)
        node = 'temp'
        for i in frontier:
            #print(i)
            #print(gDist[i])
            if fDist[i] < fDist[node]:
                node = i
        #print(node)
        if node == nodeE:
                path = []
                waight = 0
                best = float('inf')
                #print(node)
                while not node == nodeS:
                    #print(node)
                    path.insert(0, node)
                    for i in pathBuild.successors(node):
                        print(i)
                        waight += graph.get_edge_data(i , node)['weight']
                        #print(waight)
                        node = i

                path.insert(0, node)
                if waight < best:
                    best = waight
                    bestPath = path
                final = []
                #while len(bestPath)> 0:
                #    final.append(bestPath.pop())                
                return(', '.join(bestPath) +" "+ str(best))
        frontier.remove(node)
        visited.append(node)

        for n in graph.neighbors(node):
            #print(n)
            alt = gDist[node] + graph.get_edge_data(node , n)['weight']
            #print(gDist[node])
            #print(alt)
            if alt<gDist[n] + graph.get_edge_data(node , n)['weight'] and n in visited:
                #print(1)
                gDist[n] = alt
                fDist[n] = gDist[n]+abs(stationsL[n][0]-stationsL[nodeE][0]) + abs(stationsL[n][1]-stationsL[nodeE][1])
                for i in pathBuild.successors(n):
                    pathlen.append(i) 
                for i in pathlen :
                    pathBuild.remove_edge(n,i)
                pathBuild.add_edge(n,node)
            elif alt<gDist[n] and n in frontier:
                #print(2)
                gDist[n] = alt
                fDist[n] = gDist[n]+abs(stationsL[n][0]-stationsL[nodeE][0]) + abs(stationsL[n][1]-stationsL[nodeE][1])
                for i in pathBuild.successors(n):
                    pathlen.append(i) 
                for i in pathlen :
                    pathBuild.remove_edge(n,i)
                pathBuild.add_edge(n,node)
            elif not (n in frontier or n in visited):
                #print(3)
                #print(n)
                #print(alt)
                gDist[n] = alt
                fDist[n] = gDist[n]+abs(stationsL[n][0]-stationsL[nodeE][0]) + abs(stationsL[n][1]-stationsL[nodeE][1])
               # print(fDist[n])
                frontier.append(n)
                pathBuild.add_edge(n,node)



    
                       
print(aStar("lonsdale quay (seabus)","Surrey Central Station",graph))

    #while not 
    
    #    nodePath.apend(node)
     #   node.
        
