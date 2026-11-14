# 网络分析语法与教程

本仓库收集网络分析的常用语法与入门教程，分两部分：社会网络分析（适合做关系、群体、传播研究）和计算机网络分析（适合排查网络连通与流量问题）。

## 一、社会网络分析（Python + NetworkX）

安装：

```bash
pip install networkx matplotlib pandas
```

建图与基本指标：

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")])

print("节点数：", G.number_of_nodes())
print("边数：", G.number_of_edges())
print("度中心性：", nx.degree_centrality(G))
print("介数中心性：", nx.betweenness_centrality(G))
print("接近中心性：", nx.closeness_centrality(G))
print("聚类系数：", nx.clustering(G))
print("社区划分：", list(nx.community.greedy_modularity_communities(G)))
```

可视化：

```python
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True)
plt.show()
```

常用概念速查：度中心性看谁连接最多；介数中心性看谁是桥梁；接近中心性看谁离所有人最近；模块度看群体如何分群。

## 二、计算机网络分析

连通性检查：

```bash
ping -c 4 example.com
traceroute example.com
nslookup example.com
```

抓包（需要管理员权限，仅在自己有权分析的网络上使用）：

```bash
sudo tcpdump -i any -c 20
sudo tcpdump -i eth0 port 80 -w capture.pcap
```

Wireshark 常用显示过滤器：

```
http
tcp.port == 443
ip.addr == 192.168.1.1
dns
```

端口与服务扫描（仅扫描自己有权扫描的主机）：

```bash
nmap -sV 192.168.1.1
nmap -p 80,443 example.com
```

## 三、学习路径建议

1. 先用 NetworkX 在小图上算一遍中心性和社区划分。
2. 再用 ping / traceroute 理解一条请求的实际路径。
3. 最后用 tcpdump 或 Wireshark 看真实数据包，对照过滤器练习。
