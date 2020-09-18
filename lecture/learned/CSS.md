# CSS

#### 기본 사용법

h1{

​	property: value;

​	property2: value2;

}

- h1 - (selector) - html 어느 부분에 적용 시킬것이냐

- property - 무엇을 바꿀 것이냐(색, 크기, 모습, 기타 등등)

- value - property를 얼마나 or 어떻게 바꿀 것이냐

  

### selector

- `#` -> 아이디 선택자(html 문서 내에 ID는 단 한개!)
- `.` -> class 선택자
- 이 외에 HTML에 사용한 태그 명도 선택자로 사용 가능.



#### CSS 상속 - CSS는 상속을 통해 부모 요소의 속성을 모두 자식에게 상속.

- 상속 되는 것
  - Text 관련 요소(font, color, text-align)
  - opacity, visibility 등
- 상속 되지 않는 것
  - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
  - position 관련 요소(position, top/right/bottom/left, z-index) 등

# 자세한 상속 확인은 MDN에서



#### CSS 적용 우선순위

1. 중요도

   - `!important`

   ##### important 설정한 것이 가장 우선.

2. 우선순위

   - `인라인` `id선택자` `class 선택자` `요소 선택자`

   ##### 인라인-> html내 같은 라인에 적은 것이 우선.

   #### css내에 설정 시

   - ID선택자(`#`) > class 선택자(`.`) > 요소 선택자(`p`, `div`, `body`등)

3. 소스 순서구

   css내부에 같은 우선순위를 갖을 경우, 위에서 부터 한 줄씩 실행하기 때문에 가장 밑의 요소가 남게 된다.

   ex)`p`{color: blue;}

   ​	`p`{clolr: red;}

   의 경우 최종적으로 `p`태그는 모두 빨간색이 됨.



#### 크기 단위 (상대)

- px

- %

- em : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐.

- rem : 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐.

- viewport 기준 단위

  - vw, vh, vmin, vmax

  

#### Box model 구성

Content - 실제 내용 위치

Border - 테두리 영역

Padding - 테두리 안쪽의 내부 여백 요소에 적용된 배경의 컬러, 이미지까지의 영역

Margin - 테두리 바깥의 외부 여백. 배경색 지정할수 X



# *Shothand-margin*

margin1: (상,하, 좌, 우)

margin2: (상,하) (좌, 우)

margin3: (상) (좌, 우) (하)

margin4: (상) (우) (하) (좌)



# *Shothand-border*

border: (width) (style) (color)

ex: {border: 2px dashed black;}



Box-sizing: borderbox

-> border 영역 까지를 모두 한 박스로 보는 것.

# 활용:

1. ~~Box-sizing: borderbox~~

   # width100px;

   margin right 20px;
   margin left: 20px;
   border width: 1px;
   일 경우 이 박스의 크기는 142px 이다.

2. Box-sizing: borderbox

   width100px;
   margin right 20px;
   margin left: 20px;
   border width: 1px;

   일 경우 박스 크기는 100px

### default -> content-box 기 때문에 상황에 따라 변경해서 사용할 것.



#### 마진 상쇄

`<div>1</div>` -> margin bottom: 20px;



`<div>2</div>` -> margin top: 50px;

일 경우 상쇄가 일어나 실제 margin은 30px 적용.



#### 블록 레벨 요소

- div / ul, il, li / p / hr / form

#### 인라인 레벨 요소

- span / a / img / input, label / b, em, i, strong 등



# display

- display: block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로폭을 차지한다. -> content 이외에는 margin이 차지.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- display: inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하여백은 line-height로 지정한다.
- display: inline-block (inline 으로 사용하고 싶지만 block처럼 너비, 높이를 지정하고 싶을 때 사용.)
  - Block과 inline 레벨 요소의 특징을 모두 갖는다.
  - inline 처럼 한 줄에 표시 가능하다.
  - Block 처럼 width, height, margin 속성을 모두 지정할 수 있다.



- 이외에도 다양한  display 존재.



### text-align은 inline 설정이기 때문에 block요소는 적용이 X



## CSS position

#### Static: 디폴트 값(기준 위치)

- 기본적인 요소의 배치 순서에 따름(좌측상단)
- 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 된다.



#### - 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동이 가능한 것들.(음수도 O)

- relative(상대위치): static 위치를 기준으로 이동
- absolute(절대위치): static가 아닌 가장 가까이에 있는 부모/조상 요소를 기준으로 이동
- fixed(절대위치): 부모 요소와 관계 없이 브라우저를 기준으로 이동(스크롤시에도 항상 같은 위치)



#### relative(상대위치)가 움직일 때는 원래 자신의 위치(static 위치)에 자신의 흔적을 남기고 이동.

#### absolute(절대위치)의 경우 움직일 때, 자신의 원래 위치(static 위치)를 비워놓고 움직이기 때문에 다른 요소들이 빈 위치로 이동하여 레이아웃이 깨질수 있기 때문에 주의해서 사용해야 한다.



## CSS float 속성

- Float는 요소를 일반적인 흐름(normal flow)에서 벗어나도록 하는 속성 중 하나.
  - 반드시 claer 속성을 통해 초기화가 필요하며, 예상치 못한 상황이 발생할 수 있음.
- Float를 사용하는 경우 Block 사용을 뜻하며, display 값이 inline인 경우 block로 계산.

### 부모의 높이는 자식 컨텐츠의 높이가 결정. 

### float의 경우 둥둥 떠다니기 때문에 부모 입장에서 자식이 없다고 생각되어 높이가 X.

### -> 이를 해결하기 위한 방법: 의사(가상) 요소 선택자.

.clearfix:: after{} -> 잘 모르겠...

#### 

# 정리.

- 일반적으로 html 요소들은 문서의 위에서부터 아래로 순차적으로 나열.
- 이를 변경하기 위한 방법들

1. display 속성을 통해 요소가 보여지는 (표현되는) 방식 변경
   - block, inline, inline-block 등
   - table, flexible box, grid 등의 레이아웃을 활용
2. position 속성을 통해 위치 자체를 변경
   - static, relative, absolute, fixed
3. float 속성을 통해 떠 있도록 만듦
   - clear를 통해 문제가 생기지 않도록 해줘야 함.



### CSS를 어렵게 만드는 요소

- 일반적인 흐름(normal flow)을 바꿔버리는 경우!
- Normal flow
  - inline, block, relative position
- Floats
- Absolute positioning

