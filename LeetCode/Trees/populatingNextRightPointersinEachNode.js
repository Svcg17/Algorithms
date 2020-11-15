/** 
 * ----- Populating Next Right Pointers in Each Node ------
 * Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
 * Initially, all next pointers are set to NULL.
 * 
 * Restrictions:
 * You may only use constant extra space.
 * Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 */

/**
 * Definition of a Node
 * @param {Number} val 
 * @param {Node} left 
 * @param {Node} right 
 * @param {Node} next 
 */
function Node(val, left, right, next) {
   this.val = val === undefined ? null : val;
   this.left = left === undefined ? null : left;
   this.right = right === undefined ? null : right;
   this.next = next === undefined ? null : next;
};


/**
 * Populates each node's next node to its right sibling, if exists.
 * @param {Node} root
 * @return {Node} root
 */
var connect = function(root) {
    let leftmost = null
    let curr = root
    
    while (root && curr.left && curr.right) {
        curr.left.next = curr.right
        leftmost = curr.left
        while (curr.next) {
            curr.right.next = curr.next.left
            curr = curr.next
            curr.left.next = curr.right
        }
        curr = leftmost
    }
    return root
};
