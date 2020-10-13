from flask import Flask, request
import requests
import re
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)
def inic(toNumber):
    account_sid = 'AC696cc7059486e3f177486c78323722bc'
    auth_token = 'ebe494848a8c6a7a30f213095502eae2'
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='whatsapp:+14155238886', body='Olá, você esta falando com o atendente virtual da Mega Isenções! Seu veiculo é abaixo ou acima de R$70.000 ?\n1-Abaixo de R$70.000\n2-Acima de R$70.000',to=toNumber)
    print(message.sid)
    
responded6=True
responded5=False    
responded4=False
responded3=False
responded2=False
responded=False
email="gabriel.almeida@megaisencoes.com.br"
toNumber='whatsapp:+5511960360650'

if responded6==True:         
                    
            inic(toNumber)
            responded6=False

@app.route('/sms', methods=['POST'])
    

def sms():
    
    # Fetch the message
    msg = request.values.get('Body')
    # Create reply
    resp = MessagingResponse()
    mg = resp.message()
    global email
    global responded5
    global responded4
    global responded3
    global responded2
    global responded
    p1=''
    p2=''
    p3=''


  
    if responded == False:

            mensagem=perg1(msg)
            mg.body(mensagem)
            
            
           
    elif responded2==True:         
                    
            mensagem=perg2(msg, email)
            mg.body(mensagem)
            

    elif responded3==True:         
                    
            mensagem=perg3(msg)
            mg.body(mensagem)
            

    elif responded4==True:         
                    
            mensagem=validEmail(msg, email)
            mg.body(mensagem)

    elif responded5==True:         
                    
            mensagem=end(msg)
            mg.body(mensagem)

    
            
    return str(resp)



def perg1(msg):
    global responded
    global responded2
    
    if msg=='1':
                p1='*Abaixo de 70.000*'
                mensagem=("Ok, seu veículo é %s\n\nVocê pretende comprar o veiculo nos proximos 3 meses ?\n1-Sim\n2-Não"% p1)
                responded = True
                responded2 = True
            

    elif msg=='2':
                p1='*Acima de 70.000*'
                mensagem=("Ok, seu veículo é %s\n\nVocê pretende comprar o veiculo nos proximos 3 meses ?\n1-Sim\n2-Não"% p1)
                responded = True
                responded2 = True
    else:
                mensagem="*Digite uma opção valida!*"
                
    return mensagem

def perg2(msg, email):
    global responded3
    global responded2
                
    if msg=='1':
                p2='*Sim*'
                mensagem=("Você escolheu %s\n\n%s Esse é o email que você deseja receber as documentações?\n1-Sim\n2-Não"% (p2, email))
                responded2 = False
                responded3 = True
                
              
    elif msg=='2':
                p2='*Não*'
                mensagem=("Você escolheu %s\n\n%s Esse é o email que você deseja receber as documentações?\n1-Sim\n2-Não"% (p2, email))
                responded2 = False
                responded3 = True
    else:
                mensagem="*Digite uma opção valida!*"
                
    return mensagem

def perg3(msg):
        global responded5
        global responded4
        global responded3
        if msg=='1':
                p3='*Sim*'
                mensagem="Ok, email cadastrado!"
                responded3 = False
                responded5= True
           
                
        elif msg=='2':
                mensagem="Digite um email para fazer o cadastro: "
                responded3 = False
                responded4 = True
        else:
                mensagem="*Digite uma opção valida!*"

        return mensagem
                
def validEmail(msg, email):
        global responded4
        global responded5

        if re.search(r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$', msg) :
            email = msg
            mensagem=("O email %s foi cadastrado!"% email)
            responded4 = False
            responded5 = True

        elif not re.search(r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$', msg):
            mensagem='O email digitado não é valido, digite novamente: '
            responded4 = True
        return mensagem
def end(msg):
    
    if msg:
        mensagem="Para mais informações ligue em nossa central de atendimento: (11) 2344-8400"
    return mensagem



if __name__ == '__main__':
    app.run()
