# [Platinum V] Fear Factoring - 15106 

[문제 링크](https://www.acmicpc.net/problem/15106) 

### 성능 요약

메모리: 32412 KB, 시간: 1916 ms

### 분류

수학, 정수론, 조화수

### 제출 일자

2026년 2월 25일 05:19:59

### 문제 설명

<p>The Slivians are afraid of factoring; it’s just, well, difficult.</p>

<p>Really, they don’t even care about the factors themselves, just how much they sum to.</p>

<p>We can define F(n) as the sum of all of the factors of n; so F(6) = 12 and F(12) = 28. Your task is, given two integers a and b with a ≤ b, to calculate</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-munder space="4"><mjx-row><mjx-base style="padding-left: 0.379em;"><mjx-mo class="mjx-lop"><mjx-c class="mjx-c2211 TEX-S2"></mjx-c></mjx-mo></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-under></mjx-row></mjx-munder><mjx-texatom space="2" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>S</mi><mo>=</mo><munder><mo data-mjx-texclass="OP">∑</mo><mrow data-mjx-texclass="ORD"><mi>a</mi><mo>≤</mo><mi>n</mi><mo>≤</mo><mi>b</mi></mrow></munder><mrow data-mjx-texclass="ORD"><mi>F</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[S=\sum_{a \le n \le b}{F(n)}\]</span> </mjx-container></p>

### 입력 

 <p>The input consists of a single line containing space-separated integers a and b (1 ≤ a ≤ b ≤ 10<sup>12</sup>; b − a ≤ 10<sup>6</sup>).</p>

### 출력 

 <p>Print S on a single line.</p>

