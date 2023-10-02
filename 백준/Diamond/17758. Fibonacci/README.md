# [Diamond IV] Fibonacci - 17758 

[문제 링크](https://www.acmicpc.net/problem/17758) 

### 성능 요약

메모리: 34384 KB, 시간: 252 ms

### 분류

분할 정복을 이용한 거듭제곱, 수학, 정수론

### 문제 설명

<p>Liczby Fibonacciego definiujemy następująco:</p>

<p style="text-align: center;">F<sub>0</sub> = 0, F<sub>1</sub> = 1, F<sub>m</sub> = F<sub>m−1</sub> + F<sub>m−2</sub> dla m ≥ 2.</p>

<p>Twoim zadaniem jest znalezienie takiego k, że zapis dziesiętny liczby F<sub>k</sub> (bez zer wiodących) kończy się zadanym ciągiem cyfr.</p>

### 입력 

 <p>W jedynym wierszu wejścia znajduje się napis złożony z n cyfr <span style="border-top: 1px solid #555;">c<sub>1</sub>c<sub>2</sub>...c<sub>n</sub></span> (1 ≤ n ≤ 18, 0 ≤ c<sub>i</sub> ≤ 9).</p>

### 출력 

 <p>Jeśli istnieje choć jedna taka liczba całkowita k, że 0 ≤ k < 10<sup>100</sup> oraz zapis dziesiętny liczby F<sub>k</sub> kończy się ciągiem cyfr <span style="border-top: 1px solid #555;">c<sub>1</sub>c<sub>2</sub>...c<sub>n</sub></span>, to na wyjście należy wypisać dowolną taką liczbę. W przeciwnym razie na wyjście należy wpisać słowo NIE.</p>

