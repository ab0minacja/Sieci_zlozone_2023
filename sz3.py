import networkx as nx
import matplotlib.pyplot as plt
g = nx.read_edgelist('facebook_combined.txt', nodetype=int, create_using=nx.Graph())
edges_list = list(g.edges)
nodes_list = list(g.nodes)
###checking number of nodes

#rzad

rzad = len(nodes_list)
print(f"Rząd/stopień grafu: {rzad}")

#rozmiar

rozmiar = len(edges_list)
print(f"Rozmiar grafu: {rozmiar}")

#gestosc

gestosc = (2*rozmiar)/(rzad*(rzad-1))
print(f"Gestosc grafu: {gestosc}")
try:
    srednica = nx.diameter(g)
    print(f"Średnica grafu: {srednica} ")
    sw_sciezki = nx.average_shortest_path_length(g)
    print(f"Średnia długość ścieżki (z najkrótszych ścieżek): {sw_sciezki}")
except nx.NetworkXError as e:
    print("Graf nie jest spójny, więc obliczenie średnicy jest niemożliwe")

#miary centralnosci

#stopień wierzchołka - najwiekszy, najmniejszy, średni

stopien = list(g.degree())
if len(stopien)> 0:
    sredni_stopien = sum(deg for node, deg in stopien) / len(stopien)
    print(f"Średni stopien wierzcholka: {sredni_stopien}")
    max_stopien_wierzcholek, max_stopien = max(stopien, key=lambda pair: pair[1])
    min_stopien_wierzcholek, min_stopien = min(stopien, key=lambda pair: pair[1])
    print(f"Wierzcholek o najwiekszym stopniu: {max_stopien_wierzcholek}, stopień: {max_stopien}")
    print(f"Wierzcholek o najmniejszym stopniu: {min_stopien_wierzcholek}, stopień: {min_stopien}")

else: 
    print("Graf nie zawiera wierzcholków")

#bliskosc

bliskosc = nx.closeness_centrality(g)
if len(bliskosc)> 0:
    max_bliskosc_wierzcholek, max_bliskosc = max(bliskosc.items(), key = lambda item: item[1])
    min_bliskosc_wierzcholek, min_bliskosc = min(bliskosc.items(), key = lambda item: item[1])
    srednia_bliskosc = sum(bliskosc.values())/len(bliskosc)
    print(f"Srednia bliskosc wierzcholkow: {srednia_bliskosc}")
    print(f"Wierzcholek z najwieksza bliskoscia: {max_bliskosc_wierzcholek}, bliskosc wierzcholka: {max_bliskosc}")
    print(f"Wierzcholek z najmniejsza bliskoscia: {min_bliskosc_wierzcholek}, bliskosc wierzcholka: {min_bliskosc}")
else: 
    print("Graf nie zawiera wierzchołkow.")

#posrednictwo

posrednictwo = nx.betweenness_centrality(g)
if len(posrednictwo) >0:
    max_posrednictwo_wierzcholek, max_posrednictwo = max(posrednictwo.items(), key = lambda item: item[1])
    min_posrednictwo_wierzcholek, min_posrednictwo = min(posrednictwo.items(), key = lambda item: item[1])
    srednie_posrednictwo = sum(posrednictwo.values())/len(posrednictwo)
    print(f"Srednia posrednictwo wierzcholkow: {srednie_posrednictwo}")
    print(f"Wierzcholek z najwiekszym posrednictem: {max_posrednictwo_wierzcholek}, posrednictwo wierzcholka: {max_posrednictwo}")
    print(f"Wierzcholek z najmniejsza posrednictwem: {min_posrednictwo_wierzcholek}, posrednictwo wierzcholka: {min_posrednictwo}")
else: 
    print("Graf nie zawiera wierzchołkow.")

#centralnosc wektora wlasnego 

