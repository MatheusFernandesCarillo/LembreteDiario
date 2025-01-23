import schedule
import time
from plyer import notification

def enviar_lembrete():
    notification.notify(
        title="Lembrete Água",
        message="Bebe Agua, Safado",
        app_name="Lembrete Awa",
        timeout=10
    )


schedule.every(1).hour.do(enviar_lembrete)

while True:
    schedule.run_pending()
    time.sleep(1) 
