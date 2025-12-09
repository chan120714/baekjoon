# [Platinum IV] 금화 게임 - 5386 

[문제 링크](https://www.acmicpc.net/problem/5386) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

게임 이론, 스프라그–그런디 정리

### 제출 일자

2025년 12월 10일 03:10:02

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images2/doub.png" style="float:right; height:135px; width:141px">Being a pirate means spending a lot of time at sea. Sometimes, when there is not much wind, days can pass by without any activity. To pass the time between chores, pirates like to play games with coins. An old favorite of the pirates is a game for two players featuring one stack of coins. In turn, each player takes a number of coins from the stack. The number of coins that a player takes must be a power of a given integer K (1, K, K<sup>2</sup>, etcetera). The winner is the player to take the last coin(s).</p>

<p>Can you help the pirates figure out how the player to move can win in a given game situation?</p>

### 입력 

 <p>The first line of the input contains a single number: the number of test cases to follow. Each test case has the following format:</p>

<ul>
	<li>One line with two integers S and K, satisfying 1 ≤ S ≤ 10<sup>9</sup> and 1 ≤ K ≤ 100: the size of the stack and the parameter K, respectively.</li>
</ul>

### 출력 

 <p>For every test case in the input, the output should contain one integer on a single line: the smallest number of coins that the player to move can take in order to secure the win. If there is no winning move, the output should be 0.</p>

