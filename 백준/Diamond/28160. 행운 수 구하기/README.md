# [Diamond V] 행운 수 구하기 - 28160 

[문제 링크](https://www.acmicpc.net/problem/28160) 

### 성능 요약

메모리: 18884 KB, 시간: 1088 ms

### 분류

수학, 자료 구조, 세그먼트 트리, 이분 탐색

### 제출 일자

2025년 7월 28일 19:49:51

### 문제 설명

<p><a href="https://en.wikipedia.org/wiki/Lucky_number">행운 수(Lucky numbers)</a>는 에라토스테네스의 체와 비슷한 방법으로 만들어지는 자연수의 부분집합 또는 그 부분집합의 원소를 말한다.</p>

<p>행운 수의 집합은 다음과 같은 과정을 통해 구성할 수 있다.</p>

<ol>
	<li>홀수 자연수의 목록을 만든다.</li>
	<li>목록에 속한 수 중 1보다 크면서 선택한 적이 없는 수 중에서 가장 작은 수를 선택한다.</li>
	<li>2.에서 선택한 자연수를 <em>k</em>라고 할 때, 목록에서 오름차순으로 <em>i</em>×<em>k</em> (<em>i</em> ≥ 1) 번째에 해당하는 모든 자연수를 지운다.</li>
	<li>2.로 돌아간다.</li>
</ol>

<p>다음은 위 과정의 일부를 수행하는 예시이다.</p>

<ol>
	<li value="1">1 3 5 7 9 11 13 15 17 19 21 23 25 …</li>
	<li value="2">1 <u><strong>3</strong></u> 5 7 9 11 13 15 17 19 21 23 25 …</li>
	<li value="3">1 3 <s>5</s> 7 9 <s>11</s> 13 15 <s>17</s> 19 21 <s>23</s> 25 …</li>
	<li value="4">1 3 7 9 13 15 19 21 25 …</li>
	<li value="2">1 3 <u><strong>7</strong></u> 9 13 15 19 21 25 …</li>
	<li value="3">1 3 7 9 13 15 <s>19</s> 21 25 …</li>
	<li value="4">1 3 7 9 13 15 21 25 …</li>
	<li value="2">1 3 7 <u><strong>9</strong></u> 13 15 21 25 …</li>
	<li style="list-style-type:none;">…</li>
</ol>

<p>두 개의 자연수 <em>L</em>과 <em>R</em>이 주어지면 <em>L</em>번째부터 <em>R</em>번째까지의 행운 수를 알아보자.</p>

### 입력 

 <p>첫째 줄에 두 개의 자연수 <em>L</em>과 <em>R</em>이 주어진다. (1 ≤ <em>L</em> ≤ <em>R</em> ≤ 3,000,000 = 3 × 10<sup>6</sup>, <em>R</em> - <em>L</em> ≤ 100,000 = 10<sup>5</sup>)</p>

### 출력 

 <p><em>R</em> - <em>L</em> + 1개의 줄에 걸쳐 <em>i</em>번째 줄에 <em>L</em> + <em>i</em> - 1번째 행운 수를 출력한다.</p>

