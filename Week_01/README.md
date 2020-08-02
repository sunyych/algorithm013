# 学习笔记

## 如何高效学习算法教程

1. 三分看视频，七分练习
2. 五毒神掌（敢于放手，敢于死记硬背）
3. 看高手代码
4. 5分钟没思路，直接看题解或高票代码
5. 要过遍数，至少五遍
6. 死磕永在遍数上

## 数组、链表、调表的基本实现和特性

    * 数组ArrayList插入需要进行移动后面的数据，插入平均操作次数是O(n)操作
    * Array copy 效率很低，为了弥补数组缺点增加链表Linked List
    * 链表对象中可以增加Next指针往后面走，还有双向链表和环装链表
    * Linked list添加和删除就是需要调整节点，O（1）操作进行添加和删除操作，查找操作更加复杂
    * Skip list用二叉树和链表结合使用，升维，用空间换时间，增加索引Index
    * LRU Cache Linked list, Redis Skip list

            |             | ArrayList   | Linked list | SkipList |
            | ----------- | ----------- | ----------- | -------- |
            | Prepend     | O(1)        | O(1)        | O(1)     |
            | Append      | O(1)        | O(1)        | O(1)     |
            | Lookup      | O(1)        | O(n)        | O(Log(n))|
            | Insert      | O(n)        | O(1)        | O(Log(n))|
            | Delete      | O(n)        | O(1)        | O(Log(n))|

## 栈Stack，队列Queue，优先队列Priority Queue，双端队列Deque Double-end Queue

    * Stack LIFO class Vector
    * 最近相关性使用栈，洋葱结构
    * Priority Queue:
      * Insert O(1)
      * pull O(Log(n))
      * 用堆实现Heap 

    TODO: 作业： Priority queue源代码分析

# 实战题目

    * 步骤：
        1. 认真读题（5-10分钟）
           a. 暴力解决
           b. 优化暴力解决方式
           c. 找最近重复子问题，动态规划
           d. 找重复性
        2. 有思路直接写，没思路看答案
        3. 不会写代码，会的话自己写

    * 写思路方法：
        1. 写结构伪代码，收集思路
        2. 写几种不同的方法
        3. 找到最好的时间复杂度和空间复杂的的思路，写代码
        4. 写完代码后注意总结feedback

# 题目思路
    1. Move Zero
    2. 盛水最多的容易：双指针，左右往中间涌动
    3. 爬楼梯: f(n) = f(n-1) + f(n-2)
    4. 3 Sum三数之和： 排序加双指针
    5. 有效的括号 Stack栈

## 本周作业

### 简单：

* 用 add first 或 add last 这套新的 API 改写 Deque 的代码
* [分析 Queue 和 Priority Queue 的源码](QP代码分析.md)
* [删除排序数组中的重复项（Facebook、字节跳动、微软在半年内面试中考过）](26.删除排序数组中的重复项(Round1-20200728).py)
* 旋转数组（微软、亚马逊、PayPal 在半年内面试中考过）
* 合并两个有序链表（亚马逊、字节跳动在半年内面试常考）
* 合并两个有序数组（Facebook 在半年内面试常考）
* 两数之和（亚马逊、字节跳动、谷歌、Facebook、苹果、微软在半年内面试中高频常考）
* [移动零（Facebook、亚马逊、苹果在半年内面试中考过）](283.移动零(Round1-20200728).py)
* 加一（谷歌、字节跳动、Facebook 在半年内面试中考过）
  
### 中等：
* 设计循环双端队列（Facebook 在 1 年内面试中考过）
### 困难：
* 接雨水（亚马逊、字节跳动、高盛集团、Facebook 在半年内面试常考）

### 下周预习

#### 预习题目：
  * 有效的字母异位词
  * 二叉树的中序遍历
  * 最小的 k 个数