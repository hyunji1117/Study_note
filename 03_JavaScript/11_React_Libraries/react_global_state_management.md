## 1. 개념 정의

### **전역 상태 관리 라이브러리**
애플리케이션 전체에서 공유해야 하는 데이터(상태)를 특정 컴포넌트에 종속시키지 않고, **중앙 저장소(Store)**에서 관리하도록 돕는 도구이다.

* **Prop Drilling**: 부모에서 자식으로 데이터를 전달하기 위해 중간 컴포넌트들이 단순히 전달자 역할만 수행하며 복잡해지는 현상이다.
* **중앙 집중화**: 상태와 그 상태를 변경하는 로직을 한곳에 모아 관리함으로써 데이터 흐름을 예측 가능하게 만든다.

---

## 2. 사용 이유 (장점)

| 구분 | 주요 내용 | 기대 효과 |
| :--- | :--- | :--- |
| **상태 공유의 용이성** | 중앙 저장소를 통해 어느 컴포넌트에서든 즉시 상태에 접근 가능 | **Prop Drilling** 문제 해결 및 코드 간결화 |
| **관심사 분리** | 상태 변경 로직(Reducer 등)을 컴포넌트 외부로 분리 | 컴포넌트는 UI 렌더링에만 집중하여 **유지보수성** 향상 |
| **성능 최적화** | 상태 변화를 감지하여 필요한 컴포넌트만 선택적으로 업데이트 | 불필요한 전체 리렌더링 방지 및 앱 성능 개선 |
| **디버깅 및 테스트** | 상태 변화 이력을 추적하거나 독립적인 로직 테스트 가능 | 데이터 흐름의 투명성 확보 및 안정성 강화 |

---

## 3. 심화 개념 보강: 도입 시 주의사항 (Over-engineering)

라이브러리 도입이 항상 정답은 아닙니다. 프로젝트의 성격에 맞는 전략적 선택이 필요하다.

* **오버엔지니어링 경계**: 단순한 구조의 프로젝트에 복잡한 라이브러리를 도입하면 오히려 개발 생산성이 저하될 수 있다.
* **React 내장 기능 활용**: `useState`와 `useContext`만으로도 충분히 해결 가능한 범위인지 먼저 검토해야 한다.
* **도입 시점**: 컴포넌트 깊이가 깊어지거나, 다수의 컴포넌트가 동일한 데이터를 실시간으로 공유해야 하는 등 **실질적인 필요성**이 느껴질 때 도입하는 것이 바람직하다.

---

## 4. 실전 활용 예시

### **① Zustand — 전역 모달 상태 관리**
어느 컴포넌트에서나 모달을 열고 닫아야 할 때 Zustand로 전역 store를 만든다. props 없이 어디서든 직접 상태를 읽고 변경할 수 있다.

```js
// store/useModalStore.js
import { create } from 'zustand'

const useModalStore = create((set) => ({
  isOpen: false,
  content: null,
  open: (content) => set({ isOpen: true, content }),
  close: () => set({ isOpen: false, content: null }),
}))

export default useModalStore

// 헤더 컴포넌트 — 모달 열기
function Header() {
  const open = useModalStore((state) => state.open)
  return <button onClick={() => open(<LoginForm />)}>로그인</button>
}

// 모달 컴포넌트 — 상태 구독
function Modal() {
  const { isOpen, content, close } = useModalStore()
  if (!isOpen) return null
  return <div onClick={close}>{content}</div>
}
```

### **② Redux Toolkit — 장바구니 슬라이스**
Redux Toolkit의 `createSlice`는 액션과 리듀서를 한 파일에 선언한다. 기존 Redux의 boilerplate(액션 타입 상수, 액션 생성자 분리)가 대폭 줄었다.

```js
// store/cartSlice.js
import { createSlice } from '@reduxjs/toolkit'

const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [], total: 0 },
  reducers: {
    addItem: (state, action) => {
      state.items.push(action.payload)         // Immer 덕분에 직접 변경처럼 작성 가능
      state.total += action.payload.price
    },
    removeItem: (state, action) => {
      state.items = state.items.filter(i => i.id !== action.payload)
    },
  },
})

export const { addItem, removeItem } = cartSlice.actions
export default cartSlice.reducer

// 컴포넌트에서 사용
function ProductCard({ product }) {
  const dispatch = useDispatch()
  return <button onClick={() => dispatch(addItem(product))}>담기</button>
}
```

