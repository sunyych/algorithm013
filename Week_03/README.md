学习笔记
# 递归的实现和特性以及思维要点

* 需要一层层的走，
* 传输函数到每一层
* 每一层都是一个新拷贝
* 循环的另一种形式

## 思维要点

1. 不要人肉进行递归
2. 找最近重复子问题，找最近最简方法
3. 数学归纳法思维


## 递归模板

```Python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return

    # process logic in current level
    process(level, data...)
    # drill down

    self.recursion(level + 1, p1, ...)
    # reverse the current level status if needed
```

## 分治代码模板
```python
def divide_conquer(problem, param1, param2, **args):
    # recursion terminator
    if problem is None:
        print_result
        return

    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems:
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...

    # provess and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
```
