# Practical-1: The Shell

[The recorded MIT lecture] (https://www.youtube.com/watch?v=Z56Jmr9Z34Q&feature=emb_logo)

## Exercises
1. Please run the command `$SHELL`.

2. Create a new directory called `practicals` under `/home/runner/Shell`.

3. Look up the `touch` program using `--help`.

4. Use `touch` to create a new file called `semester` in `practicals`.

5. Write the following into that file, one line at a time:
`#!/bin/sh`
`curl --head --silent https://missing.csail.mit.edu`

The first line might be tricky to get working.
It might be helpful to know that # starts a comment in Bash, and ! has a special meaning even within double-quoted (") strings. 
Bash treats single-quoted strings (') differently: they will do the trick in this case.

6. Try to execute the file, i.e. type the path to the script (./semester) into your shell and press enter. 
Understand why it doesn’t work by consulting the output of `ls` 
**Hint**: look at the permission bits of the file.

7. Run the command by explicitly starting the `sh` interpreter, and giving it the file `semester` as the first argument, i.e. `sh semester`. 
Why does this work, while `./semester` didn’t?

8. Look up the `chmod` program using `--help`.

9. Use chmod to make the command `./semester` *executable* rather than having to type `sh semester`. 
How does your shell know that the file is supposed to be interpreted using `sh`?

10. Use `|` and `>` to write the "last modified" date output by `semester` into a file called `last-modified.txt` in your home directory.
