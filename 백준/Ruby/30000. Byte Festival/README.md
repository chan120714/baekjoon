# [Ruby V] Byte Festival - 30000 

[문제 링크](https://www.acmicpc.net/problem/30000) 

### 성능 요약

메모리: 111416 KB, 시간: 136 ms

### 분류

애드 혹, 사칙연산, 백트래킹, 브루트포스 알고리즘, 많은 조건 분기, 해 구성하기, 방향 비순환 그래프, 분할 정복, 다이나믹 프로그래밍, 오일러 피 함수, 분할 정복을 이용한 거듭제곱, 함수형 그래프, 그래프 이론, 그래프 탐색, 구현, 선형대수학, 수학, 모듈로 곱셈 역원, 정수론, 파싱, 런타임 전의 전처리, 누적 합, 재귀, 정렬, 문자열

### 제출 일자

2025년 11월 18일 09:44:12

### 문제 설명

<p>2010년에 개설된 Baekjoon Online Judge는 지난 14년간 많은 문제를 추가하였다. 2024년 2월 29일 <a href="/problem/30000">30000번 문제</a>가 추가되었고 이를 기념하여 와파스는 <a href="/problem/8481">바이트</a> <a href="/problem/20000">페스티벌</a>을 개최하게 된다.</p>

<p>여러분은 단순히 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>을 입력받으면 <code><span style="color:#e74c3c;">festivalN.out</span></code> 파일의 내용을 <strong>그대로</strong> 출력하면 된다. 단, 소스코드 길이는 <strong>30,000 바이트</strong>를 넘지 않아야 한다.</p>

<p>파일은 <a href="https://u.acmicpc.net/6d4975dc-cc3a-4121-b930-8c05e8c67784/festival.zip">이 링크</a>에서 볼 수 있으며 <code><span style="color:#e74c3c;">festival0.out</span></code>부터 <code><span style="color:#e74c3c;">festival9.out</span></code>까지의 10개의 파일이 담겨있다.</p>

### 입력 

 <p>정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>0</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>9</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(0 \le N \le 9)$</span> </mjx-container></p>

### 출력 

 <p><code><span style="color:#e74c3c;">festivalN.out</span></code> 파일의 내용을 출력한다</p>

