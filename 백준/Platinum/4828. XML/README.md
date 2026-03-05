# [Platinum V] XML - 4828 

[문제 링크](https://www.acmicpc.net/problem/4828) 

### 성능 요약

메모리: 32412 KB, 시간: 216 ms

### 분류

구현, 자료 구조, 문자열, 파싱, 스택, 정규 표현식

### 제출 일자

2026년 3월 4일 15:40:11

### 문제 설명

<p>In this problem, you are asked to determine if a given document satisfies the syntax of an XML-like language.</p>

<p>A simple XML-like document can be parsed as a sequence of the following:</p>

<ol>
	<li>Plain text---ASCII codes between 32 and 127 (inclusive), with none of the following symbols: <, >, &</li>
	<li>The sequences:
	<ul>
		<li>&lt;</li>
		<li>&gt;</li>
		<li>&amp;</li>
	</ul>
	</li>
	<li>These encode a <, >, or & respectively.</li>
	<li>&xHEX; HEX must be any even (positive) number of upper or lower case hexadecimal digits, and this represents the bytes given.</li>
	<li><tag> Tag can be any lowercase alphanumeric string. This tag is pushed onto the context stack.</li>
	<li><tag/> This tag is not pushed onto the context stack (there is no closing context).</li>
	<li></tag> This tag removes the <tag> context from the stack, which must be topmost on the stack.</li>
</ol>

<p>By the time the entire document is parsed, the context stack is empty for a valid document. We should also note that the empty string is considered valid.</p>

### 입력 

 <p>You will be given a number of documents to process. Each document is given as one line of text, which may be empty, consisting of ASCII codes between 32 and 127 (inclusive). The input is terminated by the end of file.</p>

### 출력 

 <p>For each document given, print valid on a single line if it is a valid XML-like document, or invalid otherwise.</p>

