# Lesson 1 解題技巧&高階函式

Created: June 23, 2023 1:11 PM

<aside>
💡 編、著:張雲翔，未經許可禁止公開散布、營利使用

</aside>

# 📜Section 1. 解題秘笈: **三+四速解公式**

## 👀解題秘笈(上): 三步破題法

### STEP 1. 瀏覽題目了解大綱

許多題目都寫得很艱澀難懂，很多學生在閱讀題目這關就會不知所措。看到題目有一堆字，加上符號看不懂，**常會給人題目很難的錯覺**，但如果將邏輯整理清楚，其實題目並不會那麼複雜，**甚至可以在短短幾分鐘內就完成解題**。

在一開始看到題目時，**不要逐字閱讀，先大概瀏覽大綱**，類似於國文的閱讀測驗，不需要將每個字句都讀完，只要**大概了解題目的內容即可**。

### STEP 2. 觀察輸入與輸出範例

很多的題目中，會有很多讓人閱讀起來很困難的符號，這時候**千萬不要從題幹中試著理解這些符號**，先去看看輸入和輸出範例，你會更快的知道這些符號的意義。

### STEP 3. 將輸入輸出內容對照回題幹

最後將你剛剛觀察到的內容統整後，對照到原本的題目中，你會發現**比起逐字檢視，理解題目，你省下了超過50%的時間**。

---

## 🔥解題秘笈(下): IFPO四步速解公式

<aside>
💡 程式結構口訣:2134 FI-PO

</aside>

### STEP 1. (I) INPUT: 獲取輸入

**一、判斷輸入類型:**

先從範例輸入中判斷，該題的輸入類型是**連續輸入**或是**單次輸入**

若是連續輸入，則需要使用**stdin**進行輸入，此時我們就必須先**import sys**套件

```python
#單次輸入
input()

#連續輸入
import sys
for i in sys.stdin:
```

**二、整理輸入內容:**

在判斷完輸入類型後，我們需要從範例輸入中整理出所有輸入的內容，可以參考以下範例表格

| 第幾行 | 內容 | 資料型態 |
| --- | --- | --- |
| 1 | x,y,z  | int,int,int |
| 2 | name | str |

### STEP 2. (F) FUNCTION: 解題工具

判斷程式中是否有**同樣的功能需要重複使用**，如果有的話，使用**function**的形式將功能建立

```python
def function_name(parameters):
	#function_process...
	return result
```

### STEP 3. (P) PROCESS: 程式流程

依據題目，安排程式的流程，**先做哪些步驟，再做哪些步驟**，是否需要迴圈、條件?將其完整規劃。

```python
# STEP 2 FUNCTION
	def add(a,b):
		return a+b

# STEP 1 INPUT
import sys
for i in sys.stdin:

# STEP 3 PROCESS
	a,b = map(int, i.split())
	ans = add(a,b)
# STEP 4 OUTPUT
```

### STEP 4. (O) OUTPUT: 輸出結果

依據題目的要求及範例輸出，我們可以將輸出的內容整理成一個和輸入一樣的表格

| 第幾行 | 內容 | 資料型態 |
| --- | --- | --- |
| 1 | a,b | int,int |
| 2 | ans | int |

```python
# STEP 2 FUNCTION
	def add(a,b):
		return a+b

# STEP 1 INPUT
import sys
for i in sys.stdin:

# STEP 3 PROCESS
	a,b = map(int, i.split())
	ans = add(a,b)
# STEP 4 OUTPUT
	print(a,b)
	print(ans)
```

---

## 範例一、 [zerojudge b964 成績指標 (apcs 2016.Mar 第一題)](https://zerojudge.tw/ShowProblem?problemid=b964)

### **題目:**

一次考試中，於所有及格學生中獲取最低分數者最為幸運，反之，於所有不及格同學中，獲取最高分數者，可以說是最為不幸，而此二種分數，可以視為成績指標。

