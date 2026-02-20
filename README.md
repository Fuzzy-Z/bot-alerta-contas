🤖 Bot de Alerta de Contas - WhatsApp
Este projeto é uma automação simples utilizando Python, Twilio API e GitHub Actions para enviar lembretes de pagamento de contas todo dia 5 de cada mês diretamente para o WhatsApp de uma lista de contatos.

🚀 Funcionalidades
Envio Automático: Programado para rodar no dia 5 de cada mês às 09:00 (horário de Brasília).

Múltiplos Destinatários: Envia mensagens individuais para uma lista de números pré-definida.

Custo Zero: Utiliza o plano Sandbox da Twilio e o agendador gratuito do GitHub Actions.

Segurança: Credenciais sensíveis (SID e Token) ficam protegidas nas Secrets do GitHub.

🛠️ Tecnologias Utilizadas
Python 3.x

Twilio SDK: Para integração com a API do WhatsApp.

GitHub Actions: Para agendamento e execução na nuvem sem precisar manter o PC ligado.

📋 Pré-requisitos
Para que o bot funcione corretamente, todos os números na lista devem:

Salvar o número da Twilio nos contatos: +1 415 523 8886.

Enviar a mensagem: join coach-percent para autorizar o recebimento.

Nota: No plano Sandbox, essa autorização precisa ser renovada a cada 72 horas.

⚙️ Configuração do Repositório
1. Variáveis de Ambiente (Secrets)
No seu GitHub, vá em Settings > Secrets and variables > Actions e adicione:

TWILIO_ACCOUNT_SID: Seu SID da conta Twilio.

TWILIO_AUTH_TOKEN: Seu Token de autenticação da Twilio.

2. Estrutura de Arquivos
bot.py: Contém a lógica de envio e a lista de números.

.github/workflows/main.yml: Contém o agendamento (Cron) da automação.

🕒 Agendamento (Cron)
O arquivo de workflow está configurado com a seguinte expressão cron:
0 12 5 * *

Minuto: 0

Hora: 12:00 UTC (09:00 Horário de Brasília)

Dia: 5

Mês: Todos

Dia da Semana: Todos

🧪 Como Testar Manualmente
Vá na aba Actions do repositório.

Selecione Alerta de Contas Mensal.

Clique em Run workflow > Run workflow.

Acompanhe o log e verifique se o círculo ficou verde ✅.

Desenvolvido para facilitar a organização financeira! 💸