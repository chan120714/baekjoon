# [Platinum V] Simple Game - 33392 

[문제 링크](https://www.acmicpc.net/problem/33392) 

### 성능 요약

메모리: 50028 KB, 시간: 288 ms

### 분류

그리디 알고리즘, 애드 혹, 게임 이론

### 제출 일자

2025년 11월 28일 12:13:37

### 문제 설명

<p>Alice and Bob like playing games. Today they play on a special grid with $2$ rows and $n$ columns. Alice and Bob each have a chess piece, starting at $(1,1)$ and $(2,n)$, respectively. They will take turns moving their chess piece, with Alice going first.</p>

<p>In each turn, they can choose to stay still or move the chess piece to any point adjacent horizontally or vertically which has not been visited by the other's piece. The game will end after $10^{10^{10}}$ turns.</p>

<p>Every point in this grid has a non-negative weight. For each player, the score that he/she gets is the sum of the weights of all the points his/her chess piece has visited. The weight is counted only once, even if the piece visited a point multiple times.</p>

<p>Both Alice and Bob want to maximize the score that they get. As a spectator, you want to know the score that Alice gets if both of them play optimally.</p>

### 입력 

 <p>The first line contains an integer $t$, the number of test cases ($1 \le t \le 5 \cdot 10^4$). The test cases follow.</p>

<p>The first line of each test case contains a single integer $n$ representing the size of the grid ($1 \le n \le 10^5$).</p>

<p>The second line of each test case contains $n$ integers $a_{1,1},a_{1,2},\ldots,a_{1,n}$. The $i$-th of them represents the weight of point $(1,i)$.</p>

<p>The third line of each test case contains $n$ integers $a_{2,1},a_{2,2},\ldots,a_{2,n}$. The $i$-th of them represents the weight of point $(2,i)$.</p>

<p>It is guaranteed that $0 \le a_{i,j} \le 10^9$, and the sum of $n$ across all test cases will not exceed $2.5 \cdot 10^5$.</p>

### 출력 

 <p>For each test case, print a line with a single integer: the score that Alice gets if both players play optimally.</p>

