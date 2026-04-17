## 1. 개념 정의

### **Node (노드)**
DOM 트리에서 **가장 기초적인 단위**이자 부모 인터페이스입니다. HTML 문서의 모든 것(태그, 텍스트, 주석 등)은 노드라는 이름 아래 하나로 묶이다.
* **주요 타입**: Element Node, Text Node, Comment Node, Document Node 등.

### **Element (요소)**
Node를 상속받은 **특정 타입의 노드**로, HTML 태그(`<p>`, `<div>` 등)로 직접 표현되는 것들을 말합니다. 모든 Element는 Node이지만, 모든 Node가 Element인 것은 아니다.



---

## 2. 비교 분석: 속성 및 메서드 차이

| 구분 | Node | Element |
| :--- | :--- | :--- |
| **포함 범위** | 태그, 텍스트, 주석, 줄바꿈 포함 | **오직 HTML 태그**만 포함 |
| **자식 탐색** | **`childNodes`**: 모든 노드 반환 | **`children`**: HTML 요소만 반환 |
| **데이터 접근** | `textContent`: 모든 텍스트 추출 | `innerHTML`: HTML 마크업 포함/조작 |
| **이동 관련** | `firstChild`, `nextSibling` | `firstElementChild`, `nextElementSibling` |
| **속성(Attribute)** | 가질 수 없음 | `id`, `class`, `style` 등 조작 가능 |

---

## 3. 심화 개념 보강: 실무 예시

### **① 공백과 줄바꿈의 함정**
HTML 코드 작성 시 태그 사이의 줄바꿈이나 공백은 DOM에서 **Text Node**로 취급된다. 
* `childNodes`를 사용하면 예상치 못한 빈 텍스트 노드가 포함되어 인덱스 계산이 틀릴 수 있다.
* 실무에서 순수하게 HTML 태그만 다루고 싶다면 `children`을 사용하는 것이 훨씬 안전하다.

### **② 컬렉션의 차이 (NodeList vs HTMLCollection)**
* **`childNodes`**가 반환하는 **NodeList**는 대개 정적(Static)이지만, 일부 경우 라이브(Live)로 동작하며 `forEach` 메서드를 지원한다.
* **`children`**이 반환하는 **HTMLCollection**은 항상 라이브(Live) 상태이며, DOM이 변하면 즉시 반영되지만 `forEach`를 바로 쓸 수 없어 배열로 변환 작업이 필요할 수 있다.

---

## 4. 실전 활용 예시

### **① children으로 탭 메뉴 순회**
탭 버튼들을 감싼 컨테이너에서 HTML 요소만 골라내야 할 때 `children`을 쓴다. `childNodes`를 쓰면 줄바꿈 텍스트 노드까지 포함되어 인덱스가 어긋난다.

```js
const tabList = document.querySelector('.tab-list')

// children — HTML 요소만 반환 (텍스트 노드 제외)
Array.from(tabList.children).forEach((tab, index) => {
  tab.addEventListener('click', () => activateTab(index))
})

// childNodes를 쓰면 아래처럼 텍스트 노드가 섞임
// tabList.childNodes → [text, button, text, button, text, ...]
//                         ↑ 줄바꿈 공백이 text 노드로 포함됨
```

### **② textContent vs innerHTML 선택 기준**
Node의 `textContent`는 HTML 태그를 무시하고 순수 텍스트만 다룬다. 사용자 입력을 DOM에 넣을 때 XSS를 막는 가장 간단한 방법이다.

```js
const el = document.querySelector('.comment')

// 사용자 입력 표시 — textContent 사용 (XSS 방어)
el.textContent = userInput
// '<script>alert(1)</script>' → 그대로 문자열로 표시됨 (실행 안 됨)

// 신뢰할 수 있는 내부 HTML 삽입 — innerHTML 사용
el.innerHTML = '<strong>공지사항</strong>입니다.'
// HTML 태그가 파싱되어 실제 볼드 처리됨
```

### **③ nextElementSibling으로 인접 요소 제어**
폼 필드 바로 다음 에러 메시지 요소를 찾을 때, `nextSibling`은 텍스트 노드를 반환할 수 있어 `nextElementSibling`이 안전하다.

```html
<input id="email" type="email" />
<span class="error-msg">이메일 형식이 올바르지 않습니다.</span>
```

