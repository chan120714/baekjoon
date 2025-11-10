# [Diamond V] 나이트 - 10562 

[문제 링크](https://www.acmicpc.net/problem/10562) 

### 성능 요약

메모리: 110904 KB, 시간: 124 ms

### 분류

수학, 다이나믹 프로그래밍, 비트마스킹, 비트필드를 이용한 다이나믹 프로그래밍, 분할 정복을 이용한 거듭제곱, 벌리캠프–매시

### 제출 일자

2025년 11월 10일 16:07:19

### 문제 설명

<p style="text-align:center"><img alt="" src="https://www.acmicpc.net/upload/images2/knights.png" style="height:119px; width:229px"></p>

<p>강호는 M행 N열 크기의 체스판 위에 나이트를 놓으려고 한다. 각각의 칸에는 최대 1개의 나이트가 놓여질 수 있다.</p>

<p>이때, 체스판 위에 있는 나이트가 서로 공격을 할 수 있으면 안 된다. 나이트가 놓여져 있을 때, 공격할 수 있는 칸의 위치는 아래 그림에 X로 표시되어 있다.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10562/1.png" style="height:150px; width:145px"></p>

<p>체스판의 크기가 주어졌을 때, 나이트를 놓을 수 있는 방법의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T (T ≤ 10)가 주어진다. 각각의 테스트 케이스는 두 정수 M과 N으로 이루어져 있다. (1 ≤ M ≤ 4, 1 ≤ N ≤ 10<sup>9</sup>)</p>

### 출력 

 <p>각각의 테스트 케이스마다, 나이트를 놓을 수 있는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.</p>

