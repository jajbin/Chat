# sshbruteforce
This is a Python script that provides a simple shell for brute-forcing SSH passwords. It uses the Paramiko library for SSH connectivity and the Colorama library for color output.

To use the script, simply run it in a Python environment, and then use the connect command to attempt to connect to an SSH server with a given hostname, username, and password file. The password file should contain one password per line. If a successful password is found, the script will output the credentials to a file named credentials.txt. The exit command can be used to exit the script.

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

