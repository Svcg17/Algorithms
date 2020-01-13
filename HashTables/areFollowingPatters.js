/*
 * areFollowingPatterns
 * Return true if strings follows patterns else return false
 * @strings: array of strings that should match with patterns
 * @patterns: array of strins that represents a sequence that strings should follow
 * Return: true or false
 */
function areFollowingPatterns(strings, patterns) {
    let newDict = {};
    let newSet = new Set();
    
    for (let i = 0; i < patterns.length; i++) {
        newSet.add(strings[i])
        if (newDict[patterns[i]]) {
            if (newDict[patterns[i]] === strings[i]) continue;
            else return false;
        } else {
            newDict[patterns[i]] = strings[i];
        }
    }
    if (Object.keys(newDict).length === newSet.size) return true
    else return false;
}

