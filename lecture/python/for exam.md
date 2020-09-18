1. ### python_intro

   ##### 시퀀스 자료형 

   - 리스트 - mutable
   - 튜플 - immutable
   - range - immutable
   - 문자열 - immutable
   - 바이너리(크게 비중X)

   순서 X 자료구조

   - set -mutable
   - dictionary - mutable

   

   ##### 연산자

   - 산술 연산자
     - `+`, `-`, `*`, `/`, `//`, `%`, `**` 

   - 비교 연산자
     - `<`, `<=`, `>`, `>=`, `==`, `!=`, `is`, `is not`

   - 논리 연산자
     - `and`, `or`, `not a`
     - 단축 평가
       - 첫 번째 값이 확실할 때, 두 번째 값 확인 X

   

   ##### 딕셔너리

   - key: value로 이루어진 자료구조형. 시퀀스X, mutable
   - 자료 구조를 순환할 때, 
     - dict.keys()로 key 순환
     - dict.values()로 value 값 순환
     - dict.items()로 key value 한번에 순환.

   

2. ### control_of_flow

   ##### 반복문

   - for 문
     - iterable 객체의 요소들을 순차적으로 코드 실행.
   - while 문
     - 조건을 걸어 해당 조건에 참일 경우 반복문 수행.
     - 종료조건을 꼭 설정해줘야 한다.

   ##### 조건문

   - if
   - elif
   - else

   ###### break

   반복문을 멈춤.

   ###### continue

   이후의 코드를 수행하지 않고, 다음 요소를 선택해 반복 수행.

   ###### else

   끝까지 반복문을 시행한 이후에 실행.

   ###### pass

   아무것도 하지 않는다. 다만, 문법적으로 문장이 필요할 때 등의 상황에 자리를 채우는 용도로 사용.



3. ### function

   ##### 함수의 인자

   - 함수는 기본적으로 인자를 위치에 따라 인식한다.

     - 기본 인자 값 설정 가능.(`인자=기본값`형식)
     - 인자의 위치에 따라 인식하는 함수의 특성 상, 기본값을 설정한 인자 이후에 기본값이 없는 인자를 사용할 수 없다.
     - 키워드 인자를 통해, 정의된 인자 순서에 상관 없이 인자 전달 가능. 단, 키워드 인자 뒤쪽에 위치 인자를 사용하면 안된다.

   - 가변 인자

     - 개수가 정해지지 않은 임의의 인자를 받기 위해 *args로 표현된 가변인자로 함수를 정의.

   - 정의되지 않은 키워드 인자.

     - dict 형태로 처리가 되며 **로 표현한다.

     

     `중요한 점!`
     `함수에 정의된 위치에 따라, 명확하게 인자를 구분할 수 없으면 사용할 수 없는 것이라 생각하자.`

     

     인자의 순서!

     `위치인자` < `가변인자` < `키워드인자`

   ##### 함수의 리턴

   - 오직 한 개의 객체만 반환.

   

   ##### 스코프

   - LEGB Rule

     - Local

       `함수 내부에서 만들어져 외부에서 접근 X`

     - Enclosed
       `함수 안의 함수가 있을 때, 지역 변수가 없다면 그 바깥 함수에서 해당 변수를 찾는다(클로저랑 비슷한 것 같다.)`

     - Global

       `함수 표현식 안에 없는 변수는 바깥에서 찾게 된다.`

     - Built-in
       `파이썬 안에 내장되어 있는 함수 또는 속성`





4. ### data_structure

   ##### map(function, iterable)

   - iterable의 모든 요소에 function을 적용한 후 결과를 반환.
   - return은 `map_object`이기 때문에 다른 함수 형태로 받아 사용해야 값 이용 가능.

   

   ##### zip(*iterables)

   - 복수의 iterable 객체를 모아준다.
   - return `zip_object`

   

   ##### filter(function, iterable)

   - iterable에서 function의 반환 결과가 True 인것만 구성하여 반환
   - return `filter object`

   

   ##### comprehension

   ###### 리스트 comprehension

   - 시퀀스의 요소 전부 또는 일부를 처리하고, 그 결과를 리스트로 돌려주는 간결한 방법.
   - [식 for 변수 in iterable]
   - list(식 for 변수 in iterable)

   ###### 리스트 comprehension + 조건문

   - [식 for 변수 in iterable if 조건식]
   - [식 if 조건식 else 식 for 변수 in iterable]

   - elif 의 경우
     - [식 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable]

   ###### list comprehension의 장점.

   1. 간결함 (코드가 줄었다고 해서 의미까지 축소되지 않음을 보장하는 간결함)
   2. 성능 (일반화하기엔 위험)
   3. 표현력 (pythonic)

   ##### 리스트 메소드

   - .append(x) : x 추가
   - .extend(iterable) : iterable 객체 내부 원소를 append
   - .insert(i, x) : i 인덱스에 X 추가
   - .remove(x) : 값이 x인 것을 삭제(제일 앞에 값.)
   - .pop(i) : i 인덱스의 값을 삭제하고 그 값을 반환.
   - .clear() : 리스트의 모든 항목 삭제.
   - .index(x[, i[, j]]) : 인덱스 i  또는 그 이후의 인덱스 j 전에 등장하는 x 의 값을 찾하 해당 인덱스 값 반환.
   - .count(x) : 시퀀스에 등장하는 x의 총 갯수.
   - .reverse() : 가변 시퀀스의 항목들의 순서를 뒤집는다.

   ##### copy

   - 얕은 복사와 깊은 복사 차이.



