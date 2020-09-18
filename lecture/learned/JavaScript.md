# 자바스크립트 -> 읽을 수 있을 정도. 차이점 등 숙지.

- JavaScript 구문
- 데이터 타입 및 변수
- 연산자
- 조건/반복문



### JS의 탄생

- 1990년대 네스케이프사의 Netscape Navigator(NN) 브라우저가 표준
- 정적인 HTML을 동적으로 표현하기 위한 언어 도입을 결정
- 1996년 브랜던 아이크 주도로 개발된 `Mocha`를 자체 브라우저에 도입
- 이후 LiveScript라는 이름을 거쳐 지금의 JavaScript의 이름으로 변경

#### 정리: 브라우저 전쟁-> MS의 폭발적 성장. IE3에서 자체적인 JScript와 CSS 지원. -> 남에게 내 브라우저의 좋은 기능을 주기 싫어! -> 호환성 문제로 크로스 브라우징 등의 이슈 발생.

#### 계속되는 파편화를 방지하고, 모든 브라우저에서 동일하게 동작하기 위한 표준의 필요성 제기.

#### Netscape는 `ECMA`인터내셔널에 기술 규격을 제출한 이후 발전

#### ES1 -> ES2 -> ES3 -> ES5 -> `ES2015`-> `ES2016` -> `ES2017`

#### ES2015

- 자바스크립트의 고질적 문제들을 많이 해결한 ES2015를 지나 현재 ES2019까지 발표.
- ES6라고 불리우는 이 버전은 기존 코드를 간결하게 작성할 수 있는 새로운 문법들이 추가 되면서 더욱 발전할 수 있는 계기가 되었음.

#### Vanilla JS

- 크로스브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장(대표적: jQuery)
- 최근 표준화된 브라우저, ES6 이후의 다양한 도구의 등장으로 `순수 자바스크립트` 활용의 증대



#### 순수 자바스크립트에서 할 수 있는 일.

- DOM 조작 : HTML 문서 조작
- BOM 조작 : 브라우저 조작
  - navigator, screen, location, frames, history, XHR
- JavaScript : 밑의 요소들을 조작
  - Object, Array, Function

JavaScript -> 브라우저에서만 사용할 수 있는 언어였다.

이를 위해 크롬과 안드로이드에 탑재되어 있던 `V8엔진`(frontend)을 기반으로 `nodejs`(backend) 라는 컴퓨터에서 실행할 수 있는 환경을 만들어주며 JS 시장이 폭발적으로 증가.

<hr> 여기까지가 자바스크립트의 역사(?)





# JavaScript 기초

number string는 이러닝의 틀린 개념 잡기 위해 넣은 것. 엄청 중요한 내용은 x)

##### `console.log 를 통해 개발자도구 활용 하자.`

#### 변수 선언

- 변수 선언은 `var` 키워드를 활용해야 함.
- ES6 기준으로 아래와 같은 키워드가 등장함.
  - const
  - let



#### 데이터 타입 분류(typeof)

- 원시 타입(primitive) - 변경 불가능한 값(immutable)
  - boolean - true, false
  - undefined
  - number(NaN도 number)
  - string
  - symbol(ES6)
- 객체 타입(object)
  - object : 일반 객체, function, array, date, RegExp(정규 표현식)



#### Number

- 모든 숫자는 number 타입
- 8진수(0), 16진수(0x)로 표현 가능
- 추가적으로 Infinity, -infinity, NaN(Not a Number)도 number 타입
  - typeof NaN / typeof Infinity / typeof -infinity => 모두 "number" 타입.

- 자세한 사항은 MDN 자바스크립트 참고서 Number 참조.

- 정수의 타입이 별도로 없지만 정수라는 수 체계는 존재한다.
- IEEE 754 표준에 따라서 부동 소숫점으로 표현되며 -2^53 ~ 2^53의 정수만 `안전하게 표현` 가능하다.

### 안전하지 않다의 의미

- `Math.pow(2, 53)`=> 2^53 = 9007199254740992
- `Math.pow(2, 53) + 1` => 2^53 + 1 = ~~9007199254740993~~ 이어야 하지만
  실제 나오는 값은 9007199254740992

- `Math.pow(2, 53) * 2` => 2^53  x 2 = 18014398509481984 로 올바르게 나온다.
  즉 항상 계산이 안되는 것이 아니라 안되는 경우가 생길 수 있기 때문에 안전한 수 범위 내에서 사용하자.
