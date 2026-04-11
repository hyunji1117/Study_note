HTML의 **데이터 속성(data-*)**은 표준에 정의되지 않은 사용자 정의 정보를 요소에 저장할 수 있게 해주는 아주 유용한 기능이다. 캡슐화와 의미론적 마크업을 중요시하는 현대 프론트엔드 개발에서 자주 활용된다. 

---

## 1. 개념 정의

### **데이터 속성 (Data Attributes)**
HTML5에서 도입된 기능으로, 특정 요소에 **비시맨틱(non-semantic)한 추가 정보**를 저장하기 위해 사용한다. `data-` 접두사 뒤에 원하는 이름을 붙여 선언하며, 브라우저의 렌더링에는 영향을 주지 않지만 자바스크립트나 CSS에서 접근이 가능하다.

---

## 2. 접근 및 활용 방식

| 구분 | 방법 | 예시 |
| :--- | :--- | :--- |
| **HTML 선언** | `data-이름` 형식으로 작성 | `<div data-user-id="77"></div>` |
| **JS 접근** | **`dataset`** 프로퍼티 사용 | `element.dataset.userId` (camelCase 변환) |
| **CSS 활용** | 속성 선택자 `[data-*]` 사용 | `div[data-status="active"] { ... }` |
| **CSS 표시** | `attr()` 함수 사용 | `div::after { content: attr(data-label); }` |

---

## 3. 심화 개념 보강

### **① 네이밍 규칙: kebab-case에서 camelCase로**
HTML은 대소문자를 구분하지 않기 때문에 하이픈(`-`)을 사용하는 kebab-case를 권장한다. 자바스크립트 엔진은 이를 읽어올 때 하이픈 뒤의 문자를 대문자로 바꾸는 **camelCase** 형식으로 자동 변환한다.
* `data-item-category` → `dataset.itemCategory`
* `data-is-valid` → `dataset.isValid`

### **② 데이터 속성 vs 데이터베이스/상태 관리**
데이터 속성은 편리하지만, 보안이 필요한 민감한 정보나 복잡한 객체 데이터를 담는 데는 적합하지 않다.
* **권장**: UI 상태 제어용 값(ID, 상태값, 필터링 키), CSS 스타일링 분기용.
* **비권장**: 사용자 비밀번호, 대규모 JSON 데이터(DOM이 무거워짐).

### **③ SEO와 접근성**
데이터 속성은 사용자에게 직접 노출되지 않으며 검색 엔진 최적화(SEO)에도 거의 영향을 주지 않습니다. 만약 스크린 리더가 읽어야 하는 중요한 정보라면 데이터 속성 대신 `aria-label` 같은 **WAI-ARIA** 속성을 사용하는 것이 올바른 접근성 준수 방법입니다.

---

## 4. 실전 활용 예시

### **① 이벤트에서 ID 꺼내기**
버튼이 100개여도 이벤트 리스너는 1개로 처리 가능하다. 클릭된 요소의 `dataset`에서 바로 값을 꺼내기 때문에 별도 변수나 배열이 필요 없다.

```html
<button data-user-id="77">삭제</button>

<script>
btn.addEventListener('click', (e) => {
  const id = e.target.dataset.userId  // "77"
  deleteUser(id)
})
</script>
```

### **② CSS 상태 연동 (쇼핑몰 품절 처리)**
JS는 상태값만 바꾸고, 화면 변화는 CSS가 자동으로 처리한다. JS가 직접 색상이나 스타일을 변경하는 코드를 짤 필요가 없다.

```html
<div class="product-card" data-status="soldout">...</div>

<style>
[data-status="soldout"] { opacity: 0.4; pointer-events: none; }
</style>

<script>
card.dataset.status = "soldout"  // 이것만 바꾸면 CSS가 자동 반응
</script>
```

### **③ 필터링/탭 구현**
클릭한 버튼의 `dataset.filter` 값과 카드의 `dataset.category`를 비교해 show/hide 처리한다.

```html
<button data-filter="book">책</button>
<button data-filter="food">음식</button>

<div data-category="book">...</div>
<div data-category="food">...</div>
```

---

## 5. 비표준 방식과의 비교

예전에는 `class="soldout"` 처럼 class로 상태를 표현하는 방식을 사용했다. 작동은 하지만 class가 많아질수록 **스타일용인지 상태값인지 구분이 불가**해진다.

```
// 비표준 (역할 혼재)
class="product-card soldout on-sale featured"

// data-* 표준 (역할 분리)
class="product-card"      ← 스타일 전용
data-status="soldout"     ← 상태/데이터 전용
```

`data-*`의 진짜 장점은 **성능이나 보안이 아니라 역할 분리와 가독성**이다.
- JS → 상태(데이터) 관리
- CSS → 화면 표현 관리

---

## 6. 보안 주의사항

`data-*`는 보안 도구가 아니다. HTML에 선언된 모든 값은 브라우저 개발자도구에서 그대로 노출된다. 비표준 방식(`class`, `id` 남용)이든 표준 `data-*`든 **보안 수준은 동일**하다.

| 저장 위치 | 노출 여부 |
| :--- | :--- |
| `data-*` 속성 | 개발자도구에서 노출 ❌ |
| JS 변수 | 개발자도구 콘솔에서 접근 가능 ❌ |
| `localStorage` | 개발자도구에서 열람 가능 ❌ |
| 서버 DB | 직접 접근 불가 ✅ |
| `HttpOnly` 쿠키 | JS 접근 차단 ✅ |

민감한 정보(비밀번호, 토큰 등)는 서버에 두고 필요할 때 API로 가져오는 것이 올바른 방식이다.