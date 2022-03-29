# Practical-3: Data Wrangling

For this Practical, we will practice processing text in different types of files with regular expressions using bash commands. You can access shell environment by writing $SHELL into terminal.

Please use `sh download.sh` to download files (htmls.txt, words.txt, ssh_log.txt) and before pushing your code to github, **DO NOT FORGET TO DELETE THEM**.

Type your answers for each question in the main.sh file.

----

## Part-1

1. Find the html tag groups for each line. Tag groups are specified by `<Name of the group>`. The tags can be anything, `<a>`, `<div>`, etc. but always between left and right angle brackets.

For example, for `<a>bla bla bla</a>`, you need to print `a`. 

2. Find the html contents for each line. Contents are in between tag open and tag close. 

For example, for `<div>bla bla bla</div>`, you need to print `bla bla bla`.

**Hint:** You can use `sed` command.

----

## Part-2

3. Find words in "words.txt" with at least three `a` or `A` (both capital and small) letters.

**Hint:** You should probably use `cat` command, then, feed its output into `grep` command.

4. Find the most common last two letters in the words you found in Question 3.

**Hint:** You can use `sort` and `uniq` commands.

----

## Part-3

5. Find the most common 5 invalid usernames in ssh_log.txt file.

6. Find the most common 5 blocked usernames in ssh_log.txt file.

7. Find the most common 5 invalid or blocked usernames in ssh_log.txt file.


