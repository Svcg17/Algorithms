function rotateImage(a) {
  let arr = new Array();
  for (let i = 0; i < a.length; i++) {
    arr.push(new Array());
    for (var j = a[i].length - 1; j >= 0; j--) {
      arr[i].push(a[j][i])
    }
  }
  return(arr)
}