請你設計一支程式，讀入全班成績(人數不固定)，請對所有分數進行排序，並分別找出不及格中最高分數，以及及格中最低分數。

當找不到最低及格分數，表示對於本次考試而言，這是一個不幸之班級，此時請你印出「worst case」；反之，當找不到最高不及格分數時，請你印出「best case」。

( 註：假設及格分數為 60 )。

**輸入說明**

第一行輸入學生人數，第二行為各學生分數(0~100 間)，分數與分數之間以一個空白間格。

每一筆測資的學生人數為 1~20 的整數。

**輸出說明**

每筆測資輸出三行。

第一行由小而大印出所有成績，兩數字之間以一個空白間格，最後一個數字後無空白

第二行印出最高不及格分數，如果全數及格時，於此行印出 best case 

第三行印出最低及格分數，如果全數不及格時，於此行印出 worst case 。

**範例輸入 #1**

`10`

`0 11 22 33 55 66 77 99 88 44`

**範例輸出 #1**

`0 11 22 33 44 55 66 77 88 99`

`55`

`66`

**範例輸入 #2**

`1`

`13`

**範例輸出 #2**

`13`

`13`

`worst case`

**範例輸入 #3**

`2`

`73 65`

**範例輸出 #3**

`65 73`

`best case`

`65`

### 範例解答(一) 21ms, 3.4MB

```python
#STEP 2 FUNCTION
def print_all(s):
	for i in range(len(s)):
		if i != len(s)-1: print(s[i], end=' ')
		else: print(s[i])

def cases(s): #STEP 4 OUTPUT
	if s[0] >= 60: #best case
		print_all(s)
		print('best case')
		print(s[0])		
	elif s[-1] < 60: #worst case
		print_all(s)
		print(s[-1])
		print('worst case')
	else:
		print_all(s)
		high, low = 0, 0
		for i in s:
			if i < 60: low = i
			if i >= 60: 
				high = i
				break
		print(low)
		print(high)

#STEP 1 INPUT
n = int(input())
s = [int(i) for i in input().split()]

#STEP 3 PROCESS
s.sort()
cases(s)
```

### 範例解答(二) 18ms, 3.3MB

```python
#STEP 2 FUNCTION
def print_all(s):
	for i in range(len(s)):
		if i != len(s)-1: print(s[i], end=' ')
		else: print(s[i])
def find(s):
	for i in s:
			if i < 60: low = i
			if i >= 60: 
				high = i
				break
	return [low, high]
cases = lambda s:[s[-1],'worst case'] if s[-1] < 60 else ['best case',s[0]] if s[0] >= 60 else find(s)

#STEP 1 INPUT
n = int(input())
s = list(map(int, input().split()))
#STEP 3 PROCESS
s.sort()
c = cases(s)
#STEP 4 OUTPUT
print_all(s)
print(c[0])
print(c[1])

```

---

# 🧰Section 2. 高階函式

在這個章節中，我們將會介紹常用一些常用的函式讓解題效率大增

| 名稱 | 用途 | 範例 |
| --- | --- | --- |
| a, b = int, int | 多重賦值 | `a, b = 3, 4` |
| map(func, [data]) | 對每一個data執行func | `a = map(int, input().split())` |
| [func(index) for index in [list]] | 使用for loop對每一個index執行func後，將結果存於新的list中 | `x = [int(i) for i in input().split()]` |
| eval(’expression’) | 得到函式中程式片段的執行結果 | `x = eval(’2+2’)` |
| lambda p1, p2: func | 完成一次性的簡短函式內容 | `x = lambda a,b: 1 if (a+b)%2 == 0 else 0` |

## 範例一、 [zerojudge a002 **簡易加法**](https://zerojudge.tw/ShowProblem?problemid=a002)

### **題目:**

請寫一個程式，讀入兩個數字，並求出它們的和。

**輸入說明:**
 每組輸入共一行，內含有兩個整數 a, b，以空白隔開，a, b絕對值皆小於10^6

**範例輸入 #1:**

