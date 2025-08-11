[CSS] CSS 속성 메모

단위(Units)
font-size px vs. em 그리고 rem

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>우선순위 선택자</title>
    <link href="https://cdn.jsdelivr.net/npm/reset-css@5.0.2/reset.min.css"
rel="stylesheet">
    <link rel="stylesheet" href="/login/css/style.css">
</head>
<body>
    <div class="parent">
        <div class="child"></div>
    </div>
</body>
</html>

.parent {
  width: 300px;
  height: 200px;
  background-color:lightcoral;
}

.child{
  width: 50%;
  height: 50%;
  background-color:royalblue;
}

기본적으로 font-size는 16px 만큼의 크기가 들어가 있다.

단위 em
폰트 사이즈(16px) 만큼의 1em으로 사용으로 한다.
주변 상황에 따라 상대적으로 폰트 크리가 달라벼 관리가 필요한 단점이 있다.

여기서 Css child width값을 10em으로 바꾸면 16px 곱하기 10으로 160px i.e.160em으로 환산된다. 
동일하게 20em으로  값을 바꾸면 아래와 같이 320px이 출력된다. 

.parent {
  width: 300px;
  height: 200px;
  background-color:lightcoral;
}

.child{
  width: 20em;    /* 16px X 20 = 320px */
  height: 50%;
  background-color:royalblue;
}

만약 부모 요소에 font-size를 10px로 세팅한다면
자식 요소에 상속이 되어 10px X 20 = 200px으로 출력이 된다. 

.parent {
  width: 300px;
  height: 200px;
  background-color:lightcoral;
  font-size: 10px;
}

.child{
  width: 20em;    /* 1px X 20 = 200px */
  height: 50%;
  background-color:royalblue;
}

이렇게 부모 요소 font-size 세팅으로 인해 상대적으로 변하는 특성으로
잘 못 사용하면 혼란스러운 단위가 될 수 있어 별도의 관리가 필요하다. 
그리고 rem은 이런 이슈를 해결해줄 수 있다. 

단위 rem
Html 요소(root요소)에 지정된 폰트 크기를 기준으로 사용한다.
주변 상황이 바뀌어도 단위가 수정되는 일이 없도록 만들어주는 장점이 있다.
루트 요소의 폰트만 바꿔주면 모든 rem 값의 폰트 크기를 동시에 비율로 제어할 수 있다. 

e.g.
html 요소에 font-size를 16px로 세팅한다고 가정
부모 요소에 font-size를 10px로 세팅하여도
결과 값은 16px X 20 = 320px로 출력된다. 
Root 요소에 지정 폰트를 기준으로 사용되는 특성이 반영된 예시라고 볼 수 있다. 

html {
  font-size: 16px;
}

.parent {
  width: 300px;
  height: 200px;
  background-color:lightcoral;
  font-size: 10px;
}

.child{
  width: 20rem;    /* 16px X 20 = 320px */
  height: 50%;
  background-color:royalblue;
}

단위 vw/vh
뷰포트의 가로/세로 넓이/높이의 절반 만큼의 크기를 사용한다.

---------------------------------
외부 여백(margin)

margin : 30px(상하) 80px(좌우);
<body>
    <div class="box"></div>
    <div class="box2"></div>
</body>

.box{
  width: 300px;
  height: 300px;
  margin: 30px 80px;
  background-color: brown;
}

.box2{
  width: 300px;
  height: 300px;
  background-color: brown;
}

margin : 10px(상) 30px(좌우) 80px(하);
.box{
  width: 300px;
  height: 300px;
  margin: 10px 30px 80px;
  background-color: brown;
}

.box2{
  width: 300px;
  height: 300px;
  background-color: brown;
}

margin 음수값 적용 (자주 쓰지 않지만 유용할 때가 있음)
잘 모르겠다.. 좀 더 찾아보고 포스팅하겠다.

블록 요소에 가로 사이즈가 있는 상태에서 margin값의 좌우가 auto라면
해당 요소는 가운데 정렬이 된다. 

.container .heroes {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  background-color: orange;
  max-width: 700px;		/* 가로 사이즈 지정 */
  margin: auto;		/* 마진 오토 적용 */
}

.container .heroes .hero {
  width: 80px;
  height: 84px;
  margin: 4px;
  background-color: #555;
}

---------------------------------
내부 여백(padding) 
% 부모 요소의 가로 너비에 대한 비율로 지정 (예시 필요 要搞清楚的 Css 심화학습에서 다룬다.)
속성 : (요소의 크기가 늘어남) 내부 여백은 추가되는 것이기에 그 만큼의 요소 크기가 늘어난다.
margin의 음수값 사진으로 정리

---------------------------------
테두리 선(border)과 생상 표현
선 두께 > 선 종류 > 선 색상 (관습에 맞게 작성 권장)]
테두리 선이 두꺼워 질수록 요소(해당 박스)의 크기가 커진다.

.container .box {
  width: 200px;
  height: 200px;
  background-color:gold;
}

.container .box:first-child {
  border: 50px solid gold;
}

border-width : border라는 각각의 방향을 아우르는 단축 속성이며
두께, 종류, 색상을 이루어진 개별 속성이기도 하다. 

