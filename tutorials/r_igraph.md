# R 语言社会网络分析（igraph）

```r
install.packages("igraph")
library(igraph)
edges <- data.frame(from = c("A", "B", "A", "C"), to = c("B", "C", "C", "D"))
g <- graph_from_data_frame(edges, directed = FALSE)
degree(g)
betweenness(g)
closeness(g)
cluster_louvain(g)
plot(g)
```
要点：degree() 是度中心性，betweenness() 是介数中心性，cluster_louvain() 做社区划分，plot() 快速可视化。
