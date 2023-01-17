# 将优选ip转化为clash配置文件


def main():
    server = input("服务器地址:")

    port = input("端口:")

    password = input("密码:")

    remark = input("别名:")

    sni = input("sni:")

    is_ws = input("是否使用ws(Y/n):")

    proxy = "\n    port: " + port + "\n    password: " + password + "\n    sni: " + sni + "\n    udp: true"

    if is_ws == "y" or is_ws == "":
        path = input("ws路径:")

        host = input("ws Host:")

        proxy += "\n    network: ws\n    ws-opts:\n      path: " + path + "\n      headers:\n        Host: " + host

    file = open("./ips.txt", "r", encoding="utf-8")

    ips = file.readlines()

    i = 1

    clash = open("./clash.yaml", "w", encoding="utf-8")

    clash.write(
        "port: 7890\nsocks-port: 7891\nmode: Rule\nlog-level: info\nproxies:\n" + "  - name: " + remark + "\n    type: trojan\n    server: " + server + proxy)

    for ip in ips:
        ip = ip.rstrip()
        clash.write("\n  - name: " + remark + str(i) + "\n    type: trojan\n    server: " + ip + proxy)
        i = i + 1

    clash.write(
        "\nproxy-groups:\n  - name: 节点选择\n    type: select\n    proxies:\n      - 自动选择\n      - 负载均衡-轮询\n      - 负载均衡-散列\n")

    proxies = "      - " + remark

    j = 1

    while j < i:
        proxies += "\n      - " + remark + str(j)
        j = j + 1

    clash.write(proxies)

    clash.write(
        "\n  - name: 自动选择\n    type: url-test\n    url: http://www.gstatic.com/generate_204\n    interval: 300\n    proxies:\n" + proxies)
    clash.write(
        "\n  - name: 负载均衡-轮询\n    type: load-balance\n    url: http://www.google.com/generate_204\n    interval: 300\n    strategy: round-robin\n    proxies:\n" + proxies)
    clash.write(
        "\n  - name: 负载均衡-散列\n    type: load-balance\n    url: http://www.google.com/generate_204\n    interval: 300\n    strategy: consistent-hashing\n    proxies:\n" + proxies)

    clash.write("\n\n")

    file = open("./rules.txt", "r", encoding="utf-8")

    clash.write(file.read() + "\n\n")

    is_white = input("是否为白名单模式(Y/n):")

    if is_white == "y" or is_white == "":
        rule = open("./whitelist.txt", "r", encoding="utf-8")
        clash.write(rule.read())

    else:
        rule = open("./blacklist.txt", "r", encoding="utf-8")
        clash.write(rule.read())


main()
