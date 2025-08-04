# [Unrated] Judging Divisionals - 16621 

[문제 링크](https://www.acmicpc.net/problem/16621) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

분류 없음

### 제출 일자

2025년 8월 5일 04:29:07

### 문제 설명

<p>After the 2018 South Pacific Divisionals, twelve teams advance to the South Pacific Regionals (you are one of those 12 teams! Congratulations!). Each team competing in the Divisionals is part of either the Central, Eastern or Western division. The teams are ranked from lowest to highest (lower is better). The 12 teams are selected in two selection steps:</p>

<ul>
	<li>Selection Step I: For each division, the best-ranked team from this division is selected (say that they are from University X), then the next best-ranked team from this division that is not from University X is selected. A total of 6 teams are selected this way.</li>
	<li>Selection Step II: Then 6 more teams are selected by repeatedly taking the the best-ranked team such that (a) they have not already been selected and (b) at most one other team from their university has already been selected.</li>
</ul>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/57739fed-e439-4711-ad4c-d59db95cef08/-/preview/" style="width: 604px; height: 341px;"></p>

<p>Which teams are selected to advance to the Regionals?</p>

### 입력 

 <p>The first line of input contains a single integer n (12 ≤ n ≤ 100), which is the number of teams that competed in the Divisionals.</p>

<p>The next n lines describe the teams (from lowest ranked first to highest ranked last). Each of these lines contains three strings which are the name, division, and university of a team, respectively. Each of these strings contains only lowercase and uppercase letters and consists of at least 1 and at most 100 characters. The division is one of Central, Eastern or Western.</p>

<p>It is guaranteed that it is possible to select the 12 teams given the above selection steps. All universities have distinct names and each university belongs to exactly one division. All teams have distinct names.</p>

### 출력 

 <p>Display the twelve teams that are selected, sorted from lowest to highest ranking.</p>

