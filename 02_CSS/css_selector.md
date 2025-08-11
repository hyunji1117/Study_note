[CSS] CSS 선택자

1. 기본
전체 선택자 (Universal Selector)
범위 안에 있는 모든 요소 선택
* {
    background-color:gold;
}

태그 선택자 (Type Selector)
태그 이름으로 요소 선택
단, 태그의 종류가 모든 요소를 구분할 만큼 고유한 것이 아니기에 원하는 요소를 조금 더 정확하게 집어낼 수 있는 class 선택자를 사용할 수 있다. 
div {
    background-color:gold;
}

클래스 선택자 (Class Selector)
class로 지정한 요소 선택 (중복 선택 가능)
.name {
    background-color:gold;
}

아이디 선택자 (ID Selector)
전역 속성 id 값을 통해 요소를 찾는 개념
#name {
    background-color:gold;
}

2. 복합
일치 선택자 (Basic Combinator)
두 요소를 동시에 만족하는 선택자
** 주의 : 태그 선택자는 맨 앞에 작성해야 컴퓨터가 태그 선택자 임을 인식할 수 있다. 
div.name {		/* 태그와 클래스를 동시에 충족시킨다. */
    background-color:gold;
}

자식 선택자 (Child Combinator)
해당 선택자의 자식 요소 선택
div>.profile {
    background-color:gold;
}

<body>
    <div> <!-- div의 -->
        <ul class="profile"> <!-- .profile 자식 요소 선택자 -->
            <li class="name">Tom</li>
            <li class="age">28</li>
        </ul>
    </div>
    <div> <!-- div의 -->
        <ul class="profile"> <!-- .profile 자식 요소 선택자 -->
            <li class="name">Nate</li>
            <li class="age">33</li>
        </ul>
    </div>
    <span class="name">Joon</span>
</body>

하위(후손) 선택자 (Descendant Combinator)
해당 선택자의 하위에 있는 요소 선택
** 주의 : 띄어쓰기가 선택자 기호이다. (아래 예시 참조)
div .name {
    background-color:gold;
}
<body>
    <div> <!-- div의 -->
        <ul>
            <li class="name">Tom</li> <!-- .name 해당되는 하위 선택자 -->
            <li class="age">28</li>
        </ul>
    </div>
    <div> <!-- div의 -->
        <ul>
            <li class="name">Nate</li> <!-- .name 해당되는 하위 선택자 -->
            <li class="age">33</li>
        </ul>
    </div>
    <span class="name">Joon</span>
</body>

인접 형제 선택자 (Adjacent Sibling Combinator) 꼭 기억 해두자!
선택자의 다음에 해당하는 형제 요소 하나를 선택
.age+li {
    background-color:gold;
}
<body>
    <div> 
        <ul class="profile"> 
            <li class="name">Tom</li>
            <li class="age">28</li> <!-- .age 선택자의 -->
            <li class="company">Kakao</li> <!-- 다음 형제 요소 -->
        </ul>
    </div>
    <div>
        <ul class="profile"> 
            <li class="name">Nate</li>
            <li class="age">33</li> <!-- .age 선택자의 -->
            <li class="company">Line</li> <!-- 다음 형제 요소 -->
        </ul>
    </div>
    <span class="name">Joon</span>
</body>

일반 형제 선택자 (General Sibling Combinator)
선택자의 다음에 해당하는 형제 요소 모두 선택
.age~li {
    background-color:gold;
}
<body>
    <div> 
        <ul class="profile">
            <li class="name">Tom</li>
            <li class="age">28</li> <!-- .age의 --> 
            <li class="company">Kakao</li> <!-- 다음 형제요소 모두 선택자 -->
            <li class="addr">Seoul</li> <!-- 다음 형제요소 모두 선택자 -->
        </ul>
    </div>
    <div>
        <ul class="profile"> 
            <li class="name">Nate</li>
            <li class="age">33</li> <!-- .age의 --> 
            <li class="company">Line</li> <!-- 다음 형제요소 모두 선택자 -->
            <li class="addr">GyeongGi</li> <!-- 다음 형제요소 모두 선택자 -->
        </ul>
    </div>
</body>

3. 가상 클래스
:hover ** 자주 사용하는 선택자
마우스를 올렸을 때 변화하는 상태를 만들어 준다. (단, 이 외는 웬만하면 Js로 만든다.)
<body>
    <div class="box"></div>
</body>
div {
  width: 100px;
  height: 100px;
  background-color:orange;
}
div:hover {
  width: 250px;
}

** 함께 사용하면 효과보는 요소
전환 효과 (Transition)
div {
  width: 100px;
  height: 100px;
  background-color:orange;
  transition: 1s; /* 전환효과로 길게 늘어난다. */
}
div:hover {
  width: 250px;
}

:active 
마우스를 올려서 클릭하고 유지하는 동안 변화한다.

:focus
사용자에게 데이터를 입력받는 요소에 마우스를 올려서 클릭 후 활성화 된 상태포커스 후 선택한다. (Html 대화형 콘텐츠에만 해당)

** 포커스가 가능한 요소에서만 작동이 된다.
input, a, label, select, button, textarea 등 

그럼 포커스가 가능하지 않는 요소에 :focus를 작동할 수 있을까? 🤔
대답은 YES!!

e.g. Html div 요소에 tabindex='-1' 추가하면 아래와같이 포커스가 되는 것을 볼 수 있다. 
i.e. Tab키를 통해 포커스 가능한 순서를 지정하는 것이다. 


