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
```

* 二叉搜索树（BST）
  * 查询和操作都是log（n）
  
* 树的面试算法都是递归，为什么？
  * 递归操作就是对重复操作的一个简化
  * 每个树节点和每个树节点的操作都是一样的，对左右子树的操作


## 堆和二叉堆的实现和特性

* 堆Heap用于找最大值或者最小值的数据结构
  * 二插堆的实现是完全二叉树
  * 完全二叉树用一维数组操作
  * 二插堆的左右节点2i+1，2i+2
  * 二插堆的操作：


## 图的实现和特性

* 有点，边，线
* 图的属性： 点Vertex和边Edge
  * 点

## 做题四部曲

1. clarification
2. possible solutions ->optimal time and space
3. code
4. test

