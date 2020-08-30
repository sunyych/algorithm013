# 贪心算法

* 眼前最优求得全局最优，通常用于辅助算法。与动态规划区别在于不能回退

# 二分查找

## 前提

1. 目标函数的额单调性
2. 存在边界
3. 能够通过索引快速访问

一次去掉一半的数据，指数级时间复杂度的运算

## 二分查找模板

```python
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target:
            return reuslt
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```