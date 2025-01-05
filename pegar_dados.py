import base64
from imap_tools import MailBox, AND
from datetime import datetime

def atualizar_dados():
    email = 'email_teste@gmail.com'
    senha = 'senha_teste'
    email_origem = 'diariooficial@prefeitura.sp.gov.br'

    conteudo_email = None

    hoje = datetime.now().date()

    try:
        mail = MailBox('imap.gmail.com').login(email, senha)

        lista_emails = mail.fetch(AND(from_ = email_origem, date = hoje))
        
        if lista_emails:
            for email in lista_emails:
                conteudo_email = email.html
                conteudo_email = conteudo_email.replace('background-image:url("https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/governo/gestao/doc/bg.png")', '')
                
        if conteudo_email:

            conteudo_email = base64.b64encode(conteudo_email.encode('utf-8')).decode('utf-8')
            
            conteudo_email = base64.b64decode(conteudo_email).decode('utf-8')

            return conteudo_email
        
        else:
            with open('templates/nao_recebido.html', 'r', encoding = 'utf-8') as file:
                resposta_nao_recebido = file.read()
            return resposta_nao_recebido
        
    except Exception as e:
        print('Erro: ', e)

        with open('templates/erro.html', 'r', encoding = 'utf-8') as file:
            resposta_erro = file.read()
        return resposta_erro
    
    finally:
        mail.logout()


if __name__ == '__main__':
    atualizar_dados()
