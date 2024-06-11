from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo=nx.DiGraph()
        self._dizionario={}
        for element in self._fermate:
            self._dizionario[element.id_fermata]=element

    def buildGraph(self):
        self._grafo.add_nodes_from(self._fermate)
        #for u in self._fermate:
            #vicini=DAO.getEdgeVicini(u)
            #for v in vicini:
                #self._grafo.add_edge(u, self._dizionario[v._id_stazA])
        res=DAO.getAllEdge()
        for element in res:
            self._grafo.add_edge(self._dizionario[element._id_stazP], self._dizionario[element._id_stazA])

    def getBFSnodes(self,source):
        edges=nx.bfs_edges(self._grafo,source)
        visited=[]
        for u,v in edges:
            visited.append(v)
        return visited
    def getDFSnodes(self,source):
        edges=nx.dfs_edges(self._grafo,source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited
    def addEdgePesati(self):
        self._grafo.clear_edges()
        AllConnessioni=DAO.getAllEdge()
        for c in AllConnessioni:
            if self._grafo.has_edge(self._dizionario[c._id_stazP], self._dizionario[c._id_stazA]):
                self._grafo[self._dizionario[c._id_stazP]][self._dizionario[c._id_stazA]]["weight"]+=1
            else:
                self._grafo.add_edge(self._dizionario[c._id_stazP],self._dizionario[c._id_stazA], weight=1)
    def getEdgeWeight(self, v1, v2):
        return self._grafo[v1][v2]["weight"]

    def buildGrafoPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgePesati()

    def getArchiPesoMaggioreUno(self):
        if len(self._grafo.edges)==0:
            print("il grafo è vuoto")
            return
        edges=self._grafo.edges
        result=[]
        for u,v in edges:
            if self.getEdgeWeight(u,v)>1:
                result.append((u,v,self.getEdgeWeight(u,v)))
        return result








    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes())
    def getNumEdges(self):
        return len(self._grafo.edges())