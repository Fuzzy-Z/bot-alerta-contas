import os
from twilio.rest import Client

# Configurações de autenticação (Pegas das Secrets do GitHub)
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# LISTA DE NÚMEROS (Adicione quantos quiser seguindo o padrão)
# Importante: O número deve ter +55, DDD e o número sem espaços
numeros_destino = [
    'whatsapp:+5511977625856',  # Seu número
    'whatsapp:+5511888888888',  # Número da outra pessoa 1
    'whatsapp:+5511777777777'   # Número da outra pessoa 2
]

def enviar_alerta():
    mensagem_corpo = (
        "🚨 *LEMBRETE DE PAGAMENTO (DIA 5)*\n\n"
        "Passando para avisar que as contas vencem hoje!\n"
        "Favor perguntar partes para o Kayky💸"
        "Para a Janaina, lembre-se de pagar suas contas!"
        "Obrigado! 🙏"
    )
    
    for numero in numeros_destino:
        try:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=mensagem_corpo,
                to=numero
            )
            print(f"Mensagem enviada com sucesso para {numero} | SID: {message.sid}")
        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

if __name__ == "__main__":
    enviar_alerta()