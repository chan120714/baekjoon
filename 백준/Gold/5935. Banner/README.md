# [Gold III] Banner - 5935 

[문제 링크](https://www.acmicpc.net/problem/5935) 

### 성능 요약

메모리: 110720 KB, 시간: 152 ms

### 분류

수학, 정수론, 유클리드 호제법

### 제출 일자

2026년 1월 28일 16:17:35

### 문제 설명

<p>Bessie is returning from a long trip abroad, and Farmer John wants to erect a nice "Welcome Home" banner in her pasture for her arrival. The banner will hang between two poles on a wire whose length is in the range L1..L2 (1 <= L1 <= L2; L1 <= L2 <= 1,500).</p>

<p>The pasture's size is W x H (1 <= W <= 1,000; 1 <= H <= 1,000), and Farmer John has installed a post at every point with integer coordinates. Of these (W + 1) * (H + 1) points, Farmer John must pick just two that will hold either end of the wire from which he will hang the banner.</p>

<p>FJ wants no interference with his banner as it hangs and requires that no post be directly under the tight wire he stretches between the two chosen posts.</p>

<p>Farmer John needs your help to figure out how many possible ways he can hang the banner. He knows the number is large and that a 32-bit integer might not be sufficient to compute the answer.</p>

<p>Consider the example pasture below, with W = 2 and H = 1:</p>

<pre>       * * *
       * * *</pre>

<p>The banner size is in the range 2..3. This pasture contains (2+1) * (1+1) = 6 points and has (6 take 2) = (6*5)/(2*1) = 15 different potential pairs of points between which the banner-holding wire might stretch:</p>

<pre>   (0,0)-(0,1)   (0,0)-(2,1)   (0,1)-(2,1)   (1,1)-(2,0)
   (0,0)-(1,0)   (0,1)-(1,0)   (1,0)-(1,1)   (1,1)-(2,1)
   (0,0)-(1,1)   (0,1)-(1,1)   (1,0)-(2,0)   (2,0)-(2,1)
   (0,0)-(2,0)   (0,1)-(2,0)   (1,0)-(2,1)</pre>

<p>Of these pairs, only four have a length in the range 2..3:</p>

<pre>                     Len                       Len
        (0,0)-(2,0) 2.00          (0,1)-(2,0) 2.24 
        (0,0)-(2,1) 2.24          (0,1)-(2,1) 2.00 </pre>

<p>Of these four, the pairs (0,0)-(2,0) and (0,1)-(2,1) both have a post directly on the line between the endpoints, and thus are unsuitable.</p>

<p>So, just two pairs of points out of 15 are acceptable candidates for hanging the banner wire.</p>

### 입력 

 <ul>
	<li>Line 1: Four space-separated integers: W, H, L1, and L2</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer denoting the number of possible banners</li>
</ul>

<p> </p>

