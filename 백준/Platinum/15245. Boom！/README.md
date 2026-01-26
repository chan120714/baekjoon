# [Platinum II] Boom! - 15245 

[문제 링크](https://www.acmicpc.net/problem/15245) 

### 성능 요약

메모리: 309472 KB, 시간: 1356 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학

### 제출 일자

2026년 1월 27일 05:11:11

### 문제 설명

<p dir="ltr">Tadhg has found an interesting tape in his school chemistry lab. The tape is divided into N segments of equal length, and can easily be bent between two segments, but only by exactly 180 degrees.</p>

<p dir="ltr">One side of the tape is completely covered with a very volatile chemical. If the chemical comes in contact with itself, it reaches critical mass and explodes.</p>

<p dir="ltr">The other side of the tape is not completely covered yet. Only the first A segments and last B segments are covered, with the exact same chemical.</p>

<p dir="ltr">Write a program that will calculate the number of different ways Tadhg can bend the tape so that it does not explode. He can bend the tape more than once and two ways are different if there is at least one bevel between segments that is not bent in one and is bent in the other.</p>

<p dir="ltr">Since the solution can be huge, print the result modulo 10301.</p>

<p dir="ltr">The following example illustrates all 6 possible ways for N=4, A=1 and B=1. For clarity, the tape is only bent 90 degrees on the illustration. Tadhg would actually bend it 180 degrees.</p>

<p dir="ltr" style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15245/1.png" style="height:125px; width:300px"></p>

<p dir="ltr">Note: The unbent stage counts as 1 position</p>

### 입력 

 <p dir="ltr">The first and only line of input contains three natural numbers N, A and B (A>0, B>0, A+B ≤ N ≤ 1000), total number of segments, number of covered segments from the left and from the right respectively.</p>

### 출력 

 <p dir="ltr">The first and only line of output should contain the number of possible ways to bend the tape modulo 10301.</p>

