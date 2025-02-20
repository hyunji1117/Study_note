# [CSS] 브라우저 간 스타일 차이를 줄이기 (reset.css, normalize.css 차이)
[CSS Reset 개념][https://brunch.co.kr/@euid/2]

웹 표준에 의거하여 각각의 벤더사들(e.g.애플, 구글 ect.)이 브라우저를 제작할 때 조금씩 다른 결과물이 나올 수 있다.
i.e. 브라우저에서 제공하는 Css 스타일을 초기화 하고 작업을 시작하는 것이 좋다.

사용하는 크롬 브라우저에서는 흰색 영역이 기본으로 margin 값이 셋팅된 것이 테스트해볼 수 있다.
구글 검색창에 'reset.css cdn' 입력 후 jsDelivr로 작성된 링크 들어간다.
링크를 들어가 코드 복사 후 index.html의 css link 코드 위에 붙여넣기 하면 된다. 

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reset-css@5.0.2/reset.min.css">

적용 후 새로고침하면 브라우저 상단 margin 공간이 없어진 것을 볼 수 있다. 


## 1.reset.css  

### ① 특징 및 접근 방식
reset.css는 모든 브라우저 기본 스타일을 제거(초기화)하는 데 초점을 둔 스타일 시트이다.
모든 요소의 기본 스타일을 제거한 후, 필요에 따라 새로운 스타일을 추가해야 한다.  

### ② 장점  
  - 일관성 제공: 브라우저 기본 스타일을 완전히 제거하므로 스타일링의 시작점이 동일하다.  
  - 예측 가능성: 기본 스타일을 초기화했기 때문에 예상하지 못한 스타일 충돌이 줄어든다.  
  - 간단함: 초기화만 수행하며, 불필요한 코드가 적다. (즉, 추가적인 "스타일링 코드"는 들어있지 않다는 의미이다.)  

### ③ 단점  
  - 완전 초기화로 인해 기본 스타일도 재정의 필요: 기본 요소들(버튼, 폼 등)의 스타일을 새로 지정해야 한다.   
  - 모든 프로젝트에 적합하지 않음: 특정 프로젝트에서는 브라우저 기본 스타일을 활용하는 것이 효율적일 수 있다. 

```
< reset.css가 적합한 프로젝트 >

예:  
- 의류 쇼핑몰
독창적인 브랜딩을 강조하기 위해 버튼, 폼 요소, 헤더, 푸터 등의 스타일을 완전히 새로 정의해야 하는 경우.
고급 패션 브랜드 사이트 (모던한 UI, 큰 타이포그래피, 이미지 중심)

- 포트폴리오 웹사이트
완전히 차별화된 디자인을 구현하고, 기본 스타일이 간섭되지 않도록 원하는 대로 스타일링 가능.

- 게임 플랫폼 / 엔터테인먼트 웹사이트
독특한 테마를 강조해야 하므로, 브라우저 기본 스타일을 제거하고 새롭게 정의할 필요가 있음.

- 스타트업 랜딩 페이지
미니멀하고 커스터마이징된 디자인을 통해 사용자의 시선을 사로잡아야 할 때.
```  

```
< normalize.css가 적합한 프로젝트 >

예: 
- 아웃도어 쇼핑몰  
필터, 정렬, 장바구니와 같은 요소에 브라우저 기본 스타일을 활용하면서 빠른 개발이 필요한 경우.  
예: 기본적인 버튼, 인풋 필드 스타일을 유지하면서 브라우저 간 차이를 줄임.

- 블로그 또는 뉴스 포털
기본적인 텍스트 스타일링을 활용하고, 콘텐츠 가독성이 중요하며 스타일링을 간소화하고 싶은 경우.

- 기업 웹사이트
정보 제공이 주된 목적이며, 복잡한 커스터마이징이 필요하지 않은 사이트.
(예: 컨설팅 회사, 기술 회사의 소개 페이지.)

- 교육 플랫폼
사용자 경험이 직관적이고, 기본적인 폼 및 테이블 스타일을 유지하면서 브라우저 간 일관성을 보장해야 하는 경우.
```


****
## 2.normalize.css  

### ① 특징 및 접근 방식  
normalize.css는 브라우저 기본 스타일을 제거하는 대신, 브라우저 간의 스타일 차이를 "조정"하는 데 초점을 둔다.  
브라우저마다 다른 기본 스타일을 표준화하여 각 요소가 일관되게 보이도록 한다.  

### ② 장점  
  - 기본 스타일 유지: HTML 요소의 기본 스타일을 유지하면서 브라우저 간 차이만 보정한다.  
  - 빠른 시작 가능: 모든 요소를 다시 정의할 필요 없이 브라우저 기본 스타일을 활용할 수 있다.   
  - 사용자 경험 향상: 폼, 버튼 등의 기본 스타일이 그대로 유지되어 자연스러운 사용자 경험을 제공한다.  
  - 적은 재정의: 필요한 부분만 조정하므로 불필요한 스타일 재정의 작업이 줄어든다.  

### ③ 단점  
  - 초기화 수준이 낮음: 완전히 통제된 스타일을 원하는 경우 추가적인 작업이 필요하다.  
    ```
    button {
    all: unset; /* 모든 기본 스타일 제거 */
    background-color: #FF5733;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 16px;
    }
    ```
  - 복잡성 증가 가능성: 초기화 대신 조정이 이루어지므로 일부 프로젝트에서는 비효율적일 수 있다.  

<p align="center">
  <img width="460" height="300" src="./image/compare/reset.css_normalize.css.png">
</p>

# 요구사항에 맞춘 최적화된 초기화 방식  
```
/* 기본 스타일 초기화 (reset.css 기반) */
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
}

/* HTML5 디스플레이 초기화 */
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
    display: block;
}

/* 기본 브라우저 차이 조정 (normalize.css 기반) */
body {
    line-height: 1.5;
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
}

ul, ol {
    list-style: none; /* 기본 불릿 포인트 제거 */
}

a {
    text-decoration: none; /* 기본 밑줄 제거 */
    color: inherit;
}

/* 추가적인 커스텀 초기화 */
button {
    all: unset; /* 기본 스타일 제거 */
    cursor: pointer;
}
```


# 어떤 것을 선택해야 할까?  

  - 커스터마이징이 중요한 경우:  
모든 스타일을 처음부터 설계해야 한다면 reset.css가 더 적합하다.  

  - 기본 스타일을 활용하고 싶을 때:  
브라우저 간의 차이만 줄이고 빠르게 개발을 시작하려면 normalize.css를 선택하자. 

  - 혼합 접근법:  
프로젝트에 따라 두 접근법을 혼합해 사용할 수도 있닫.  
두 파일은 목적과 프로젝트의 요구 사항에 따라 선택적으로 사용할 수 있습니다. 직접 작성한 reset 스타일과 normalize.css의 장점을 결합하는 것도 일반적인 접근 방식이다.  
  
```
< 결합 접근 방식이 필요한 프로젝트 >

특징:
기본 스타일 초기화와 브라우저 표준화가 모두 중요한 경우.

예: 
- 이커머스 플랫폼 (종합 쇼핑몰)
다양한 섹션 (폼, 상품 카탈로그, 결제 시스템 등)을 포함하며, 일부 요소는 완전히 새롭게 스타일링하고 다른 요소는 기본 스타일을 활용할 경우.
(예: Amazon 같은 대규모 쇼핑몰.)

- 소셜 네트워크 플랫폼
사용자가 상호작용하는 다양한 컴포넌트 (댓글 박스, 버튼, 알림)를 포함하므로 브라우저 차이를 줄이는 것이 중요하지만, 핵심 UI 요소는 커스터마이징이 필요.

- SAAS 대시보드
데이터 시각화와 폼 입력 요소가 중요한 경우, 일관성 있는 스타일과 맞춤 디자인의 조화가 필요.
```








크로스 브라우징 (Cross Browsing) : 
모든 브라우저에서 화면이 동일하게 보이는 것이 아니라, 동등한 수준의 정보 및 기능 제공이 우선이라는 개념이다.

우리가 사용하는 웹브라우저들은 각기 다른 속성과 기술요소(렌더링엔진)가 존재하며,
이로 인해 웹브라우저 별로 표현하는 것에는 차이가 있을 수밖에 없습니다.
동일한 웹사이트라 하더라도 어떤 웹브라우저로 보느냐에 따라 다르게 보일 수 있는 것이죠.
​
'모든 브라우저에서 동일하게 보여준다'는 현실적으로 불가능한 얘기입니다.
다만, '크로스 브라우징'은 최대한 다양한 브라우저에서 제작자가 의도한 내용을 이상 없이 동작하게 해줍니다.
[출처] 크로스브라우징 (Cross Browsing) 이란|작성자 패치워크