5. ### module

   ##### 모듈 사용법

   - import로 모듈을 이름 공간으로 가져온 뒤 사용.
   - from 모듈명 import 어트리뷰트



6. ### errors

   ##### 에러

   - SyntaxError(문법 에러)
     - Exceptions - 문법이나 표현식은 바르지만 실행 시 발생하는 에러.
       - zeroDivisionError(0으로 나눌 수 없다.)
       - NameError(정의되지 않은 변수 호출.)
       - TypeError(올바르지 않은 타입 사용 시.)
       - argument(누락, 많을 경우)(함수 호출 과정에서 필수 argument 누락 or 많을 때.)

   - ValueError
     - 타입은 올바르나 값이 적절하지 못할 때(int(3.5))
   - IndexError
     - 인덱스가 범위 바깥을 가리킬 때.
   - KeyError
     - 딕셔너리에 key가 없을 경우.
   - ModuleNotFoundError
     - 모듈을 찾을 수 없는 경우.
   - ImportError
     - 모듈을 찾았으나 가져오는 과정에서 실패하는 경우(대부분 없는 클래스/메소드를 불러올 때.)

   ##### 예외 처리

   - `Try` `except`

     `try`구문을 이용해 예외 처리 가능.

   - try:

     except 예외:

   - try 절이 실행된다. 예외가 발생할 경우 남은 부분을 수행하지 않고, excetp가 실행된다.

   - 반드시 수행해야 하는 문장은 finally 활용

     - 예외 발생 여부와 관계없이 try문을 떠날 때 항상 실행

   - assert 상태를 검증하는데 사용

7. ### OOP_basic

   > 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나이다. 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.
   >
   > 명령형 프로그래밍인 절차지향 프로그래밍에서 발전된 형태를 나타내며, 기본 구성요소는 다음과 같다.

   ##### 클래스(Class) -> 자주 사용하는 객체를 만들 수 있도록 미리 속성, 행위 등 필요한 것들을 정의해 놓은 것. (like 도장)

   - 객체를 표현하는 문법
   - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 **속성(attribute)**과 **행위(behavior)**를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있다.
   - 클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인하여야 한다.

   

   ##### 인스턴스(instance) -> 정의된 클래스에 따라 사용자가 만들어낸 것(like 도장으로 찍은 거.)

   - 클래스의 인스턴스/객체(실제로 메모리상에 할당된 것)
   - 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다.
   - 객체의 행위는 클래스에 정의된 행위에 대한 정의(메서드)를 공유함으로써 메모리를 경제적으로 사용한다.

   

   ##### 속성(attribute)

   - 클래스/인스턴스 가 가지고 있는 속성(값)

   - 메서드(Method) -> 클래스 or 인스턴스를 편리하게 사용할 수 있도록 정의해놓은 함수(ex-list.pop)
     - 클래스/인스턴스 가 할 수 있는 행위(함수)

   

   ##### 생성자(클래스를 생성할 때, `new` + `init`)

   - new를 통해 creat 되고, init를 통해 초기화 된다.

   메서드:

   - `__init__()`: 인스턴스가 생성된 후 자동으로 호출되어 실행.
   - `__del__()`: 인스턴스가 소멸되기 직전에 자동으로 호출되어 실행.
   - `__repr__`: 객체만 입력했을 때, 나오는 설명.
   - `__str__`: print(객체) 를 입력했을 때, 나오는 설명

   ###### `__매직메서드__`

   

