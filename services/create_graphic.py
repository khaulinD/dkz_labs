from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def create_graphic(metrics):
    # Extract the relevant data
    timestamps = [key['timestamp'] for key in metrics]
    print(timestamps)
    cpu_usage = [key['cpu_usage'] for key in metrics]
    memory_usage = [key['memory_usage'] for key in metrics]
    disk_usage = [key['disk_usage'] for key in metrics]

    # Convert timestamps to readable time format if necessary (optional)
    # You can use `datetime` to convert to human-readable time
    # Example: `datetime.fromtimestamp(ts).strftime('%H:%M:%S')`

    # Plotting the data
    plt.figure(figsize=(10, 6))

    # Plot each usage
    plt.plot(timestamps, cpu_usage, label="CPU Usage", marker='o', color='b')
    plt.plot(timestamps, memory_usage, label="Memory Usage", marker='o', color='g')
    plt.plot(timestamps, disk_usage, label="Disk Usage", marker='o', color='r')

    # Formatting the plot
    plt.xlabel('Time (Timestamp)', fontsize=12)
    plt.ylabel('Usage (%)', fontsize=12)
    plt.title('CPU, Memory, and Disk Usage Over Time', fontsize=14)
    plt.legend()

    # Convert timestamps to readable format
    readable_timestamps = [datetime.fromtimestamp(ts).strftime('%H:%M:%S') for ts in timestamps]

    # Plot with formatted x-axis (optional)
    plt.xticks(timestamps, readable_timestamps, rotation=45)
    # Show the plot
    plt.tight_layout()
    plt.show()