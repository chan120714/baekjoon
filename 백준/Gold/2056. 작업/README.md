# [Gold IV] 작업 - 2056 

[문제 링크](https://www.acmicpc.net/problem/2056) 

### 성능 요약

메모리: 33432 KB, 시간: 376 ms

### 분류

다이나믹 프로그래밍, 그래프 이론, 방향 비순환 그래프, 위상 정렬

### 제출 일자

2026년 2월 22일 19:24:34

### 문제 설명

<p>Farmer John's family pitches in with the chores during milking, doing all the chores as quickly as possible. At FJ's house, some chores cannot be started until others have been completed, e.g., it is impossible to wash the cows until they are in the stalls.</p>

<p>Farmer John has a list of N (3 <= N <= 10,000) chores that must be completed. Each chore requires an integer time (1 <= length of time <= 100) to complete and there may be other chores that must be completed before this chore is started. We will call these prerequisite chores. At least one chore has no prerequisite: the very first one, number 1. Farmer John's list of chores is nicely ordered, and chore K (K > 1) can have only chores 1,.K-1 as prerequisites. Write a program that reads a list of chores from 1 to N with associated times and all perquisite chores. Now calculate the shortest time it will take to complete all N chores. Of course, chores that do not depend on each other can be performed simultaneously.</p>

### 입력 

 <ul>
	<li>Line 1: One integer, N</li>
	<li>Lines 2..N+1: N lines, each with several space-separated integers. Line 2 contains chore 1; line 3 contains chore 2, and so on. Each line contains the length of time to complete the chore, the number of the prerequisites, Pi, (0 <= Pi <= 100), and the Pi prerequisites (range 1..N, of course).</li>
</ul>

### 출력 

 <p>A single line with an integer which is the least amount of time required to perform all the chores.</p>

