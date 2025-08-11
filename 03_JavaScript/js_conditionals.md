# [JS] javascript 자바스크립트 조건문

## 조건문 (if, else)
조건의 결과(truthy, falsy)에 따라 다른 코드를 실행하는 구문  
bloolean 값으로 ture를 isShow 라는 변수 이름에 할당한다.  
```
let isShow = true;
let checked = false;


// if 조건 구문
if (isShow){
  console.log('Show!!'); // Show!
};

if (checked){
  console.log('checked!');
};
```
<img width="337" alt="스크린샷 2024-02-05 오후 10 34 22" src="https://github.com/hyunji1117/everyday_study/assets/151576407/c14572e3-a6ba-41a4-beac-0c8b1929d3a1">
<img width="688" alt="스크린샷 2024-02-05 오후 10 43 56" src="https://github.com/hyunji1117/everyday_study/assets/151576407/97fce097-3091-4bd1-8dd5-5131bba4c347">

else 조건을 추가하여 보자!  
isShow조건이 참인 경우, if (isShow)가 참이니 'Show!'를 출력하게 되고, 아니면(else) 'hide!'는 출력되지 않는다.  
```
let isShow = true;	// 주목!

if (isShow) {
  console.log('Show!');
}else{
  console.log('hide!');
};
```
<img width="685" alt="스크린샷 2024-02-05 오후 10 53 06" src="https://github.com/hyunji1117/everyday_study/assets/151576407/dd4ca510-8c21-4e89-b783-aa1aaf8fe66f">

isShow조건이 거짓인 경우, if (isShow)가 참이기에 'Show!'를 출력하지 않고, 아니면(else) 'hide!'가 출력된다.  
```
let isShow = false;	// 주목!

if (isShow) {
  console.log('Show!');
}else{
  console.log('hide!');
};
```
<img width="688" alt="스크린샷 2024-02-05 오후 10 53 50" src="https://github.com/hyunji1117/everyday_study/assets/151576407/468348f4-0d09-4565-a41b-ce5182b36504">
