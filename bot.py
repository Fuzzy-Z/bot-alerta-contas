import os
from datetime import datetime
from twilio.rest import Client

# --- CONFIGURAÇÕES MANUAIS ---
# Mude estes valores todo mês entre o dia 1 e 4
VALOR_SABESP = "Verificar"
VALOR_ENEL = "Verificar"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

numeros_destino = [
    'whatsapp:+5511977625856',  # Kayky
    'whatsapp:+5511957624486',  # Mãe
    'whatsapp:+5511981622972',  # Carol
    'whatsapp:+5511977281609',  # Anna
    'whatsapp:+5511962568459',  # Janaina
]

def enviar_alerta():
    # Pega o dia de hoje (1 a 31)
    dia_atual = datetime.now().day
    
    # SE FOR DIA 5: Manda o lembrete oficial
    if dia_atual == 5:
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
    # SE NÃO FOR DIA 5: Manda apenas uma mensagem de sinal
    else:
        mensagem_corpo = "🤖 *Bot de Contas:* Sistema ativo e conexão verificada! Tenha um excelente dia. 👍"
    
    for numero in numeros_destino:
        try:
            client.messages.create(
                from_='whatsapp:+14155238886',
                body=mensagem_corpo,
                to=numero
            )
            print(f"Sucesso para {numero}")
        except Exception as e:
            print(f"Erro em {numero}: {e}")

if __name__ == "__main__":
    enviar_alerta()