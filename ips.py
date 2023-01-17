
# 将trojan订阅连接批量提取ip


file = open("ips.txt", "r")
ips = file.readlines()
file.close()
file = open("ips.txt", "w")
for ip in ips:
    file.write(ip.split("@")[1].split(":")[0] + "\n")
