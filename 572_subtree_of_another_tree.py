from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub = None

        while root is not None:
            if root.val == subRoot.val:
                sub = root
                break
        
        if sub == None:
            return False
        print(sub.val)
        
        def check(sub1, sub2):
            print(sub1, sub2)
            if sub1.val == sub2.val:
                check_right, check_left = True, True
                if sub1.right is not None:
                    if sub2.right is None:
                        return False
                    else:
                        check_right = check(sub1.right, sub2.right)
                else:
                    if sub2.right is not None:
                        return False
                
                if sub1.left is not None:
                    if sub2.left is None:
                        return False
                    else:
                        check_left = check(sub1.left, sub2.left)
                else:
                    if sub2.left is not None:
                        return False
                if check_right and check_left:
                    return True
                return False
            else:
                return False

        return check(sub, subRoot)
    
root = TreeNode()