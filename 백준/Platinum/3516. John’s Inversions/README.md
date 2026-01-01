# [Platinum V] John’s Inversions - 3516 

[문제 링크](https://www.acmicpc.net/problem/3516) 

### 성능 요약

메모리: 3684 KB, 시간: 48 ms

### 분류

자료 구조, 정렬, 세그먼트 트리, 값 / 좌표 압축

### 제출 일자

2026년 1월 2일 05:47:52

### 문제 설명

<p>John has recently come across the definition of an inversion.</p>

<p>An inversion in a sequence of numbers s<sub>k</sub> is any pair s<sub>i</sub>, s<sub>j</sub> such that i < j and s<sub>i</sub> > s<sub>j</sub>.</p>

<p>John believes that inversions are a perfect tool for estimation of how well a sequence of numbers is sorted.</p>

<p>The smaller the number of inversions in the sequence, the better it is sorted. For example, the sequences sorted in the ascending order have zero inversions in them. Peter gave John a stack of n cards. Each card has two numbers written on it — one in red and one in blue color. John is anxious to apply his knowledge of inversions to that stack.</p>

<p>He places the cards in front of him in arbitrary order and calculates the total number of nice inversions in front of him. John considers an inversion to be nice if it consists of the numbers of the same color. In our case nice inversion can be formed by either two blue or two red numbers. If the number of nice inversions is too big by John’s standards, he rearranges the cards and repeats the process.</p>

<p>Your task is to help John find out the minimal possible number of nice inversions he can get while following his algorithm.</p>

### 입력 

 <p>The first line of the input file contains one integer number n — the number of cards in the deck (1 ≤ n ≤ 100 000). The following n lines describe one card each. The i-th line contains two integer numbers r<sub>i</sub> and b<sub>i</sub> (1 ≤ r<sub>i</sub>, b<sub>i</sub> ≤ 10<sup>9</sup>) — the numbers written on i-th card in red and blue colors respectively.</p>

### 출력 

 <p>Output should contain exactly one integer number — the minimal possible number of nice inversions.</p>

