# [JS] javascript 자바스크립트 변수, 예약어

## 변수  
저장된 데이터를 참조(사용)하는 용도로 데이터의 이름을 짓는 변수  
변수를 만들 수 있는 데이터 이름 (var, let, const)
```
특징 : 
- 저장된 변수는 재사용이 가능하다.
- let키워드를 통해 변수a를 명시 후 데이터'2'를 집어넣는 행위를 변수 선언 이라고 한다.
- 값(데이터) let으로 재할당 가능 (const 재할당 불가) **재할당 용으로 let을 쓰고, 이 외는 const를 사용한다.
```

```
let a = 2; // let키워드를 통해 변수a를 명시 후 데이터'2'를 집어넣는다.
let b = 5;

console.log(a+b); // 7
console.log(a-b); // -3
console.log(a*b); // 10
console.log(a/b); // 0.4

a = 5; // 변수의 데이터 재할당 가능!

console.log(a+b); // 10
console.log(a-b); // 0
console.log(a*b); // 25
console.log(a/b); // 1
```
![스크린샷 2024-01-30 오전 8 52 10](https://github.com/hyunji1117/everyday_study/assets/151576407/b5d2acce-6a1c-4641-89c1-286aa5ddf997)


## 예약어(Reserves Word)  
특별한 의미를 가지로 있어서, 변수와 함수의 이름으로는 사용할 수 없는 특정한 단어을 뜻 함.
```
let this = 'Hello :)'; // SyntaxError(문법에러) i.e.예약어를 사용하면 안되는데 사용했다는 뜻.
let if = 123; // SyntaxError
let break = true; // SyntaxError
```

이 처럼 예약이 되어져 있는 단어 (this, if, break)를 사용할 경우 문법에러가 뜨게 된다.  
사용할 수 없는 예약어의 종류들이 많아 에디터 도움으로 알아나가자.  

예약어 종류 [https://www.w3schools.com/js/js_reserved.asp﻿]
