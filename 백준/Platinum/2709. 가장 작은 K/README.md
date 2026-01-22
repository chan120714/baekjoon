# [Platinum III] 가장 작은 K - 2709 

[문제 링크](https://www.acmicpc.net/problem/2709) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 정수론, 임의 정밀도 / 큰 수 연산, 런타임 전의 전처리

### 제출 일자

2026년 1월 23일 02:30:43

### 문제 설명

<p>Since most computers are binary machines, both powers of two and problems that involve only two values are important to computer scientists. The following problem has to do with powers of two and the digits 1 and 2.</p>

<p>Some powers of two as decimal values, such as 2<sup>9</sup> = 512 and 2<sup>89</sup> = 618,970,019,642,690,137,449,562,112 end in a string of digits consisting only of 1's and 2's (12 for 2<sup>9</sup> and 2112 for 2<sup>89</sup>). In fact, it can be proved that:</p>

<blockquote>
<p>For every integer R, there exists a power of 2 such that 2<sup>K</sup> uses only the digits 1 and 2 in its last R digits.</p>
</blockquote>

<p>This is shown a bit more clearly in the following table:</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/tworag.png" style="height:191px; width:297px"></p>

<p>Your job is to write a program that will determine, for given R, the smallest K such that 2<sup>K</sup> ends in a string of R digits containing only 1's and 2's.</p>

### 입력 

 <p>The first line of the input contains a single decimal integer, N, 1 £ N £ 50, the number of problem data sets to follow. Each data set consists of a single integer R, 1 £ R £ 20, for which we want a power of 2 ending in a string of R 1's and 2's.</p>

### 출력 

 <p>For each data set, you should generate one line of output with the following values: The data set number as a decimal integer (start counting at one), a space, the input value R, another space, and the smallest value K for which 2<sup>K</sup> ends in a string of R 1's and 2's.</p>

