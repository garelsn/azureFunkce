import logging
import json
import datetime
import random
import azure.functions as func
from enum import Enum

# Enumerace Sender
class Sender(Enum):
    Me = "me"
    AI = "ai"
app = func.FunctionApp()
@app.function_name("get_object")
@app.route(route="data", auth_level=func.AuthLevel.ANONYMOUS)  # Nastavení úrovně autorizace na ANONYMOUS
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    now =datetime.datetime.now()

    # Vytvoření objektu Message
    message = {
        "Message":{
            "id": random.randint(1, 1000),  # Náhodné ID
            "sender": Sender.AI.value,  # Vždy "AI"
            "text": "dummy answer from AI",  # Dummy text
            "time": f"{now.hour}:{now.minute},{now.day}.{now.month}.{now.year}"  # Aktuální datum a čas a Aktuální datum# 
        }
    }

    # Vrátí jako JSON
    return func.HttpResponse(
        json.dumps(message),
        mimetype="application/json",
        status_code=200
    )