`5 10`

**範例輸入 #2:**

`1 2`

**輸出說明:** 
對於每組輸入，輸出該兩整數的和。

**範例輸出 #1:**

`15`

**範例輸出 #2:**

`3`

### 範例解答(一) 18ms, 3.3MB

```python
a,b = map(int, input().split())
print(a+b)
```

### 範例解答(二) 18ms, 3.3MB

```python
print(sum(map(int,input().split())))
```

## 範例二、 [zerojudge a003 兩光法師占卜術](https://zerojudge.tw/ShowProblem?problemid=a003)

### **題目:**

兩光法師時常替人占卜，由於他算得又快有便宜，因此生意源源不絕，時常大排長龍，他想算 得更快一點，因此找了你這位電腦高手幫他用電腦來加快算命的速度。

他的占卜規則很簡單，規則是這樣的，輸入一個日期，然後依照下面的公式：

M=月
D=日
S=(M*2+D)%3

得到 S 的值，再依照 S 的值從 0 到 2 分別給與 普通、吉、大吉 等三種不同的運勢

**輸入說明:**

輸入資料共一行，包含兩個整

數，分別為月份及日期

**範例輸入 #1:**

`1 1`

**範例輸入 #2:**

`1 2`

**輸出說明:** 

運勢

**範例輸出 #1:**

`普通`

**範例輸出 #2:**

`吉`

### 範例解答(一) 18ms, 3.3MB

```python
m,d = map(int, input().split())
s = (m*2+d)%3
r = lambda s: '普通' if s == 0 else '吉' if s == 1 else '大吉'
print(r(s))
```

## 範例三、 [zerojudge a017 五則運算](https://zerojudge.tw/ShowProblem?problemid=a017)

### **題目:**

計算五則運算式的結果，包含加、減、乘、除、餘

**輸入說明:**

輸入資料若干行直到 EOF 為止。

每一行包含輸入一個字串，其中包含運算元及運算子，為了方便讀取，所有的運算子及運算元均以空格區隔。

運算元為 0 ~231 -1 的整數

運算子則包含 + - * / % 及 ( )

運算時請注意先乘除後加減及() 優先運算的計算規則

**輸出說明:** 

對每一行輸入，輸出運算結果。

為了避免小數點誤差，所有的運算過程都不會產生小數點，可以放心使用整數進行運算

**範例輸入 #1**

`2 + 3 * 4`

`2 * ( 3 + 4 ) * 5`

**範例輸出 #1**

`14`

`70`

### 範例解答(一) 18ms, 3.3MB

```python
from sys import stdin
for i in stdin:
    print(eval(i.replace('/','//')))
```

---

# 👨‍🏫Section 3.解題範例

## 範例一、 [zerojudge c291 小群體 APCS 2017年三月第二題](https://zerojudge.tw/ShowProblem?problemid=c291)

### **題目:**

計算五則運算式的結果，包含加、減、乘、除、餘

問題描述

Q同學正在習程式， P老師出了以下的題目讓他練習。

一群人在一起時經常會形成一個一個的小群體。假設有 N個人，編號由 0到 N-1，每個人都寫下他最好朋友的編號（最好朋友有可能是他自己的編號，如果他自己沒有其他好友）， 在本題中，每個人的好友編號絕對不會重複，也就是說0到 N-1每個數字 都恰好出現一次。

這種好友的關係會形成一些小群體。例如 N=10，好友編號如下，

| 自己編號 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 好友編號 | 4 | 7 | 2 | 9 | 6 | 0 | 8 | 1 | 5 | 3 |

0的好友是 4，4的好友是 6，6的好友是 8，8的好友是 5，5的好友是 0，所以 0、4、 6、8、和 5就形成了一個小群體。另外， 1的好友是7而且7的好友是1，所以1和7形成另一個小群體，同理3和9是一個小群體，而2的好友是自己，因此他的好友是自己，因此他自己是一個小群體。總而言之在這個例子裡有4個小群體：{0,4,6,8,5}、{1,7} 、{3,9} 、 {2} 。本題的問題是：輸入每個人好友編號，計算出總共有幾小群體。

