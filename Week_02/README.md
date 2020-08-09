# 学习笔记

## 哈希表、映射、集合的实现和特征

* 通过哈希函数转化成Index
* 哈希碰撞
```Python
list_x = [1,2,3,4]
map_x = {'jack': 100, 'Rose': 80}
set_x = {'jack', 'rose', 'andy'}
set_y = set(['jack','rose','andy'])
```

## 树、二叉树、二叉搜索树的实现和特性

* 树和图的区别是图循环，树不循环
* 抽象生活到树型结构，Decision Tree
```Python
class TreeNode:
# standard tree
    def __init__(self, val):
        self.val=val
        self.left, self.right = None, None
```
* 树的遍历
  * 前序遍历（Pre-order）：根-左-右
  * 中序遍历（In-order）：左-根-右
  * 后序遍历（Post-order）：左-右-根
```Python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)



## 做题四部曲
1. clarification
2. possible solutions ->optimal time and space
3. code
4. test

