# Trojan2Clash

个人使用,所以功能基本写死

作用:将优选ip转化为clash配置文件,仅支持trojan
用法:
先把优选ip一行一个的填入ips.txt中    ips.py可以从trojan链接中提取ip(因为我用的v2rayn来优选ip)(注意手动删除空行,不能留空行)
然后跟着脚本提示将自己的trojan配置填进去然后就会生成配置文件

配置文件的rules取决于rules.txt whitelist.txt blacklist.txt这三个文件,可以修改这些文件来自定义规则(别的只能改代码了),原本的规则不一定好用

(其实clash配置文件我自己也懂得不多)
