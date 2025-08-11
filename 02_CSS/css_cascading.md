[CSS] CSS 선택자 우선순위 (중요!)

선택자 우선순위 란?
하나의 요소가 여러 선언 대상이 된 경우
어떤 선언을 우선적으로 적용할지 결정하는 방법이다. 

조건1
Css 내용을 Html에 적용할 때 붙는 점수가 높은 선언이 화면에 출력된다.

조건2
점수가 같을 경우, 맨 마지막으로 작성한 코드 내용이 우선 적용된다.

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style="color:green;">
</head>
	<div id="color_orange"
     	 class="color_yellow"
     	 style="color:green;">		<!-- 2순위 (인라인 선언 - 1000점 -->
      	 Hello World!!
    </div>
</html>

div {color:red !important;}		/* 1순위 (!important - 9999999점) */
#color_orange {color:orange;}		/* 3순위 (ID 선택자 - 100점) */
.color_yellow {color:yellow;}		/* 4순위 (Class 선택자 - 10점) */
div {color:blue;}			/* 5순위 (태그 - 1점)*/
* {color:darkblue;}			/* 6순위 (전체 선택자) - 0점) */
body {color:purple;}			/* 상속되지 않음 */

!importnat > Inline Style > id > class > tag
왼쪽부터 오른쪽 방향으로
명시도 우선순위가 높은 순에서 낮은 순으로 간다.
CSS에서 Cascading은 중요한 개념이기 때문에
선택자를 적절하게 사용해서 우선순위를 부여해주는것이 바람직하다고 한다.

[출처_daeyun대윤]
https://iamdaeyun.tistory.com/entry/Lesson-7-CSS-%EC%82%AC%EC%9A%A9%EC%8B%9C-%EB%B0%98%EB%93%9C%EC%8B%9C-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0%EA%B2%83-%EB%AA%85%EC%8B%9C%EB%8F%84﻿

** 기본 선택자 점수별 순서 (우선 순위 선택자) 기억 해두자.
아래 이미지의 style.css파일 참조! (링크 통해 확인 가능)
https://developer-eve.tistory.com/26
