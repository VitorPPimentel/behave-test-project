# Projeto Padrão De testes DATACOM

--Projeto criado como exemplo de código de automatização de testes para possível implementação na DATACOM.

## Começando

--De inicio existem coisas que são necessárias para o projeto funcionar, são elas Python3, pip, behave e selenium.

#Instalação

- Python:
sudo apt install python3

- pip:
sudo apt install python3-pip

- Selenium:
pip install -U selenium

- Behave:
pip install -U behave

## Executando projeto

--Estando na raiz do projeto, basta executar o comando "behave" que os testes serão executados.

- Comando(behave):
Executa os testes do projeto inteiro.

- Comando(behave --tags @Login):
Executa os testes que estão marcados com a tag "@Login"

## Estrutura de pastas

- Features:
É a pasta principal dos testes, onde se encontra a estrutura que faz os testes funcionarem.

- Profiles:
Definem as variáveis que vão ser usadas em todo o projeto, como url do sistema, email de login e até senhas que serão usadas pelo selenium.

- Steps:
É o local onde o código da execução dos testes se encontra, feito em python.

- TC:
"TC" é a abreviação de "Test Cases", neles se encontram os arquivos feature, que vão ser as representações do caso de uso do usuário, simulando os caminhos que eles fazem pelo sistema.

- Tools:
Na pasta tools é onde colocamos o chromedriver para a execução do projeto.

- Report/allure:
Nessa estrutura de pastas são onde vão ser colocado os arquivos para serem lidos pelo report gráfico do allure, que é um report gráfico para exibição dos testes.

demo - https://demo.qameta.io/allure/

## Arquivos principais

- environment.py:
Nesse arquivo se organiza a estrutura de como o ambiente do código funciona, a leitura dos ambientes e o tempo entre os steps.

- behave.ini:
Nesse arquivo se define o ambiente que você está usando, assim como o chrome driver e algumas outras configurações de exibição e de report.

- chromedriver:
Talvez o arquivo mais importante do projeto, ele permite que o google chrome seja executado, também é possível executar esse projeto de teste em outros navegadores, mas por padrão ele foi feito para ser executado no google chrome.

Nota: aqui é estritamente necessário verificar a versão do chrome e baixar o chromedriver da versão do chrome que você está ultilizando.

site para dowload - https://chromedriver.chromium.org/downloads