- `Number.isSafeInteger(Math.pow(2, 53))` => 2^53 이 안전한 수 입니까? => false

- `Number.isSafeInteger(Math.pow(2, 53)-1)` => 2^53 - 1 이 안전한 수 입니까? => true



#### String - 템플릿 문자열(ES6)

- 템플릿 문자열 (파이썬의 fstring과 비슷한 것.)
  - 편하게 문자열 내에 변수를 사용(string interpolation) 가능
  - 여러 라인으로 이뤄진 문자열 사용 가능

ex)

```javascript
var name = 'kim'
console.log(`welcome to live session,
            Mr. ${name}!`)
```

결과:

`Welcome to live session,`

`Mr. kim!`



#### null vs undefined

- null
  - 의도적으로 변수에 값이 없다는 것을 명시
  - typeof 출력시 object로 출력되는 것은 설계상의 실수 (옛날에 코딩된 것들의 호환을 위해 남겨둠.)
- undifined
  - 선언 이후 할당하지 않은 변수에 지정된 값
  - 자바스크립트 엔진이 할당 이전에 초기화된 값
  - 직접 값으로 할당해서 사용하는 것 금지



#### 객체(object)

- 자바스크립트는 원시타입(primitive type)을 제외하고는 모두 객체이다.
- 자바스크립트의 객체는 키(문자열 또는 심볼)와 값(모두)으로 구성된 속성(property)의 집합이며, 속성 값이 함수일 경우 구분을 위해 메소드라고 부른다.

`JavaScript Object Notation` =>`JSON`

object 생성 방법.

```javascript
var person = {
	name: 'hong'
	greeting: function() {
		console.log(`Hi, I'm ${this.name}`)
	}
}
```

`person.greeting()` => 메서드



#### 배열(Array)

- 자바스크립트 배열은 [] 대괄호를 사용하여 생성.

  ```javascript
  var a = [1, 2, 3, 'hi']
  ```



#### 함수

- ##### 함수의 선언 방법

  1. add 를 사용.

  ```javascript
  function add(num1, num2) {
  	return num1 + num2;
  }
  ```

  2. 변수에 저장하여 사용

  ```javascript
  const sub = function(num1, num2) {
      return num1 + num2;
  }
  ```

  3. 화살표 함수(arrow function)

  뒤에 나옴.



#### 변수 유효 범위(scope)

- 자바스크립트는 함수 레벨 스코프를 가진다.
- 따라서 함수 내에서 선언된 변수는 지역 변수이며, 
- 나머지는 전역 변수로 활용된다.
- 변수 선언시 키워드를 쓰지 않으면, 암묵적 전역으로 설정된다.
  - 주의: 변수가 아닌 전역객체(window)의 프로퍼티로 생성.
  - 따라서, delete(객체의 속성을 지우는 연산자)로 지워지는 값.

전역변수 => global 어디서든 접근할 수 있는 변수



### `키워드를 사용하지 않으면 변수가 전역 변수로 설정되고, 나중에 해당 이름으로 변수를 조작할 경우 전역변수로 설정된 변수가 조작되어 문제가 생길 수 있다!` 라고 이해가 됨.





#### 호이스팅과 let, const(ES6)

## 호이스팅(Hoisting) 함수 안에 있는 선언들을 모두 끌어올려 해당 함수 유효 범휘 최상단에 선언하는 것을 말한다.

```javascript
console.log(a)
var a
//이 경우 a는 호이스팅을 통해 가장 최상단으로 선언되어 console.log(a)가 문제 없이 실행.
console.log(b)
let b
//이 경우 b는 호이스팅되지 않기 때문에 에러가 발생.
```

```python
def eng(a):
    print(a)
	a = 'abc'
#이렇게 실행하면 파이썬에서 오류가 생기겠지만, 자바스크립트에서 var로 선언하면 오류 없이 실행된다. 이게 호이스팅.
```



- 자바스크립트에서는 모든 선언을 호이스팅 한다.

- ES6에서 새롭게 등장한 let와 const 키워드는 이러한 내용을 방지할 수 있다.

  - 호이스팅 자체는 이뤄지지 않는 것은 아니고,

    - var는 선언과 동시에 초기화(undefined)를 하고,

    - let, const는 선언과 초기화 단계가 분리되어 진행된다.

  - 뿐만 아니라, 블록 레벨 스코프를 가지고 있으며, 이는 나중에 다룰 예정.





# JavaScript 문법

#### `==` VS `===`

- `==` 동등 연산자.
  - 값 비교 및 예상치 않은 변환
- `===` 일치 연산자.
  - 엄격한 같음. 형 비교.

```javascript
0 == ''
//true

