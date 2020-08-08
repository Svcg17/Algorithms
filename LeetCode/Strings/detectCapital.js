/** Detect Capital
 We define the usage of capitals in a word based on the following conditions:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Example 1:

Input: "USA"
Output: True
*/

/**
 * detectCapitalUse - Checks if word uses capitals in a correct way or not 
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    /*
    const sliced = word.slice(1);
    if (word[0] === word[0].toUpperCase()) {
        if (sliced === sliced.toUpperCase()) return true;
        if (sliced == sliced.toLowerCase()) return true;
    } else if (word[0] === word[0].toLowerCase()) {
        if (sliced === sliced.toLowerCase()) return true;
    }
    return false;
    */
    if (word[0] === word[0].toUpperCase() && word[1] && word[1] === word[1].toUpperCase()) {
        for (let i = 2; i < word.length; i++) {
            if (word[i] === word[i].toLowerCase()) return false;
        }
    } else {
        for (let i = 1; i < word.length; i++) {
            if (word[i] == word[i].toUpperCase()) return false;
        }
    }
    return true
   
};


// main
console.log(detectCapitalUse('USA'));
console.log(detectCapitalUse('leetcode'));
console.log(detectCapitalUse('G'));
console.log(detectCapitalUse('g'));
console.log(detectCapitalUse('incOrrecT'));
