# 메소드 체이닝 (Method Chaining)

## split 메소드:  
문자를 split에 적용되어 있는 인수 기준으로 배열로 쪼개서 데이터로 변환해서 반환.  
i.e. '문자'를 배열 데이터로 변환  

## reverse 메소드:  
배열을 기본 순서가 아닌 반대의 순서로 뒤집어 주는 역할을 한다.  

## join 메소드:
배열 데이터를 인수 기준으로 문자들을 하나씩 붙여서 병합해 변환한다.  

```
const a = 'Evelyn!';
const b = a.split('').reverse().join(''); 
// a 배열 뒤에 메소드+메소드+메소드... 이런 형식을 메소드 체이닝이라고 한다.

console.log(a); // Evelyn!
console.log(b); // !nylevE
```

<img width="599" alt="스크린샷 2024-02-11 오후 4 48 45" src="https://github.com/hyunji1117/everyday_study/assets/151576407/b58536ed-4d19-4618-a6c1-ce97aabcfbd2">