단축 속성 이란?
서로 다른 여러 가지 CSS 속성의 값을 지정할 수 있는 CSS 속성
e.g.
background 속성의
background-color
background-image
background-repeat
background-position (en-US)

---------------------------------
개별속성
개별속성으로 border-style: solid(실선) / dashed(파선) / dotted(점선)을 주로 사용한다. (점선 사용률 크지 않음)

border-color : 색상 표현
색상 이름	브라우저에 제공하는 색상 이름	e.g. red, tomato
Hex 색상코드	16진수 색상	e.g. #000, #FFF(#fff)
RGB	빛의 삼원색	e.g. rgb(255, 215, 0)
RGBA	빛의 삼원색 + 투명도	e.g. rgba(0, 0, 0, 0.5) / 투명도 0=투명, 0.5=반투명, 1=불투명

---------------------------------
border-방향-속성 단축 속성 (대표예시)

border-top: 두께 종류 색상;
.box {
  width: 200px;
  height: 200px;
  background-color:gold;
  margin: 25px;
  border-top: 5px solid #000; <!-- 주목! -->
}

border-top-width: 두께;
border-top-style: 종류;
border-top-color: 색상;
.box {
  width: 200px;
  height: 200px;
  background-color:gold;
  margin: 25px;
  border-top-width: 10px; <!-- 주목! -->
  border-top-style: dashed; <!-- 주목! -->
  border-top-color: #000; <!-- 주목! -->
}

---------------------------------
모서리 둥글게 (border-radius)

border-radius : 0 0 10px 0;
여기서 0은 단위를 붙이지 않기로 한다. 
.box {
  width: 200px;
  height: 200px;
  background-color:gold;
  margin: 25px;
  border-radius : 0 0 50px 0; <!-- 주목! -->
}

---------------------------------
크기 계산 (box-sizing) 
box의 사이즈를 150px로 지정하였는데
border과 padding을 적용하고 나니
개발자 도구에서 Box1은 270px로 출력된다. 

i.e.
Box1 가로 : 150px(기본가로값) + 10px(border좌) + 10px(border우) + 50px(padding좌) + 50px(padding우) = 270px
Box2 세로 : 150px(기본가로값) + 10px(border좌) + 10px(border우) + 50px(padding좌) + 50px(padding우) = 270px

아래 이미지 처럼 box1과 box2의 크기를 맞추려 수동으로 셋팅하는 것에는 한계가 보인다. 
여기서 box1에 box-sizing : border-box;를 추가하면 자동으로 box2와 동일한 사이즈로 맞출 수 있다. 

다른 예시로 보자!
hero라는 작은 박스가 32개 있다. 
hero 박스에 border값을 3px씩 주고나니 박스가 위,아래,좌,우 3px씩 늘어난 상황! (아래 왼쪽 이미지 참조)
box-sizing: border-box; 명시하고 박스의 크기 기준을 가로,세로 80px,84px로 픽스한다.

.container .heroes {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  background-color: orange;
  max-width: 700px;
  margin: 0 auto;
  padding: 40px 20px;
}

.container .heroes .hero {
  width: 80px;
  height: 84px;
  margin: 4px;
  background-color: #555;
  border: 3px solid #fff;		/* border사용으로 위아래좌우 3px 늘어난 상황 */
  border-radius: 10px;
  box-sizing: border-box;		/* 적용하여 가로,세로 80px,84px 유지! */
  transform: skewX(-14deg);
}

---------------------------------
넘침 제어(overflow)
부모와 자식 요소가 있다고 가정한다.

<body>
    <div class="parent">
      <div class="child"></div>
    </div>
</body>

.parent{
  width: 200px;
  height: 150px;
  margin: 20px;
  background-color: gold;
}

.child {
  height: 100px;
  background-color: darkorange;
}

여기서 자식의 가로 넓이를 부모보다 크게 설정하였을 때
.parent{
  width: 200px;
  height: 150px;
  margin: 20px;
  background-color: gold;
  overflow: hidden;   /* 부모요소에 적용 */
}

.child {
  width: 300px;   /* 더 크게 설정 */
  height: 100px;
  background-color: darkorange;
}

overflow : visible;
넘치는 영역을 그대로 보여준다.

overflow : hidden;
넘치는 영역이 잘려서 보인다.

overflow : scroll;
직관적으로 잘려서 보이지만
넘치는 영역의 내용을
사용자가 볼 수 있도록 한다. 

overflow : auto;
브라우저가 스트롤바를 만들지 자동으로 판단 후 생성한다. 
(가로는 넘치지 않아서 스트롤바 생성되지 않음)

개별 속성으로 overflow-x / overflow-y는 x축/y축 각각의 축을 명시하여 적용한다.

---------------------------------
출력 특성(display)

block요소는 가로 세로 값을 가지고 있는데
그에 반에 가로와 세로를 지정하지 못하는 span 요소는
display: block; 속성을 추가하여 가로, 세로를 바꿀 수 있는 요소로 활용을 많이 한다.

<body>
  <span class="parent">
    Evelyn.Kim
  </span>
</body>

