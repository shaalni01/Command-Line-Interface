<h1 align = "center">
COMMAND LINE INTERFACE APPLICATION
</h1>

<h2>Introduction</h2>
In the realm of computer systems, a shell serves as a vital interface between users and the underlying operating system, 
enabling efficient interaction through a command-line interface. This code represents the implementation of a shell, 
equipped with a comprehensive set of commands designed to empower users with control over their computer systems.

<h2>Implementation</h2>
The implemented shell supports a range of essential commands, each serving a specific purpose. For instance, the "cd" 
command allows users to navigate and change the current default directory, with the ability to report the current directory
if no argument is provided. Furthermore, it updates the PWD (Present Working Directory) environment variable,
 ensuring consistent tracking of the current directory.
 
 <h2>Execution of Commands</h2>
 The sample screenshot for the cd command
 <img src="https://github.com/shaalni01/Command-Line-Interface/blob/main/assets/Creating%20cd%20command.JPG"/>

`clr`: The "clr" command clears the screen, providing users with a clean and uncluttered environment for executing subsequent commands.
The sample screenshot for the clr command

<img src="https://github.com/shaalni01/Command-Line-Interface/blob/main/assets/Creating%20clr%20command.JPG"/>

`dir`: Meanwhile, the "dir" command lists the contents of a specified directory, enabling users to examine the files and subdirectories it contains.
The sample screenshot for the dir command is

<img src="https://github.com/shaalni01/Command-Line-Interface/blob/main/assets/Creating%20Dir%20Command.JPG"/>

`environ` :The "environ" command provides users with a valuable overview of all the environment strings associated with the shell session.
 This includes variables and settings that influence the shell's behavior and functionality.

`echo`:The "echo" command allows users to display custom comments on the screen, facilitating informative and interactive interactions. 
 Multiple spaces or tabs within the comment are intelligently reduced to a single space, ensuring clarity in the displayed output.
 The sample screensht for the echo command
 
 <img src="https://github.com/shaalni01/Command-Line-Interface/blob/main/assets/Creating%20Quit%20Command.JPG"/>

`help`:For users seeking guidance and assistance, the "help" command proves invaluable. It presents a detailed list of all available commands, 
along with their inputs and behaviors. This comprehensive command reference equips users with the knowledge to maximize their utilization of 
the shell's capabilities.

`pause`:To accommodate varying needs, the shell also features the "pause" command, enabling users to temporarily suspend the shell's operation until they
 press the "Enter" key. This functionality is particularly useful when users require a momentary interruption without exiting the shell.

`quit`:Lastly, the "quit" command gracefully terminates the shell session, allowing users to exit the environment effortlessly.
The same screenshot for the Quit Command

<img src="https://github.com/shaalni01/Command-Line-Interface/blob/main/assets/Creating%20Quit%20Command.JPG"/>

Additionally, this shell implementation provides support for output redirection, a powerful feature that enhances usability and versatility. 
By utilizing the redirection tokens ">" and ">>", users can redirect command outputs to specified files. If the file does not exist, 
it will be created, while existing files can be either truncated or appended to, based on the chosen redirection token.

By leveraging this shell implementation and its diverse command set, users gain a robust toolset for efficient system navigation, 
file management, environment exploration, and interactive communication. With the added advantage of output redirection, 
users can streamline their workflows and tailor their command outputs to specific needs.

Now, users can embark on a seamless and productive journey with the implemented shell, 
harnessing its capabilities to simplify tasks and maximize their productivity within the computer system environment.
