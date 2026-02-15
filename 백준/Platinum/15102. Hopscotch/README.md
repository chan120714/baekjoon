# [Platinum IV] Hopscotch - 15102 

[문제 링크](https://www.acmicpc.net/problem/15102) 

### 성능 요약

메모리: 72404 KB, 시간: 2308 ms

### 분류

조합론, 분할 정복을 이용한 거듭제곱, 페르마의 소정리, 수학, 모듈로 곱셈 역원, 정수론

### 제출 일자

2026년 2월 16일 05:47:47

### 문제 설명

<p>You’re playing hopscotch! You start at the origin and your goal is to hop to the lattice point (N, N). A hop consists of going from lattice point (x<sub>1</sub>, y<sub>1</sub>) to (x<sub>2</sub>, y<sub>2</sub>), where x<sub>1</sub> < x<sub>2</sub> and y<sub>1</sub> < y<sub>2</sub>.</p>

<p>You dislike making small hops though. You’ve decided that for every hop you make between two lattice points, the x-coordinate must increase by at least X and the y-coordinate must increase by at least Y.</p>

<p>Compute the number of distinct paths you can take between (0, 0) and (N, N) that respect the above constraints. Two paths are distinct if there is some lattice point that you visit in one path which you don’t visit in the other.</p>

<p>Hint: The output involves arithmetic mod 10<sup>9</sup> + 7. Note that with p a prime like 10<sup>9</sup> + 7, and x an integer not equal to 0 mod p, then x(x<sup>p−2</sup>) mod p equals 1 mod p.</p>

### 입력 

 <p>The input consists of a line of three integers, N X Y. You may assume 1 ≤ X, Y ≤ N ≤ 10<sup>6</sup>.</p>

### 출력 

 <p>The number of distinct paths you can take between the two lattice points can be very large. Hence output this number modulo 1 000 000 007 (10<sup>9</sup> + 7).</p>

