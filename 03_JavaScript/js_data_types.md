# Javascript 자바스크립트 데이터 종류(자료형)

## String (문자 데이터)  
따옴표 사용 (쌍따옴표, 홑따옴표, 빽틱)

```
let myName = "Evelyn"; // myName이라는 변수에 "Evelyn"이라는 문자 데이터를 할당 한다.
let email = 'hj5678@gmail.com'; // 작은 따옴표로 표시된 문자 데이터도 동일하게 할당 한다.
let hello = `Helllo ${myName}!!`; // 빽틱 기호로 myName라는 데이터를 보관하겠다는 의미이다. i.e. "Evelyn"이라는 문자가 ${myName}에 들어가는 개념이다.

console.log(myName); // Evelyn
console.log(email); // hj5678@gmail.com
console.log(hello); // Hello Evelyn!!
```
<img width="691" alt="스크린샷 2024-01-29 오후 8 29 27" src="https://github.com/hyunji1117/everyday_study/assets/151576407/7630e682-cc33-4532-a34f-5c6ba01d64bf">


## Number (숫자 데이터)  
정수 및 부동 소수점 숫자
```
let number = 123;
let opacoty = 1.37;

console.log(number); // 123
console.log(opacity); // 1.37
```
<img width="691" alt="스크린샷 2024-01-29 오후 8 42 39" src="https://github.com/hyunji1117/everyday_study/assets/151576407/8e21b96d-ea97-4e49-b69c-1ff68fff0178">


## Boolean(불린 데이터)  
true, false 값으로 이뤄진 논리 데이터
```
let checked = true;
let isShow = false;

console.log(checked); // true
console.log(isShow); // false
```
<img width="691" alt="스크린샷 2024-01-29 오후 8 47 32" src="https://github.com/hyunji1117/everyday_study/assets/151576407/bea4504b-2c60-4078-a285-1fbc1655b495">


## Undefined  
값이 지정되지 않은 상태 (할당되지 않음)
자바스크립트 만의 특이한 문법이다. 
```
let undef;
let obj = { abc: 123 }; // (object의 약어 obj) (숫자 데이터123을 속성abc에 할당한다. => i.e. 데이터의 집합, 객체 데이터라고 한다.)

console.log(undef); // undefined
console.log(obj.abc); // 123 (obj변수 내부로 들어가 abc속성 데이터를 접근하여 그 값이 무엇인가 확인하는 코드)
console.log(obj.xyz); // undifined
```
<img width="690" alt="스크린샷 2024-01-29 오후 8 55 33" src="https://github.com/hyunji1117/everyday_study/assets/151576407/d2f4cc20-91df-4a68-b9db-625d8a565211">


## Null  
어떤 값이 의도적으로 비어있음을 의미
```
let empty = null; // i.e. 비어있는 값 임을 명시한 것이다.

console.log(empty); // null
```
![스크린샷 2024-01-30 오전 7 22 55](https://github.com/hyunji1117/everyday_study/assets/151576407/84a3ff60-b960-466e-a0fc-4b661022c769)

## Object(객체 데이터)  
key: value 형식으로 저장하는 {데이터의 집합}
```
let user = {
  name: 'Evelyn',
  age: 22,
  isValid: true //boolean 데이터 true가 들어가 있음
};

console.log(user.name); // Evelyn
console.log(user.age); // 22
console.log(user.isValid); // true
```
![스크린샷 2024-01-30 오전 7 33 27](https://github.com/hyunji1117/everyday_study/assets/151576407/c385a488-fcf5-4e87-b1c3-d905a988945a)

## Array(배열 데이터)  
[데이터를] 순차적으로 저장
```
let name = ['Kate', 'Daniel', 'Anna'];

console.log(name[0]); // 'Kate'
console.log(name[1]); // 'Daniel'
console.log(name[2]); // 'Anna'
```
![스크린샷 2024-01-30 오전 7 49 28](https://github.com/hyunji1117/everyday_study/assets/151576407/5486a339-cf1e-4436-9b5c-da712ea82305)
