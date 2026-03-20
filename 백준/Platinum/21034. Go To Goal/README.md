# [Platinum IV] Go To Goal - 21034 

[문제 링크](https://www.acmicpc.net/problem/21034) 

### 성능 요약

메모리: 36264 KB, 시간: 156 ms

### 분류

수학, 정수론, 조합론, 분할 정복을 이용한 거듭제곱, 모듈로 곱셈 역원, 페르마의 소정리

### 제출 일자

2026년 3월 21일 05:51:27

### 문제 설명

<p>Ani is playing a game containing a piece and 2N + M + 1 squares, numbered from 0 to 2N + M. The piece is initially located at square 0. Ani also has N super cards and M normal cards.</p>

<p>In one turn, Ani can use one of her unused card. If Ani chooses to use a normal card, her piece will move one square ahead (i.e. from square x to square x + 1). Otherwise, if Ani chooses to use a super card, her piece will move two squares ahead (i.e. from square x to square x + 2). Ani cannot use a super card too often–she cannot use three super cards in three consecutive turns.</p>

<p>After N + M turns, the piece should be located at square 2N + M, which is the goal. Ani is wondering the number of possible paths that her piece can use to the goal. Two paths are considered different if the piece is located at different squares after the same number of turns.</p>

<p>For example, if N = 3, and M = 1, then there are two different paths that Ani’s piece can use to the goal:</p>

<ol>
	<li>Use the normal card in the second turn, and use the super cards in the first, third, and fourth turn.</li>
	<li>Use the normal card in the third turn, and use the super cards in the first, second, and fourth turn.</li>
</ol>

<p>Note that Ani cannot use the normal card in the first turn, since then she will need to use the super cards in the last three turns consecutively.</p>

### 입력 

 <p>Input begins with a line containing two integers: N M (1 ≤ N, M ≤ 100 000) representing the number of super cards and normal cards, respectively.</p>

### 출력 

 <p>Output in a line an integer representing the number of possible paths that her piece can use to the goal. As this output can be large, you need to modulo the output by 1 000 000 007.</p>

