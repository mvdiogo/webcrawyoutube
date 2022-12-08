<p align="center">
  <a href="https://github.com/mvdiogo/webcrawyoutube">
    <img src="https://raw.githubusercontent.com/github/explore/d744245de144b89f3e3462949e08bfc91eda7fcf/topics/youtube/youtube.png" width="30%">
  </a>
  <h3 align="center">Yuflube</h3>
  <h4 align="center">Projeto educacional em como clicar em videos do youtube usando rede TOR e Selenium. Use por sua conta e risco. Cuidado pois se abusar da ferramenta você pode ser bloqueado pelo Youtube.</h4>
</p>

<p align="center">
  <a href="#instalação">Instalação</a> |
  <a href="#como-usar">Como Usar</a> |
  <a href="#teste-unitário">Teste unitário</a> |
</p>

# Instalação

### Instale e configure docker em sua máquina

[1] https://docs.docker.com/get-docker/

### Verifique se as portas 8118, 9040, 9050 e 9051 de sua máquina estão livres. Se sim instale o container tor.

```

    docker run -it -p 8118:8118 -p 9040 -p 9050:9050 -p 9051:9051 -e PASSWORD=tor -d dperson/torproxy

```

### Baixe o repositório e instale as dependências.
```

    git clone https://github.com/mvdiogo/webcrawyoutube.git
    cd youflubegit
    pip install requirements.txt
    python ./src/app.py

```

### Instale e configure o webdriver Chrome

[2] https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/install_drivers/

##### Caso queira instalar outro webdriver deve alterar o projeto.
##### Caso queira definir o path do driver altere a configuração para:

```

    self.driver = webdriver.Chrome(
         options=chrome_options, executable_path=DRIVER_PATH
         )  

```

# Como usar

### Altere os parâmetros do arquivo app.py

```
qtd_repeticoes = 1 # quantas vezes ele vai rodar
qtd_objetos = 1  # foi testado até 40 cliques ao mesmo tempo
duracao_video = [30, 50] # em segundos
url = "https://www.youtube.com/watch?v=[link do seu video]"
proxy = "127.0.0.1:9050"  # endereço local do tor
```
### Rode o programa app.py

```

    python app.py
    ou
    python3 app.py

```

# Teste unitário

### Este programa foi testado com os programas mypy e pytest.

```sh 
{
    pytest test.py 
}
```
