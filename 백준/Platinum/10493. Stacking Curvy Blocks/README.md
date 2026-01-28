# [Platinum V] Stacking Curvy Blocks - 10493 

[문제 링크](https://www.acmicpc.net/problem/10493) 

### 성능 요약

메모리: 110712 KB, 시간: 132 ms

### 분류

미적분학, 수학

### 제출 일자

2026년 1월 28일 14:53:03

### 문제 설명

<p>You’re doing some construction work, and, to save money, you’re using some discount, “irregular” construction materials. In particular, you have some blocks that are mostly rectangular, but with one edge that’s curvy. As illustrated below, you’re going to use these irregular blocks between stacks of ordinary blocks, so they won’t shift sideways or rotate. You’ll put one irregular block on the bottom, with its curvy edge pointing up, and another above it, with it’s curvy edge pointing down. You just need to know how well these blocks fit together. You define the fit quality as the maximum vertical gap between the upper edge of the bottom block and the lower edge of the top block when the upper block is just touching the lower one.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/stacking.png" style="height:236px; width:529px"></p>

<p style="text-align: center;">Figure 1: Block stacking and coordinate system</p>

<p>All blocks are one unit wide. You’ve modeled the curvy edges as cubic polynomials, with the left edge of the block at x = 0 and the right edge at x = 1.</p>

### 입력 

 <p>Each test case is given on two lines, with each line containing four real numbers. The numbers on the first line, b<sub>0</sub> b<sub>1</sub> b<sub>2</sub> b<sub>3</sub>, describe the shape of the upper edge of the bottom block. This edge is shaped just like the polynomial b<sub>0</sub> + b<sub>1</sub>x + b<sub>2</sub>x<sup>2</sup> + b<sub>3</sub>x<sup>3</sup> for 0 ≤ x ≤ 1. The numbers on the next input line, t<sub>0</sub> t<sub>1</sub> t<sub>2</sub> t<sub>3</sub>, describe the bottom edge of the block that’s going on top. This edge is shaped just like the polynomial t<sub>0</sub> + t<sub>1</sub>x + t<sub>2</sub>x<sup>2</sup> + t<sub>3</sub>x<sup>3</sup> for 0 ≤ x ≤ 1. No input value will have magnitude greater than 50000. There are at most 500 test cases. Input ends at end of file.</p>

### 출력 

 <p>For each test case, print out a single line giving the fit quality. An answer is considered correct if its absolute or relative error is at most 10<sup>−7</sup>.</p>

