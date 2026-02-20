import os
from twilio.rest import Client

# --- CONFIGURAÇÕES MANUAIS ---
# Altere os valores abaixo todo mês antes do dia 5
VALOR_SABESP = "Verificar"
VALOR_ENEL = "Verificar"

# Configurações de autenticação (Pegas das Secrets do GitHub)
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# LISTA DE NÚMEROS
numeros_destino = [
    'whatsapp:+5511977625856',  # Kayky
    'whatsapp:+5511957624486',  # Mãe
    'whatsapp:+5511981622972',  # Carol
    'whatsapp:+5511977281609',  # Anna
    'whatsapp:+5511962568459',  # Janaina
]

def enviar_alerta():
    # Montagem da mensagem visual
    mensagem_corpo = (
        "🔔 *LEMBRETE DE PAGAMENTO* 🔔\n"
        "📅 *Vencimento:* Dia 05\n\n"
        "-------------------------------------\n\n"
        f"💧 *Sabesp:* R$ {VALOR_SABESP}\n"
        f"💡 *Enel:* R$ {VALOR_ENEL}\n\n"
        "Olá! Passando para avisar que as suas\n"
        "contas vencem *hoje*! 💸\n\n"
        "📌 *Orientações:*\n"
        "• Favor perguntar as partes para o *Kayky* 💸\n"
        "• *Janaina*, lembre-se de pagar suas contas!\n\n"
        "-------------------------------------\n\n"
        "Obrigado! 🙏✨"
    )
    
    for numero in numeros_destino:
        try:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=mensagem_corpo,
                to=numero
            )
            print(f"Sucesso para {numero}")
        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

if __name__ == "__main__":
    enviar_alerta()