# sshbruteforce
This is a Python script that provides a simple shell for brute-forcing SSH passwords. It uses the Paramiko library for SSH connectivity and the Colorama library for color output.

To use the script, simply run it in a Python environment, and then use the connect command to attempt to connect to an SSH server with a given hostname, username, and password file. The password file should contain one password per line. If a successful password is found, the script will output the credentials to a file named credentials.txt. The exit command can be used to exit the script.

# Installing and requirements

     sudo git clone https://github.com/jajbin/sshbruteforce.git 
     
     cd sshbruteforce
     
     sudo pip install -r requirements.txt 
     
     python3 bruteforce-ssh.py

Here's a brief overview of the different parts of the script:

    The import statements bring in the necessary libraries: Paramiko, socket, time, and Colorama.
    The init() function initializes Colorama for color output.
    The GREEN, RED, RESET, and BLUE constants define different color codes for output.
    The SSHBruteForceShell class is defined, which extends the built-in cmd.Cmd class to provide a simple shell.
    The do_connect method is called when the user enters the connect command. It takes three arguments: the hostname, username, and password file path. It then reads the password file into a list, and attempts to connect to the SSH server with each password in turn until a successful connection is made. If a successful connection is made, the credentials are output to the credentials.txt file.
    The is_ssh_open method attempts to connect to the SSH server with a given hostname, username, and password. It returns True if the connection is successful, and False otherwise.
    The do_exit method is called when the user enters the exit command. It exits the script.
    The do_help method is called when the user enters the help command. It outputs a list of available commands.
    The final if statement checks whether the script is being run as the main program, and if so, creates an instance of the SSHBruteForceShell class and enters the shell loop with the cmdloop() method.

#To use this script, you need to have Python installed on your system. Follow these steps to run the script in the command line:

    Save the script to a file with a .py extension, for example ssh_brute_force.py.

    Open a command prompt or terminal window in the directory where you saved the script.

    Type python ssh_brute_force.py and press Enter to run the script.

    Once the script starts running, you'll see the prompt (sshbf) .

    Type help or ? to see the list of available commands.

    Type connect [hostname] [username] [password file] to attempt to connect to an SSH server with a given hostname, username, and password file path. For example, connect example.com myusername passwords.txt.

    If the script successfully connects to the SSH server with a given password, it will output the credentials to a file named credentials.txt.

    Type exit to exit the script.
    
 #Disclaimer about the disuse of this script
This SSH brute force script is for educational purposes only. The use of this script to gain unauthorized access to a system is illegal and strictly prohibited. It is your responsibility to ensure that you have the necessary permissions to test the security of a system before using this script.

Using this script to attempt to gain unauthorized access to a system without the owner's consent may result in legal consequences. Additionally, using this script on a system that you do not have permission to test may cause damage to the system and result in unintended consequences.

The author of this script is not responsible for any damages or legal issues that may arise from the misuse of this script. Use it at your own risk and discretion.

Note: The script requires the paramiko and colorama libraries to be installed. If you haven't already installed them, you can install them using pip. For example, pip install paramiko colorama.
