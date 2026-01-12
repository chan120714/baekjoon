# [Platinum II] Lexical Sign Sequence - 16580 

[문제 링크](https://www.acmicpc.net/problem/16580) 

### 성능 요약

메모리: 6432 KB, 시간: 52 ms

### 분류

자료 구조, 그리디 알고리즘, 느리게 갱신되는 세그먼트 트리, 우선순위 큐, 세그먼트 트리

### 제출 일자

2026년 1월 12일 18:13:44

### 문제 설명

<p>Andi likes numbers and sequences, especially, sign sequences. A sign sequence is a sequence which consists of −1 and 1. Andi is a curious person, thus, he wants to build a sign sequence which length is N (the positions are numbered from 1 to N, inclusive).</p>

<p>However, Andi also likes some challenges. Therefore, he prefilled some positions in the sequence with −1 or 1 (the number in these positions cannot be changed). Andi also wants the sequence to fulfill K constraints. For each constraint, there are 3 numbers: A<sub>i</sub>, B<sub>i</sub>, and C<sub>i</sub>. This means that the sum of numbers which position is in the range [A<sub>i</sub>, B<sub>i</sub>] (inclusive) must be at least C<sub>i</sub>.</p>

<p>Sounds confusing, right? It is not done yet. Since there can be many sequences that fulfill all the criteria above, Andi wants the sequence to be lexicographically smallest. Sequence X is lexicographically smaller than sequence Y if and only if there exists a position i where X<sub>i</sub> < Y<sub>i</sub> and X<sub>j</sub> = Y<sub>j</sub> for all j < i.</p>

<p>Find the sequence Andi wants.</p>

### 입력 

 <p>Input begins with a line containing two integers: N K (1 ≤ N ≤ 100000; 0 ≤ K ≤ 100000) representing the length of the sequence and the number of constraints, respectively. The second line contains N integers: P<sub>i</sub> (−1 ≤ P<sub>i</sub> ≤ 1). If P<sub>i</sub> = 0, then the i<sup>th</sup> position in the sequence is not prefilled, otherwise the i<sup>th</sup> position in the sequence is prefilled by P<sub>i</sub>. The next K lines, each contains three integers: A<sub>i</sub> B<sub>i</sub> C<sub>i</sub> (1 ≤ A<sub>i</sub> ≤ B<sub>i</sub> ≤ N; −N ≤ C<sub>i</sub> ≤ N) representing the i<sup>th</sup> constraint.</p>

### 출력 

 <p>Output contains N integers (each separated by a single space) in a line representing the sequence that Andi wants if there exists such sequence, or “Impossible” (without quotes) otherwise.</p>

