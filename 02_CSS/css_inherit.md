[CSS] CSS 상속, 상속되는 CSS속성

1. 스타일 상속
Css 내용을 적용했을 때, 적용된 내용이 기타 하위 요소까지 영향을 주는 것을 말한다.

body {
  margin:50px;
}

.people {		/* people에 Css를 적용하였는데 */
  color:lightpink;
  font-weight:bold;
}

<body>
    <div class="worker">직원
      <div class="people">사람		<!-- people 요소 외 하위요소까지 모두 선택이 되었다. -->
        <div class="Jim">Jim</div>		<!-- 주목! -->
        <div class="Tommy">Tommy</div>  	<!-- 주목! -->
        <div class="Eve">Eve</div>      	<!-- 주목! -->
      </div>
      <div class="robot">로봇</div>
    </div>
</body>

이렇게 부모 요소를 통해 상속되는 Css 속성은 모두 글자/문자와 관련된 속성 이라는 것!
** 주의 : 그렇다고 모든 글자/문자 속성이 상속되는 것은 아니다.

e.g.
font-size | 글자 크기
font-family | 폰트(서체)
font-weight | 글자 두께
font-style | 글자 기울기
Inline-height | 글자 높이
color | 글자 색상
text-align | 정렬
...

2. 강제 상속
실제로 상속이 되지 않는 속성을 강제로 상속시키는 것.

<body>
    <div class="parent">
      <div class="child">
    </div>
</body>

.parent {
  width:500px;
  height:300px;
  background-color:lightblue;
}

.child {
  width:300px;
  height:inherit;		/* 부모 요소에 상속하라는 뜻이다. */
  background-color:blue;
}

