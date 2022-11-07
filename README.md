# Binary-Puzzle

## Description
  NxN Binary puzzle which n is an even number. There are empty spots in the puzzle that should get filled. Specific rules should be applied before filling them. Rules are:
  Each row and column should have an equal number of 1's and 0's.
  Each row and column should have an equal string number.
  Each row and column should not have more than two 1 or 0 in a row.
  Example of a 4*4 puzzle:  

  1001  
  0110  
  1100  
  0011    

### Solving the puzzle:
  For solving the puzzle we use the "Backtracking Algorithm".
  Variables are the empty spots and the domain is 0 and 1.
  
### Heuristics:
  MRV: Choose the variable with the fewest possible values.
  LCV: Tries to avoid failure by assigning values that leave maximal flexibility for the remaining variables.
  
### Constraint propagation:
  Forward Checking: Maintains arc-consistency on constraints with exactly one uninstantiated variable 
  MAC: Performs full arc-consistency after each domain value is rejected
  
	
## Usage
	  
### Input Format:
  The first row is (n n). Two numbers are always the same and even.
  Follow by the n*n puzzle with each cell that can have the value of 1, 0, or  -,which is representing the empty spots.  
  **Example:**
  ```
6 6
- - 1 - - 1
- - - 1 1 0
- - 0 - 0 -
0 - - - 0 -
- - - - - -
- - - - - 1
  ```
### Output Format:
  The solved puzzle will be printing on the screen.  
  **Example:**    
![output](https://i.ibb.co/Y36drJG/1.jpg)  
### Graphical output:
A GUI is implemented in order to illustrate stages of solving the puzzle:  
**Early stages:**   
  
![goutput](https://i.ibb.co/tqczs8J/Capture.jpg)    
**Final output:**  
  
![goutput](https://i.ibb.co/5vGzjcc/Capture3.jpg)  
## License
[ GNU GPLv3](https://github.com/DelaramRajaei/Binary-Puzzle/blob/main/LICENSE)
