# [Platinum IV] 현주와 윤주의 재미있는 단어 게임 - 3172 

[문제 링크](https://www.acmicpc.net/problem/3172) 

### 성능 요약

메모리: 57920 KB, 시간: 472 ms

### 분류

자료 구조, 문자열, 정렬, 세그먼트 트리

### 제출 일자

2025년 12월 23일 04:19:09

### 문제 설명

<p>Little Lovro likes to play games with words. During the last few weeks he realized that some words don't like each other. </p>

<p>The words A and B don't like each other if the word A is lexicographically before the word B, but the word B' is lexicographically before the word A', where X' stands for the word X reversed (if X="kamen" then X'="nemak"). For example, the words "lova" and "novac" like each other, but the words "aron" and "sunce" don't like each other. </p>

<p>Given some set of the words, we define the degree of chaos of the set as the number of pairs of different words that don't like each other. </p>

<p>Write a program that, given a set of words, finds the chaos degree for the set. </p>

### 입력 

 <p>The first line of input contains an integer N, 2 ≤ N ≤ 100 000. </p>

<p>Each of the following N lines contains one word – a sequence of at most 10 lowercase letters of the English alphabet ('a'-'z'). There will be no two identical words in the set. </p>

### 출력 

 <p>The first and only line of output should contain a single integer – the chaos degree of the given set of words. </p>

<p>Note: use 64-bit signed integer type (int64 in Pascal, long long in C/C++). </p>

