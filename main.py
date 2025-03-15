import os
import platform
from time import sleep

import psutil
import datetime


def get_system_info():
    # Дата та час оновлення
    now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print(f"Останнє оновлення: {now}\n")
    res = {

    }
    # ОС
    print(f"ОС: {platform.system()} {platform.release()} ({platform.version()})")

    # Процесор
    print(f"Процесор: {platform.processor()}")

    # Кількість ядер
    print(f"Кількість ядер: {os.cpu_count()}")

    # Завантаження CPU
    print(f"Завантаження CPU: {psutil.cpu_percent(interval=1)}%")
    res['cpu'] = psutil.cpu_percent(interval=1)

    # RAM
    ram = psutil.virtual_memory()
    print(f"ОЗП: {ram.total / (1024**3):.2f} ГБ")
    print(f"Завантаження ОЗП: {ram.percent}%")
    res['mem'] = ram.percent

    # Диски
    print("\nДиски:")
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  {partition.device} ({partition.mountpoint}) - {usage.total / (1024**3):.2f} ГБ, "
              f"використано: {usage.percent}%")
        res['disk'] = usage.percent

    net = psutil.net_io_counters()
    res['bytes_sent_MB'] = net.bytes_sent / (1824 ** 2)

    res['bytes_recv_MB'] = net.bytes_recv / (1024 * 2)
    print(res)
    return res


def main():
    counter = 0
    while counter <= 30:
        metrics_data = get_system_info()

        counter += 1
        sleep(1)


if __name__ == "__main__":
    main()