```js
const input = document.querySelector('#email')

// nextSibling — 줄바꿈 텍스트 노드가 반환될 수 있음
input.nextSibling          // → Text Node ('\n  ')

// nextElementSibling — 반드시 HTML 요소만 반환
input.nextElementSibling   // → <span class="error-msg">
input.nextElementSibling.style.display = 'block'
```

---

## 5. 기존 방식과의 비교

Node 기반 API(`childNodes`, `firstChild`)와 Element 기반 API(`children`, `firstElementChild`)는 혼용하면 버그가 생긴다.

```
// HTML 구조
<ul>
  <li>첫 번째</li>
  <li>두 번째</li>
</ul>
```

```js
const ul = document.querySelector('ul')

// Node 기반 — 텍스트 노드 포함
ul.childNodes         // NodeList [text, li, text, li, text]  (길이 5)
ul.firstChild         // Text Node (줄바꿈)
ul.childNodes[1]      // <li>첫 번째</li>  (인덱스 1이 실제 첫 번째 태그)

// Element 기반 — HTML 요소만
ul.children           // HTMLCollection [li, li]  (길이 2)
ul.firstElementChild  // <li>첫 번째</li>  (인덱스 0이 첫 번째 태그)
```

| 목적 | 쓸 API | 이유 |
| :--- | :--- | :--- |
| HTML 요소 순회 | `children`, `firstElementChild` | 텍스트/주석 노드 제외됨 |
| 순수 텍스트 추출 | `textContent` | 태그 무관하게 모든 텍스트 반환 |
| 노드 타입 직접 확인 필요 | `childNodes`, `nodeType` | 텍스트·주석 노드까지 처리해야 할 때 |

---

## 6. 주의사항 및 한계

### **① nodeType으로 타입을 직접 확인하지 않으면 오류가 발생한다**
`childNodes`로 받은 목록을 그냥 순회하면 텍스트 노드나 주석 노드에서 Element 전용 메서드를 호출하다 에러가 난다.

```js
ul.childNodes.forEach(node => {
  // 잘못된 방식 — 텍스트 노드에는 classList가 없음
  node.classList.add('active')  // ← TypeError 발생 가능

  // 올바른 방식 — Element 노드일 때만 처리
  if (node.nodeType === Node.ELEMENT_NODE) {
    node.classList.add('active')
  }
})

// nodeType 상수
// Node.ELEMENT_NODE  → 1
// Node.TEXT_NODE     → 3
// Node.COMMENT_NODE  → 8
```

### **② innerHTML은 기존 이벤트 리스너를 모두 제거한다**
`innerHTML`로 자식 요소를 교체하면 기존에 `addEventListener`로 등록된 리스너가 전부 사라진다. 동적으로 생성된 요소에 이벤트를 붙였다가 갑자기 동작하지 않는 버그의 주된 원인이다.

```js
// 잘못된 방식 — innerHTML 재할당으로 리스너 소멸
container.innerHTML += '<li>새 항목</li>'  // 기존 li의 이벤트 리스너 모두 삭제

// 올바른 방식 — appendChild로 기존 DOM 유지
const li = document.createElement('li')
li.textContent = '새 항목'
container.appendChild(li)
```

### **③ HTMLCollection은 live 상태라 반복 중 DOM을 변경하면 무한 루프가 생긴다**
`children`이 반환하는 HTMLCollection은 DOM이 바뀌면 즉시 반영된다. 순회 중에 요소를 추가·삭제하면 컬렉션 길이가 변해 예기치 않은 동작이 발생한다.

```js
const items = ul.children  // HTMLCollection (live)

// 잘못된 방식 — 순회 중 DOM 변경으로 무한 루프 위험
for (let i = 0; i < items.length; i++) {
  ul.appendChild(items[i].cloneNode(true))  // 추가할수록 items.length도 늘어남
}

// 올바른 방식 — 배열로 변환해 static 스냅샷으로 처리
Array.from(ul.children).forEach(item => {
  ul.appendChild(item.cloneNode(true))
})
```

**Node는 DOM의 모든 것을 다루는 기반 타입이고, Element는 HTML 태그만 다루는 실무 타입이다. 대부분의 DOM 조작은 Element API를 쓰는 것이 안전하다.**