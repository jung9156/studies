

# HTML

#### 부모, 형제 관계

```
<body>
  <h1> 웹문서 </h1>
  <ul>
    <li>HTML</li>
    <li>CSS</li>
  </ul>
</body>
```

부모 관계

- body - h1, ul
- ul-li

형제 관계

- h1-ul
- li-li

#### 

#### semantic - 내부적으로 활용(눈에 보이는 부분X)

- header : 문서 전체나 섹션의 헤더(머릿말 부분)
- nav : 네비게이션
- aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
- section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
- article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
- footer : 문서 전체나 섹션의 푸터(마지막 부분)
- h1
- table

#### Non semantic

- div
- span

#### 그룹 컨텐츠

- P
- hr
- ol, ul
- pre, blockquote
- figure div

#### 텍스트 관련

- a

- b vs `strong  강조!`

- i  vs `em  강조!`

  # b, i 는 html 자체에서 강조를 하려는 것.

  # -> html5부터는 css에서 스타일을 변화해야 하기 때문에 강조 의미를 나타내는 strong, em 을 사용하자.

  # 굵기, 기울이기 등은 css로 설정하자!(No `<b>`,`<i>` )

- span, br, img

- 기타 등등

#### Table

- tr, td, th
- thead, tbody, tfoot

##### `tfoot 의 경우 테이블의 합계 등에 사용하는데, tfoot 을 맨 위에 위치시켜도 시각적으로 맨 밑으로 위치 하지만, 시각 장애인 등이 접근했을 때, 합계를 먼저 듣는 등의 편의성 제공.`

- caption
- 셀 병합 속성 : colspan, rowspan
- scope 속성
- col colgroup

#### form - 서버에서 처리될 데이터를 제공하는 역할

- action
- method



# `태그 정리` - https://developer.mozilla.org/ko/docs/Web/HTML/Element