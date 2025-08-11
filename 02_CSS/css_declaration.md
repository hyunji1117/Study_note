[CSS] Css 선언방식

내장방식
Html 안에서 Css를 작성하는 방식.
장점 : 별도의 Css파일을 만들지 않아도 된다.
단점 : Css양이 많이질 경우, Html 안에서 한번에 다 처리하기 어렵고 유지 보수가 비효율적이다. 

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evelyn.kim</title>
    <link rel="stylesheet" href="./css/main.css">
    <script src="/js/main.js"></script>
    <style> <!-- Html 안에서 Css 작성하는 방법 -->
        div {
            text-decoration:underline;
        }
        a {
            font-size: 50px;
        }
    </style>
</head>

** 단, 프론트엔드 개발 방식으로 Html, Css, Javascript 파일을 구별해서 관리하면 장점이 많다는 점을 기억해두자. 
** 번들 : Html, Css, Javascript를 한번에 묶어서 서버에 올리는 방식이다. 
   번들하는 과정에서 개발하는 내용을 제품화시킬 때 파일로 분류한 내용들을 컴퓨터가 자동으로 합쳐서 내장방식으로 심는 경우가 있다. 
   이럴 경우, '내장방식'으로 Css를 작성하는 방법은 직접적으로 관리할 필요가 없어서 문제가 되지 않는다. 


인라인 방식 (Inline CSS)
해당 요소에 직접적으로 style 속성을 작성하는 방식.
장점 : 속성을 별도로 추가하지 않아도 된다.
단점 : Css 우선순위로 봤을 때 style이 지나치게 우선하는 문제를 가지고 있어서 유지보수 시 다른 코드로 Css 내용을 덮어서 수정이 어렵다.

<div style=font-size:100px;>Evelyn kim</div> <!-- 인라인 방식 -->


링크방식 (External CSS) (= 병렬로 연결)
외부에서 Css 파일을 한번에 가져오는 방식.
i.e. 해석이 빨리 끝나는 Css가 먼저 연결되는 구조를 갖게 된다. (빠르게 모든 Css파일을 연결하는 방식으로 추천한다.)

<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Evelyn.kim</title>
<link rel="stylesheet" href="./css/main.css"> <!-- 링크방식 -->
<script src="/js/main.js"></script>


@import 방식 (= 직렬로 연결)
링크방식 + import 규칙
Css의 import 규칙으로 main.css와 연결되어 있는 box.css를 가져오기 위한 연결 방식.
장점 : 연결을 지연시키는 목적으로 사용이 가능하다. 
단점 : 연결이 지연된다. 
i.e. box.css는 main.css가 @import를 통해 Html에 연결되기 전까지는 Html에 연결될 수 없다. 
이 개념을 장점으로 승화시킬 수 있지만, 단점이 될 수 있다는 것이다. (많이 사용되지 않는 방식)

<link rel="stylesheet" href="./css/main.css"> <!-- 첫 번째 Css 파일 작성하기 -->

@import url("./box.css"); /* 두 번째 Css 파일 작성하기 */
div {
  font-size: 100px;
}
div {			/* box.css 파일 */
    color: coral;
}

위 코드를 vscode에 한번에 정리하면 아래 이미지처럼 보이게 된다.

** 직렬, 병렬 차이 : 
applepop님의 <건전지의 직렬과 병렬 연결>을 보면 이해하기 쉽다.
https://blog.naver.com/applepop/221160828735
