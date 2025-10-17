# [Diamond I] 비로소 서로소 - 32240 

[문제 링크](https://www.acmicpc.net/problem/32240) 

### 성능 요약

메모리: 278044 KB, 시간: 4848 ms

### 분류

수학, 정수론, 누적 합, 소수 판정, 에라토스테네스의 체, 오일러 피 함수, 뫼비우스 반전 공식

### 제출 일자

2025년 4월 18일 12:11:54

### 문제 설명

<p>양의 정수 $N$이 주어진다.</p>

<p>각 성분이 $N$ 이하인 서로소인 모든 양의 정수쌍 $\left( i,j \right)$에 대해 각 성분의 합의 총합을 계산해 보자! 즉, 아래의 수식 값을 구하면 된다.</p>

<p>\[\sum_{i=1}^{N}\sum_{j=1}^N{\left( i+j \right) I\left\{ \gcd\left( i,j \right) =1 \right\}}\]</p>

<p>$I\left\{ condition \right\}$는 <a href="https://en.wikipedia.org/wiki/Indicator_function"><code>Indicator Function</code></a>으로, $condition$이 참일 때 $1$, 거짓일 때 $0$을 반환한다.</p>

### 입력 

 <p>첫 번째 줄에 정수 $N(1\le N\le 10^{11})$이 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 각 성분의 합의 총합, 즉 주어진 수식의 결과를 출력한다. 단, 답이 너무 커질 수 있으므로 답을 $10^9+7$로 나눈 나머지를 출력한다.</p>

