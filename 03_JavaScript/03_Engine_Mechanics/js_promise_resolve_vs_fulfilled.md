## 1. 개념 정의

### **resolve() (동작/함수)**

`Promise` 생성자 내부에서 호출되는 **콜백 함수**이다. 비동기 작업이 성공적으로 마쳤음을 자바스크립트 엔진에 알리는 '신호탄' 역할을 하며, 작업의 결과물을 인자로 전달한다.

### **fulfilled (상태)**

`Promise`가 가질 수 있는 **세 가지 상태(State)** 중 하나이다. `resolve()`가 호출되는 순간, `Promise` 객체는 `pending`(대기)에서 `fulfilled`(이행) 상태로 영구적으로 전환된다.

---

## 2. 비교 분석: 함수 vs 상태

| 구분 | resolve() | fulfilled |
| --- | --- | --- |
| **성격** | 실행 가능한 **함수 (Method)** | Promise의 **상태 (State)** |
| **역할** | 상태를 변경시키는 **트리거 (Trigger)** | 성공적으로 완료된 **결과값 (Status)** |
| **시점** | 비동기 로직이 성공한 직후 호출 | `resolve()` 호출에 의해 상태가 확정된 후 |
| **연결 메서드** | `.then()`의 첫 번째 인자로 값 전달 | `.then()` 핸들러가 실행되는 조건 |

---

## 3. 심화 개념 보강

### **① Promise의 불변성 (Settled)**

`Promise` 상태는 한 번 `fulfilled`(이행) 또는 `rejected`(거부)가 되면 다시는 변하지 않는다. 이를 **Settled(확정)** 상태라고 한다. 만약 `resolve()`를 호출한 뒤 바로 아래 줄에서 `reject()`를 호출하더라도, 이미 `fulfilled`가 된 `Promise`는 꿈쩍도 하지 않는다.

### **② resolve()에 따른 후속 처리 (Microtask Queue)**

`resolve()`가 호출되어 상태가 `fulfilled`로 변하면, 등록된 `.then()` 콜백은 자바스크립트 엔진의 **Microtask Queue**에 담긴다. 이는 일반적인 `setTimeout` 같은 Task보다 우선순위가 높아 더 빠르게 실행된다.

### **③ resolve에 또 다른 Promise가 전달될 때**

흥미로운 점은 `resolve(otherPromise)`처럼 또 다른 `Promise`를 인자로 넘길 수도 있다는 것이다. 이 경우 현재 `Promise`는 즉시 `fulfilled`가 되지 않고, 넘겨받은 `otherPromise`가 완료될 때까지 기다렸다가 그 결과에 따라 자신의 상태를 결정한다.