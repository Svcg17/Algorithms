/*
 * Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
    sub-boxes of the grid.

Empty cells are indicated by the character '.'.
*/

/* @desc checks if the current number can be placed in the board correctly
 * @param [[]] board - 2d board representing the puzzle board
 * @param int row - current row in the board
 * @param int col - current col in row
 * @param int num - value to try to include in the board
 * @return: true or false
 */
function isValidPlace(board, row, col, num) {
    let rowIdx = Math.floor(row / 3) * 3;
    let colIdx = Math.floor(col / 3) * 3;
    // valid in rows and columns
    for (let i = 0; i < 9; i++) {
        if (board[row][i] === num){
            return false 
        }
        if (board[i][col] === num)  {
            return false
        }
    }
    // valid in 3x3 subarray
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[rowIdx + i][colIdx + j] === num) {
                return false
            }
        }
    }
    return true
}
/* @desc iterates through all possible rows and columns, recursively calling
 * itself and backtracking to constantly change values to check when needed.
 * @param [[]] board - 2d array of characters representing the puzzle
 * @param int row - current row of board
 * @param int col - current column of row
 * @return true or false
 */
function solver(board, row, col) {
    // if last column has been reached, increment row
    if (col == board[row].length) {
        col = 0;
        row++;
        // if last row has been reached, success
        if (row == board.length) {
            return true
        }
    }
    // skip already placed characters
    if (board[row][col] != ".") {
        return solver(board, row, col + 1)
    }
    // try to place nums from 1 to 9
    for (let i = 1; i <= 9; i++) {
        if (isValidPlace(board, row, col, i.toString())) {
            // if valid, set value in board
            board[row][col] = i.toString();
            // recursively calls itself to check next column
            if (solver(board, row, col + 1)) {
                return true;
            }
            // placement failed, backtracking
            board[row][col] = ".";
        }
    }
    // no value could be placed
    return false
}
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    solver(board, 0, 0)
};


// main
board = [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
solveSudoku(board)
for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
        process.stdout.write(board[i][j])
    }
    console.log()
}
