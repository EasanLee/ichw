## 1、北京大学某单位的某台机器IP地址为162.105.80.160, 子网掩码为255.255.255.192
#### 1-1 该单位的网络号(网络+子网)是多少？
10100010 01101001 01010000 11
#### 1-2 该单位理论上能容纳多少主机？
64
#### 1-3 北大可以有多少个这样的子网(假定北大全部是162.105网段)？
1024
## 2、解释TCP协议建立连接为什么设计为三步握手（3-way handshake）？
客户端向服务器发送syn包，服务器确认后给客户端发出syn+ack包，客户端确认后向服务器发ack包，此包发送完毕，进入连接状态。三次握手是为了确认信息能够准确地传输给对方而不至于丢失，若少于三次握手，可能导致信息丢失。若多于三次握手，造成传输速率减慢。
## 3、有哪些恶意软件, 如何防范恶意软件？
- 木马软件，间谍软件，广告软件等
---
- 安装杀毒软件/安全防护软件, 及时打补丁
- 使用防火墙, 禁止外部计算机通过网络访问本机
- 不随便下载运行可执行程序
- 不打开未知的邮件附件
- U 盘 通常带毒, 打开前要先查毒
- 不随便暴露自己的 email、生日、手机等重要信息
- 不以 Administrator 权限操作计算机
