[HTML] 핵심 요소 정리

div
특별한 의미가 없는 구분을 위한 요소. (Division)

h1 (heading)
제목을 의미하는 요소.

p (Paragraph)
문장을 의미하는 요소. (블록*상자* 요소)

img (Image)
이미지를 삽입하는 요소. (인라인*글자*요소)

e.g. <img src="https://www.naver.com" alt="네이버 홈페이지"> 필수속성 (누락될 경우, 웹표준에 어긋난다)
                이미지 경로 명시           alternate : 이미지의 이름 명시
                                       이미지가 출력되지 못했을 때 대신해서 출력된다. 

제목을 의미하는 요소 (Heading)
중요도가 클 수록 숫자가 작아진다. 
<h1></h1> 대주제
<h2></h2> 중간주제
<h3></h3> 소주제
<h4></h4>
<h5></h5> 여기까지 사용하는 경우가 거의 없음
<h6></h6> 여기까지 사용하는 경우가 거의 없음

a (Anchor)
e.g. <a href="https://www.naver.com" target="_blank"></a>
             넘어갈 경로 명시               링크 걸어서 페이지 이동할 때
                                        새 탭으로 열어서 명시한다. 

span
특별한 의미가 없는 구분을 위한 요소. (인라인*글자*요소)
i.e. 글자들의 범위를 잡아낼 때 사용하는 태그.

br (break)
줄바꿈 요소

input
사용자에게 테이터를 입력받는 요소. (인라인*글자*요소와 동시에 블록*상자*요소이다.)
i.e. 인라인 요소이지만 블록요소가 가지고 있는 몇 가지 특성을 추가적으로 사용할 수 있기 때문이다. 
     수평으로 쌓이는 특성, 가로세로 여백 지정 가능

e.g. <input type="text">
     입력받을 데이터의 타입 명시
     text = 글자가 화면에 출력

     <input type="text" value="evelyn.kim1">
     value = 사용자가 데이터를 입력하기 전에 미리 데이터를 입력하는 속성이다.

     <input type="text" placeholder="evelyn.kim2">
     사용자가 어떤 값을 입력해야 하는지 힌트를 명시해놓은 속성이다.

     <input type="text" disabled/>
     값을 명시하는 않는 속성, 빈태그처럼 '/'표시로 태그 마무리 명시하기.

     <label>
          <input type="checkbox"> Red<br/>
          <input type="checkbox"> Yellow<br/>
          <input type="checkbox"> Green<br/>
     </label>
     (인라인 요소) 사용자에게 체크 여부를 입력받는 데이터 종류이다. 
     input요소는 라벨링 가능하다.
     제목(e.g. Red,Yellow,Green)을 명시할 때 label이라는 요소를 함께 사용한다.
     label 요소로 묶었기 때문에 체크박스와 글자 모두가 동시에 클릭 가능하다.

     <label>
          <input type="checkbox"> Red<br/>
          <input type="checkbox"> Yellow<br/>
          <input type="checkbox" checked> Green<br/> <!-- 주목! -->
     </label>
     미리 체크한 상태로 출력하려면 위와같이 코딩하면 된다.

     <label>
          <input type="radio" name="color"> Red<br/>
          <input type="radio" name="color"> Yellow<br/>
          <input type="radio" name="color"> Green<br/>
     </label>
     체크박스와 달리 레디오는 제목 간의 관계를 중요시한다. 
     라디오를 한데 묶어서 둘 중 하나만 선택이 가능한 관계를 보여준다. 
     name 속성을 통해 원하는 이름으로 묶으면 된다. 
     name 속성이 없으면 항목 체크 후 취소가 적용되지 않는다.
