import psutil
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import subprocess


class ProcessMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Process Monitor - Tech View")
        self.root.geometry("800x550")
        self.root.configure(bg="#1e1e2f")  

        style = ttk.Style()
        style.theme_use('clam') 
        style.configure("Treeview",
                        background="#2b2b3c",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#2b2b3c",
                        font=('Segoe UI', 10))
        style.configure("Treeview.Heading",
                        background="#3b3b4f",
                        foreground="white",
                        font=('Segoe UI', 11, 'bold'))
        style.configure("TLabel", background="#1e1e2f", foreground="white")
        style.configure("TLabelframe", background="#1e1e2f", foreground="white")
        style.configure("TButton", background="#444", foreground="white", font=('Segoe UI', 10))

        
        self.resource_frame = ttk.LabelFrame(root, text="System Usage", padding=10)
        self.resource_frame.pack(fill="x", padx=10, pady=5)

        self.cpu_label = ttk.Label(self.resource_frame, text="CPU Usage: ", font=('Segoe UI', 11))
        self.cpu_label.pack(anchor='w', padx=10)

        self.memory_label = ttk.Label(self.resource_frame, text="Memory Usage: ", font=('Segoe UI', 11))
        self.memory_label.pack(anchor='w', padx=10)

        
        self.process_frame = ttk.LabelFrame(root, text="Running Processes", padding=10)
        self.process_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(self.process_frame, columns=("PID", "Name", "CPU%", "Memory%"),
                                 show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor='center')
        self.tree.pack(fill="both", expand=True)

        
        self.kill_button = ttk.Button(root, text="Kill Selected Process",
                                      command=self.kill_process)
        self.kill_button.pack(pady=10)
        self.graph_button = ttk.Button(root, text="Show Live Graph", command=self.open_graph)
        self.graph_button.pack(pady=5)

        self.update_thread = threading.Thread(target=self.update_loop, daemon=True)
        self.update_thread.start()

    def update_loop(self):
        while True:
            self.update_usage()
            self.update_process_list()
            time.sleep(2)

    def update_usage(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        mem_percent = mem.percent

        cpu_color = 'red' if cpu_percent > 80 else 'white'
        mem_color = 'red' if mem_percent > 80 else 'white'

        self.cpu_label.config(text=f"CPU Usage: {cpu_percent}%", foreground=cpu_color)
        self.memory_label.config(text=f"Memory Usage: {mem_percent}%", foreground=mem_color)

    def update_process_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                cpu = proc.info['cpu_percent']
                mem = proc.info['memory_percent']

                color_tag = ''
                if cpu > 50:
                    color_tag = 'red'
                elif cpu > 20:
                    color_tag = 'orange'

                self.tree.insert('', 'end', values=(pid, name, f"{cpu:.1f}", f"{mem:.1f}"),
                                 tags=(color_tag,))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        self.tree.tag_configure('red', foreground='red')
        self.tree.tag_configure('orange', foreground='orange')

    def kill_process(self):
        selected_item = self.tree.selection()
        if selected_item:
            pid = self.tree.item(selected_item)['values'][0]
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                messagebox.showinfo("Success", f"Process {pid} terminated.")
                self.update_process_list()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                messagebox.showerror("Error", f"Could not terminate process: {e}")
        else:
            messagebox.showwarning("Warning", "No process selected.")

    def open_graph(self):
        subprocess.Popen(["python", "usage_graph.py"])




if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessMonitor(root)
    root.mainloop()
