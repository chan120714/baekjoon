# [Gold III] K진 트리 - 11812 

[문제 링크](https://www.acmicpc.net/problem/11812) 

### 성능 요약

메모리: 2020 KB, 시간: 52 ms

### 분류

수학, 트리, 최소 공통 조상

### 제출 일자

2024년 5월 6일 23:36:25

### 문제 설명

<p>You are given a tree of order K with N nodes or, in other words, each node can have at most K children. The tree is constructed so it’s of the "lowest energy": the nodes are placed in a new depth of the tree only when all the places (from left to right) in the previous depth have been filled. This is also the order of enumerating the nodes, starting with 1. Image depicts an example of a tree of order 3 with 9 nodes.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11812/1.png" style="height:124px; width:188px"></p>

<p>You need to output answers to Q queries in the form of x y, where the answer is the minimal number of steps needed to get from node x to node y.</p>

### 입력 

 <p>The first line of input contains the integers N (1 ≤ N ≤ 10<sup>15</sup>), K (1 ≤ K ≤ 1 000) i Q (1 ≤ Q ≤ 100 000) from the task. Each of the following Q lines contains pairs xy (1 ≤ x, y ≤ N, x ≠ y) from the task.</p>

### 출력 

 <p>Output Q lines, each line containing the answer to a query from the task.</p>