4. (동작을 처리하지 않는) 가상 선택자 (pseudo-classes)
:hover, :active, :focus는 Js에서 다루는 Css 동작 처리가 가능하다.
단, Css는 동작을 처리하는 개념이 아니기에 극히 일부분에 해당된다.

:first-child
첫 번째 자식이면 선택하는 선택자 (가상 선택자 기호인 : 으로 시작)
div가 부모 요소이며, 자식요소 span,p,h3는 같은 부모를 가진 자식 요소이다.
<div class="name">
    <span>Tomy</span>
    <span>Betty</span>
    <p>Lora</p>
    <h3>Lily</h3>
</div>

.name span:first-child{
  background-color: rgb(187, 238, 157);
}

:last-child
선택자가 형제 요소 중 막내라면 선택.
클래스 name의 하위 요소 span의 첫 번째 자식 요소 선택.

.name h3:last-child{
  background-color: rgb(237, 202, 164);
}

:nth-child(숫자)
선택자가 형제 요소 중 몇 번째에 해당하면 선택.
br태그도 하나의 자식요소에 해당된다. (예시1)
<div class="name">
    <span>Tomy</span>
    <span>Betty</span>
    <p>Lora</p>
    <h3>Lily</h3>
</div>
클래스 name 부모요소의 모든 자식요소 중 두 번째 요소 선택
.name *:nth-child(2){
  background-color: rgb(237, 202, 164);
}

<br/>태그를 Html 코드에 추가할 경우,
:nth-child 3번째 자식요소를 선택해야 (예시1)과 동일하게 'Betty'를 동일하게 선택 가능하다.(예시2)
<div class="name">
    <span>Tomy</span><br/>
    <span>Betty</span>
    <p>Lora</p>
    <h3>Lily</h3>
</div>
.name *:nth-child(3){
  background-color: rgb(237, 202, 164);
}

:nth-child(숫자n)
n은 0부터의 숫자를 들어가는 자리이다.

이 외로 여러가지 사용 방법이 있다. 
2n = 2x1, 2x2, 2x3 = 짝수 번째
2n+1 = 2x1+1, 2x2+1, 2x3+1 = 홀수 번째
n+2 = 0+2, 1+2, 2+2 = 2번째 요소부터 선택

부정 선택자 (Nagation) NOT
괄호 안에 있는 가장 선택자를 제외하고 선택
.name *:not(span){
  background-color: rgb(237, 202, 164);
}

5. 가상 요소 선택자 (Pseudo-Elements) **자주 사용
가상의 요소를 만들어서 실제로 삽입할 수 있는 구조를 가진다.

::before (콜론::두개 붙여서 쓰는게 웹표준이다.)
선택자 요소의 내부로 들어가, 선택자의 맨 앞에 내용을 삽입하는 개념.

아래 예시와같이 name이라는 선택자를 가지는 요소 앞에 contant속성에 작성한 내용을 명시한다.
i.e. '앞!!'이라는 글자를 ::before라는 가상 인라인 요소를 만들어서 name이라는 클래스를 가진 요소의 내부 앞에다 삽입하는 구조이다.

.name::before{		/* ::before는 인라인요소 */
  content: "앞!!";
  color: rgb(83, 177, 254);
}

::after
선택자 요소의 내부로 들어가, 선택자의 맨 뒤에 내용을 삽입하는 개념.
** 주의 : Css content 내 " "으로 비워두는 한이 있어도, 필수로 작성해야 한다.

.name::after{
  content: "뒤!!";
  color: rgb(83, 177, 254);
}

인라인 요소는 가로,세로 값을 지정해도 실제로 적용이 안된다. 
가로, 세로 값을 만들어주려면
인라인 요소 -> 블럭 요소로 전환해주는 속성을 넣어줘야 한다.
e.g. display : block 을 추가하면 된다.

.name::after{
  content: "";
  color: rgb(83, 177, 254);
  display: block; /* 인라인 요소를 블록 요소로 전환하는 방법 */
  width: 100px;
  height: 100px;
  background-color:lightpink;
}

6. 속성 선택자 (Attribute) ATTR
**주의 : 대괄호[] 이용하여 속성 선택자 임을 명시하기.

[속성Attribute]
속성의 이름만 가지고 선택하는 선택자
disabled를 가진 요소가 선택되어 글자 색상이 파란색으로 적용되는 구조.

<body>
    <input type="text" value="evelyn.kim">
    <input type="password" value="password">
    <input type="text" value="ddeok.kim" disabled>
</body>

[disabled] {
    color: blue;
}

(동일html코드에) 속성 이름이 type인 요소 명시하기.
[type] {
    color: blue;
}

[속성Attribute="속성 값"]
속성 선택자와 그의 속성 값과 함께 명시하여 찾는 선택자
장점 : 정확하게 원하는 속성을 찾을 수 있다.

<body>
    <input type="text"/><br/>
    <input type="password"/>
    <span data-worker-name="evelyn.kim">ddeok.kim</span>
</body>

속성 선택자 부분에 실제로 값을 입력하지 않아도
해당 속성을 가지고 있으면 유용하게 사용 가능.

body {
  margin:50px;
}
[data-worker-name] {		/* 모든 속성에 부합하는 선택자_대표적으로 data속성이 있음. */
    background-color: lightpink;
    color:red ;
}

