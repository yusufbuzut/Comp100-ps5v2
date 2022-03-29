# PS3.5 - Recursion Problems

# Deadline: 13/12/2020-23:00
In this assignment you will learn how to apply the recursion technique to solve different problems.
This assignment consists of 4 independent problems.

## Problem 1: Permuations of a String
A permutation is simply a name for a reordering. So the permutations of the string `"abc"` are `"abc"`, `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`. Note that a sequence is a permutation of itself (the trivial permutation). For this part of the problem set you will need to write a **recursive** function ``get_permutations``  that takes a string and returns a list of all its permutations.

Please note that: **Recursion MUST be used**, global variables **may NOT** be used. Additionally, it is okay to use loops to code the solution. The order of the returned permutations does not matter. Your returned list must contain exactly n! elements where n is the length of the input sequence. So do not remove duplicate elements from your final list. For example if the input is `'aa'`, you must return exactly `['aa', 'aa']` 


#### Suggested Approach

In order to solve any recursive problem, we must have at least one base case and a recursive case (or cases). We can think of our base case as the simplest input we could have to this problem (for which determining the solution is trivial and requires no recursion). For this approach, our base case is if `sequence`  is a single character (there’s only one way to order a single character).

If `sequence`  is longer than one character, we need to identify a simpler version of the problem that, if solved, will help us easily find all permutations for `sequence`. The pseudocode below gives one approach to recursively solving this problem.


Given an input string `sequence` :
- Base case: if `sequence` is a single character, there’s only one way to order it.
- Recursive case: suppose we have a method that can give us a list of all permutations of **all but the first character**  in `sequence`  (Hint: think recursion).
then the permutations of all characters in `sequence` would be **all the different ways** we can insert the first character into each permutation of the remaining characters
example: if our word was `"comp"`, we hold out the character `"c"` and get the list `["omp", "mop", "mpo", "opm", "pom", "pmo"]`
then `"omp"` gives us: "**c**omp", "o**c**mp", "om**c**p", "omp**c**"
and `"mop"` gives us: "**c**mop", "m**c**op", "mo**c**p", "mop**c**"
and so on ...

Implement the `get_permutations` function in `permutations.py` according to the specifications in the docstring.


## Problem 2: Power Set of a Set
A power set of a set is a set containing all of the subsets of that set.
In this problem you are requiered to generate the power set of a given set.

You will be given a set in the form of a list, for example: `[1, 2, 3]` You can assume that the input list does not contain any duplicate elements.
The power set of this list (represented as a list) is : `[[1,2,3], [1,2], [1,3], [2,3], [1], [2], [3], []]`. Note that the empty list is represented as an empty list `[]`.

You must generate a list containing all of the subsets of the input using **Recursion**. Please not that global variables **MUST NOT** be used. You **MUST NOT** use the `set` data type in python and must only work with lists. the order of your returned subsets in the powerset does not matter.

Implement the `generate_powerset` function in `powerset.py` according to the function specifications.


## Problem 3: Determinant of a Matrix
In linear algebra, determinant of a square matrix A is a number that is assigned to that square matrix and is denoted as `|A|`. It can be computed in different ways, but we are interested in the recursive definition of it:
- The determinant of a 1 by 1 matrix is the single entry in that matrix. 
- Given a larger square matrix which has `n` rows and `n` columns, delete the `0`th row and the `j`th column. This leaves `n-1` rows and `n-1` columns. The determinant of this smaller matrix can be computed recursively. 
- Multiply the determinant of this smaller matrix by the entry in row `0` column `j`, then negate the result if `j` is odd.
- Finally, add up all these products as `j` runs from `0` to `n-1` to obtain the determinant of the original matrix.

You can find the exact mathematical definition of it [here](https://www.bookofproofs.org/branches/recursive-definition-of-the-determinant/ "here") (pay attention that in python we start indexing at `0` but in this link it starts at `1`)

You will be given a matix as a list of lists where each inner list denotes a row of the matrix, for example:
``` 
[[2,3,1],
 [-4,5,2],
 [2,1,-4]]
  ```

You are required to cacluate the determinant of this matrix using **Recursion**. Note that you **MUST NOT** use global variables and you **MUST NOT** use any libraries such as `numpy`. 

Implement the function `determinant` in `matrix.py` according to specifications.


## Problem 4: Strictly Increasing Path in Grid
Consider an M by N grid and suppose that we are in the top-left cell of that grid.

|  1  |  4  |  3  |
|:---:|:---:|:---:|
|**5**|**6**|**7**|

At each step we can go the one of the left, right, up or down cells only if the that cell is **strictly greater than our current cell**. (We cannot move diagonally). We want to find all the paths that we can go from the top-left cell to the bottom-right cell.
In our example, these paths are: 1->4->6->7 and 1->5->6->7

You are given this grid as a list of lists where each sublists corresponds to a row in the grid. For our example the grid would be 
```
[[1,4,3],
 [5,6,7]]
 ```

You are required to print all of the paths that we can take to reach from the top-left cell to the bottom-right cell. Note that you **Must Use Recursion**. Do not forget that the paths must be **strictly increasing**.
You should print each of these paths as a list in a separate line. In our example, they would be:
```
[1, 4, 6, 7]
[1, 5, 6, 7]
```

fill in the `print_paths` function in the `grid.py` file according to the specifications.
Note that you should not return anything. Only print the paths.
(Hint: You can define a helper function that takes the current location and the path traversed so far as inputs and apply recursion on that function)