centralnosc_wektora_wlasnego = nx.eigenvector_centrality(g)
if len(centralnosc_wektora_wlasnego) >0:
    max_cww_wierzcholek, max_cww = max(centralnosc_wektora_wlasnego.items(), key = lambda item: item[1])
    min_cww_wierzcholek, min_cww = min(centralnosc_wektora_wlasnego.items(), key = lambda item: item[1])
    srednie_cww = sum(centralnosc_wektora_wlasnego.values())/len(centralnosc_wektora_wlasnego)
    print(f"Srednia centralnosc wektora wlasnego: {srednie_cww}")
    print(f"Wierzcholek z najwiekszą centralnoscia wektora wlasnego: {max_cww_wierzcholek}, centralnosc wierzcholka: {max_cww}")
    print(f"Wierzcholek z najmniejsza centralnoscia wektora wlasnego: {min_cww_wierzcholek}, centralnosc wierzcholka: {min_cww}")
else: 
    print("Graf nie zawiera wierzchołkow.")

#pagerank

pagerank = nx.pagerank(g)
if len(pagerank) >0:
    max_pagerank_wierzcholek, max_pagerank = max(pagerank.items(), key = lambda item: item[1])
    min_pagerank_wierzcholek, min_pagerank = min(pagerank.items(), key = lambda item: item[1])
    srednie_pagerank = sum(pagerank.values())/len(pagerank)
    print(f"Srednia wartosc pagerank: {srednie_pagerank}")
    print(f"Wierzcholek z najwiekszą wartoscia pagerank: {max_pagerank_wierzcholek}, pagerank wierzcholka: {max_pagerank}")
    print(f"Wierzcholek z najmniejsza wartoscia pagerank: {min_pagerank_wierzcholek}, pagerank wierzcholka: {min_pagerank}")
else: 
    print("Graf nie zawiera wierzchołkow.")

#tworzenie podgrafow dla ciekawych wartosci
special_nodes = [max_bliskosc_wierzcholek, max_cww_wierzcholek, max_pagerank_wierzcholek, max_posrednictwo_wierzcholek, max_stopien_wierzcholek]
special_nodes_values = [max_bliskosc, max_cww, max_pagerank, max_posrednictwo, max_stopien]
sub_titles = ["Podgraf dla wierzchołka z najwieksza bliskoscia", "Podgraf dla wierzcholka z najwieksza centralnoscia wektora wlasnego", "Podgraf dla wierzcholka z najwieksza wartoscia pagerank", "Podgraf dla wierzcholka z najwiekszym posrednictwem", "Podgraf dla wierzcholka z najwiekszym stopniem"]

def make_subgraph(special_nodes):
    neighbors = list(g.neighbors(special_nodes))
    nodes_for_subgraph = [special_nodes] + neighbors
    subgraph = g.subgraph(nodes_for_subgraph)
    kolory = ['blue' if node != special_nodes else "red" for node in nodes_for_subgraph]
    nx.draw(subgraph, with_labels = True, font_size = 5, node_color = kolory)

for i in range(len(special_nodes)):
    fig2 = plt.figure()
    if i == 0:
        plt.title("Podgraf dla wierzchołka z najwieksza bliskoscia", loc= 'left')
        make_subgraph(special_nodes[i])
        print(sub_titles[i])
    else:
        plt.title(sub_titles[i], loc= 'center')
        make_subgraph(special_nodes[i])
        print(sub_titles[i])


fig1, (ax1, ax2) = plt.subplots(1,2)
nx.draw(g, node_size = 10, ax =ax1)
ax1.set_title("Rozważany graf")
wartosci = {"Rząd grafu: ": rzad,
            "Rozmiar grafu: ": rozmiar,
            "Gęstość grafu: ":gestosc,
            "Średnica grafu: ": srednica,
            "Średni stopień wierzchołka: ":sredni_stopien,
            "Srednia bliskosc wierzcholkow: ":srednia_bliskosc,
            "Srednie posrednictwo wierzcholkow: ": srednie_posrednictwo,
            "Srednia centralnosc wektora wlasnego: ": srednie_cww,
            "Srednia wartosc pagerank: ": srednie_pagerank
            }
text = "\n".join(f"{klucz}:{wartosc}" for klucz, wartosc in wartosci.items())
ax2.text(0.0,0.5, text, transform=ax2.transAxes, ha='left', va='baseline')
ax2.set_title("Wartości charakteryzujace graf")
ax2.axis('off')

plt.show()
  
