# Bitcoin Price Tracker

Esse programa foi desenvolvido para rastrear a cotação do bitcoin em tempo real e apresenta-la em Dolar, Euro, Real e Yuan. 


## 🔧 Ferramentas Utilizadas

-   tkinter: para criar toda a parte visual da aplicação (telas, botões, menus de entrada de informação e textos visíveis).
-   Pillow: para instanciar a imagem do icone, dentro da interface do programa ao lado do título.
-   API: para recuperar as cotações em tempo real. Link: https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CBRL%2CCNY

## ⚙️ Como Funciona

-   Inicialização da aplicação demonstra na parte superior da tela uma label (Bitcoin Price Tracker). 
-   Logo abaixo são apresentadas as labels com as informações da cotação atual do bitcoin em: Dolar($), Euro(€), Real(R$) e Yuan(¥)
-   As cotações são atualizadas a cada um segundo.

## 💻 Como executar o código

- Instalar Python
- Para executar esse código, você precisa ter as seguintes bibliotecas instaladas: pillow e tkinter. Elas podem ser instaladas usando o gerenciador de pacotes Python pip com os seguinte comandos: (pip install) 
- Para executar o arquivo (python **bitcoinPriceTracker.py**)
