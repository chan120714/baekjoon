# [Platinum III] Future Generation - 16582 

[문제 링크](https://www.acmicpc.net/problem/16582) 

### 성능 요약

메모리: 164236 KB, 시간: 508 ms

### 분류

비트마스킹, 다이나믹 프로그래밍, 비트필드를 이용한 다이나믹 프로그래밍, 정렬

### 제출 일자

2026년 1월 18일 22:45:20

### 문제 설명

<p>Andi is getting married! He and his partner plan to have N children. To avoid any hassle in the future, Andi wants to decide all their children’s name in advance. Specifically, he wants each child to have a name which is lexicographically larger than any of his/her older siblings. Of course, his partner also agrees with this idea. String A is lexicographically larger than string B if and only if B is a prefix of A or there exists an index i where A<sub>i</sub> > B<sub>i</sub> and A<sub>j</sub> = B<sub>j</sub> for all j < i. Note that a proper name can be as short as one character, but it cannot be an empty string.</p>

<p>Life is good for Andi, until one day he told his soon-to-be-grandmother-in-law (i.e. his partner’s grandma) about this marriage plan. After learning that Andi plans to have N children with her granddaughter, she gave him N names to be used. Moreover, the i<sup>th</sup> name can only be used for the i<sup>th</sup> child.</p>

<p>After going through a long debate with her grandma, Andi came into an agreement: The i<sup>th</sup> child’s name should be a subsequence of the i<sup>th</sup> name her grandma gave. A string A is a subsequence of string B if A can be obtained by deleting zero or more characters from B without changing the remaining characters’ order, e.g., ABC is a subsequence of DAEBCCB, but EFG is not a subsequence of FABEGC.</p>

<p>Even though Andi dislikes the given list of names, he still wants to impress his partner by showing that he can satisfy both her grandma’s wish and his own desire (i.e. each child’s name is lexicographically larger than any of his/her older siblings). However, Andi wonders, what is the maximum possible total length of their children names?</p>

<p>For example, let N = 3, and the names given by his partner’s grandma are (KARIM, PARBUDI, CHANDRA). Here are several example set of names which satisfies Andi’s desire:</p>

<ul>
	<li>[AR, BI, CRA] with a total length of 2 + 2 + 3 = 7.</li>
	<li>[ARI, BUDI, CHANDRA] with a total length of 3 + 4 + 7 = 14.</li>
	<li>[ARIM, ARUDI, CHANDRA] with a total length of 4 + 5 + 7 = 16.</li>
	<li>[AIM, ARBUDI, CHANDRA] with a total length of 3 + 6 + 7 = 16.</li>
	<li>· · ·</li>
</ul>

<p>Among all sets of names which satisfy Andi’s desire in this example, the maximum total length is 16. Note that there might be cases where valid set of names cannot be obtained. In such case, you should output -1.</p>

<p>For example, let N = 2 and the names given by his partner’s grandma are (ZORO, ANDI). In this example, all subsequences of the 2<sup>nd</sup> name are lexicographically smaller than all subsequences of the 1<sup>st</sup> name, thus, no possible valid set of names can be obtained.</p>

### 입력 

 <p>Input begins with a line containing an integer N (1 ≤ N ≤ 15) representing the number of children. The next N lines, each contains a string S<sub>i</sub> (1 ≤ |S<sub>i</sub>| ≤ 15) representing the i<sup>th</sup> name given by Andi’s soon-tobe-grandmother-in-law. S<sub>i</sub> contains only uppercase alphabets (S<sub>ij</sub> ∈ {A − Z}).</p>

### 출력 

 <p>Output contains an integer in a line representing the maximum possible total length of their children names, or -1 if no possible valid set of names can be obtained.</p>

