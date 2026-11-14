"""社会网络分析示例：读入边列表，计算中心性与社区划分，并导出 Gephi 文件。运行：python examples/social_network_example.py"""
import csv
from pathlib import Path
import networkx as nx

edges = []
with open(Path(__file__).parent / "sample_edges.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        edges.append((row["source"], row["target"]))

G = nx.Graph()
G.add_edges_from(edges)
print("节点数：", G.number_of_nodes(), "边数：", G.number_of_edges())
print("度中心性：", nx.degree_centrality(G))
print("介数中心性：", nx.betweenness_centrality(G))
print("接近中心性：", nx.closeness_centrality(G))
print("社区：", [sorted(c) for c in nx.community.greedy_modularity_communities(G)])
nx.write_gexf(G, Path(__file__).parent / "sample_network.gexf")
print("已导出 sample_network.gexf，可用 Gephi 打开。")
