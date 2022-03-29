# PS2 - Wheel of Fortune
# Deadline: 15/11/2020-23:00

## Introduction

In this problem set, you will implement a modified version of the well-known game Wheel of Fortune (Çarkıfelek in Turkish). 

Throughout this assignment, you will learn how to
* read a text file
* pick a random element from a list 
* run a conditional loop 
* manage lists
* ask the user for input
* manipulate strings
* and properly use functions

## Game Details

Welcome to the game of Wheel of Fortune!  This is a game where you need to have a good sense of English proverbs as well as good fortune.  Before enjoying the gameplay, we will see how to design the game in a single-player fashion.

### First Steps

The game is initiated with reading the "proverbs.txt" file into a list. This file containing a list of famous English proverbs is provided in the same folder. Your program should read it line by line and store it in a list such that every item in the list is a proverb. Finally, you should randomly select one item from that list and keep it in a variable called `proverb`. Now, we know which proverb to ask to the contestant. 

At first, the contestant will see the proverb with every letter replaced with underscore. With every correct guess letters will be revealed.

**Hints:** 
* It might be useful to keep the locations of the vowels in `vowelsLocs` list and the locations of the revealed vowels in `revealedVowelsLocs` list to be used later.
* Similarly, it might be a good idea to keep the consonants in the proverb in a list called `allConsonants`.

### Rewarding and Punishing

Now, we continue with deciding how to reward or cut points. 

Contestant starts with 200 points. They (the contestant) can only make consonant guesses and with every consonant they correctly guess, they are rewarded with some point that is randomly selected between 50 and 150.  

For example if they predict the letter "L" and there are two "L"s in the proverb and if the wheel (random number generator) outputs 73, they would be rewarded with 146  points. With  every  wrong  prediction,  they  lose  75  points.   

At  the  expense  of  250  points they can open a vowel. In this case, one of the vowels in the proverb will be revealed but the contestant will lose 250 points.

**Hint**: Please refer to [the official documentation of Python on random](https://docs.python.org/3/library/random.html) to learn about how random number generator works. Observe why these numbers are called pseudo-numbers. 

### How the Proverb Should Look Like

At each turn of the game, you should print the proverb such that unrevealed letters are replaced by underscores, separated with a white space. None of the proverbs contains any punctuation including full stops, commas and apostrophes.

Also you should print the current score.  At the beginning it will be 200.

### Turns and Turns and Turns...

Each turn, the contestant has three choices:  
1. "Making a guess"
2. "Opening a vowel”
3. "Guessing the whole proverb"  

You should take the input from the contestant. If they press "1", ask for a consonant.  If they enter a vowel or anything that is not alphabetic it will be considered as a wrong answer. True answers will be rewarded as explained before and the correctly guessed letters will be revealed. 
Please write a comment such as 

``Congratulations the letter "K" appears 3 times and you are rewarded with 216 points.`` 

or 

``Unfortunately  the  letter  "B"  does  not  appear  and  you  lose  75  points.``  

Also  keep  a  list  of made guesses. If the same guess is made once more, do not do anything, end the turn. 

If they press "2", reveal one of the vowels and print a message like 

``Letter A is revealed.``

In this case if the letter A appears multiple times, reveal only one of them. 

If they press "3", ask the user for the whole proverb. If the guess is correct reward them with 200 points for every unrevealed letter. If the guess is wrong, they do not lose any additional points but they lose the game. Either way, when "3" is pressed, the game will end this turn.

### This is the End

The game ends either when the contestant's `currentScore` gets below zero or when the contestant presses "3". If the contestant tries to guess the whole proverb, just ask for the whole proverb and end the game accordingly. 

Implement the previous steps in a conditional loop such that every iteration of the loop is a single turn in the game. Exit the loop if;
* The contestant runs out of points (they lose)
* The contestant presses "3"

At the end of the game, please print the proverb all normal. For example, 

``The proverb was:  All for one one for all.`` 

Please print the final score and print out 
``You Won :)`` 
or 
``You Lost :(``

## Helper Functions

It is very important to work in a modular fashion in all sorts of projects. Writing all your code in just one unit might seem appropriate at first. However, if you first read the assignment carefully and try to understand what you need to implement by breaking it into smaller pieces, you will see that it is much easier to accomplish complex tasks. By testing smaller functions and then combining them for higher level tasks, yuo can make your code easier to read and debug. One final perk of using these functions is that you eradicate the need of same pieces of code over and over again in your project. Reusability of the code enhances your coding practices.

Here we provide you with the descriptions of the helper functions that you might need. The most important helper function (`turnRoutine`) is the function that you should call each turn.  Other functions will be used inside the first one. You are advised to write the smaller functions first.


### `turnRoutine`

Gets user input and runs the turn.

**Inputs:** `proverb`, `madeGuesses`, `currentScore`, `vowelsLocs`, `revealedVowelsLocs`
**Outputs:** `madeGuesses`, `currentScore`, `revealedVowelsLocs`, `continueGame`

You should write a function that asks user for input. According to the input, which can be "1", "2" or "3", you should perform certain tasks as described above.

If option "1" is selected, the score and the list of made guesses should be updated accordingly. Also, the proverb should be printed such that known letters are revealed, after the guess is made.

If  option  "2"  is  selected  the  score  should  be  updated.   Proverb  should  be  printed  such  that known consonants and a random vowel are revealed. The index of that vowel should be added to the  `revealedVowelsLocs` list.

If option "3" is selected check whether the game is won or lost. Exit from the loop. You should give an output of `continueGame` as 0, since the game is over.

### `printProverb`

Prints the proverb in a readable way for the user.

**Inputs:** `proverb`, `madeGuesses`, `revealedVowelsLocs`
**Outputs:** -

This function should print the current situation of the game. In the proverb if a letter is in the list of `madeGuesses` or the location of the letter is in the list of `revealedVowelsLocs`, print the letter, otherwise print "_". For whitespaces between words, print "-". To make it look more readable, you can put spaces between tem.

### `openVowel`

Reveals an unrevealed vowel from the proverb.

**Inputs:** `proverb`, `vowelsLocs`, `revealedVowelsLocs`
**Outputs:** `revealedVowel`, `revealedVowelsLocs`

This function should select an unrevealed vowel and add its index to the `revealedVowelsLocs` list.

## Example gameplay

You can check gameplay.txt for an example game play.