0 == '0'
//true

'' == '0'
//false
```

`JavaScript`에선  '`===` ' 이 `python`의 `==` 처럼 쓰인다.



#### if 조건문.

```javascript
//	if ('조건') {
//	    수행할 내용
//	}

if (userName === '홍길동') {
    message = '<h1> 아버지를 아버지라 부르지 못하고.</h1>'
} else if (userName === '심청이') {
    message = '<h1> 아버지 꼭 눈을 뜨세요...</h1>'
} else {
    message = '<h1> 아버지 날 보고있다면 정답을 알려줘.</h1>'
}
```

#### for 반복문.

```javascript
//	for (변수선언 반복조건 변수조작) {
//		반복 실행문
//	}


for (let j=0; j < 10; j++) {
    console.log(j)
}
//j=0 이고 j가 10보다 작다면 j를 1 더하면서 반복 실행문 반복.
```

#### while 반복문.

```javascript
//	변수 선언
//	while (반복저건) {
//	반복 실행문;
//	변수조작
//	}


let i = 0;
while (i < 10) {
    console.log(i);
    i++
}
//i=0 이고 i가 10보다 작으면 반복실행문을 실행하고 i를 1 더한다.
```



#### 객체(object) 생성 방법

#### -객체 : Key와 Value로 구성된 property(속성)들의 모임

- 기본 객체 생성법

  - 객체 리터럴

  ```javascript
  var cat1 = {}
  var cat2 = {name: 'nero', age: 3}
  //	cat2 => {name: 'nero', age: 3}
  ```

  -객체 리터럴로 생성을 하는 경우 Key가 문자열로 표기될 수 있다면, 암묵적 형변환이 발생.

  -그게 아닐 경우 반드시 `'따옴표'`를 통해 문자열로 만들어 주어야 한다.

  

  

  - Object 생성자 함수

  ```javascript
  var dog1 = new Object()
  dog1.name = 'baduki'
  dog1.age = 5
  //	dog1 => {name: 'baduki', age: 5}
  ```

  -생성자 함수를 만들어 사용하면, 마치 클래스처럼 속성이 동일한 객체를 쉽게 생성할 수 있다.

  ```javascript
  function Person(name, age) {
      this.name = name;
      this.age = age
  }
  var p1 = new Person('hong', 100)
  
  p1
  //	Person {name: 'hong'. age: 100} 생성.
  ```

  

#### 객체(Object) 속성 접근

- 속성 접근은 `.` 혹은 `[]`로 가능하다.
  - 단, 반드시 `[]`로 접근을 해야하는 경우가 있다.



#### 배열(Array)

- JS에서 배열은 값만 존재한다.

  - 배열 리터럴

  ```javascript
  var a = [1, 2, 3]
  ```

  - Array 생성자 함수

  ```javascript
  var b = new Array(1, 2, 3)
  ```

#### 배열(Array) 순회

A = [1, 2, 3, name: 'alpha']

- `for`(배열을 인덱스로 접근해서 순회 `파이썬의 for i in range()와 비슷`)

```javascript
for (var i = 0; i < a.length; i++) {실행문}
```



A = [1, 2, 3, name: 'alpha']

- `for ... of`(배열을 요소로 순회 `파이썬의 for i in A`와 비슷)

```javascript
for (var elem of a) {실행문}
```



A = [1, 2, 3, name: 'alpha']

- `forEach`(배열의 인덱스와 요소 모두 순회 `파이썬의 for idx, v in enumerate(A)`와 비슷)

```javascript
A.forEach(function(v, idx) {실행문})
```



A = [1, 2, 3, name: 'alpha']

- `for...in`(배열의 요소만 접근하는 것이 아닌 속성(property)까지 출력될 수 있다.)

-> 자바스크립트에서 배열도 Object기 때문에 속성 설정이 가능하지만, 요소가 아니라 객체의 속성이 된다.

```javascript
for (var i in a) {
    console.log(i, a[i])
}
//	실행 시
0 1
1 2
2 3
name alpha
```



#### 배열(Array) 메소드

##### .sort

- sort  메소드에 비교 함수(인자)가 없으면 문자열 기준으로 정렬한다.

- 비교함수가 있다면, 해당 함수의 리턴값이 0보다 크거나 작음으로 정렬한다.

```javascript
var numbers = [4, 2, 5, 1, 3, 100];
numbers.sort()
//	결과:(6) [1, 100, 2, 3, 4, 5] =>문자열 정렬
```

```javascript
var numbers = [4, 2, 5, 1, 3, 100];
numbers.sort(function(a, b){
	return a - b;
})
//	결과:(6) [1, 2, 3, 4, 5, 100]
```

밑의 `function(a, b)` 는 비교함수로 `return a - b` 의 경우 오름차순 정렬, `return b - a`의 경우 내림차순으로 정렬할 수 있다.

-> 자세한 작동 원리는 잘 모르겠음.

 (예상: a - b가 양수면 b가 작으므로 a 먼저 정렬 / b - a 가 양수면 a가 작으므로 b 먼저 정렬해서 오름차순.)



##### 문자열 관련 - join, toString

```javascript
var a = [1, 2, 3]
a.join('-')
//	'1-2-3'
a.toString()
//	'1,2,3'
```



##### 배열 합치기 - concat

```javascript
var a = [1, 2, 3]
a.concat([4, 5])
//	(5) [1, 2, 3, 4, 5]
a + [4, 5]
//	'1,2,34,5'
a.concat(4, 5)
//	(5) [1, 2, 3, 4, 5]
```



##### 원소 삽입/삭제

```javascript
var a = [1, 2, 3]
```

##### - push

```javascript
a.push(4)
//	4(새 배열의 길이를 반환.)
//	[1, 2, 3, 4]
```

##### - pop

```javascript
a.pop()
//	4(제거된 요소를 반환.)
//	[1, 2, 3]
```



##### - unshift

```javascript
a.unshift(0)
//	4(새로운 배열의 길이를 반환)
//	[0, 1, 2, 3]
```

##### - shift

```javascript
a.shift()
//	0(제거된 요소를 반환)
//	[1, 2, 3]
```



##### 인덱스 탐색

##### - indexOf

```javascript
var a = [1, 2, 3]
a.indexOf(3)
//	2(같은 값을 가지는 첫 번째 요소의 인덱스 반환.)
a.indexOf(5)
// -1(찾지 못하면 -1 반환.)
```



##### 배열 조작

##### - splice (원본 배열을 바꿔버림.)

```javascript
var a = [1, 2, 3]
a.splice(1, 2, '처음', '다음')
//	[2, 3](지워진 요소를 담은 배열 반환.)

