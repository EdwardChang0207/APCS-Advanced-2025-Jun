# Lesson 3 補充-效能分析

Created: June 13, 2025 7:22 PM

# 📏Session 1. Space Complexity 空間複雜度 ⭐

## 1.空間複雜度 SP(P) = C + SP(I): algo P 之 Space需求

### (1)C:Fixed Space 固定空間需求：

eg.Code Space(Instruction Space)，**變數、常數空間不計**

### (2)SP(I) 動態空間需求:

程式**執行**時，所需之額外動態空間(不包含input space)

來源：

一、有**結構型參數(eg.array, class, struct,…etc)**且採取**“call by value”**傳遞方式

```cpp
//assume int:2 byte, address:2 byte
void Test(int A[], int n){
	...
}
void main(){
	int List[100];
	Test(List, 100); //->call by value:程式需準備100個int空間 = 200 byte
	Test(*List, 100); // ->call by address:程式只需準備一個address的空間 = 2 byte
}
```

二、**Recursion Algo/Code**所需之**Stack** space:

每發生一次Recursion Call → 

push 1.parameter 參數, 2.local variable 區域變數, 3.return address返回位址

以上皆稱為**Activation Record** 再乘以**exec時的遞迴呼叫次數**

### Ex.計算SP(I)

**(1)**

```cpp
float abc(float a, float b, float c){
	return a+b+b*c*(a+b-c)/a+b+4;
}
```

### Sol.

I.Check 結構型參數 → None

II.Check Recursion → None

→ **SP(I) = 0**

**(2)**

```cpp
float sum(float list[], int n){
	float tempsum = 0;
	int i;
	for(i=0; i<n; i++){
		tempsum += list[i];
	}
	return tempsum
}
```

### Sol.

I.Check 結構型參數 → list(array)

II.Check Recursion → None

→ case1: if list[] is **‘call by value’**: **SP(I) = n**

→ case2: if list[] is **‘call by address’**: **SP(i) = 0**

# ⏱️Session 2. Time Complexity 時間複雜度 ⭐⭐⭐

## 1.時間複雜度 T(P) = ~~Development Time(實務上不care)~~ + Execution Time

Execution Time之測量方式：

(1)~~Measurement(實際測量)~~ 

(2)**Analysis(分析、預估)**：統計Algo中指令執行之總次數與資料量n之關係

Ex1.求Time Complexity

```python
for i in range(n):
	for j in range(n):
		count += 1
```

sol.1 Logical Analysis

i = 0: j = 0

i = 1: j = 0~1

i = 2: j = 0~2

…

i = n: j = 1~n

$$
count = \frac{(n+1) \cdot n}{2}
$$

sol.2 級數

$$
count = \sum_{i=1}^{n} \sum_{j=1}^{n} 1=\frac{(n+1) \cdot n}{2}
$$

Ans. $O(n^2)$

Ex2.求Time Complexity

```cpp
for(i=1; i<=n; i++)
	for(j=1; j<=i; j*=2) //lg(i)
		x++
```

sol.

$$
x = \sum_{i=1}^{n} \log_2i = log_2(1*2*3...*n)=log_2(n!) \approx nlog_2n
$$

Ans. $O(nlgn)$

# 🏃Session 3. Growth Rate Of Function 函數成長速率⭐⭐⭐

## (1)常數：

1. 1
2. $n^{\frac{1}{lgn}}$ 

## (2)對數：

1. $lg(lg^*n)$
2. $lg^*n$ and $lg^*(lg(n))$
3. $2^{log^*n}$
4. $ln(ln(n))$
5. $\sqrt{lgn}$
6. $ln(n)$
7. $lg^2n$

## (3) $2^{\sqrt{2lgn}}$

## (4)多項式(polynomial function)

1. $\sqrt{2}^{lgn}$
2. $n$
3. $nlgn$ and $lg(n!)$
4. $n^2 = 4^{lgn}$
5. $n^3$

---

### **polynomial-bound**

## (5) $(lgn)!$

## (6) $(lgn)^{lgn}$

## (7)指數

1. $(\frac{3}{2})^n = 1.5^n$
2. $2^n$
3. $n(2^n)$
4. $e^n$

