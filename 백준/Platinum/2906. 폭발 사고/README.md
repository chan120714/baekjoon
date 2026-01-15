# [Platinum II] 폭발 사고 - 2906 

[문제 링크](https://www.acmicpc.net/problem/2906) 

### 성능 요약

메모리: 309464 KB, 시간: 1292 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2026년 1월 15일 16:41:56

### 문제 설명

<p>Luka found an interesting tape in the chem lab. The tape is divided into N segments of equal length, and can easily be bent between two segment, but only by exactly 180 degrees.</p>

<p>One side of the tape is completely covered with a very volatile chemical. If the chemical comes in contact with itself, it reaches critical mass and explodes.</p>

<p>The other side of the tape is not completely covered yet. Only the first A segments and last B segments are covered, with the exact same chemical.</p>

<p>Write a program that will calculate the number of different ways Luka can bend the tape so that it does not explode. He can bend the tape more than once and two ways are different if there is at least one bevel between segments that is not bent in one and is bent in the other</p>

<p>Since the solution can be huge, print the result modulo 10301.</p>

<p>The following example illustrates all 6 possible ways for N=4, A=1 and B=1. For clarity, the tape is only bent 90 degrees on the illustration. Luka would actually bend it 180 degrees.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/52ce6484-e80c-42f5-a5cd-6ec9932b8b1c/-/preview/" style="width: 594px; height: 280px;"></p>

### 입력 

 <p>The first and only line of input contains three natural numbers N, A and B (A>0, B>0, A+B ≤ N ≤ 1000), total number of segments, number of covered segments from the left and from the right respectively.</p>

<p> </p>

### 출력 

 <p>The first and only line of output should contain the number of possible ways to bend the tape modulo 10301.</p>

