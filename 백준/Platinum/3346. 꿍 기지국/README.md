# [Platinum II] 꿍 기지국 - 3346 

[문제 링크](https://www.acmicpc.net/problem/3346) 

### 성능 요약

메모리: 215040 KB, 시간: 708 ms

### 분류

기하학, 이분 탐색, 스위핑, 매개 변수 탐색

### 제출 일자

2026년 1월 14일 18:22:47

### 문제 설명

<p>The well-known mobile network operator Totalphone has set up a number of new base transceiver stations in order to cover a newly-built highway with its network. As always the programmers of Totalphone have been sloppy; as a result, the transmission power cannot be set up individually for the stations, but one can only set the transmission power to a fixed common value for all the stations. In order to minimize power consumption, the company wants to know the maximal distance of a point on the highway to the nearest base transceiver station.</p>

### 입력 

 <p>The first line of input consists of two integers N(1 ≤ N ≤ 10<sup>6</sup>) and L(1 ≤ L ≤ 10<sup>9</sup>) representing the number of base transceiver stations and the length of the highway, respectively. N lines follow, each containing a pair of integers x<sub>i</sub>, y<sub>i</sub> (-10<sup>9</sup> ≤ x<sub>i</sub>, y<sub>i</sub> ≤10<sup>9</sup>) which describes the coordinates of a base transceiver station. All points are distinct. Coordinates are sorted in the non-decreasing order with respect to x<sub>i</sub> coordinates. If two values of x<sub>i</sub> are the same, then coordinates are sorted with respect to y<sub>i</sub> coordinates in increasing order.</p>

<p>The highway is a straight line ranging from (0; 0) to (L; 0).</p>

### 출력 

 <p>The first and only line of standard output should contain a single number - the maximal distance of a point on the highway to the nearest base transceiver station. Your output will be regarded as correct if it differs by at most 10<sup>-3</sup> from the precise result.</p>