//	a = [1, '처음', '다음']
//	splice(1번 인자, 2번인자, 그 외...) => 1번인자 인덱스부터 2번인자 개를 지우고 1번인자 인덱스 뒤에 그외...를 추가
```

##### - slice (return 해줌. 원본 배열 유지)

```javascript
a.slice(1, 2)
//	[2]

//	1부터 2(2 미포함)번 인덱스까지의 요소를 담은 새 배열 반환
//	원본 배열에 영향을 끼치지 않는다.
//	slice(1번인자, 2번인자) => 1번인자부터(포함) 2번인자(미포함) 인덱스 까지의 요소를 담은 새배열 반환.
```



#### 함수 선언

1. 함수 선언문

```javascript
function sum(a, b) {
	return a + b;
}

//	함수의 이름 sum 이 선언.
```

2. 함수 표현식

```javascript
var sum = function(a, b) {
	return a + b
}

//	함수의 이름이 선언X
```

3. 즉시 실행 함수(`파이썬의 lambda와 비슷`)

```javascript
(function(a, b){return a + b})(1, 2)
//	3

//	함수를 즉시 실행(1, 2)라는 인자 전달까지 한번에!
```

4. 화살표 함수(ES6)

```javascript
var sum = (a, b) => a + b

//	`=>` === `function` / `(a, b)` === 인자 / `a + b` === `return`
```



##### 함수 인자

- 자바스크립트에서 함수는 매개변수 전달에 대한 제한이 없음.
- arguments 객체는 매개변수로 넘겨진 모든 정보를 가지고 있음

#### ! undefined 는 함수를 초기화 할때 사용하는 것, 선언되지 않은 변수 등 도 undefined. 오류가 아니다.

<hr>

# DOM(Document Object Model)

-가장 최 상위의 객체를 말하는 것 같음. 크롬의 창(window), Html 문서 하나(index.html)

- 문서의 구조화된 표현을 제공하며, DOM 구조에 접근 할 수 있는 방법을 제공
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 도우며, 구조화된 노드와 오브젝트로 문서를 표현
- 주요 객체
  - window : DOM문서를 표현하는 창. 가장 최상위 객체/(전역 객체, 다양한 함수, 이름공간, 객체 등이 포함)
  - document : 페이지 콘텐츠의 진입점 역할을 하며, `<body>` 등 다른 요소들을 포함
  - navigator, location, history, screen

```
python : snake_case
JS : CamelCase
여러 요소의 이름등을 붙일 때 사용하는 방법이 다름.(ex.변수명)
```



#### DOM 접근->querySelector/querySelectorAll 2 개가 중요.

- 단일 Node ->id 이기 때문에 하나의 Node 반환.

  - document.getElementByID(id)

  - `document.querySelector(selector)`

  

  ##### 단일 노드와 달리,`HTMLCollection, NodeList`은 유사 배열 형식의 [Node1, Node2...] or [Node] 과 같이 배열 형태로 반환.

- HTMLCollection(live)

  - document.getElementsByTagName(class)
  - document.getElementsByClassName(class)

- NodeList(non-live)

  - `document.querySelectorAll(selector)`



=>`HTMLCollection(live)` VS `NodeList(non-live)`

`live collection` => 배열이 바뀌면 즉시 변화가 적용.

ex)a = [1, 2, 3] 에서 인덱스 0~2를 접근하며 해당 요소를 del 한다고 생각하면 처음 0번 인덱스 1을 지우면

a = [2, 3] 이 되어 다음 1번 인덱스의 요소는 2가 아닌 3을 지워 최종적으로 a = [2] 가 남는다.



`non-live`=>배열이 바뀌어도 바로 적용 안됨.

a = [1, 2, 3]에서 인덱스 0~2를 접근하여 해당 요소를 del 하면 a = [] 가 된다.





#### Node 생성

- document.createElement(tagName) : 특정 태그를 생성
- document.createTextNode(text) : 텍스트 노드를 생성
- parentNode.appendChild(Node) : 마지막 자식 요소로 추가
- parentNode.removeChile(Node) : 해당 요소를 제거

이와 관련하여

##### innerHTML, insertAdjacentHTML

- DOM 조작시 아래와 같은 메서드를 통해서도 가능하나, XSS공격에 취약점이 있으므로 사용시 주의.
- element.innerHTML(text)
- element.insertAdjacentHTML(position, text)
  - position : neforebegin, agterbegin, beforeend, agterend(어디든 위치를 지정해 넣을 수 있다.)



#### Node attribute

- element.style
  - element.style.color
  - element.style.backgroundColor
- element.setAttribute(attributeName, value)
- element.getAttribute(attributeName)

element.style , set/get Attribute 를 통해 속성값을 바꿔줄 수 있다

<hr>

# Event

- 브라우저에서 특정한 이벤트가 발생하면 이에 대한 이후 행위를 정의할 수 있다.
- 이벤트를 정의하는 경우, 인라인으로도 작성 가능하나 분리하여 작성하는 것이 좋다.
- 가능한 이벤트의 예시(load, copy, mouseover, click, submit 등)



#### addEventListener

- EventTarget.addEventListener(type, listener, [, useCapture]);

  - type : 이벤트 유형

  - listener : 이벤트가 발생했을 때 실행할 콜백 함수(핸들러)

  - useCapture : 기본 값(false), 상위 노드로 전파(버블링)를 캐치./만약 true인 경우 하위 노드로 전파(캡처링)되는 것을 캐치.

    => 이벤트 전파는 항상 캡쳐링으로 시작하여 버블링으로 끝난다. 다만 useCapture를 통해 어떤 상태의 전파를 잡아 사용할지 지정하는 것으로 이해.

```javascript
const button = document.querySelector('button');

