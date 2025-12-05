# [Diamond V] Perfect Squares - 32850 

[문제 링크](https://www.acmicpc.net/problem/32850) 

### 성능 요약

메모리: 45204 KB, 시간: 76 ms

### 분류

수학, 브루트포스 알고리즘, 정수론, 소수 판정, 소인수분해

### 제출 일자

2025년 12월 5일 11:12:02

### 문제 설명

<p>A famous theorem in number theory states that every positive integer can be written as the sum of four perfect squares. You have noticed, though, that usually fewer squares are enough. For example, $27$ only requires three perfect squares: $27 = 5^2 + 1^2 + 1^2$.</p>

<p>You share your observations with a mathematician friend, who rattles off the following perfect squares facts:</p>

<ul>
	<li>An odd prime $p$ can be written as the sum of <em>two</em> squares if and only if $p \equiv 1 \pmod 4$.</li>
	<li>If two positive integers $a$ and $b$ can be written as the sum of two squares, then so can their product $ab$.</li>
	<li>Every positive integer can be written as the sum of <em>three</em> perfect squares, unless it is of the form $4^a \cdot (8b + 7)$, where $a$ and $b$ are some non-negative integers.</li>
</ul>

<p>This last fact about sums of three squares intrigues you, and so you would like to write a program that verifies the claim is true by producing the actual squares.</p>

### 입력 

 <p>Input contains a single integer $n$ ($1 ≤ n ≤ 10^{12}$).</p>

### 출력 

 <p>If $n$ can be expressed as the sum of three squares, output three integers $x$, $y$, and $z$. Your answer will be judged correct if $0 ≤ x, y, z ≤ \sqrt{n}$ and $n = x^2 +y^2 +z^2$. If there are multiple valid choices for $x$, $y$, and $z$ you may output any of them. You must output exactly three integers, even if $n$ can be expressed as the sum of two or fewer squares.</p>

<p>If $n$ cannot be expressed as the sum of three squares, output $-1$ and no further output.</p>

