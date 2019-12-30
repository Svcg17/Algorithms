function firstDuplicate (a) {
  let idx = {};
  let temp = [];
  let min = 0;
  for (let i = 0; i < a.length; i++) {
    if (!idx[a[i]]) {
     idx[a[i]] = [i]
    } else if (idx[a[i]].length < 2){
      idx[a[i]].push(i)
    } 
  }
  for (let [k, v] of Object.entries(idx)) {
    if (v.length === 2) {
      temp.push(v[1]);
    }
  }
  if (temp.length > 0) {
    min = Math.min.apply(null, temp);
    let key = Object.keys(idx).find(key => idx[key].includes(min))
    return (Number(key))
  } else return -1;
}

