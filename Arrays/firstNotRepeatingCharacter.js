function firstNotRepeatingCharacter(s) {
   let arr = new Array();
   let dup = new Set();
   for (const i of s) {
       if (arr.includes(i)) dup.add(i);
       else arr.push(i)
   }
   for (const j of dup) {
      s = s.replace(new RegExp(`[${j}]`, 'gi'), '')
    }
    if (s.length === 0) return '_';
    return s[0]
}
