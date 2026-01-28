# [Platinum V] 3-sided dice - 3854 

[문제 링크](https://www.acmicpc.net/problem/3854) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

기하학, 많은 조건 분기

### 제출 일자

2026년 1월 28일 15:48:21

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images2/3dice.png" style="float:right; height:173px; width:182px">Just like every fall, the organizers of the Southwestern Europe Dice Simulation Contest are busy again this year. In this edition you have to simulate a 3-sided die that outputs each of three possible outcomes (which will be denoted by 1, 2 and 3) with a given probability, using three dice in a given set. The simulation is performed this way: you choose one of the given dice at random, roll it, and report its outcome. You are free to choose the probabilities of rolling each of the given dice, as long as each probability is strictly greater than zero. Before distributing the materials to the contestants, the organizers have to verify that it is actually possible to solve this task.</p>

<p>For example, in the first test case of the sample input you have to simulate a die that yields outcome 1, 2 and 3 with probabilities 3/10, 4/10 and 3/10 . We give you three dice, and in this case the i-th of them always yields outcome i, for each i = 1, 2, 3. Then it is possible to simulate the given die in the following fashion: roll the first die with probability 3/10 , the second one with probability 4/10 and the last one with probability 3/10.</p>

### 입력 

 <p>The input consists of several test cases, separated by single blank lines. Each test case consists of four lines: the first three of them describe the three dice you are given and the last one describes the die you have to simulate. Each of the four lines contains 3 space-separated integers between 0 and 10 000 inclusive. These numbers will add up to 10 000, and represent 10 000 times the probability that rolling the die described in that line yields outcome 1, 2 and 3, respectively.</p>

<p>The test cases will finish with a line containing only the number zero repeated three times (also preceded with a blank line).</p>

### 출력 

 <p>For each case, your program should output a line with the word YES if it is feasible to produce the desired die from the given ones, and NO otherwise.</p>

