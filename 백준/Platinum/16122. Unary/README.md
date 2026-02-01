# [Platinum IV] Unary - 16122 

[문제 링크](https://www.acmicpc.net/problem/16122) 

### 성능 요약

메모리: 65552 KB, 시간: 812 ms

### 분류

조합론, 페르마의 소정리, 수학, 모듈로 곱셈 역원, 정수론

### 제출 일자

2026년 2월 2일 05:33:30

### 문제 설명

<p>많은 프로그래밍 언어에서는 정수에 대해 다음과 같은 두 개의 단항 연산을 지원한다.</p>

<ul>
	<li><code>-x</code>: <code>x</code>의 부호를 바꾼다. <code>x</code>의 값이 0인 경우는 값이 변하지 않는다.</li>
	<li><code>~x</code>: <code>x</code>의 모든 비트를 뒤집는다. 예를 들어 <code>x</code>의 2진수 표현이 <code>0000 1010</code>일 경우 <code>~x</code>는 <code>1111 0101</code>이 된다.</li>
</ul>

<p>편의상 이 문제에서 다루는 프로그래밍 언어에서는 정수를 무한히 많은 비트로 표현하며, 음수를 나타낼 때 2의 보수 표현법(음수를 표현할 때 무한히 큰 2의 거듭제곱에서 그 수를 뺀 값으로 나타내는 표현법)을 쓴다고 가정한다. 이때 <code>~x</code>의 연산 결과는 <code>-x-1</code>과 같다.</p>

<table cellpadding="0" cellspacing="0" class="table table-bordered" style="width: 250px; margin: 0 auto;">
	<thead>
		<tr>
			<td style="text-align: center;">연산</td>
			<td style="text-align: center;">10진법</td>
			<td style="text-align: center;">2진법</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;"><code>x</code></td>
			<td style="text-align: center;"><code style="margin-left: 1.07ex;">10</code></td>
			<td style="text-align: center;"><code>0000 1010</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>-x</code></td>
			<td style="text-align: center"><code>-10</code></td>
			<td style="text-align: center;"><code>1111 0110</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>~x</code></td>
			<td style="text-align: center;"><code>-11</code></td>
			<td style="text-align: center;"><code>1111 0101</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><code>x</code>의 값이 10인 경우의 예시</p>

<p>정수 0에 위의 두 연산을 총 <em>N</em>번 적용해서 정수 <em>M</em>을 만들고자 할 때, 가능한 연산 순서의 가짓수를 구하여라.</p>

### 입력 

 <p>첫 줄에 연산 횟수를 의미하는 정수 <em>N</em>과 만들고자 하는 정수 <em>M</em>(0 ≤ <em>N</em> ≤ 300,000, -300,000 ≤ <em>M</em> ≤ 300,000)이 주어진다.</p>

### 출력 

 <p>첫 줄에 정수 0에 <em>N</em>번의 연산을 적용하여 <em>M</em>을 만드는 방법의 가짓수를 998,244,353으로 나눈 나머지를 출력한다.</p>

