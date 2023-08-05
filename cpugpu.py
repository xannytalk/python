import psutil
import tkinter as tk
from tkinter import ttk

def get_cpu_temperature():
    try:
        temperatures = psutil.sensors_temperatures()
        if 'coretemp' in temperatures:
            core_temps = temperatures['coretemp']
            avg_temp = sum([temp.current for temp in core_temps]) / len(core_temps)
            return f"{avg_temp:.1f} °C"
        else:
            return "N/A"
    except Exception as e:
        return "Error"

def get_gpu_temperature():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            return f"{gpus[0].temperature} °C"
        else:
            return "N/A"
    except Exception as e:
        return "Error"

def update_temperatures():
    cpu_temp_label.config(text=get_cpu_temperature())
    gpu_temp_label.config(text=get_gpu_temperature())
    root.after(5000, update_temperatures)  # Update every 5 seconds

root = tk.Tk()
root.title("CPU and GPU Temperature Monitor")

cpu_label = tk.Label(root, text="CPU Temperature:")
cpu_label.pack(pady=5)

cpu_temp_label = tk.Label(root, text="", font=("Helvetica", 16))
cpu_temp_label.pack()

gpu_label = tk.Label(root, text="GPU Temperature:")
gpu_label.pack(pady=5)

gpu_temp_label = tk.Label(root, text="", font=("Helvetica", 16))
gpu_temp_label.pack()

update_temperatures()  # Start updating temperatures

root.mainloop()
