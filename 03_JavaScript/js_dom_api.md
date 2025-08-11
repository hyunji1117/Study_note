# [JS] javascript 자바스크립트 DOM API

## DOM API (Document Object Model, Application Programming Interface)
(어플리케이션)웹사이트가 동작하도록 입력하는 프로그래밍 명령  
i.e. 자바스크립트에서 (DOM)HTML을 제어하는 여러가지 명령들(API)이다.  
```
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="./main.js"></script>
</head>
<body>
    <div class="box">BOX!</div>    
</body>
</html>
```
CSS 선택자(.box)를 통해 HTML부분에서 특정 요소를 찾아서 그것을 변수 boxEl에 할당한다.  
```
let boxEl = document.querySelector('.box');

console.log(boxEl);
```
하지만 브라우저가 위에서 아래로 HTML코드를 읽어 내려가는 특성으로  
HTML <script> 영역까지 코드를 읽고 콘솔창에 값을 출력하는 오류가 발생된다.  
<img width="688" alt="스크린샷 2024-02-06 오전 7 42 19" src="https://github.com/hyunji1117/everyday_study/assets/151576407/8d17b7e1-fb6d-43a8-b85c-9a7780b6a297">
> 해당 값을 찾을 수 없다고 Null이 뜨게 된다.

여기서 script 코드에 defer를 추가하면 브라우저가 코드를 쭉 읽고 다시 <script>로 올라와서 요청한 값을 확인하여 출력하게 된다. 
(CSS .box > html class "box"를 가진 div요소를 찾아서 boxEl에 할당이 되어 출력)   
```
<title>Document</title>
<script defer src="./main.js"></script>		<!-- defer 추가 -->
```
<img width="688" alt="스크린샷 2024-02-06 오전 7 44 32" src="https://github.com/hyunji1117/everyday_study/assets/151576407/ea51768d-7076-4d0f-aa60-090936ad2684">

### DOM API  실행 과정
요소 1개만 검색,찾기를 통한 실행 과정
```
// HTML 요소(Element) 1개 검색/찾기
const boxEl = document.querySelector('.box');
/*
querySelector: 메소드
('.box'): class 선택자 인수
boxEl: box요소 약자

해당 CSS 선택자를 통해 찾아진 요소 중 가장 먼저 찾은 요소 하나만 반환하는 특징이 있다.
*/

// HTML (boxEl)요소에 메소드 추가 가능
boxEl.addEventListener();

// 명령어 addEventListener 메소드에 인수(Arguments, 데이터X) 추가 가능
boxEl.addEventListener(1,2);

// 1 - 첫 번째 인수_이벤트(Event, 상황)
boxEl.addEventListener('click', 2);
/*
사용자가 boxEl를 클릭했을 때의 상황을 브라우저는 '이벤트'라고 본다.
i.e. 클릭이라는 상황이 일어나면 무언가를 하겠다는 의미로 사용되는 코드이다.
*/

// 2 - 두 번째 인수_핸들러(Handler, 실행할 함수)
boxEl.addEventListener('click', function (){
  console.log('click!');
});
/*
두 번째 인수에 익명 함수를 대신 넣어 데이터처럼 활용한다.
i.e. boxEl에 이벤트를 추가할지 듣고 있다가 클릭이 일어나면 익명 함수를 실행시킨다는 의미이다.  
*/
```

js에서 class 추가하기  
```
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script defer src="./main.js"></script>
</head>
<body>
    <div class="box">BOX!</div>    
</body>
</html>
```
그리고 콘솔창에 active 추가/제거 하고 추가/제거 되었는지 확인도 함께 해준다.
```
let boxEl = document.querySelector('.box');

console.log(boxEl);

boxEl.addEventListener('click', function(){
  console.log('Click!');
  boxEl.classList.add('active');	// class추가!!
});
```
<img width="688" alt="콘솔창에 class active 추가 확인하기" src="https://github.com/hyunji1117/everyday_study/assets/151576407/0bf32c97-d6d2-414d-a730-3ce54929b27f)">
<img width="688" alt="스크린샷 2024-02-09 오후 10 42 03" src="https://github.com/hyunji1117/everyday_study/assets/151576407/dd29a9fd-026c-4a7c-b477-c555d8d6d403">

요소 모두 검색,찾기를 통한 실행 과정
```
// HTML 요소(Element) 모두 검색/찾기
const boxEls = document.querySelectorAll('.box');
console.log(boxEls);

// 찾은 요소들 반복해서 익명 함수로 실행
// 여기서 익명 함수를 인수로 추가했다.
boxEls.forEach(function (){});

// 첫 번째 매개변수(boxEl): 반복되는 요소 (이름 지정 가능)
// 두 번째 매개변수(index): 반복되는 번호 (통상적으로 index로 사용)
boxEls.forEach(function (boxEl, index){});

// 콘솔창 출력
boxEls.forEach(function (boxEl, index){
  boxEl.classList.add(`other-${index + 1}`);
  console.log(index, boxEl);
});
```
이런 데이터를 기반으로 js를 통해 box class order번호 만들어 보자!  
```
const boxEls = document.querySelectorAll('.box');

boxEls.forEach(function (boxEl, index){
  boxEl.classList.add(`order-${index + 1}`);
  console.log(index, boxEl);
});
```
<img width="1194" alt="스크린샷 2024-02-09 오후 11 06 56" src="https://github.com/hyunji1117/everyday_study/assets/151576407/34b219b7-5c54-4fd4-91b6-c4bc65c1e342">

textContent 라는 속성을 통해 text로 된 내용을 얻고  
이 text 를 다른 내용으로 지정하는 것을 보도록 하자!  
```
const boxEl = document.querySelector('.box');

// Getter, 값을 얻는 용도
// textContent 라는 속성을 통해 text로 된 내용이 반환되는 것.
console.log(boxEl.textContent); // Box!!

// Setter, 값을 지정하는 용도
// textContent 부분에 1 대신 Evelyn!을 넣겠다(지정하겠다).
boxEl.textContent = 'Evelyn!';
console.log(boxEl.textContent); // Evelyn!!
```
<img width="1192" alt="스크린샷 2024-02-09 오후 11 18 20" src="https://github.com/hyunji1117/everyday_study/assets/151576407/2e00e3e2-1e5a-4f81-9748-2cd9e5122d8c">








