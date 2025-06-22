# Lesson 2 遞迴 Recursion

Created: June 23, 2023 1:11 PM

<aside>
💡 編、著:張雲翔，未經許可禁止公開散布、營利使用

</aside>

# ❓Section 1. 什麼是遞迴

遞迴函式是指**會在函式中呼叫自己的函式**，例如以下範例:

```python
def a(i):
	if i < 1:
		return 1
	return a(i-1)
```

從上面的程式碼，我們可以看到在a(i)中，如果i大於1時，程式會再呼叫a(i-1)，這個函式我們就可以稱為遞迴函式

---

# 🎨Section 2. 遞迴結構與設計

當我們要設計遞迴函式時，我們會需要先了解遞迴函式的結構

```python
def recursion_func(p):
	if 終止條件
		return 初始值
	return recursion_func(p-1)
```

在使用遞迴時，我們必須設置一個**收斂**的條件，使程式在執行時不會變成無限迴圈，最終超過，python對於遞迴的限制導致程式崩潰。

補充:python對於遞迴限制通常為10^3

## 常見的遞迴範例：

### Ex.1 連續加法：計算1+2+3+…+i的總和

$$
f(n) = 
\begin{cases} 
f(n-1) + n & \text{for } n \geq 2, \\
1 & \text{for } n = 1.
\end{cases}
$$

```python
def sum(i):
 if i == 1: return 1
 return i + sum(i-1)
```

### Ex.2 階乘：計算n!的值

$$
f(n) = 
\begin{cases} 
f(n-1) \cdot n & \text{for } n \geq 1, \\
1 & \text{for } n = 0.
\end{cases}
$$

```python
def f(n):
	if n == 0: return 1
	return n * f(n-1)
```

### Ex.3 指數(exp)：計算x的n次方

[sol1] O(n)

$$
f(x, n) = 
\begin{cases} 
f(x, n-1) \cdot x & \text{for } n \geq 1, \\
1 & \text{for } n = 0.
\end{cases}
$$

```python
def f(x, n):
	if n == 0: return 1
	return f(x, n-1) 
```

[sol2] O(logn)

$$
f(x, n) = 
\begin{cases} 
1 \cdot (x^2)^{\frac{n}{2}} & \text{for } n \text{ even}, \\
x \cdot (x^2)^{\frac{n}{2}} & \text{for } n \text{ odd}.
\end{cases}
$$

```python
def f(x, n):
	if n % 2 == 0:
		f = 1
	else:
		f = x
	if n < 2: return f
	return f*f(x*x, n/2) 
```

### Ex.4 費氏數列 Fibonacci Numbers

$$
F(n) = 
\begin{cases} 
0 & \text{for } n = 0, \\
1 & \text{for } n = 1, \\
F(n-1) + F(n-2) & \text{for } n \geq 2.
\end{cases}
$$

```python
def f(n):
	if n == 0: return 0
	if n == 1: return 1
	return f(n-1)+f(n-2)
```

### Ex.5 阿克曼函數

$$
A(m, n) =
\begin{cases}
n + 1 & \text{if } m = 0, \\
A(m-1, 1) & \text{if } m > 0 \text{ and } n = 0, \\
A(m-1, A(m, n-1)) & \text{if } m > 0 \text{ and } n > 0.
\end{cases}
$$

```python
def A(m,n):
	if m == 0: return n + 1
	else:
		if n == 0: return A(m-1, 1)
		return A(m-1, A(m, n-1))
```

### Ex.6 二項式係數

$$
\binom{n}{m} = \frac{n!}{k!(n-k)!}
$$

降階公式

$$
\binom{n}{m} = \binom{n-1}{m-1} + \binom{n-1}{m}
$$

```python
def Bin(n, m):
	if n == m or m == 1: return 1
	return Bin(n-1, m) + Bin(n, m-1) #二項式係數降階公式
```

# 🥊Section 3. 遞迴 V.S. 迴圈

## 例題:輸出0累加到9

## 迴圈(Loop):

### for loop:

```python
ans = 0
for i in range(10):
	ans += i
print(i)
```

### while loop:

```python
i = 0
while i <= 9:
	print(i)
	i += 1
print(i
```

## 遞迴(Recursion)

```python
def func(i):
	if i > 0:
		return (i+func(i-1))
	return 0
```

# 🔨Section 4. 遞迴實作

如前面所述，當我們要設計一個遞迴函式，我們必須要定義一個**收斂**的執行範圍，接著依據程式內容進行呼叫

## ZeroJudge e357 **遞迴函數練習**

### 題目:

定義一個函數F(x)，

若x = 1, 則 F(x) = 1
若x 為偶數，則 F(x) = F(x/2)

其餘狀況，F(x) = F(x - 1) + F(x + 1)

**輸入說明**

輸入只有一行，其中包含一個正整數x (1 <= x <= 2000000)。

**範例輸入#1**

`6`

**輸出說明**

輸出只有一行，其中包含一個正整數F(x)。

**範例輸出#1**

`2`

### 參考解答:

```python
def F(x):
    if x == 1:
        return 1
    elif x % 2 == 0:
        return F(int(x/2))
    return F(x-1) + F(x+1)

print(F(int(input())))
```

**執行時間: 44ms**

**檔案大小: 3.3MB**

# 👨‍🏫Section 5. 解題範例

## ZeroJudge d487 **Order's computation process**

### 題目:

1751年，歐拉以大寫字母 M 表示 m 階乘

M=1．2．3．...．m

1799 年，魯非尼在他出版的方程論著 述中，則以小寫字母 π 表示 m 階乘。

而在 1813年，高斯則以 Π(n) 來表示 n 階乘。

用來表示 n 階乘的方法起源於英國，但仍未能確定始創人是誰。

直至1827年，由於雅萊特的建議而得到流行，現在有時也會以這個符號作為階乘符號。

而最先提出階乘符號 n! 的人是克拉姆（1808），後來經過歐姆等人的提倡而流行，直至現在仍然通用。

**輸入說明**

每行一個整數 n

0 <= n <= 10

**輸出說明**

輸出 n! = n * (n-1) * (n-2) * ... * 2 * 1 = ( n! 的答案 )

請注意空格的輸出

處理完每組測資請換行

**範例輸入#1**

`0`

`5`

**範例輸出#1**

`0! = 1 = 1`

`5! = 5 * 4 * 3 * 2 * 1 = 120`

### 參考解答:

```python
import sys
def F(x):
    if x > 1:
        return x*F(x-1)
    else:
        return 1

for i in sys.stdin:
    print(int(i), '! = ',sep='', end='')
    if int(i) == 0: print(1, end=' ')
    else: 
        [print(j, end=' * ') for j in range(int(i), 1, -1)]
        print(1, end=' ')
    print("=", F(int(i)))
```

**執行時間: 18ms**

**檔案大小: 3.3MB**