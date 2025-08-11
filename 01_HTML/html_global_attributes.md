[HTML] 전역 속성

전역 속성이란? 
Html body의 전체 영역에서 모두 사용할 수 있는 속성을 뜻한다. 

1. <태그 title="설명"></태그>
전체 영역에서 설명을 명시하는 속성

2. <태그 style="스타일"></태그>
요소에 적용할 스타일 을 지정하는 것

3. <태그 class="이름"></태그>
Css, Js 정확히 짚어서 제어하기 위한 속성. 중복가능한 이름이다. 

4. <태그 id="이름"></태그
class와 달리 중복해서 사용하면 안 된다. 핵심적인 요소에 이름을 부여할 때 사용하자.

5. <태그 data-이름="데이터(문자 데이터)"></태그**(난이도 있음)
해당 속성은 '태그' 소속된 요소에 데이터를 잠시 저장하게 된다. 
이는 향후 Css 또는 Js에서 사용하게 된다. 

Html에 저장된 데이터를 Js에서 어떻게 활용할 수 있을까?

[HTML]
<div data-animal-name="bear">곰</div>
<div data-animal-name="tiger">호랑이</div>

[JS]
const els = document.querySelectorAll('div') /*html 데이터에서 querySelector를 통해 div 찾기*/
els.forEach(el => { /*그 데이터를 잠시 els에 담아두고, 해당 데이터를 각각 반복해서 */
	console.log(el.dataset.animalName) /*dataset 영역에 animal-name 해당되는 데이터를 콘솔창에 기록을 남긴다.*/
})

/*
먼저 그릇을 만들자
이 그릇의 이름은 element의 약어로 els로 짓겠다. 
여기에 어떤 값을 할당할 것이다. (=부분)
document, 즉 html 구조에서
querySelectorAll, query selector를 통해 모든 요소를 찾을 것이다.
그리고 우리가 찾을 요소는 div 태그이다. 
------> 여기서 찾은 값은 els라는 그릇에 담아서 다음줄에 활용한다. 

그릇에 담겨졌던 요소들을 하나씩 반복해서 데이터를 처리할 것이다. 
이 반복되는 각각의 내요은 el이라는 별도의 그릇에 담아서 내부에서 사용하겠다고 선언한다. 
그리고 console창에
el 그릇에 담겨 있는 dataset을 추출하는 개념에서 사전에 저장한 html에 작성한 animal-name 데이터를 넣는다.
*/

해당 코드를 vscode에 출력 시 오류가 발생할 수 있어
js를 html에 연결할 때 아래와 같이 defer를 추가하여 코드를 입력하면 js가 html 전체 코드를 읽으면서 오류가 해결된다. 

<script defer src="/js/main.js"></script>
