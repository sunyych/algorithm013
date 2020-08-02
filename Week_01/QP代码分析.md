# Queue cpython source code:
    [queue.py](https://github.com/python/cpython/blob/3.8/Lib/queue.py)

## Queue

* 从现有倒入可以看到这个Queue是使用的Simple Queue，增加功能得来，是Thread safe，拥有线程保护，可以用于多线程变成
  * 线程锁主要有三个标准，都是一些简单功能，但在多线程操作是非常重要：
    * not_empty,
    * not_full，
    * all_tasks_done,
* 初始值设定queue的大小，如果没有设置则为无穷大
* 主要逻辑都在put和get操作增加了空间缩和异常
* 在Python中，队列是最常用的线程间的通信方法，因为它是线程安全的，自带锁。而Condition等需要额外加锁的代码操作，在编程对死锁现象要很小心，Queue就不用担心这个问题。

Queue多线程代码示例如下：

``` Python

from Queue import Queue
import time,threading
q=Queue(maxsize=0)
 
def product(name):
    count=1
    while True:
        q.put('气球兵{}'.format(count))
        print ('{}训练气球兵{}只'.format(name,count))
        count+=1
        time.sleep(5)
def consume(name):
    while True:
        print ('{}使用了{}'.format(name,q.get()))
        time.sleep(1)
        q.task_done()
t1=threading.Thread(target=product,args=('wpp',))
t2=threading.Thread(target=consume,args=('ypp',))
t3=threading.Thread(target=consume,args=('others',))
 
t1.start()
t2.start()
t3.start()

```

## Prority Queue

* 优先队列使用了 heapq 模块的结构，用heappush和heappop分别实现put和get
* 一个简单的例子

    ```python
    import queue

    class A:
        def __init__(self, priority, value):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority

    q = queue.PriorityQueue()

    q.put(A(1, 'a'))
    q.put(A(0, 'b'))
    q.put(A(1, 'c'))

    print(q.get().value)
    ```
