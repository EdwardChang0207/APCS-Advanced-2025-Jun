# Lesson 3. 時間複雜度

Created: June 23, 2023 1:11 PM

<aside>
💡 編、著:張雲翔，未經許可禁止公開散布、營利使用

</aside>

# Section 1 什麼是複雜度

複雜度可以想像成程式執行時，**所進行的工作次數**。

好比規劃路徑時，同樣從A點到B點，可以有很多不一樣的路徑，其中有些路徑較短，有些路徑較長，在同樣速度的情況下，路徑較短的到達時間較早。

![APCS進階課本圖片.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/APCS%25E9%2580%25B2%25E9%259A%258E%25E8%25AA%25B2%25E6%259C%25AC%25E5%259C%2596%25E7%2589%2587.png)

所以為了增進程式的執行速度，我們必須依據複雜度，選擇執行較快的方法。

---

# Section 2 複雜度計算

你能說出以下程式總共執行了幾次嗎?

```python
for i in range(10):
	print(i)
```

如果我們將10替換掉，你能說出程式共執行幾次嗎?

```python
for i in range(n)
	print(i)
```

所以當我們看到迴圈時，我們會說他的複雜度會是**O(n)**，那麼以下的程式碼你能算出複雜度嗎?

```python
for i in range(n):
	for j in range(n)
		print(j)
```

所以當我們使用巢狀迴圈時，複雜度則變為**O(n^2)**

請判斷以下程式碼的複雜度

```python
for i in range(n)
	for j in range(3*n):
		print(j)
```

此時如果直觀思考，複雜度應為**O(3n^2)**，但討論複雜度時，我們通常**不考慮常數部分**，所以此題的複雜度為**O(n^2)**

## 範例一、複雜度計算

### 請計算以下程式碼的複雜度

```python
for i in range(2*n)
	for j in range(n^2)
		for k in range(n)
```

### 參考解答

一開始，我們先計算程式執行的次數:

$$
2n *n^2*n=2n^4
$$

接著，我們將常數部分省略，所以複雜度為:

$$
O(2n^4) = O(n^4)
$$

# Section 3 程式複雜度

為了了解複雜度和執行次數的關係，我們可以參考以下圖表:

### $O(1)$ 陣列取值

![1.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/1.png)

### $O(n)$ 單層迴圈

![n.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/n.png)

### $O(n^2)$ 巢狀迴圈(兩層)、選擇排序(Selection Sort)、泡泡排序(Bubble Sort)、插入排序(Insertion Sort)

![n^2.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/n2.png)

### $O(n^3)$ 巢狀迴圈(三層)

![n^3.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/n3.png)

### $O(logn)$ 二分搜尋法(Binary Search)

![logn.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/logn.png)

### $O(nlogn)$ 合併排序(Merge Sort)

![nlogn.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/nlogn.png)

### $O(n^n)$

![n^n.png](Lesson%203%20%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%20c3d24cf0341544af9ace725d02fcb16f/nn.png)

# Section 4. 範例練習

## ZeroJudge e283 **APCS 類似題 - 小崴的特殊編碼**

### 題目:

# **小崴要來玩編碼了~~!!!**

這次，他打算跟你講很多字串!

這些字串均經過特殊編碼的~~

祝你全部解讀成功!

P.S. 編碼方式: 每個字串均只由 A~F 組成，

並由以下對照表將每一個字元轉換成長度為4的二元序列

A  -> 0 1 0 1

B  -> 0 1 1 1

C  -> 0 0 1 0

D  -> 1 1 0 1

E  -> 1 0 0 0

F  -> 1 1 0 0

### 輸入說明

**多筆輸入!!!**

**每筆輸入 第一行有一個 正整數N 代表此字串的長度，**

**接下來有n行，每一行給一個字元經編碼後的序列 !**

**以EOF結束~~**

### 輸出說明

**多筆輸出!!!**

**輸出原始字串**

**記得空行歐~~**

### 範例輸入#1

```
1
0 1 0 1
1
0 0 1 0
2
1 0 0 0
1 1 0 0
4
1 1 0 1
1 0 0 0
0 1 1 1
1 1 0 1
```

### 範例輸出#1

```
A
C
EF
DEBD
```

### 參考解答

```python
import sys
a = {"0 1 0 1": "A",
          "0 1 1 1": "B",
          "0 0 1 0": "C",
          "1 1 0 1": "D",
          "1 0 0 0": "E",
          "1 1 0 0": "F"}
 
for i in sys.stdin:
    n = int(i)
    ans = ""
    for j in range(n):
        s = sys.stdin.readline().strip()
        ans += a[s]
    print (ans)
```