button.addEventListener('click', function(){
    console.log('click')
})

//	버튼을 클릭했을 때, 콘솔 로그에 click 기록.
//	button.addEventListener('click'/type/, function/콜백 함수/(){
//		console.log(동작)
//	}) addEventListener 라는 객체 안에 동작할 function을 넣고 최종적으로 객체 닫음 `})`
```



#### 이벤트 전파

- 이벤트는 해당 요소에서 전파되며, 캡처링(하위로)과 버블링(상위로)으로 구분된다.
- 항상 캡처링부터 시작하여 버블링으로 종료되며, addEventListener 메소드의 useCapture를 통해 특정 상황에 대하여 이벤트 관리가 가능하다.



#### 이벤트 객체와 this

- 이벤트 리스너의 콜백함수에서 this를 활용하는 경우, 이벤트 리스너에 바인딩 되어 있는 요소가 지정된다.

  ->this는 해당 함수를 사용한 객체 자체를 말하는데, 이벤트가 전파되면 해당 객체가 계속 변하므로 this의 값도 계속 변한다고 이해.



#### 이벤트 객체

- 이벤트에 지정된 함수(핸들러)는 이벤트 객체를 매개변수로 받을 수 있음
- 이벤트 객체에는 대표적으로 아래와 같은 속성과 메소드들이 있다.
  - Event.target : 이벤트가 원래 발생하였던 대상
  - Event.currentTarget : 이벤트가 발생하였던 대상
  - Event.preventDefault() : 이벤트를 취소
  - Event.stopPropagation() : 이벤트 전파 중단



# 함수의 고급 기능

#### 함수의 선언 방식:

1. 함수 선언문(function sum(인자){실행문})
2. 함수 표현식(var sum = function(인자){실행문})
3. 즉시 실행 함수(function(인자){실행문}(실행인자))



#### 함수 호이스팅

- 자바스크립트에서는 모든 선언이 호이스팅 된다.
- 앞서 설명한 함수 선언 방식의 가장 큰 차이점은 다음과 같다.
  - 함수 선언문의 경우 선언, 초기화, 할당이 모두 이뤄져 실행 가능
  - 함수 표현식은 변수 호이스팅이 발생하여, undefined. 즉 실행 불가. => 변수 sum에 대한 호이스팅으로 함수라는 값 대신 undefined가 들어가기 때문에 실행이 안된다.(그렇기 때문에 함수표현식을 사용 할때는 사용할 코드보다 위쪽에 함수 표현식을 선언해야 한다.)



#### Array helper methods(자세한 사용법은 MDN참조)

- forEach : 주어진 함수를 배열의 요소 각각에 대해 실행
- filter : 주어진 함수를 배열의 요소 각각에 대해 실행하여 반환 값이 true인 요소를 모아 배열을 반환
- map : 주어진 함수를 배열의 요소 각각에 대해 실행한 결과를 모아 배열을 반환
- every : 주어진 함수에 모든 요소가 true인 경우 true (boolean값을 반환) (and)
- some : 주어진 함수에 하나라도 true인 경우 true (bollean값을 반환) (or)
- 이외에도 reduce, find 함수 등이 존재한다.

```javascript
const numbers = [1, 2, 3]

