# [JS] javascript 자바스크립트 함수  

## 함수(function)
자바스크립트로 만들 수 있는 여러가지 특정 동작/기능들을 실제로 실행할 수 있는 코드의 집합이다.  
i.e. 명령들을 감싸고 있는 집합을 뜻한다. 그리고 프로그래밍은 거의 함수로 이루어져 있다.  
```
function helloEve(){ // 함수 선언할 때는 function 키워드 명시. 그리고 원하는 함수 이름'helloEve' 작성. (소괄호 1set){중괄호 1set} 기호 사용. => 코드들의 집합
  // 실행 코드 (코드 내용)
  console.log(123); // {중괄호 1set} 사이에 명령 코드를 넣는다. i.e. 여기에서는 console창에 log를 남기고, 그 데이터는 숫자 123 임을 명시하는 것이다. => 코드 내용
};

// 함수 호출해서 실행
helloEve(); // 123
```

### 반환
함수 내에서 return 함수를 사용하여 자바스크립트 데이터를 함수 밖으로 내보내는 것.  
그리고 내보내진 함수를 새로운 변수에 할당해서 추가적으로 사용할 수 있다.  
```
function returnAge() {
  return 38;
};

let a = returnAge(); // 반환된 데이터'123'을 키워드let을 사용하는 함수a가 받아서 returnEve함수가
		    //호출되면 (호출을 하면 실행이 되어야 한다.)
console.log(a); // 함수에서 반환된 123 출력
```
<img width="685" alt="스크린샷 2024-02-02 오전 8 19 22" src="https://github.com/hyunji1117/everyday_study/assets/151576407/20647d00-e5cb-4939-b9d2-9d1dd4d92caa">

함수가 호출되는 부분 sum(7, 4)에서 데이터를 집어넣고  
데이터를 받아줄 변수 sum(a, b)  
```
// 함수 선언
function sum(a,b) { // (2-1) 이 함수 내에서 사용하는 변수를 각각 a, b 이름으로 정의하였는데, 이 변수를 매개변수(Parameters)하고 한다. 
  return a+b; // (2-2) 내부 처리 및 함수 실행을 통해 밖으로 내보내 진다. 
};

// 재사용
let a = sum(7,4); // (1) 데이터 인수들을 함수가 받아 (3) 그 값을 변수a에 담아 밖으로 내보낸다. **7과 4는 매개변수를 받는 인수(Arguments)라고 한다. 
let b = sum(6,3);
let c = sum(2,4);

console.log(a,b,c); // (4) 변수 a,b,c 출력 > 11,9,6
```
<img width="686" alt="스크린샷 2024-02-02 오전 8 54 30" src="https://github.com/hyunji1117/everyday_study/assets/151576407/965a0b1d-0946-4b35-9620-b63393ed0ce8">  

### 기명 함수
이름이 있는 함수를 '기명 함수'라고 한다.  
```
// 함수를 선언하는 것
function Evelyn(){  // 함수 이름('Evelyn'부분)에는 원하는 이름을 넣어주면 된다.
  console.log('Evelyn!');
};

// 함수를 호출하는 것
Evelyn();
```

### 익명 함수
이름이 없는 함수는 '익명 함수'라고 한다.  
이러한 익명 함수들은 데이터로써 활용되거나 변수(예시 name과같은)에 할당되어서 활용되기도 한다.  
```
// 함수를 표현하는 것
let name = function (){ // 해당 function = 익명 함수
  console.log('What is your name?'); 
};

// 함수를 호출하는 것
name();
```
<img width="691" alt="스크린샷 2024-02-03 오후 8 52 31" src="https://github.com/hyunji1117/everyday_study/assets/151576407/b5e2d63a-964e-4856-a5f8-589f3e1a4561">

### 객체 데이터
'name', 'age'와 같은 속성에 함수 데이터가 들어가 있는 것을 메소드(Method)** 라고 한다.  
함수(function)가 실행되기 위해 반환(return)해야 한다. (아래 코드 참조)  
return 'this'키워드 뒤에 점표기법을 통해서 'name' 데이터를 변환하고 있다.  
여기서 'this'가 소속되어 있는 객체 데이터를 의미하게 되는 것이다.  
i.e. Evelyn 안에서 getName을 실행하게 되면서 Evelyn 안에 있는 name의 값 'Evelyn'이 getName 밖으로 빠져나가는(반환) 구조이다. (예시1)  
```
// 객체 데이터
const Evelyn = { // const는 재할당 불가
  name: 'Evelyn', // 데이터(1) - 문자 데이터
  age: 22, // 데이터(2) - 숫자 데이터
  // 메소드(Method)
  getName: function (){
    return this.name; // 데이터(3) - 익명 함수가 데이터에 들어 있다.(함수의 표현)
  }
};

const herName= Evelyn.getName();
console.log(herName);
// 또는
console.log(Evelyn.getName());
```
<img width="636" alt="스크린샷 2024-02-03 오후 11 13 13" src="https://github.com/hyunji1117/everyday_study/assets/151576407/5bcdae21-635e-41de-bb99-bb01385a5037">
(https://velog.io/@harimad/JavaScript%EC%97%90%EC%84%9C-this-%ED%82%A4%EC%9B%8C%EB%93%9C%EB%9E%80)
(https://velog.io/@gud_wns/%EC%A0%90%ED%91%9C%EA%B8%B0%EB%B2%95%EA%B3%BC-%EA%B4%84%ED%98%B8-%ED%91%9C%EA%B8%B0%EB%B2%95)

getName에서 빠져나온 데이터는 herName에 할당되면서  
console에 그 결과를 출력하여 확인하게 되는 것이다.  

<img width="689" alt="스크린샷 2024-02-03 오후 11 43 55" src="https://github.com/hyunji1117/everyday_study/assets/151576407/69949b0e-a39b-4ca5-9d70-7a05c6cac3c0">
