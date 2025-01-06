# Pega_dados_diario_ofc
Desenvolvimento de um sistema que lê dados recebidos do email do Diário Oficial, e os apresenta em uma página para ser incorporado em sistemas como o SharePoint.

# Requisitos do Sistema
- Python 3.8.10
## Pacotes importados:
- Flask
- imap_tools
- datetime
- base64.

# Processos da Automação
## Pega texto do Diário Oficial:
- Acessa as mensagens do e-mail através do protocolo imap(Protocolo de acesso de mensagens via internet –Permite com que possamos acessar mensagens de e-mail).
- Filtramos as mensagens enviadas somente pelo e-mail do Diário Oficial e no dia atual.
- Identifica e armazena o texto do e-mail selecionado.
- Decodifica os textos e envia como resposta da requisição.
- Caso não tenha recebido nenhum e-mail relacionado, ou tenha ocorrido algum erro no processo, será retornado uma página html sobre o não recebimento do e-mail ou informando o erro, respectivamente.
## Código hospedado na web:
- O código está hospedado na web através da plataforma “Vercel”, ele realiza o processo e mostra a resposta quando o site é acessado ou requisitado.
- Nele é apresentado o conteúdo html do e-mail ou das mensagens e problemas que possam ter ocorrido.
- O site pode ser acessado através do seguinte link: https://pegadiarioofcsmc.vercel.app/
## Dados no SharePoint:
- Como os dados são apresentados ao acessarmos a página, no SharePointde está presente um iframe que referencia o site e mostra suas informações atualizadas na própria página.

# Arquivos do Projeto
## Arquivo app.py:
Este é o arquivo que cria o sistema de endereços na url. Através da biblioteca Flask, ele roda o código do processo e renderiza o HTML na página quando a url é acessada (Através da requisição “GET”).
## Arquivo pegar_dados.py:
Arquivo que contém o código onde todo o processo é realizado, desde a definição do e-mail até o retorno do conteúdo HTML.
## Pasta templates:
A pasta contém arquivos com conteúdo HTML e CSS para os outros tipos de respostas que podem ocorrer no site.
## Arquivo requirements.txt:
Arquivo que contém bibliotecas usadas e suas versões, necessárias para que o Vercel consiga entender e executar o código.
## Arquivo vercel.json:
Arquivo de configuração para o Vercel.

# Explicação de Funções
## atualizar_dados():
- É definido o e-mail e a senha de aplicativo de onde serão pegas as mensagens de e-mail.
- É definido o e-mail do Diário Oficial, para fazer a filtragem de e-mails.
- Conecta no servidor imap para pegar as informações dos e-mails.
- Filtra e pega os e-mails com a data atual e enviados pelo Diário Oficial.
- Caso um e-mail seja encontrado, ele pega o conteúdo, trata para encaixar na formatação, e retorna o conteúdo HTML.
- Caso não tenha encontrado ou tenha ocorrido algum erro, ele retorna o conteúdo HTML correspondente da pasta templates.
## atualizar_dados_pagina():
- É a função que é executada quando é feito um acesso na página.
- Pega o HTML retornado pela função “atualizar_dados()” e renderiza o conteúdo na página.
