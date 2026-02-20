# --- FUNÇÃO PRINCIPAL DO BOT ATUALIZADA ---
def enviar_alerta():
    # 1. Busca os valores nos e-mails
    # Procuramos por remetentes que contenham 'sabesp' e 'enel'
    valor_sabesp = buscar_valor_no_email("sabesp")
    valor_enel = buscar_valor_no_email("enel")
    
    # 2. Configura a Twilio
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

    # 3. Mensagem com os dois valores automáticos
    mensagem_corpo = (
        "🔔 *LEMBRETE DE PAGAMENTO* 🔔\n"
        "📅 *Vencimento:* Dia 05\n\n"
        "-------------------------------------\n\n"
        f"💧 *Sabesp:* {valor_sabesp}\n"
        f"💡 *Enel:* {valor_enel}\n\n"
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
            client.messages.create(from_='whatsapp:+14155238886', body=mensagem_corpo, to=numero)
            print(f"Sucesso para {numero}")
        except Exception as e:
            print(f"Erro em {numero}: {e}")