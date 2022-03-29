## PART 0: Getting Started with Repl.it

0. **Please use VPN if you're connecting from outside Turkey.** You can follow [these steps](https://confluence.ku.edu.tr/kuhelp/ithelp/it-services/network-and-wireless/vpn-access) for VPN access. 
1. Please go to https://github.com/ and create an account with your Koc University e-mail.
2. Please go to https://repl.it/ and click `sign up`. At the top of the menu, find `Git` symbol and connect to Repl.it using your Git account.
3. You will recieve a verification code in your e-mail. Type it and `verify`. Please hit `Authorize Repl.it Online IDE`.
4. Go to the link provided here: [Practical-1: The Shell](https://classroom.github.com/a/4mO89Rm9). Find and click onto your student id. `Authorize github` and `Accept this assignment`. 
5. After a minute, refresh the page and you should see `Work in repl.it` button. `Authorize github` again. You should be directed to the Repl.it page, where we will conduct our lab session.
6. On the left, you will see the shell file `main.sh`, hidden file `.replit` and `instructions.md` file where you will find the instructions for the practical.
7. At the bottom-right, you will see `terminal` on which we will be writing our shell commands. Please follow the instructions and look for the right command. Hit `enter` to run your commands. Do not hessitate to try and observe the results.
8. `ctrl+l` and backspace icon at the top-right of the clears the terminal. Please never clear the terminal during the session, so that we can see your progress. Do not worry about wrong answers or failed trails. As long as you try to answer exercise questions and try to learn the material, you will get a *Complete*.
9. **At the end of the session *before closing the repl.it tab*, please let the TA know that you are finished. We will check your terminal and view your commands. When the TA confirms that you have completed the tasks you can close repl.it.**


## PART1: Hello World!

The goal of this programming exercise is to make sure your python and numpy settings are correct, to get you more comfortable with using Repl.it, and to begin using simple elements of Python. Standard elements of a program include the ability to print out results (using the `print` operation), the ability to read input from a user at the console (for example using the `input` function), and the ability to store values in a variable, so that the program can access that value as needed.

**Repl.it and Basic git**

Before you start, follow these tutorials first:
1. [The Repl Environment](https://docs.repl.it/misc/quick-start#the-repl-environment)
2. [Repl.it + Git tutorial](https://repl.it/talk/learn/Replit-Git-Tutorial/23331)


**Raising a Number to a Power and Taking a Logarithm**

Write a program that does the following in order:

1. Asks the user to enter a number x.
2. Asks the user to enter another number y.
3. Prints out the number x, raised to the power y.
4. Prints out the log (base 2) of x.
5. Commit your work to the master branch with a meaningful commit message. Note that only your latest commit counts and it should be before the deadline.

Use Repl.it to create your program, and save your code in the file named 'main.py'. An example of an interaction with your program is shown below.

```
Enter number x: 2
Enter number y: 3
x**y = 8
log(x) = 1
```

**Hints**

* To see how to use the `print` command, you may find it convenient to look at the [input](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Hello,_World) and [output](https://en.wikibooks.org/wiki/Learning_Python_3_with_the_Linkbot/Who_Goes_There%3F) of the Python Wikibook. This will show you how to use print statements to print out values of variables.

* To see how to read input from a user's console into the Python environment, you may find it convenient to look at the same section (see for example the `input()` function).

* Reference the [basic math section](https://en.wikibooks.org/wiki/Python_Programming/Basic_Math) of the Python Wikibook to read more about using basic mathematical operators in Python.

* To take the logarithm of a variable, import either of the `numpy` or `pylab` packages. You can then call either `numpy.log2` or `pylab.log2` to calculate the logarithm. See [Repl.it tutorial](https://docs.repl.it/misc/quick-start#the-repl-environment) on importing packages and [the many Numpy examples](https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html#log2.28.29) online for more info. Googling the `log2` function may take you [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.log2.html), which has some helpful info.

* Remember that if you want to hold onto a value, you need to store it in *a variable* (i.e., give it a name to which you can refer when you want that value). You may find it convenient to look at [the Variables and Strings section](https://en.wikibooks.org/wiki/Python_Programming/Variables_and_Strings) of the Python Wikibook. (As you read through, remember that in Python 3.x you should be using `input()` not `raw_input()`). Take a look at [the "Combining Numbers and Strings" sub-section](https://en.wikibooks.org/wiki/Python_Programming/Variables_and_Strings#Combining_Numbers_and_Strings), because you will be working with numbers and strings in this problem and will have to convert between the two using the `str()` and `int()` functions.