body {
  margin: 20px;
}
.parent{
/*   display: block; */		/* 적용하지 않음! 이미지 블로그 참조 */
  width: 200px;
  height: 150px;
  background-color: gold;
}

.parent{
  display: block;		/* 적용 후! 이미지 블로그 참조 */
  width: 200px;
  height: 150px;
  background-color: gold;
}

---------------------------------
글꼴
font-style : 글자의 기울기;
font-weight : 글자의 두께 100 ~ 900 숫자 사용;
font-family: 글꼴(서체), "글 꼴(서체)", ... 글꼴계열;

글꼴 계열_serif (바탕체 계열)
글꼴 계열_sans-serif (고딕체 계열)
특징 : 웹에서 주로 보이는 글꼴 계열이다.
글꼴 계열_monospace (고정넓이 동등 글꼴 계열)
특징 : 글자 간 간격이 일정하여 가독성이 좋다. 코드 에디터에서 주로 사용.
글꼴 계열_cursive (필기체 계열)
글꼴 계열_fantasy (장식 글꼴 계열)

<body>
  <p>
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
    Itaque porro aliquam animi! Libero, beatae consequuntur 
    vero minima assumenda quis quas mollitia, maxime non temporibus 
    magnam aut doloremque error sunt dolores.
  </p>
</body>

body {
  margin: 20px;
}
p {
  width: 300px;
  box-sizing: border-box;
  border: 3px solid darkorange;
/*   line-height: 1.4; */
}

여기서 글자 행간 간격은 line-height로 넣으면 된다. 

body {
  margin: 20px;
}
p {
  width: 300px;
  box-sizing: border-box;
  border: 3px solid darkorange;
  line-height: 1.4;		/* 추가 내용! */
}

---------------------------------
문자
text-indent : 50px (들여씌기), -50px (내어쓰기);
text-align : left, right, center 문자 정렬 방식 (수평 정렬);
text-decoration : none, underline, overline*(윗줄 잘 안씀), line-through(중앙선, 취소선)
a 태그로 연결된 글자는 기본적으로 파란색 글씨에 밑줄이 있다. (아래 예시 참조)

<body>
  <a href="www.google.com">Google</a>
</body>

body {
  margin: 20px;
}
a {
  display: block;
  width: 300px;
  height: 200px;
  /* color: #000; */
  font-size: 100px;
/*   text-decoration: none; */
  background-color: gold;
}

여기서 글자색 지정 및 밑줄 없애기 위해 text-decoration을 사용하면 된다.

body {
  margin: 20px;
}
a {
  display: block;
  width: 300px;
  height: 200px;
  color: #000;    /* 주목! */
  font-size: 100px;
  text-decoration: none;    /* 주목! */
  background-color: gold;
}

---------------------------------
배경
background-image : url("함수 경로 입력")요소의 배경 이미지로 삽입
<body>
  <div></div>
</body>