Q同學想了卻不知如何下手，和藹可親的P老師於是給了他以下的提示：如果你從任何一人x開始，追蹤他的好友，好友的好友，….，這樣一直下去，定會形成個圈回到 x，這就是一個小群體。如果我們追蹤的過程中把追蹤過的加以標記，很容易知道哪些人已經追蹤過，因此當一個小群體找到之後，我們再從任何還未蹤過的開始繼續找下一個小群體，直到所有人都追蹤完畢。

Q同學聽完之後很順利的成了作業。

在本題中，你的任務與Q同學一樣：給定群人的好友，請計算出小群體個數。

**輸入說明:**

第一行是一個正整數N，說明團體中人數。

第二行依序是 0的好友編號 、1的好友編號 、…… 、N-1的好友編號。共有N個數字，包含 0到 N-1的每個數字恰好出現一次，數字間會有一個空白隔開。

**輸出說明:** 

請輸出小群體的個數。不要有任何多餘的字或空白，並以換行字元結尾。

**範例輸入 #1**

`10`

`4 7 2 9 6 0 8 1 5 3`

**範例輸入 #2**

`3`

`0 1 2`

**範例輸出 #1**

`4`

**範例輸出 #2**

`2`

### 範例解答(一) 56ms, 9.2MB

```python
#STEP 2.FUNCTION
def find(cur):
    visited[cur]=True
    while not visited[friends[cur]]:
        cur=friends[cur]
        visited[cur]=True

#STEP 1.INPUT
n=int(input())
friends=list(map(int,input().split()))

#STEP 3.PROCESS
visited=[False]*n
ans=0
for i in range(n):
    if not visited[i]:
        find(i)
        ans+=1

#STEP 4.OUTPUT
print(ans)
```

## 範例二、 [zerojudge b966 線段覆蓋長度 APCS 2016年三月第三題](https://zerojudge.tw/ShowProblem?problemid=b966)

### **題目:**

給定一維座標上一些線段，求這些線段所覆蓋的長度，注意，重疊的部分只能算一次。

例如給定 4 個線段：(5, 6)、(1, 2)、(4, 8)、(7, 9)，如下圖，線段覆蓋長度為 6 。

[](https://zerojudge.tw/ShowImage?id=956)

**輸入說明:**

第一列是一個正整數 N ，表示此測資有 N 個線段。
接著的 N 列每一列是一個線段的開始端點座標整數值 L 和結束端點座標整數值 R ，開始端點座標值小於等於結束端點座標值，兩者之間以一個空格區隔。

其中  30%的測資滿足， N < 100 ， 0 ≤ L , R < 1000 ，並且線段沒有重疊。
其中  70%的測資滿足， N < 100 ， 0 ≤ L , R < 1000 ，並且線段可能重疊。
其中100%的測資滿足， N < 10000 ， 0 ≤ L , R < 10000000 ，並且線段可能重疊。

**輸出說明:** 

輸出其總覆蓋的長度。

本題為**嚴格比對**，請務必按照說明進行輸出。

**範例輸入 #1**

`5`

`160 180`

`150 200`

`280 300`

`300 330`

`190 210`

**範例輸入 #1**

`1`

`120 120`

**範例輸出 #1**

`110`

**範例輸出 #1**

`0`

### 範例解答(一) 75ms, 5.6MB

```python

#STEP 1.INPUT
N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

#STEP 2.FUNCTION
l.sort(key= lambda x:(x[0],x[1]))
t = 0
s, e = l[0][0], l[0][1]

#STEP 3.PROCESS
for i in range(1, len(l)):
    if l[i][0] > e:
        t += e - s
        s, e = l[i][0], l[i][1]
    else:
        if l[i][1] > e:
            e = l[i][1]
t += e-s

#STEP 4.OUTPUT
print(t)
```