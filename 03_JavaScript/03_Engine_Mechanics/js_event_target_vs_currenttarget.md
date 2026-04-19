## 1. 개념 정의

### **event.target (실제 발생지)**
이벤트가 **처음으로 발생한 가장 깊은 요소**를 가리킵니다. 버블링이 진행되어도 이 값은 변하지 않고 처음 이벤트를 촉발시킨 '주인공'을 계속 유지한다.

### **event.currentTarget (리스너 소유자)**
현재 **이벤트 핸들러가 실제로 부착된 요소**를 가리킨다. 이벤트가 버블링되어 상위 요소의 핸들러가 실행될 때마다, 해당 핸들러가 붙어 있는 그 요소를 가리키게 된다. (참고: 함수 내부에서 `this`와 동일한 값을 가집니다.)

---

## 2. 비교 분석

| 구분 | event.target | event.currentTarget |
| :--- | :--- | :--- |
| **의미** | 이벤트가 **시작된** 곳 (Origin) | 이벤트 핸들러가 **등록된** 곳 (Owner) |
| **변화 여부** | 전파 과정 내내 일정함 | 핸들러가 실행되는 위치에 따라 변함 |
| **주요 용도** | 클릭된 구체적인 자식 요소 식별 | 이벤트 위임 시 부모 요소의 데이터 접근 |
| **비유** | 사고를 낸 **범인** | 신고를 접수한 **경찰서** |

---

## 3. 실무 예시 및 활용 전략

### **① 이벤트 위임에서의 활용**
리스트(`ul`)에 이벤트를 하나만 걸고 클릭된 항목(`li`)을 찾을 때 유용하다. 
* `event.currentTarget`: 항상 `ul`을 가리킵니다.
* `event.target`: 실제 클릭된 `li` 또는 그 안의 `span` 등을 가리킨다.

### **② 버그 예방: `closest()`와의 조합**
`event.target`은 사용자가 클릭한 가장 구체적인 요소를 집어낸다. 만약 버튼 안에 아이콘(`<i>`)이 있고 사용자가 아이콘을 클릭했다면 `target`은 `<i>`가 된다. 이때 버튼의 데이터가 필요하다면 아래와 같이 조합하는 것이 실무 팁이다.

```javascript
const handleClick = (event) => {
  // target이 무엇이든 상관없이, 가장 가까운 button 요소를 찾아줌
  const button = event.target.closest('button');
  
  // currentTarget은 리스너가 걸린 '부모'를 확정적으로 가리킴
  const parent = event.currentTarget; 
};
```

---

## 4. 실전 활용 예시

### **① 이벤트 위임 — 리스트 아이템 클릭 처리**
`li`가 100개여도 이벤트 리스너는 `ul` 하나로 처리한다. `event.target`으로 실제 클릭된 항목을 구분하고, `event.currentTarget`으로 부모 컨테이너의 데이터에 접근한다.

```html
<ul id="menu" data-section="nav">
  <li data-id="1">홈</li>
  <li data-id="2">소개</li>
  <li data-id="3">연락처</li>
</ul>
```

```js
document.querySelector('#menu').addEventListener('click', (e) => {
  // currentTarget → 항상 #menu (리스너가 붙은 곳)
  const section = e.currentTarget.dataset.section  // "nav"

  // target → 실제 클릭된 li
  const itemId = e.target.dataset.id               // "1", "2", "3" 중 하나
  console.log(`${section} > item ${itemId} 클릭`)
})
```

### **② closest()로 아이콘 클릭 오탐 방지**
버튼 안에 `<svg>` 아이콘이 있으면 아이콘을 클릭했을 때 `target`이 `<svg>`나 `<path>`가 된다. `closest()`로 의도한 버튼을 명확히 잡는다.

```html
<button class="delete-btn" data-user-id="42">
  <svg>...</svg>
  삭제
</button>
```

```js
document.addEventListener('click', (e) => {
  const btn = e.target.closest('.delete-btn')
  if (!btn) return  // 버튼 외 클릭은 무시

  // e.target은 svg 또는 path일 수 있지만
  // btn은 항상 .delete-btn을 보장함
  const userId = btn.dataset.userId  // "42"
  deleteUser(userId)
})
```