### **③ Context API — 테마/언어처럼 변화 빈도가 낮은 전역값**
자주 바뀌지 않는 값(다크모드, 언어 설정)은 Context API로 충분하다. 라이브러리 없이 React 내장 기능만 사용한다.

```js
// context/ThemeContext.js
const ThemeContext = createContext()

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light')
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

export const useTheme = () => useContext(ThemeContext)

// 어떤 컴포넌트에서든 바로 사용
function Button() {
  const { theme } = useTheme()
  return <button className={theme}>클릭</button>
}
```

---

## 5. 라이브러리 비교

상태 변경 빈도와 앱 규모에 따라 선택 기준이 달라진다.

| 비교 항목 | Context API | Zustand | Redux Toolkit |
| :--- | :--- | :--- | :--- |
| **설치 필요 여부** | 없음 (React 내장) | 필요 | 필요 |
| **보일러플레이트** | 적음 | 매우 적음 | 중간 |
| **상태 변경 빈도** | 낮음에 최적 | 높음에도 적합 | 높음에 적합 |
| **DevTools 지원** | 없음 | 기본 제공 | Redux DevTools |
| **비동기 처리** | 직접 구현 필요 | 직접 구현 필요 | RTK Query 내장 |
| **적합한 규모** | 소규모 | 소~중규모 | 중~대규모 |

```
// 선택 기준 요약
변경 빈도 낮고 소규모     →  Context API
빠른 개발, 중규모 앱     →  Zustand
대규모, 팀 협업, DevTools 중요  →  Redux Toolkit
서버 상태 포함           →  React Query / RTK Query 병행
```

---

## 6. 주의사항 및 한계

### **① 전역 상태 남용 — 모든 상태를 store에 넣지 않는다**
form 입력값, hover 여부, 특정 컴포넌트 내부 토글 같은 **로컬 UI 상태**는 전역 store에 두면 오히려 복잡해진다.

```js
// 잘못된 방식 — 로컬 상태를 전역 store에 저장
const useStore = create((set) => ({
  inputValue: '',         // ← 이건 로컬 상태로 충분함
  isDropdownOpen: false,  // ← 이것도 마찬가지
  setInputValue: (v) => set({ inputValue: v }),
}))

// 올바른 방식 — 컴포넌트 내부에서 useState로 처리
function SearchBar() {
  const [inputValue, setInputValue] = useState('')  // 컴포넌트 안에서 끝냄
  return <input value={inputValue} onChange={e => setInputValue(e.target.value)} />
}
```

### **② 불필요한 리렌더링 — selector를 좁게 구독한다**
store 전체를 구독하면 관련 없는 상태가 바뀔 때도 리렌더링이 발생한다.

```js
// 잘못된 방식 — store 전체를 구독
const store = useStore()           // store 안의 무엇이 바뀌든 리렌더링

// 올바른 방식 — 필요한 값만 selector로 선택
const count = useStore((state) => state.count)    // count가 바뀔 때만 리렌더링
const open = useStore((state) => state.open)      // open이 바뀔 때만 리렌더링
```

### **③ 서버 상태와 클라이언트 상태를 분리한다**
API에서 가져온 데이터(서버 상태)를 Redux/Zustand에 직접 저장하면 캐싱, 갱신, 로딩 처리를 모두 직접 구현해야 한다. React Query나 RTK Query 같은 서버 상태 전용 도구와 역할을 나누는 것이 올바른 구조다.

```
// 책임 분리 기준
전역 상태 라이브러리 (Zustand / Redux)
  → UI 상태: 로그인 여부, 테마, 모달 열림 상태, 장바구니

서버 상태 라이브러리 (React Query / RTK Query)
  → 서버 데이터: 게시글 목록, 유저 프로필, 상품 재고
```

**전역 상태 라이브러리는 클라이언트 UI 상태 관리에 집중하고, 서버 데이터는 전용 도구에 맡기는 것이 유지보수하기 쉬운 구조다.**