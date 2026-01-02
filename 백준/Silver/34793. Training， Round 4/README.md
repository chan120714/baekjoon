# [Silver III] Training, Round 4 - 34793 

[문제 링크](https://www.acmicpc.net/problem/34793) 

### 성능 요약

메모리: 32412 KB, 시간: 56 ms

### 분류

그리디 알고리즘

### 제출 일자

2026년 1월 2일 18:43:32

### 문제 설명

<p>T1 Ashley is training for another programming contest on Brandon's Online Judge. Brandon's Online Judge still has the same feature which allows Ashley's coach, Tom, to load in a list of problems for Ashley to work on.</p>

<p>Tom has curated some problems for Ashley to work on. Each problem is parameterized by "implementation difficulty" and "thinking difficulty", both of which are positive integers. Ashley must solve them in order.</p>

<p>Ashley starts out with a given implementation skill and thinking skill level. Ashley can solve a problem if and only if her implementation skill level is greater than or equal to the implementation difficulty of the problem, and her thinking skill level is greater than or equal to the thinking difficulty of the problem. After solving a problem, exactly one of her implementation skill level and thinking skill level increases by $1$, and Ashley can pick which increases.</p>

<p>Compute the minimum possible sum of implementation and thinking skill levels that Ashley can start out with such that she can solve all the problems on Tom's list in order.</p>

### 입력 

 <p>The first line contains a single integer $n$ ($1 \le n \le 50$).</p>

<p>The next $n$ lines each contain two integers, $i$ and $t$ $(1 \le i, t \le 10^9)$, representing the implementation and thinking difficulties of one of the problems on Tom's list.</p>

<p>The problems are presented in the order that Ashley must solve them.</p>

### 출력 

 <p>Output a single integer, the minimum possible sum of implementation and thinking skill levels that Ashley can start out with such that she can solve all the problems on Tom's list in order.</p>

