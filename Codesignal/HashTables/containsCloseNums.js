/*
 * containsCloseNums - Return true if the distance of two indexes of the same value
 * equals k
 * @nums: array of integers
 * @k: integer
 * Return: true or false
 */
function containsCloseNums(nums, k) {
    let newObj = {};
    
    for (i in nums) {
        if (!newObj[nums[i]]) newObj[nums[i]] = i;
        else {
            if (i - newObj[nums[i]] <= k) return true;
            else newObj[nums[i]] = i;
        }
    }
    return false;
}