8. ### oop_advanced

   ##### 클래스변수

   - 모든 인스턴스가 공유하는 클래스의 속성. 클래스 선언 블록 최상단에 위치.
   - class.변수 와 같이 접근(할당)

   

   ##### 인스턴스변수

   - 인스턴스들의 고유한 변수.
   - 인스턴스의 속성
   - 인스턴스 생성 이후 instance.변수 로 접근(할당)

   

   ##### 메소드 -> 인스턴스&클래스 메서드는 .method()를 입력하면 각각 인스턴스 자신, 클래스 자신이 인자로 넘어가게된다. 하지만 스태틱 메서드의 경우 인자가 넘어가지 않고 오류가 난다.

   ###### 인스턴스 메서드

   - 인스턴스가 사용할 메서드, 첫 번째 인자로 `self`를 받도록 정의. 인스턴스 객체 자신이 `self`가 된다.

   

   ###### 클래스 메서드

   - 클래스가 사용할 메서드.
   - 정의 위에 `@classmethod`라는 데코레이터를 사용한다. 첫 번째 인자로 클래스(cls)를 받도록 정의.
   - 이때 자동으로 클래스 객체가 `cls`가 된다.

   

   ###### 스태틱 메서드

   - 클래스가 사용할 메서드
   - 정의 위에 `@staticmethod` 데코레이터 사용\
   - 묵시적인 첫 번째 인자를 받지 않는다. 인자 정의가 자유롭다.
   - 어떠한 인자도 자동으로 넘어가지 않는다. -> 아무런 일도 자동으로 일어나지 않는다.

   

   #### 정리1. 인스턴스와 메서드

   - 인스턴스는 3가지 메서드에 모두 접근할 수 있다.(인스턴스, 클래스, 스태틱 메서드)
   - 하지만 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않아야 한다.(가능해도 사용하지 말자!)
   - 게다가 클래스간 상속이 있을 경우 다르게 동작한다.
   - 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계하자.

   #### 정리2. 클래스와 메서드

   - 클래스도 3가지 메서드에 모두 접근 할 수 있다.
   - 하지만 클래스에서 인스턴스 메서드는 호출하지 않는다.(가능해도 사용하지 말자!)
   - 클래스가 할 행동은 다음 원칙에 따라 설계한다.
     - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 __클래스 메서드__로 정의한다.
     - 클래스와 클래스 속성에 접근할 필요가 없다면 __스태틱 메서드__로 정의한다.

   

   ### 상속-클래스의 가장 큰 특징. 부모 클래스의 모든 속성이 자속에게 상속되도록 되어 있어 코드 재사용성이 높다.

   ```python
   class BabyClass(ParentClass):
       code block
   ```

   

   ##### SUPER() : 자식 클래스에서 메서드를 추가로 구현시, 부모 클래스의 내용을 사용하고자 할 때 사용.

   ```python
   class BabyClass(ParentClass):
       def method(self, arg):
           super().method(arg)
   ```

   ex.

   ```python
   class Person:
       def __init__(self, name, age, number, email):
           self.name = name
           self.age = age
           self.number = number
           self. email = email
           
       def greeting(self):
           print(f'반갑습니다. {self.name} 입니다.')
           
   class Student(Person):
       def __init__(self, name, age, number, email, student_id):
           self.name = name
           self.age = age
           self.number = number
           self. email = email
           self.student_id  = student_id
           
   p1 = Person('짱구', 6, 15, 'jjanggu@naver.com')
   s1 = Student('동동', 17, 21, 'dongdong2@gmail.com', 12014)
   ```

   Student 클래스는 Person의 클래스를 상속받았음에도 불구하고 name, age, number, email을 반복하는 코드가 있다. 이를 위해 super()을 사용하면

   ```python
   class Person:
       def __init__(self, name, age, number, email):
           self.name = name
           self.age = age
           self.number = number
           self. email = email
           
       def greeting(self):
           print(f'반갑습니다. {self.name} 입니다.')
           
   class Student(Person):
       def __init__(self, name, age, number, email, student_id):
           super().__init__(name, age, number, email)
           self.student_id  = student_id
           
   p1 = Person('짱구', 6, 15, 'jjanggu@naver.com')
   s1 = Student('동동', 17, 21, 'dongdong2@gmail.com', 12014)
   ```

   이와 같이 수정 가능.

   ##### 메서드 오버라이딩

   상속받은 메서드를 같은 이름의 메서드로 재 정의하여 덮어 쓰는 것.

   

   ##### 스코프

   기존: 인스턴스 -> 클래스 -> 전역

   상속 후: 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역

   

   ##### 다중 상속: 두개 이상의 클래스를 상속받은 경우.

   우선순위는 class chile(dad, mom): 일 때, dad가 먼저 상속되었기 때문에 dad를 따라가게 된다.

   

   ##### 클래스 매서드 vs 정적 메서드

   ```python
   class Animal:
       class_var = '이건 Animal 의 클래스 변수'
       
       def __init__(self):
           self.name = self.class_var
       
       def instance_method(self):
           return self.name
       @staticmethod
       def static_method():
           return Animal()
           
       @classmethod
       def class_method(cls):
           return cls()
       
       
   class Dog(Animal):
       class_var = '이건 지금 Dog의 변수'
       
   a = Dog.static_method()
   b = Dog.class_method()
   
   print(a.instance_method())
   print(b.instance_method())
   ```

   ```
   이건 Animal 의 클래스 변수
   이건 지금 Dog의 변수
   ```

   - 자식 클래스에서 부모 클래스에 있는 정적 메서드에 접근하면, 부모 클래스의 클래스 속성 값을 가져온다.
   - 자식 클래스에서 부모 클래스에 있는 클래스 메서드에 접근하더라도 `cls`인자 때문에 자식 클래스 자신이 호출되어 자식 클래스의 속성을 가져온다.

   #### 클래스 메서드를 사용하면 `cls`인자가 있기 때문에 그 자손, 부모 클래스에 관계 없이, 그 클래스 메서드를 호출한 클래스 자체의 속성을 우선순위로 접근하게 된다.





특히 파이썬의 가장 기초가 되는 01.python_intro와 앞으로 장고 수업에서 많이 활용될 
클래스의 개념을 설명하는 07.oop_basic 파트의 문제 비중이 높은 편입니다.
참고하여 시험 준비 해주세요 