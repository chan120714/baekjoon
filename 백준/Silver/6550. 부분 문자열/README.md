# [Silver V] 부분 문자열 - 6550 

[문제 링크](https://www.acmicpc.net/problem/6550) 

### 성능 요약

메모리: 32412 KB, 시간: 56 ms

### 분류

그리디 알고리즘, 문자열

### 제출 일자

2025년 12월 1일 17:00:18

### 문제 설명

<p>

You have devised a new encryption technique which encodes a message
by inserting between its characters randomly generated strings in a
clever way. Because of pending patent issues we will not discuss in
detail how the strings are generated and inserted into the original
message. To validate your method, however, it is necessary to write
a program that checks if the message is really encoded in the final
string.

</p><p>

Given two strings <i>s</i> and <i>t</i>, you have to decide whether
<i>s</i> is a subsequence of <i>t</i>, i.e. if you can remove
characters from <i>t</i> such that the concatenation of the remaining
characters is <i>s</i>.

</p>

### 입력 

 <p>

The input contains several testcases. Each is specified
by two strings <i>s, t</i> of alphanumeric ASCII characters
separated by whitespace. Input is terminated by EOF.

</p>

### 출력 

 <p>

For each test case output, if <i>s</i> is a subsequence
of <i>t</i>.

</p>

