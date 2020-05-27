function sudoku2(grid) {
  let subOne = {};
  let subTwo = {};
  let subThree = {};
  let dupRow = {};
  let dupCol = {};
  for (let i = 0; i < grid.length; i++) {
    dupCol = {};
    if (i % 3 === 0) {
      subOne = {};
      subTwo = {};
      subThree = {};
    }
    for (let j = 0; j < grid[i].length; j++) {
      if (parseInt(grid[i][j]) > 0 && parseInt(grid[i][j]) < 10) {
        if (j < 3) {
          if (!subOne[grid[i][j]]) subOne[grid[i][j]] = 1;
          else subOne[grid[i][j]] += 1;
        } else if (j < 6) {
           if (!subTwo[grid[i][j]]) subTwo[grid[i][j]] = 1;
          else subTwo[grid[i][j]] += 1;
        } else if (j < 9) {
           if (!subThree[grid[i][j]]) subThree[grid[i][j]] = 1;
          else subThree[grid[i][j]] += 1;
        }
          if (!dupCol[grid[i][j]]) dupCol[grid[i][j]] = 1;
          else dupCol[grid[i][j]] += 1;
        }
      if (dupCol[grid[i][j]] > 1 || subOne[grid[i][j]] > 1 || subTwo[grid[i][j]] > 1 || subThree[grid[i][j]] > 1) {
        return false;
      }
    }
  }
        
  for (let i = 0; i < grid.length; i++) {
   dupRow = {};
    for (let j = 0; j < grid[i].length; j++) {
      if (parseInt(grid[j][i]) > 0 && parseInt(grid[j][i]) < 10) {
        if (!dupRow[grid[j][i]]) dupRow[grid[j][i]] = 1;
        else dupRow[grid[j][i]] += 1;
      }
      if (dupRow[grid[j][i]] > 1) {
        return false;
      }
    }
  }
  return true;
}

