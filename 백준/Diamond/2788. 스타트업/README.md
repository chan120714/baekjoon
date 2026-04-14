# [Diamond V] 스타트업 - 2788 

[문제 링크](https://www.acmicpc.net/problem/2788) 

### 성능 요약

메모리: 95784 KB, 시간: 416 ms

### 분류

자료 구조, 세그먼트 트리, 느리게 갱신되는 세그먼트 트리, 볼록 껍질을 이용한 최적화, 키네틱 세그먼트 트리

### 제출 일자

2026년 4월 15일 02:08:14

### 문제 설명

<p>A new town was just inaugurated in a small country. As usual, Mirko has secured the position of the chief tax inspector. His duty is ensuring adequate accounting in all the different companies in the town.</p>

<p>There are N business offices along the main street, numbered 1 to N from left to right. All offices are empty in the beginning; in time, companies will move in and out of these offices. From time to time, Mirko will pass by some of the offices and inspect the accounting of only one company, the currently wealthiest one in those offices.</p>

<p>A company moving in is described by four integers:</p>

<ul>
	<li>T – the move-in day, numbered from town inauguration (which is day 1),</li>
	<li>K – the office number,</li>
	<li>Z – the daily profit of the company (can be negative if the company is losing money),</li>
	<li>S – balance of the company's account on move-in day. </li>
</ul>

<p>If there is already a company in office K, that company moves out when the new company moves in. The new company doesn't open for business (or earn profit) until the day after move-in.</p>

<p>Mirko's inspection stroll is described by three integers:</p>

<ul>
	<li>T – the inspection day, numbered from town inauguration,</li>
	<li>A and B – Mirko will pass by all offices with numbers between A and B, inclusive.</li>
</ul>

<p>Since Mirko works only at the end of the day, all companies will have already finished business and posted profit for the day by the time of Mirko's stroll.</p>

<p>Help Mirko by writing a program to find, for each stroll, the account balance of the currently wealthiest company that Mirko is passing by.</p>

### 입력 

 <p>The first line of input contains two positive integers, N (1 ≤ N ≤ 100 000) and M (1 ≤ M ≤ 300 000), the number of offices and events, respectively.</p>

<p>Each of the following M lines contains a description of one event, formatted either as “1 T K Z S” (for company move-in) or as “2 T A B” (for Mirko's inspection stroll).</p>

<p>All events are given chronologically, and at most one event will happen each day (that is, T will be strictly increasing). The last event's day number will be less than 10<sup>6</sup>, and all Z and S numbers' absolute values will be less than 10<sup>6</sup>.</p>

### 출력 

 <p>For each Mirko's stroll output a line containing the account balance of the company that Mirko will inspect, or the word “nema” (without quotes) if all offices that he will pass by are empty.</p>

