from time import sleep

from db.base import create_diagnostics, get_diagnostics
from services.create_graphic import create_graphic
from services.ollama_service import make_ollama_request
from services.sys_diagnostics import get_system_info


def main():
    counter = 0
    while counter <= 30:
        metrics_data = get_system_info()
        create_diagnostics(metrics_data)

        counter += 1
        sleep(1)

    res = get_diagnostics(30)
    create_graphic(res)
    chat_response = make_ollama_request(res)
    print(chat_response)



if __name__ == '__main__':
    main()