body {
  margin: 20px;
}
div {
  width: 200px;
  height: 200px;
  background-color: gold;
  background-image: url("https://s.pstatic.net/shopping.phinf/20240103_
  15/6a8a1221-4b79-4c18-be35-4bd3619a6671.jpg");		/* 링크 추가! */
};

background-size : 이미지 크기 제어 속성 (바둑판식 배열)
cover(더 긴 너비에 맞춰서 출력), contain(더 짧은 너비에 맞춰서 출력)

background-repeat : 반복 제어 속성

background-position : 요소의 배경 이미지 위치
방향으로 위치 결정 : 상,하,좌,우,center
단위로 x,y축 위치 결정 : 200px(x축) 50px(y축)

background-attachment : 배경 이미지 스크롤 특성 scroll, fixed;
background-attachment: scroll;
특징 : 스크롤 내리면 이미지가 올라간다.
background-attachment: fixed;
특징 : 스크롤 내려도 이미지는 화면에 고정되어 있다.

**패럴렉스(parallax)
스크롤에 따라 오브젝트와 배경 이미지가 시간차를 두고 변하는 기법.

---------------------------------

포지션 position : 요소의 위치 지정 기준 (원하는 위치에 배치하기) ** (중요!)
i.e.기준을 먼저 잡고 위치값을 설정해야 한다. 

함께 사용되는 속성 : (방향 별 거리 지정)
top
bottom
left
right
z-index

position: relative (요소 자신을 기준으로 지정)
relative 선언 후 아무 변화가 없는 것이 정상이다. 

<body>
  <div class="container">
    <div class="box">BOX 1</div>
    <div class="box">BOX 2</div>
    <div class="box">BOX 3</div>
  </div>
</body>

body {
  margin: 50px;
}
.container {
  width: 400px;
  height: 400px;
  background-color: #d9ed92;
  font-size: 50px;
  font-weight: 700px;
}

.container .box:nth-child(1) {
  width: 200px;
  height: 200px;
  background-color: #99d98c;
}

.container .box:nth-child(2) {
  width: 150px;
  height: 100px;
  background-color: #52b69a;
  position:relative;		/* 적용 후 변화 없음 */
}

.container .box:nth-child(3) {
  width: 250px;
  height: 100px;
  background-color: #168aad;
}

여기서 방향 설정하면 BOX2가 이동한 것을 볼 수 있다. 

.container .box:nth-child(2) {
  width: 150px;
  height: 100px;
  background-color: #52b69a;
  position:relative;
  top: 50px;		/* 이동 방향 설정 */
  left: 200px;		/* 이동 방향 설정 */
}

하지만 극단적이 예시로 들었을 때 BOX2가 오른쪽 끝으로 갈 경우
BOX1과 BOX3 사이 공백이 생기는 원인을 알 도리가 없어진다. 
그렇기에 자기자신을 기준으로 배치하는 position: relative는 쓰지 않는다고 보면 된다. 
**사실 상 BOX2는 해당 공백에 있고, left: 2000px;로 배치된  BOX2는 허상인 것이다. 

.container .box:nth-child(2) {
  width: 150px;
  height: 100px;
  background-color: #52b69a;
  position:relative;
  top: 50px;
  left: 2000px;		/* 변경! */
}

position: absolute (부모 요소를 기준으로 지정)
위치를 지정하기 위한 기준을 설정해주는 속성
i.e. 기준을 먼저 잡고 위치값을 지정해야 한다. 

여기서 조금 전에 추가한 position: relative를 absolute로 바꾼다면
자신을 절대 기준으로 했던 relative와 달리 상대 기준을 잡는 absolute는 뷰포트(브라우저)를 기준으로 잡는 것을 볼 수 있다.

.container .box:nth-child(2) {
  width: 150px;
  height: 100px;
  background-color: #52b69a;
  position: absolute;		/* 변경! */
  top: 50px;
  left: 200px;
}

그리하여 상대 기준으로 부모 요소를 절대적 기준으로 잡는다고 명시를 해야 한다. 

.container {
  width: 400px;
  height: 400px;
  background-color: #d9ed92;
  font-size: 50px;
  font-weight: 700px;
  position: relative;		/* 2.여기를 쓰는 것! */
}

.container .box:nth-child(2) {
  width: 150px;
  height: 100px;
  background-color: #52b69a;
  position: absolute;		/* 1.여기를 쓰기 위해 */
  top: 50px;
  left: 200px;
}

position: fixed (뷰포트i.e.브라우저를 기준으로 지정)
i.e. fixed를 쓰는 것은 주변 배치와 더이상 상호작용하지 않고 뷰포트 기준으로 배치한다
웹페이지 우하단 '맨 위로 올라가기' 버튼 경우, 해당 기능으로 구현가능.

---------------------------------
요소 쌓인 순서(stack order)

조건 :
1. 요소에 position값이 있는 경우, 위에 쌓인다.
2. 1번의 조건을 충족할 경우, z-index 속성 값이 높을 수록 위로 쌓인다.
3. 1번과 2번의 조건이 같은 경우, Html의 구조가 더 나중에 작성되어 있을 수록 위에 쌓인다.

body {
  margin: 50px;
}
.container {
  width: 300px;
  height: 300px;
  background-color: #f4acb7;
  font-size: 25px;
  font-weight: 700px;
  position: relative;		/* postion 값이 있음 */
}

.container .box { 
  border: 1.5px solid #000;
  box-sizing: border-box;
}

.container .box:nth-child(1) {
  width: 100px;
  height: 100px;
  background-color: #ffcad4;
  position: relative;		/* postion 값이 있음 */
}

.container .box:nth-child(2) {
  width: 100px;
  height: 100px;
  background-color: #ffcad4;
  position: absolute; 		/* postion 값이 있음 + Html 구조가 나중에 있음 */
  top: 30px;
  left: 80px;
}

.container .box:nth-child(3) {
  width: 100px;
  height: 100px;
  background-color: #ffcad4;
}

---------------------------------
z-index

z-index를 적용하면 BOX1이 가장 위에 쌓인다. 

.container .box:nth-child(1) {
  width: 100px;
  height: 100px;
  background-color: #ffcad4;
  position: relative;
  z-index: 1;		/* 주목! */
}

더 뒤에 쌓고 싶으면 -1이하로 설정하면 된다.

** 주의사항 (중요!)
인라인 요소여도 position: relative/absolute를 쓰면 자동으로 block 요소로 바뀌어 가로,세로 넓이를 지정할 수 있다.

<body>
  <span>
    Evelyn.Kim
  </span>
</body>

body {
  margin: 20px;
}

span { 
  width: 100px;
  height: 100px;
  background-color: gold;
  position: absolute;
}

---------------------------------
flex(정렬) - container
display : flex 를 통해 수평정렬 출력 가능하다.

body {
  margin: 50px;
}
.container {
  /* width: auto; */		/* flex일 때 블로요소로 가로 넓이가 최대로 늘어나려고 한다. */
  background-color: #f4acb7;
  font-size: 25px;
  font-weight: 700px;
  /* display: flex; */
}

.container .box { 
  border: 1.5px solid #000;
  box-sizing: border-box;
}

.container .box:nth-child(1) {
  width: 100px;
  height: 100px;
  background-color: #ffcad4;
}

.container .box:nth-child(2) {
  width: 100px;
  height: 100px;
  background-color: #ffcad4;
}

.container .box:nth-child(3) {
  width: 100px;
  height: 100px;
  background-color: #ffcad4;
}

그리고 아래는 display: flex 적용 후 Flex container으로 만들어 출력된 화면이다. 

.container {
  background-color: #f4acb7;
  font-size: 25px;
  font-weight: 700px;
  display: flex;		/* 주목! */
}

Css flex 관련된 속성에 대해 자세하게 살펴보자!
Css flex를 사용하기 앞서 display: flex; 부여로 flex contatiner를 만들어야 한다. (대부분 수평정렬 목적으로 사용)
display: flex를 부여한 container(큰 박스)를 flex container라고 부르고
그 안에 블록 요소(작은 박스)를 flex items라고 한다. (위 예시 이미지 참조)
여기서 Flex Container에 부여하는 속성, Flex Items에 부여하는 속성이 각각으로 나누어져 있다.

Flex Container 속성
- display
- flex-flow / flex-direction / flex-wrap
- justify-content (주축,X축 의 수평정렬 방법)
- align-content (여러줄의 수직정렬 방법)
stretch
flex-start
flex-end
center
- align-items (한 줄의 수직정렬 방법)
stretch
flex-start
flex-end
center

Flex Items 속성
- order
- flex / flex-grow / flex-shrink / flex-basis
- align-self


Flex Container 지정 속성 : 
display: block, inline 값을 입력하여 화면에 출력되는 특성을 제어하는 속성
display: inline-flex; 인라인 요소처럼 동작할 수 있도록 한다. 

flex-direction
주축 설정 (박스 정렬)
위에서 flex container과 flex items를 만들고 container의 주축을 설정하는 것. (수평 or 수직)
flex container를 기준으로.. (하지만 flex container 안에서는 수평 정렬된 구조여서 flex-direction이 필요 없다)

(기본값) row : (좌 > 우 / 행) - X축 주축(Main-axis) 그리고 이를 가로 지르는 Y축 교차 축(Cross-axis)가 있다.
             row-reverse : (우 > 좌 / 행)
             column : (위 > 아래 / 열) - Y축 주축 (사용빈도 낮음)
             column-reverse : (아래 > 위 / 열) (사용빈도 낮음)
i.e. display는 수평정렬을 하던 수직정렬을 하던 1차원의 하나의 축을 가지고 정렬하는 개념이다. 

flex-wrap : Flex Items 줄바꿈 처리여부 (묶음여부)
i.e. container가 items 보다 작으면(수용불가) 아래 nowrap 예시처럼 박스들이 찌그러진다. 

nowrap (줄바꿈 없음)
flex container의 넓이가 부족하고 각각의 item(box)들을 한 줄에 표현할 때 지정된 크기보다 작게 찌그러진 item(box)를 볼 수 있다.

<body>
  <div class="container">
    <div class="box">BOX 1</div>
    <div class="box">BOX 2</div>
    <div class="box">BOX 3</div>
    <div class="box">BOX 4</div>
    <div class="box">BOX 5</div>
  </div>
</body>

body {
  margin: 50px;
}
.container {
  width: 400px;
  height: 200px;
  background-color: #007f5f;
  font-size: 25px;
  font-weight: 700px;
  display: flex;		/* 먼저 선언 후 */
  flex-wrap: nowrap;		/* 줄바꿈 안 함 */
}

.container .box { 
  border: 1px solid #007f5f;
  box-sizing: border-box;
}

.container .box:nth-child(1) {
  width: 100px;
  height: 100px;
  background-color: #55a630;
}

.container .box:nth-child(2) {
  width: 100px;
  height: 100px;
  background-color: #80b918;
}

.container .box:nth-child(3) {
  width: 100px;
  height: 100px;
  background-color: #aacc00;
}

.container .box:nth-child(4) {
  width: 100px;
  height: 100px;
  background-color: #bfd200;
}

.container .box:nth-child(5) {
  width: 100px;
  height: 100px;
  background-color: #d4d700;
}

wrap (줄바꿈)
.container {
  width: 400px;
  height: 200px;
  background-color: #007f5f;
  font-size: 25px;
  font-weight: 700px;
  display: flex;		/* 먼저 선언 후 */
  flex-wrap: wrap;		/* 줄바꿈 하기 */
}

** PS **
.container {
  width: 250px;
  /* height: 200px; */		/* 높이 삭제 또는 auto로 바꾸면 
  				줄바꿈한 박스의 최종 높이에 맞게 배경이 맞춰진다. */
  background-color: #007f5f;
  font-size: 25px;
  font-weight: 700px;
  display: flex;
  flex-wrap: wrap;
}

justify-content : 주축(X축) 의 수평정렬 방법
flex-start : Flex Items 왼쪽으로 정렬
flex-end : Flex Items 오른쪽으로 정렬

.container {
  /* width: 300px; */
  /* height: 200px; */
  background-color: #007f5f;
  font-size: 25px;
  font-weight: 700px;
  display: flex;
  justify-content: flex-end;		/* 오른쪽 정렬 적용 */
  flex-wrap: nowrap;
}

center : Flex Items 가운데로 정렬
.container {
  /* width: 300px; */
  /* height: 200px; */
  background-color: #007f5f;
  font-size: 25px;
  font-weight: 700px;
  display: flex;
  justify-content: center;		/* 가운데로 정렬 */
  flex-wrap: nowrap;
}

(** 여기서 아이템(박스)의 순서는 바뀌지 않는다.)

align-content
주축을 수직으로 바꾸어 여러 줄 정렬 방법

조건 : 
1. 줄바꿈 상태여야 한다. (flex-wrap: wrap;)
2. 정렬이 가능한 빈 공간이 있어야 한다. 
3. flex items가 두줄 이상 이어야 한다.
조건이 까다로워서 생각보다 활용도가 높지 않다.

stretch : Flex Items 세로 높이를 늘려 container 높이에 맞추며 왼쪽 정렬
body {
  margin: 50px;
}
.container {
  width: 350px;
  height: 300px;
  background-color: #007f5f;
  font-size: 25px;
  font-weight: 700px;
  display: flex;
  flex-wrap: wrap;
}

.container .box { 
  border: 1px solid #007f5f;
  box-sizing: border-box;
}

.container .box:nth-child(1) {
  width: 100px;
  /* height: 100px; */		/* 높이 미지정으로 stretch하여 container 높이에 맞추게 된다. */
  background-color: #55a630;
}

.container .box:nth-child(2) {
  width: 100px;
  /* height: 100px; */
  background-color: #80b918;
}

.container .box:nth-child(3) {
  width: 100px;
  /* height: 100px; */
  background-color: #aacc00;
}

.container .box:nth-child(4) {
  width: 100px;
  /* height: 100px; */
  background-color: #bfd200;
}

.container .box:nth-child(5) {
  width: 100px;
  /* height: 100px; */
  background-color: #d4d700;
}

stretch 상태에서 flex items(작은 박스) 높이를 지정하면 아래와같이 출력된다. 
.container .box:nth-child(1) {
  width: 100px;
  height: 100px;		/* 세로 높이 지정 */
  background-color: #55a630;
}

.container .box:nth-child(2) {
  width: 100px;
  height: 100px;
  background-color: #80b918;
}

.container .box:nth-child(3) {
  width: 100px;
  height: 100px;
  background-color: #aacc00;
}

.container .box:nth-child(4) {
  width: 100px;
  height: 100px;
  background-color: #bfd200;
}

.container .box:nth-child(5) {
  width: 100px;
  height: 100px;
  background-color: #d4d700;
}

flex-start
Flex Items 수직축 기준 위쪽 정렬
.container {
  width: 350px;
  height: 300px;
  background-color: #007f5f;
  font-size: 25px;
  font-weight: 700px;
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;		/* 적용!! */
}

flex-end
Flex Items 아래쪽 정렬

center
Flex Items 가운데 정렬


align-items : 주축을 수직으로 바꾸어 한 줄 정렬 방법

stretch
Flex Items 각 줄 정렬 (items 높이 값 미적용)

flex-start
Flex Items 각 줄 위쪽 정렬

flex-end
Flex Items 각 줄 아래쪽 정렬

center
Flex Items 각 줄 중앙 정렬


Flex Items 지정 속성 : 

order : 숫자; (기본값 0)
정렬되는 순서 (숫자가 작은 순으로 앞으로 배치)
body {
  margin: 50px;
}
.container {
  width: 550px;
  height: 150px;
  background-color: #0077b6;
  font-size: 25px;
  font-weight: 700px;
  display: flex;
  flex-wrap: nowrap;
  /* align-items: flex-end; */
}

.container .box { 
  border: 1px solid #0077b6;
  box-sizing: border-box;
}

.container .box:nth-child(1) {
  width: 100px;
  height: 100px;
  background-color: #caf0f8;
  /* 기본값-0으로 세팅되어 있다. */
}

.container .box:nth-child(2) {
  width: 100px;
  height: 100px;
  background-color: #ade8f4;
  /* 기본값-0으로 세팅되어 있다. */
}

.container .box:nth-child(3) {
  width: 100px;
  height: 100px;
  background-color: #90e0ef;
  order: -2;		/* 적용! */
}

.container .box:nth-child(4) {
  width: 100px;
  height: 100px;
  background-color: #48cae4;
  /* 기본값-0으로 세팅되어 있다. */
}

.container .box:nth-child(5) {
  width: 100px;
  height: 100px;
  background-color: #00b4d8;
  order: -1;		/* 적용! */
}

flex
flex-grow : 숫자; (기본값 0)
요소가 증가하는 비율 

i.e. 아래와같이 flex-grow: 1; 선언은
BOX1이 빈 공간을 채우고 (아래 사진 참조)
나머지 공간을 BOX2, BOX3이 채우는 것이다.

.container .box:nth-child(1) {
  width: 80px;
  height: 80px;
  background-color: #caf0f8;
  flex-grow: 1;		/* 적용! */
}

여기서 BOX2에 flex-grow: 2;를 적용한다면
BOX3을 제외한 공간을 BOX1과 BOX2가 1:2의 비율로 나눈다는 뜻이 된다.

.container .box:nth-child(1) {
  width: 80px;
  height: 80px;
  background-color: #caf0f8;
  flex-grow: 1;
}

.container .box:nth-child(2) {
  width: 80px;
  height: 80px;
  background-color: #ade8f4;
  flex-grow: 2;		/* 추가 적용! */
}

flex-shrink : 숫자; (기본값 1)
감소 너비 비율
Flex container 너비에 따라 감소비율 적용

Container가 점점 줄어서 안에 있는 flex items를 찌그러트리는 상황을 보자. (박스를 찌그러지지 않게 하려면?)

.container .box { 
  border: 1px solid #0077b6;
  box-sizing: border-box;
  flex-shrink: 0;		/* 기본값 1을 막아 0으로 적용하면 각 items의 실체 크기를 유지 해준다. */
}

flex-basis : 단위; (기본값 auto)
공간 배분 전 기본 너비
비율로 계산되도록 만들어준다.

flex-basis : auto;는 content 내용의 너비를 뜻한다. 
여기서 flex-grow를 설정해도 실제 (content)글씨 내용이 들어있기 때문에 적용되지 않는다. 

body {
  margin: 50px;
}
.container {
  width: 500px;
  height: 150px;
  background-color: #0077b6;
  font-size: 25px;
  font-weight: 700px;
  display: flex;
  flex-wrap: nowrap;
}

.container .box { 
  border: 1px solid #0077b6;
  box-sizing: border-box;
  flex-basis: 0;		/* 글자 만큼의 너비를 0으로 설정 */
  text-align: center;		/* text 중앙 정렬 */
  line-height: 100px;		/* 위아래 높이 추가하여 센터로 맞추기 */
}

.container .box:nth-child(1) {
  width: 100px;
  height: 100px;
  background-color: #caf0f8;
  flex-grow: 2;		/* 기본너비 없이 증가너비 2배수로 정렬 */
}

.container .box:nth-child(2) {
  width: 100px;
  height: 100px;
  background-color: #ade8f4;
  flex-grow: 1;		/* 기본너비 없이 증가너비 1배수로 정렬 */
}

.container .box:nth-child(3) {
  width: 100px;
  height: 100px;
  background-color: #90e0ef;
  flex-grow: 3;		/* 기본너비 없이 증가너비 3배수로 정렬 */
}

여기서 flex-basis를 100으로 설정한다면
기본 contant(글자영역)을 100px로 지정하는 것이다.
그리고 남은 영역을 기존 세팅한 2:1:3 비율로 배분하게 된다.

.container .box { 
  border: 1px solid #0077b6;
  box-sizing: border-box;
  flex-basis: 100;		/* 새로 설정! */
  text-align: center;
  line-height: 100px;
}

i.e. 시각적으로 2:1:3 비율로 보이지 않아 복잡하기에
기본적으로 flex-basis를 0으로 맞춰서 flex-grow에 맞는 비율로 출력하려고 한다. 

______________________________

전환 효과 (transition)
요소의 전 상태와 후 상태를 자연스럽게 만들어주는 전환효과 지정 단축 속성

transition-property : 속성이름; (기본값 all - 모든 Css속성에 적용)
전환 효과를 사용할 특정 속성의 이름을 명시한다.

<body>
  <div class="container">
    <div class="box">Transition</div>
  </div>
</body>

body {
  margin: 50px;
}

div {
  width: 150px;
  height: 150px;
  background-color: #16E2F5;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
  transition: 1s;		/* 적용 후 자연스러운 색상,크기 변화! */
}

div:active {
  width: 500px;
  background-color: #F52916;
}

여기서 특정  속성 이름(width)을 명시한다면
위에서 부드럽게 변했던 색상이 뚝뚝 끊기면서 바뀌고
직접 명시를 했던 속성 이름(width)는 그대로 부드럽게 움직인다. 

div {
  width: 150px;
  height: 150px;
  background-color: #16E2F5;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
  transition: width 1s;		/* 특정 속성 이름 추가 */
}

transition-duration : 시간; (기본값 0) (필수 포함 속성)
전환 효과의 지속시간 지정

여기서 transition 속성이름 지정 외 다른 속성도 함께 지정 가능하며
각각 다른 지속시간을 지정할 수 있는 장점이 있다. 

div {
  width: 150px;
  height: 150px;
  background-color: #16E2F5;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
  transition: 
    width .5s,				/* 각각 줄 나누고 */
    background-color 3s;		/* 지속시간을 별도 명시할 수 있다. */
}

transition-timing-function (=easing function) : ease 기본값(느리게>빠르게>느리게), linear(일정하게), 
ease-in(느리게>빠르게), ease-out(빠르게>느리게), ease-in-out(느리게>빠르게>느리게)
전환효과의 타이밍 함수를 지정한다.

자세한 정보는 아래 참조
Easing 함수 치트 시트 https://easings.net/ko﻿
Html, Css, Javascript로 easing 효과를 얻을 수 있다. https://gsap.com/docs/v3/Eases﻿

transition-dely : 시간; (기본값 0s)
전환 효과가 몇 초 뒤에 시작할지 대기시간 지정 속성

div {
  width: 150px;
  height: 150px;
  background-color: #16E2F5;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
  transition: 1s 2s;		/* 선 지속시간, 후 대기시간 */
}

:hover, :active를 자연스럽게 만들어 주는 단축 속성이다. 
개별 속성으로는 4가지가 있다. (비교 이미지 정리)
전환 속성의 특정 속성만 사용이 가능 하다. (정리)

transition-timming-function : 전환 효과의 타이밍 함수를 지정하는 것.
transition-delay : 전환 효과가 몇 초 뒤에 시작하는지 대기시간 지정하는 것.


변환 효과 (transform)

요소를 변환시켜주는 속성
변환 함수를 사용하여 원근법, 이동, 크기, 회전, 기울임 등 변환 효과를 주는 것이다.

body {
  margin: 50px;
}

.container {
  width: 150px;
  height: 150px;
  background-color: #BDF516;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
}

.container .item {
  width: 150px;
  height: 150px;
  color: #fff;
  background-color: #4E16F5;
  transform: rotate(45deg);		/* 변환 함수 명시 */
}

여기서 scale(크기)를 명시 해보자. 

.container .item {
  width: 150px;
  height: 150px;
  color: #fff;
  background-color: #4E16F5;
  transform: rotate(45deg) scale(1.2);		/* 크기를 1.2배로 명시 */
}

변환 함수
2D
translate : X축, Y축으로 이동 (단위 px)

body {
  margin: 50px;
  background-color: #DADBDD;
}

.container {
  width: 150px;
  height: 150px;
  background-color: #837E7C;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
}

.container .item {
  width: 150px;
  height: 150px;
  color: #000;
  background-color: #FFDF00;
  translate: 30px 30px;		/* X축으로 30px 이동, Y축으로 30px 이동 */
}

translate : X(x) 축 개별 이동 (단위 px)
translate : Y(y) 축 개별 이동 (단위 px)
scale : 숫자(X축,Y축 동시 적용 가능) (권장, X축 Y축 개별 크기 지정 비권장)

.container .item {
  width: 150px;
  height: 150px;
  color: #000;
  background-color: #FFDF00;
  scale: 1.5;		/* 크기 1.5배 명시 */
}

.container .item {
  width: 150px;
  height: 150px;
  color: #000;
  background-color: #FFDF00;
  scale: 1.5;
  opacity: 0.5;		/* 투명도 지정하여 scale가 얼마나 커졌는지 보자! */
}

rotate(degree) : 회전(각도) (단위 deg)
skewX(x) : X축 개별 기울임 (단위 deg) - 마름모 만들 수 있음
skewY(y) : Y축 개별 기울임 (단위 deg) - 마름모 만들 수 있음

.container .item {
  width: 150px;
  height: 150px;
  color: #000;
  background-color: #FFDF00;
  transform: perspective(500px) skew(45deg);		/* 적용! */
}

3D
rotateX(x) : X축을 기준으로 3D 회전
rotateY(y) : Y축을 기준으로 3D 회전
**글씨가 있으면 찌그러 지는 이슈가 있다. 

perspective(함수) : 원근법(거리)
앞에 있어야지만 적용이 가능하다. 
rotate만 명시하면 3D로 보이지 않아 원근법 함수를 추가하여 회전하는 것을 보자.

.container .item {
  width: 150px;
  height: 150px;
  color: #000;
  background-color: #FFDF00;
  transform: perspective(500px) rotateX(45deg);	/* X축을 기준으로 3D회전 */
}				  /* 꼭 회전 함수 앞에, i.e.transform 모든 속성 맨 앞에 배치해야 한다. */


perspective(속성) : 단위; (원근거리 해당 값)
하위요소를 관찰하는 원근 거리를 지정

perspective함수와 perspective속성 차이점 : 

속성/함수	적용 대상	요소가 변환되는 기준점(위치) 설정
perspective : 500px;             (권장)속성 형태	관찰 대상의 부모 요소에 적용	perspective-origin
transform:perspetive(500px);       함수 형태	관찰 대상의 원근거리 부여 요소에 직접 적용	transform-origin
i.e. 관찰대상을 부모로 지정 혹은 본인에게 지정의 차이

body {
  margin: 50px;
  background-color: #DADBDD;
}

.container {
  width: 400px;
  height: 150px;
  background-color: #6698FF;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
  
}

.container .item {
  width: 225px;
  height: 150px;
  background-color: #FFCC66;
  color: #000;
  transform: perspective(500px) rotateY(50deg);		/* perspective함수로 자기자신에게 지정 */
}

----

.container {
  width: 400px;
  height: 150px;
  background-color: #6698FF;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 150px;
  perspective: 500px;		/* 부모 요소에 perspective속성 적용 */
}

.container .item {
  width: 225px;
  height: 150px;
  background-color: #FFCC66;
  color: #000;
  transform: rotateY(50deg);
}

backface-visibility
뒤집었을 때 뒷면이 보이지 않도록 해주는 속성

.container .item {
  width: 225px;
  height: 150px;
  background-color: #FFCC66;
  color: #000;
  transform: rotateY(180deg);		/* 180도 회전 */
}

.container .item {
  width: 225px;
  height: 150px;
  background-color: #FFCC66;
  color: #000;
  transform: rotateY(180deg);
  backface-visibility: hidden;		/* 뒷면이 보이지 않독록 명시 */
}










