function isCryptSolution(crypt, solution) {
    let dict = {};
    let match = '';
    let sum = [];
    for (let i = 0; i < solution.length; i++) {
      dict[solution[i][0]] = solution[i][1]
    }
    for (let i = 0; i < crypt.length; i++) {
        match = '';
        for (let j = 0; j < crypt[i].length; j++) {
            if (dict[crypt[i][j]]) match += dict[crypt[i][j]];
        }
        sum.push(match)  
    }
    if (sum[2].length === 1 && sum[2] == 0 && sum[1] == 0 && sum[0] == 0) return true;
    if ((sum[0].length > 1 || sum[1].length > 1 || sum[2].length > 1) && (parseFloat(sum[0][0]) === 0 || parseFloat(sum[1][0]) === 0) || parseFloat(sum[2][0]) === 0) return false;
    else if (parseFloat(sum[0]) + parseFloat(sum[1]) === parseFloat(sum[2])) return true;
    else return false;
}

