# Pega_dados_diario_ofc
Desenvolvimento de um sistema que lê dados recebidos do email do Diário Oficial, e os apresenta em uma página para ser incorporado em sistemas como o SharePoint.

# Processos da Automação
## Pega texto do Diário Oficial:
Acessa as mensagens do e-mail pelo através do protocolo imap(Protocolo de acesso de mensagens via internet –Permite com que possamos acessar mensagens de e-mail).
Filtramos as mensagens enviadas somente pelo e-mail do Diário Oficial e no dia atual.
Identifica e armazena o texto do e-mail selecionado.Decodifica os textos e envia como resposta da requisição.
Caso não tenha recebido nenhum e-mail relacionado, ou tenha ocorrido algum erro no processo, será retornado uma página html sobre o não recebimento do e-mail ou sobre o erro, respectivamente.
## Código hospedado na web:
O código está hospedado na web através da plataforma “Vercel”, ele realiza o processo e mostra a resposta quando o site é acessado ou requisitado.
Nele é apresentado o conteúdo htmldo e-mail ou das mensagens e problemas que possam ter ocorrido.
O site pode ser acessado através do seguinte link: https://pegadiarioofcsmc.vercel.app/
## Dados no SharePoint:
Como os dados são apresentados ao acessarmos a página, no SharePointde cada localidade está presente um iframe que referencia o site e mostra suas informações atualizadas na própria página.

# Arquivos do Projeto
## Arquivo app.py:
Este é o arquivo que cria o sistema de endereços na url. Através da biblioteca Flask, ele roda o código do processo e renderiza o HTMLnapágina quando a url é acessada (Através da requisição “GET”).
## Arquivo pegar_dados.py:
Arquivo que contém o código onde todo o processo é realizado, desde a definição do e-mail até o retorno do conteúdo HTML.
## Pasta templates:
Apasta contém arquivos com conteúdo HTMLe CSSpara os outros tipos de respostas que podem ocorrer no site.
## Arquivo requirements.txt:
Arquivo que contém bibliotecas usadas e suas versões, necessárias para que o Vercelconsiga entender e executar o código.
## Arquivo vercel.json:
Arquivo de configuração para o Vercel.