### **③ 모달 외부 클릭으로 닫기**
`target`과 `currentTarget`이 같을 때(= 오버레이 자체를 클릭했을 때)만 닫도록 처리한다. 모달 내부를 클릭하면 버블링이 올라오지만 두 값이 달라지므로 닫히지 않는다.

```html
<div id="overlay">
  <div id="modal">
    <p>모달 내용</p>
  </div>
</div>
```

```js
document.querySelector('#overlay').addEventListener('click', (e) => {
  // target === currentTarget → 오버레이 직접 클릭 (모달 외부)
  if (e.target === e.currentTarget) {
    closeModal()
  }
  // 모달 내부 클릭 시 → target은 p 또는 #modal, currentTarget은 #overlay
  // → 조건 불충족, 닫히지 않음
})
```

---

## 5. 기존 방식과의 비교

`target` / `currentTarget` 구분 없이 짜면 생기는 문제와 이를 올바르게 활용했을 때를 비교한다.

```js
// 잘못된 방식 — 각 li마다 리스너를 개별 등록
document.querySelectorAll('li').forEach(li => {
  li.addEventListener('click', (e) => {
    highlight(e.target)   // li가 100개면 리스너도 100개 생성
  })
})

// 올바른 방식 — 부모에 리스너 하나만 등록 (이벤트 위임)
document.querySelector('ul').addEventListener('click', (e) => {
  if (e.target.tagName === 'LI') {
    highlight(e.target)       // 클릭된 li
    console.log(e.currentTarget)  // 리스너가 등록된 ul
  }
})
```

| 비교 항목 | 개별 등록 방식 | 이벤트 위임 방식 |
| :--- | :--- | :--- |
| **리스너 개수** | 요소 수만큼 생성 | 1개 |
| **동적 요소 대응** | 새 요소에 별도 등록 필요 | 자동 처리 |
| **메모리 효율** | 요소 증가 시 비례해서 증가 | 일정 |
| **target 활용** | 불필요 | 클릭 대상 식별에 핵심 |

---

## 6. 주의사항 및 한계

### **① 화살표 함수에서 `this`는 currentTarget이 아니다**
`currentTarget`과 `this`는 일반 함수에서만 같다. 화살표 함수는 외부 컨텍스트의 `this`를 물려받으므로 예상과 다른 값이 나온다.

```js
// 일반 함수 — this === event.currentTarget (동일)
el.addEventListener('click', function(e) {
  console.log(this === e.currentTarget)  // true
})

// 화살표 함수 — this는 외부 스코프 (다를 수 있음)
el.addEventListener('click', (e) => {
  console.log(this === e.currentTarget)  // false (this는 window 또는 상위 컨텍스트)
  // this 대신 e.currentTarget을 명시적으로 사용하는 것이 안전함
})
```

### **② stopPropagation()은 target을 바꾸지 않는다**
버블링을 막아도 `event.target`은 여전히 원래 발생 요소를 가리킨다. 전파를 막은 것이지 target을 리셋한 게 아니다.

```js
inner.addEventListener('click', (e) => {
  e.stopPropagation()  // 버블링 중단
  // e.target은 여전히 inner — 값이 바뀌지 않음
})

outer.addEventListener('click', (e) => {
  // stopPropagation 덕분에 이 핸들러는 아예 실행되지 않음
  // currentTarget이 outer가 될 기회 자체가 없어짐
})
```

### **③ 이벤트 핸들러 밖에서 currentTarget은 null이다**
`currentTarget`은 핸들러가 실행되는 동안에만 유효한 값이다. 비동기 콜백에서 참조하면 이미 `null`이 되어 있다.

```js
el.addEventListener('click', (e) => {
  const target = e.currentTarget  // 여기서 저장해두어야 함

  setTimeout(() => {
    console.log(e.currentTarget)  // null — 핸들러 실행 종료 후 초기화됨
    console.log(target)           // el — 미리 변수에 담아두면 안전
  }, 100)
})
```

**`event.target`은 이벤트의 출발지, `event.currentTarget`은 리스너의 위치다. 이벤트 위임 패턴에서 이 둘을 명확히 구분하는 것이 버그 없는 DOM 이벤트 처리의 핵심이다.**