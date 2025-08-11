[Keyboard shortcuts] In MAC OS

Keyboard shortcuts	Actions
⌘⌥S	모두 저장 (프로젝트 전체 내용 저장 용도) 
⌘B	사이드바 열기/닫기
⌘P	빠른 열기 (파일/기호 탐색 e.g.css파일명)
⌘⇧P
모든 명령 표시, 에디터 모든 명령 접근
⌘W	현재 편집기 닫기
⌘⌥ F	찾기(검색) / 바꾸기(대체)
⌥↑ / ⌥↓	줄 위로 이동 / 줄 아래로 이동
⌘⌥ L	Beautify (정리된 코드 만들기 **확장자 설치 시)
⌘ \	편집기 분할 (백슬래쉬)


[Keyboard Shortcuts] 에밋 Emmet abbreviations in vs code
Emmet abbreviations (에밋 약어)

<<<<<<<<<<<<<<<<<<<< Html >>>>>>>>>>>>>>>>>>>>
! + tab키 ----- 기본 html 셋팅화면
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body></body>
</html>

img + tab키 ------ <img src="" alt="">
h1 + tab키 ----- <h1></h1>

(클래스 부여 . )
div.flower + tab키 ----- <div class="flower"></div>

(자식노드 >)
div>ul>li ----- <div>
                    <ul>
                      <li></li>
                    </ul>
                </div>
(형제노드 + )
div>ul+ol+div ----- <div>
                        <ul></ul>
                        <ol></ol>
                        <div></div>
                    </div>

(반복하기 *, 텍스트 입력 {} + 자동 넘버링 부여 $ )
div>ul>li*4{$} ----- <div>
                          <ul>
                              <li>1</li>
                              <li>2</li>
                              <li>3</li>
                              <li>4</li>
                          </ul>
                     </div>

(그룹화 () )
div>(header>ul>li*2>a)+footer ----- <div>
                                        <header>
                                             <ul>
                                                 <li><a href=""></a></li>
                                                 <li><a href=""></a></li>
                                             </ul>
                                        </header>
                                        <footer></footer>
                                    </div>

(그룹화 하지 않는 경우)
div>header>ul>li*2>a+footer ----- <div>
                                      <header>
                                          <ul>
                                              <li>
                                                  <a href=""></a>
                                                  <footer></footer>
                                              </li>
                                              <li>
                                                  <a href=""></a>
                                                  <footer></footer>
                                              </li>
                                          </ul>
                                      </header>
                                  </div>

#page>#nav>ul>li.item{hello$}*5+dldd ----- <div id="page">
                                                <div id="nav">
                                                    <ul>
                                                        <li class="item">hello1</li>
                                                        <li class="item">hello2</li>
                                                        <li class="item">hello3</li>
                                                        <li class="item">hello4</li>
                                                        <li class="item">hello5</li>
                                                        <dl></dl>
                                                    </ul>
                                                    <dd></dd>
                                                </div>
                                            </div>

<<<<<<<<<<<<<<<<<<<< Css >>>>>>>>>>>>>>>>>>>>
w:200 tab키 ----- width: 200px;
bc:orange tab키 ----- background-color: orange;
.item{h100+w100} tab키 ----- .item{
                                  height: 100px;
                                  width: 100px;
                              }

(단위 교체 가능)
기본값 → px
p → %
e → em
x → ex
r → rem	

(margin, padding)
.item{m100p+p100e} tab키 ----- .item{
                                    margin: 100%;
                                    padding: 100em;
                                }

.item {c#111} ----- .item {color: #111;}

.item {fsz13} ----- .item {font-size: 13px;}

** 자세한 emmet은 아래 링크로 들어가 확인 가능하다.
Abbreviations Syntax
