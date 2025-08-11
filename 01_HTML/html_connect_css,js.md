[HTML] 버전 지정 / CSS, JS 연결하기

<!DOCTYPE html>의 html는 문서의 HTML 버전을 지정한다고 보면 된다.
<!DOCTYPE html>	---> HTML5
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Trans...	---> XHTML

코드 예시 : 
<!DOCTYPE html> <!-- html 버전 지정 -->
<html lang="ko"> <!-- 페이지 자동 번역 팝업여부 -->
<head>
    <meta charset="UTF-8"> <!-- 문자 인코딩 방식 지정 -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <!-- viewport:모바일과 관련 있음 content: 관련 내용 -->
    <title>Document</title>
    <link rel="stylesheet" href="main.css"> <!-- **css 연결하기 -->
    <script src="./main.js"></script> <!-- **js 연결하기 -->
</head>
<body>
    <div>Hello World</div>
</body>
</html>

대표적으로 사용하는 아이콘 - 파비콘 이라고 부른다. 
HTML Favicon을 적용할 때는 이름을 favicon이라고 지정하길 권장한다.
favicon.ico 또는 favicon.png 파일이 주로 사용된다. 
** 파비콘 (Favorite Icon, Favicon)


-----------------------------------------------------------------------------

Javascript를 html에 연결하는 2가지 방법 : 
<link></link> 외부에서 (JS)파일을 가져오는 방식
<script></script> (JS를)내부에서 직접 작성하는 방식
Meta(정보) 태그 :
link, style, scriprt, title 등 각각의 태그로  나타낼 수 없는 나머지 모든 정보를 표시할 때 사용하는 태그

<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

name - 기본적인 정보의 종류 (author제작자)
content - 기본 정보의 실제 값 기재
i.g. </meta>는 HTML 문서(웹페이지)의 제작자, 내용, 키워드 같은, 여러 정보를 검색엔진이나 브라우저에게 제공하는 태그이다. 

viewport - 웹페이지가 실제로 표시되는 영역 (웹페이지 출력되는 영역)
** 모바일에 대응하는 작업을 할 때 필요한 내용이고 일반 desktop에서는 해당사항이 없다.
content - 표시되는 영역에 해당하는 값이다.

<meta charset="UTF-8">

charset(Character set)
화면에 표시하는 문자를 어떠한 방식으로 인코딩할 것인지 나타내는 속성.

문자 인코딩(Encoding)
웹페이지에서 볼 수 있는 각각의 문자를 어떤 방식으로 처리할 것인지에 대한 방식 의미.

e.g.
한글로 '딩' 글자를 표현하고 싶다고 가정한다.
'딩'글자는 'ㄷ', 'ㅣ', 'ㅇ', 으로 이루어져 있다.
i.g. 모음과 자음으로 각각의 조합을 만들 수 있다.
문자 인코딩 방식이 달라질 경우, 모음과 자음으로 글자를 만드는 것이 아닌 '딩'글자가 온전히 존재해야지 문자로 출력이 가능할 수 있다.
(e.g. EUC-KR 옛날 인코딩 방식)

최근에는 웹에서 UTF-8 인코딩 방식을 표준처럼 사용하고 있다. 
