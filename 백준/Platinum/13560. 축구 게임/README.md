# [Platinum V] 축구 게임 - 13560 

[문제 링크](https://www.acmicpc.net/problem/13560) 

### 성능 요약

메모리: 33432 KB, 시간: 44 ms

### 분류

수학, 그래프 이론, 그리디 알고리즘, 정렬, 차수열

### 제출 일자

2026년 2월 23일 03:34:40

### 문제 설명

<p>Football is one of the most popular sports in the world. There is a football league with n teams. A team plays against all the other teams and there is exactly one match for each pair of teams. Therefore, each team plays n − 1 matches. A draw is broken by the penalty shoot-out so there is no draw. After a match, if a team wins, it earns one point. If it loses, then it earns zero point.</p>

<p>After the match schedule is over, each team reports its point to the league office to decide the best team. The league office wants to be sure that each team made no mistake in reporting its point. Especially it wants to know whether the reported points are valid, that is, it is possible to assign those points to teams under the league rule.</p>

<p>Given n integers which are points reported by the teams, write a program to determine whether they are valid.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of two lines. The first line contains an integer n (2 ≤ n ≤ 10,000) where n is the number of teams. The next line contains n integers which are points reported by teams. Each integer is between zero and n − 1, inclusive.</p>

### 출력 

 <p>Your program is to write to standard output. Print 1 if the reported points are valid. Otherwise, print -1. </p>

