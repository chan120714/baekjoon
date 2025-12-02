# [Platinum V] 막대 배치 - 8895 

[문제 링크](https://www.acmicpc.net/problem/8895) 

### 성능 요약

메모리: 33432 KB, 시간: 2736 ms

### 분류

수학, 다이나믹 프로그래밍, 조합론

### 제출 일자

2025년 12월 2일 18:35:58

### 문제 설명

<p>There are n poles of height 1, 2, ... , n in a row. If you look at these poles from the left side or the right side, smaller poles are hidden by taller poles. For example, consider the two arrangements of 4 poles in the next figure:</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/polearr.png" style="height:157px; width:412px"></p>

<p>For each arrangement, only one pole can be seen from the left, and two poles can be seen from the right.</p>

<p>You are to write a program to calculate the number of arrangements of n poles such that seen from the left you see l poles and seen from the right you see r poles.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case consists of a line containing three integers, n, l, and r (1 ≤ l,r ≤ n ≤ 20), where n is the number of poles and (resp. r) is the number of poles that can be seen from the left(resp. right).</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for each test case. The line should contain the number of arrangements of poles for the test case.</p>