numbers.forEach(function(elem, idx, arr){
	console.log(elem, idx, arr)
})
//	method 내부의 함수(function)은 함수 호출이 아닌, `함수 선언`이다. 그리고 javaScript의 특성 상, 함수의 argument(여기서는 elem, idx, arr)는 모두 사용이 안되더라도 따로 해당 argument를 저장해놓는 것을 기억하자.
```



### Closure

<hr>

##### First class function

- 자바스크립트 함수는 아래와 같은 특징을 가진다.
  - 함수를 인자로 전달 가능함
  - 함수를 반환할 수 있음
  - 변수에 함수를 할당 가능함
- 위의 조건은 프로그래밍 언어에서의 일급 객체(first class object / first class citizen)의 조건이다.

### `자바스크립트는 함수도 일급객체 라는것을 기억하자.`

<hr>

##### Closure

- 클로저는 함수와 함수가 선언된 어휘적 환경(Lexical scoping, environment)의 조합이다.

=> 클로저란 함수가 할당될 때, 함수 실행문만 저장되는 것이 아니라, 그 함수 안의 변수 선언 등도 함께 저장이 된다고 이해하면 됨.

`파이썬 예.`

```python
def count():
    cnt = 0
    def plus():
        nonlocal cnt
        cnt += 1
        return cnt
    return plus

a = count()
print(a())	#cnt = 1 출력
print(a())	#cnt = 2 출력
b = count()
print(b())	#cnt = 1 출력
print(b())	#cnt = 2 출력
#1,2,1,2 인 이유는 a = count() 이 부분에서 a에 cnt = 0 저장 그리고 a를 두번 호출했기 대문에 cnt = 2
#b = count()에서 다시 cnt = 0 저장, 이후 b두번 호출했기 때문에 cnt = 2
```