## (8)階乘

1. $n!$
2. $(n+1)!$

## (9)指數再指數

1. $2^{2^n}$
2. $2^{2^{n+1}}$

# 🖊️Session 4. Asymptotic Notations 漸進式符號⭐⭐⭐

## (1)Big-Oh: $O(f(n))$ → 小於等於

### 1.定義

$f(n) = O(g(n)) \iff \exist \text{ two constants }C,n_0\text{ s.t }f(n) \leq C \cdot g(n), \forall n\geq n_0$

$O(g(n))=\{f(n)\mid\exist C>0, n_0 \text{ s.t }0\leq f(n)\leq cg(n),\forall n\geq n_0 \}$

Note. O is asymptotic “Upper Bound”(上限)

## (2)Little-Oh: $o(f(n))$ → 絕對小於

### 1.定義

$f(n) = o(g(n)) \iff \forall C \text{:positive constant},\exist n_0\text{:postive constant,}\\ \text{ s.t }f(n) < C \cdot g(n), \forall n\geq n_0$

$o(g(n))=\{f(n)\mid\exist C>0, n_0 \text{ s.t }0\leq f(n)< cg(n),\forall n\geq n_0 \}\\(\lim_{n \to \infty} {\frac{f(n)}{g(n)}=0}
)$

## (3)Omega: $\Omega(f(n))$ → 大於等於

### 1.定義

$f(n) = \Omega(g(n)) \iff \exist \text{ two constants }C,n_0\text{ s.t }f(n) \geq C \cdot g(n), \forall n\geq n_0$

$\Omega(g(n))=\{f(n)\mid\exist C>0, n_0 \text{ s.t }0\leq c\cdot g(n)\leq f(n),\forall n\geq n_0 \}$

Note. O is asymptotic “Lower Bound”(下限)

## (4)Little-Omega: $\omega(f(n))$ → 絕對大於

### 1.定義

$f(n) = \omega(g(n)) \iff \forall C \text{:positive constant},\exist n_0\text{:postive constant,}\\ \text{ s.t }f(n) > C \cdot g(n), \forall n\geq n_0$ 

$o(g(n))=\{f(n)\mid\exist C>0, n_0 \text{ s.t }0\leq f(n)< cg(n),\forall n\geq n_0 \}\\\\(\lim_{n \to \infty} {\frac{f(n)}{g(n)}=\infty}
)$

## (5)Theta: $\Theta(f(n))$ → 絕對等於

### 1.定義

$f(n) = \Omega(g(n)) \iff \exist \text{ three constants }C_1,C_2,n_0 \\ \text{ s.t }C_1 \cdot g(n) \leq f(n) \leq C_2 \cdot g(n), \forall n\geq n_0$

$\Theta(g(n))=\{f(n)\mid\exist C_1>0,C_2>0, n_0>0 \text{ s.t }0\leq C_1\cdot g(n)\leq f(n) \leq C_2\cdot g(n),\forall n\geq n_0 \}$

Ex.3 以下哪些是”polynomial-bound”?

(1) $n^2$

(2) $log(n!)$

(3) $2^n$

(4) $(logn)!$

(5) $(loglogn)!$

sol.1

$n^2$ → Yes

sol.2

$log(n!) \approx nlogn$ → Yes

sol.3

$2^n$ → No

sol.4

sol.4

$(logn)!$ → No

$$
\because f(n) \text{ is polynomial bound} \iff log(f(n)) = O(logn)\\
eg.n^{100} \implies log(n^{100}) = 100\cdot log(n) = O(log(n))\\
\therefore log(log(n)!) \approx log(n) \cdot log(logn) [\because log(n!) \approx nlogn]\\
\implies log(n) \cdot log(log(n)) \neq O(logn)\\
\therefore \text{not polynomial-bound} 
$$

sol.5

$(loglogn)!$ → Yes

$$
\because (loglogn)! \approx loglogn \cdot (logloglogn) \leq loglogn \cdot loglogn\\
\implies (loglogn)^2 < logn [\because(logn)^2<n]\\
\therefore (loglogn)! \text{ is polynomial-bound}
$$