# Practical5: Command Line Environment

For this practical, we will practice command line environment, very powerful skill that each computer scientist should have.

Type your answers for each question in the main.sh file.

## PART1:  Job Control

1. Start a job to sleep 100 seconds and then pause its execution.
2. Start another job to sleep for 13 minutes and run it in the background.
3. Start one more job to sleep for 1.7 hours without getting affected by the hangup signal, also running in the background.
4. Resume the first job to run in the foregorund and then interrupt its execution.
5. Send a hangup signal to the remaining two jobs. Explain what happens. How can you kill the remaining one? 

----

##  PART2: Creating Aliases

Create three directories under your home folder, called 

* `docsforcomp100_1`
* `docsforcomp100_2`
* `docsforcomp100_3` 

Create three aliases 

`section1`, `section2`, and `section3`

to change directory to `docsforcomp100_1`,  `docsforcomp100_2`, `docsforcomp100_3` respectively, no matter what the current directory is.

Test your implementation. You should be able to switch between directories with your aliases.

----

## PART3: Modifying .bashrc

Recall that many programs are configured using plain-text files known as dotfiles because the file names begin with a '.' and they are listed only when we provide the flag `-a` with `ls`. 

In this assignment, we are going to configure our bash by modifying our `.bashrc` file!

1.  Create an alias `dc` that resolves to `cd` for when you type it wrongly. Then, create a file called `.bash_aliases` under your home directory as we did in the class and append your alias to this file.

2. To make this change permanent, we need to source the aliases file with every terminal session. Remember, we need to modify our `.bashrc` file for that purpose, since it is loaded every time we start a new interactive terminal session.

Add the following

`source ~/.bash_aliases` 

or 

`. ~/.bash_aliases` 

to your `.bashrc` file. As you may remember from the class, this is already done on repl.it (l.105) but you need it if you are on your local terminal. 

3. Start a new terminal session or source your modified `.bashrc` on your current session and test your alias by typing `dc docsforcomp100_1`.

----

## PART4: SSH to a Remote Machine

For this part, please first, refer to LinuxPooL_VPN.md file to setup your environment so that you can connect to the Linuxpool server.

1. As you can see, you have to enter your password every time you ssh to the server. This becomes annoying after a while. For the server to remember us, we can generate a pair of keys on our local machine by using `ssh-keygen` command. Follow the steps, by choosing a directory and a passphrase as prompted. Then check the directory to see the key pair created. 

Now, we need to copy the public key, i.e. the one that ends with .pub, to the server. We do that by using the `ssh-copy-id` command:

`ssh-copy-id -i ~/.ssh/id_rsa.pub USER@linuxpool.ku.edu.tr`

Enter your password one last time and done! Check if it works by doing multiple logins without needing your password.

**Note:** If you're on Windows, `ssh-keygen` part is the same but `ssh-copy-id` is not available. So you need to copy your key "by hand" by doing the following:

`cat env:USER\.ssh\id_rsa.pub | ssh USER@linuxpool.ku.edu.tr 'cat >> ~/.ssh/authorized_keys'`

`env:USERPROFILE\.ssh\id_rsa.pub` is the location of your public key, e.g. `C:\Users\cagan/.ssh/id_rsa.pub` for your TA. If you get confused, please refer to powershell.png under the img folder.

2. Let's dive a bit deeper into the rabbit hole. Linuxpool server actually consists of multiple servers, 6 to be precise, to be able to accommodate all of you. You might have noticed that you are redirected to a different one each time you login, linux02 or linux05, etc. 

For some reason, as you will see in the next part with screen and tmux, you need to be able to switch between servers. While we are logged into one of them, we can ssh to any of them. Let's say we are on linux05, and we want to switch to linux01. All we need to do is:

`ssh linux01`

Why didn't we need the username? Why not `ssh USER@linux01`?

The problem is linux01 does not recognize us coming from linux05. In other words, it does not have a key matching mechanism like the one we created in step 1 between our local machine and the Linuxpool server. As you might guess, we need to the same here on the Linuxpool to be able to jump between servers easily without needing to enter our pasword every time. Use `ssh-keygen`, and then `ssh-copy-id` as we did in the first step.

By doing this for only one of them, we are able to ssh to any of them without a password. We didn't need to repeat it for all the 6 linux servers. Any wild guesses, why?

**Hint1:** Remember what happens when we do `ssh-copy-id`. If we only need to do it once, and then all the servers can see it, what does it mean? 

**Hint2:** Do `pwd` on different servers, and explain what you see.


## PART5: Screen and Terminal Multiplexer (tmux)

In this part, our goal is to practice screen and tmux. We need to ssh to the the Linuxpool server for this purpose (screen and tmux are not installed on repl.it). 

1. Create a tmux session. Name it as `session1`.

2. Run ticker.py in `session1`. Our ticker.py uses a Python module "argparse" that makes it easy to pass an argument to the ticker. You can run it as

`python ticker.py --interval 10`

Then, it will echo the date and time every 10 seconds. 

Now, detach from that session. Do not worry, your code will continue running and printing date and time every 10 seconds in the background. That's what it means to *detach*.

3. List the sessions. You should see `session1` as active.

4. Create another tmux session, and name it `session2`.

5. Run ticker.py in `session2`, but this time, set the print interval to 5 seconds. It will echo the date and time every five seconds. Then detach from that session. As you might guess, your code will continue running in the background.

6. List all the sessions. You should see `session1` and `session2` as active.

7. Attach to `session2`. Check that the ticker.py is still running. Then kill the session.

8. Do the same in step 7 for `session 1`.
