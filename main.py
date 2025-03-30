import threading
from time import sleep

from db.base import create_diagnostics, get_diagnostics
from services.create_graphic import create_graphic
from services.ollama_service import make_ollama_request
from services.sys_diagnostics import get_system_info
from ui.simple_ui import create_ui


def main():
    counter = 0
    while counter <= 30:
        metrics_data = get_system_info()
        create_diagnostics(metrics_data)

        counter += 1
        sleep(1)

def start_data_collection():
    """Runs `main()` in a separate thread."""
    data_thread = threading.Thread(target=main, daemon=True)  # Run in the background
    data_thread.start()





if __name__ == '__main__':
    start_data_collection()  # Start background data collection
    create_ui()  # Start Streamlit UI