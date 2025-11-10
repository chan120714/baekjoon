# [Platinum V] Little Difference - 15142 

[문제 링크](https://www.acmicpc.net/problem/15142) 

### 성능 요약

메모리: 239260 KB, 시간: 188 ms

### 분류

수학, 브루트포스 알고리즘, 정수론, 이분 탐색

### 제출 일자

2025년 11월 10일 12:46:54

### 문제 설명

<p>Little Lidia likes playing with numbers. Today she has a positive integer n, and she wants to decompose it to the product of positive integers.</p>

<p>Because Lidia is little, she likes to play with numbers with little difference. So, all numbers in decomposition should differ by at most one. And of course, the product of all numbers in the decomposition must be equal to n. She considers two decompositions the same if and only if they have the same number of integers and there is a permutation that transforms the first one to the second one.</p>

<p>Write a program that finds all decompositions, which little Lidia can play with today.</p>

### 입력 

 <p>The only line of the input contains a single integer n (1 ≤ n ≤ 10<sup>18</sup>).</p>

### 출력 

 <p>In first line output the number of decompositions of n, or −1 if this number is infinite. If number of decompositions is finite, print all of them one per line. In each line first print number k<sub>i</sub> of elements in decomposition. Then print k<sub>i</sub> integers in this decomposition in any order. Don’t forget that decompositions which are different only in order of elements are considered the same.</p>

