import schedule
import time
from plyer import notification

def enviar_lembrete(): #definir a função enviar_lembrete
    notification.notify(
        title="Lembrete Água",
        message="Bebe Agua",
        app_name="Lembrete água",
        timeout=10
    )


schedule.every(1).hour.do(enviar_lembrete) #fazer com que a notificação aparece a cada uma hora

while True: #loop para manter o script rodando
    schedule.run_pending()
    time.sleep(1) 

# utilizado pyinstaller para transformar o arquivo .py em .exe
# pyinstaller --onefile --noconsole LembreteDiario.py
