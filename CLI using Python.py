import os
import sys
from os.path import exists


def banner():
    print(" #########################################    ")
    print("This is the command line interface developed by SHALINI PILLI")
    print(" #########################################    ")


def tool_usage():
    print("cd <directory name>  to change the current directory")
    print("clr to clear the screen")
    print("dir <directory name> to list the contents of directory")
    print("environ to list the environment strings")
    print("echo <comment> to display <comment> followed by a new line; accepted commands: echo <text> or echo > or >> <filename.txt> <text> ")
    print("help to display a list of all commands")
    print("pause to pause operation of the shell")
    print("quit to quit the shell")

def run_clr(t,flag):
    if not flag:
        os.system('cls')

def run_echo(comments,flag):
    if flag:
        #divide the string accordingly -  done
        #check if the file exists - done
        #if no then create a file - both tasks taken care of by open() function 
        #write the ouput into the file - done
        # print(comments)
        temp = comments.split(" ",2)
        # print("after split",temp)
        indicator = temp[0]
        file_name = temp[1]
        task = temp[2]
        path = os.getcwd() + "/" + file_name
        hehe = ""
        res = task.split(" ")
        for i in res:
            if not(i == ""):
                hehe = hehe + i + " "
        print(hehe)
        if(indicator == ">>"):
            a = 'a'
        elif indicator == ">":
            a = 'w'
        with open(path, a) as f:
            print("writing into the file", hehe)
            f.write(hehe)
            f.write("\n")
    else:
        comment = comments.split(" ")
        for i in comment:
            if not(i == ""):
                print(i, end =" ")
        print("\n")

def run_help(t,flag):
    command_list = {
        "clr": "clears the screen",
        "cd":"<directory name>  to change the current directory",
        "dir" : "<directory name> to list the contents of directory; accepted commands: dir <path> or dir <path> > or >> <filename.txt>",
        "environ" : "list the environment strings; accepted commands: environ or environ > or >> <filename.txt>",
        "echo" : "echo <comment> to display <comment> followed by a new line; accepted commands: echo <text> or echo > or >> <filename.txt> <text>",
        "help" :  "help to display a list of all commands ; accepted commands: help or help > or >> <filename.txt>",
        "pause": "pause to pause operation of the shell",
        "quit": "quit to quit the shell",
        "for output redirection" : "Make sure that there are spaces in between the command and > Ex : help > example.txt"
    }
    if flag:
        indicator = t.split(" ",1)[0]
        print(indicator)
        file_name = t.split(" ", 1)[1]
        path = os.getcwd() + "/" + file_name
        if(indicator == ">>"):
            a = 'a'
        elif indicator == ">":
            a = 'w'
        with open(path, a) as f:
            print("writing into the file")
            for i in command_list:
                hehe = i + ":" + command_list[i]
                f.write(hehe)
                f.write("\n")
        
    else:
        for i in command_list:
            print(i, ": ", command_list[i])

def run_pause(t,flag):
    if not flag:
        # //os.system("read -p 'Press Enter to continue...' var")
        # //print("Press Enter to continue")
        # input()
        if sys.platform == 'win32':
            #print("hello you are in win32")
            os.system('pause')
        else:
            print("Press any key to continue")
            input()


def run_cd(path,flag):
    #Need to keep all the os calls in the try catch block
    if not flag:
        # print("inside runcd")
        try:
            os.chdir(path)
            print(os.getcwd())
        except:
            print("Invalid Directory Path")

def run_dir(directory,flag):
    # path = os.getcwd(y)+"/"+directory
    print(directory)
    isabsolute = False
    check = directory.split(" ",2)[0]
    if(os.path.isabs(check)):
        isabsolute = True
    if not flag:
        if isabsolute:
            path = check
            print(os.listdir(path))
        else:
            path = os.getcwd()+"/"+check
            print(os.listdir(path))
    else:
        indicator = directory.split(" ",2)[1]
        print(indicator)
        # path_given = directory.split()[0]
        if(isabsolute):
            result = os.listdir(check)
        else:
            path_given = os.getcwd()+"/"+check
            result = os.listdir(path_given)
        file_name = directory.split()[2]
        path = os.getcwd() + "/" + file_name
        if(indicator == ">>"):
            a = 'a'
        elif indicator == ">":
            a = 'w'
        with open(path, a) as f:
            print("writing into the file")
            for i in result:
                f.write(i)
                f.write("\n")


def run_environ(t,flag):
    if not flag:
        result = os.environ
        for i in result:
            print(result[i])
    else:
        file_name = t.split(" ", 1)[1]
        indicator = t.split(" ", 1)[0]
        path = os.getcwd() + "/" + file_name
        result = os.environ
        if(indicator == ">>"):
            a = 'a'
        elif indicator == ">":
            a = 'w'
        with open(path, a) as f:
            print("writing into the file")
            for i in result:
                f.write(i)
                f.write("\n")


def confirm():
    print("Please press (yes/no) or (y/n)\n to execute any other options")
    option = input()
    if "yes" in option or "y" in option:
        status = True
    else:
        status = False
    return status


def run_quit(t,flag):
   if not flag:
        print("\nExiting CLI Tool")
        sys.exit()


def show_invalid_option_message():
    print("Invalid Option..!")


def launch_cli():
    try:
        loop_flag = True
        user_confirmation_flag = False
        outputintofile_flag = False

        banner()
        tool_usage()
        try:
            options = input("Enter the option: \n" )
            if(">" in options or ">>" in options):
                # print("***************")
                outputintofile_flag = True
            # print(options)
            # print("Hello I am here")
            command = options.split(' ', 1)[0]
            result = " "
            if(command == "cd" or command == "dir" or command == "echo" or outputintofile_flag):
                result = options.split(' ', 1)[1]
                # print(result)
        except ValueError:
            print("Error! This is not an options. Try again.")
            launch_cli()

        option_redirection = {
            "clr": run_clr,
            "cd": run_cd,
            "dir": run_dir,
            "environ": run_environ,
            "echo": run_echo,
            "help": run_help,
            "pause": run_pause,
            "quit": run_quit
        }

        while loop_flag:
            if options == "quit":
                loop_flag = False
                run_quit("t",False)

            selected_func = option_redirection.get(command, lambda: "Noting")
            # print(options)
            # print("before printing selected func")
            # print(selected_func)
            if(command == 'cd' or command == 'dir' or command == 'echo' or outputintofile_flag):
                # print(result)
                selected_func(result,outputintofile_flag)
            else:
                selected_func("check", outputintofile_flag)
            
            if loop_flag:
                user_confirmation_flag = confirm()
            else:
                loop_flag = False

            if user_confirmation_flag:
                tool_usage()
                try:
                    outputintofile_flag = False
                    options = input("Enter the option: \n" )
                    if(">" in options or ">>" in options):
                        # print("252 line ***************")
                        outputintofile_flag = True
                    # print("In the second options")
                    # print(options)
                    # print("Hello I am here")
                    command = options.split(' ', 1)[0]
                    result = " "
                    if(command == "cd" or command == "dir" or command == "echo" or outputintofile_flag):
                        result = options.split(' ', 1)[1]
                        # print(result)
                except ValueError:
                    print("Error! This is not a number. Try again.")
                    launch_cli()
                user_confirmation_flag = False
            else:
                loop_flag = False
                run_quit("t",False)

    except KeyboardInterrupt:
        run_quit("t", False)


launch_cli()
