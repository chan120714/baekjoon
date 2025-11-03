# [Platinum V] Kamui - 34658 

[문제 링크](https://www.acmicpc.net/problem/34658) 

### 성능 요약

메모리: 17644 KB, 시간: 324 ms

### 분류

수학, 자료 구조, 세그먼트 트리, 누적 합, 조합론

### 제출 일자

2025년 11월 3일 17:22:42

### 문제 설명

<p>There is a graph with a total of $2N$ vertices. There are no edges between the $1$st and $N$-th vertices, and there are no edges between the $(N+1)$-th and $2N$-th vertices. That is, the given graph is a bipartite graph.</p>

<p>A sequence of positive integers $a_1, a_2, \cdots, a_N$ is given. For any $(i,j)$ pair with $1 \le i, j \le N$, the necessary and sufficient condition for vertices $i$ and $N+j$ to be connected is that $j \le a_i$.</p>

<p>A total of $Q$ queries are given. Each query is represented by two integers $v$ and $x$, indicating that the value of $a_v$ will be changed to $a_v + x$. It is guaranteed that $x = 1$ or $x = -1$. For each query, you must count the number of cycles of length $4$ in the given graph. Since the count may be large, output the remainder when divided by $998\,244\,353$. Two cycles are considered different if the sets of edges composing them are different.</p>

### 입력 

 <p>The first line contains two positive integers $N$ and $Q$, separated by a space.</p>

<p>The second line contains a total of $N$ integers $a_1, a_2, \cdots, a_N$, separated by spaces.</p>

<p>The next $Q$ lines each contain two integers $v$ and $x$ separated by a space. The input on the $i$th line indicates that $a_v$ will be changed to $a_v + x$.</p>

### 출력 

 <p>After each query is executed, output the remainder when the number of cycles of length $4$ is divided by $998\,244\,353$ on each line.</p>

