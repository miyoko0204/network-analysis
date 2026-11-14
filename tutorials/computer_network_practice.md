# 计算机网络分析练习

1. 连通性：ping -c 4 example.com，若丢包率高，先查本地网络再查目标。
2. 路径：traceroute example.com，看在哪一跳开始延迟变大或超时。
3. 抓包：sudo tcpdump -i any -c 20 port 80，观察三次握手。
4. 过滤：Wireshark 里依次试 http、dns、tcp.port == 443、ip.addr == 192.168.1.1。
5. 排查顺序：先 ping 网关，再 ping 外网，再查 DNS，最后看端口是否开放。
注意：只在自己有权分析的网络和主机上抓包和扫描。
