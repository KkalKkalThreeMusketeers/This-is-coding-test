# 1 주차(3장. 그리디)
<br>

## 교재 문제

<br>

### 거스름돈

#### [코드]

```java
코드 작성란
```

<br>

#### [해결방안]

- 작성란

<br>

#### [어려웠던 부분]

- 작성란
---

### 큰 수의 법칙

#### [코드]

```java
코드 작성란
```

<br>

#### [해결방안]

- 작성란

<br>

#### [어려웠던 부분]

- 작성란
---

### 숫자 카드 게임

#### [코드]

```java
코드 작성란
```

<br>

#### [해결방안]

- 작성란

<br>

#### [어려웠던 부분]

- 작성란
---

### 1이 될 때까지

#### [코드]

```java
코드 작성란
```

<br>

#### [해결방안]

- 작성란

<br>

#### [어려웠던 부분]

- 작성란
---
---

<br><br>

## OJ 문제

<br>

### [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)

#### [코드]


```java
import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        //체육복 개수 배열 (인덱스가 학생)
        int[] num = new int[n];
        Arrays.fill(num, 1);
        
        for (int l : lost) {
            num[l - 1] -= 1;    
        }
        for (int r : reserve) {
            num[r - 1] += 1;
        }
        
        for (int i = 0; i < n; i++) {
            //앞 사람에게 빌리기
            if (i != 0 && num[i] == 0 && num[i - 1] == 2) {
                num[i] += 1;
                num[i - 1] -= 1;

            //뒷 사람에게 빌리기
            } else if (i != n - 1 && num[i] == 0 && num[i + 1] == 2) {
                num[i] += 1;
                num[i + 1] -= 1;
            }
        }
        
        //체육복이 1개 이상인 사람 수 구하기
        for (int i = 0; i < n; i++) {
            if (num[i] >= 1) {
                answer++;
            }
        }
        return answer;
    }
}
```

<br>

#### [해결방안]

- 체육복 개수를 담을 n크기의 배열을 만든다
- 앞 사람의 체육복 개수를 확인하고 2개라면 앞 사람한테 빌린다. 
  (내 체육복 수: +1, 앞 사람 체육복 수: -1)
- 앞 사람에게 못 빌린다면, 뒷사람의 체육복 개수를 확인하고 2개라면 뒷 사람에게 빌린다.
  (내 체육복 수: +1, 뒷 사람 체육복 수: -1)


<br>

#### [어려웠던 부분]

- 처음엔 빌려주는 방법을 어떻게 해야될지 떠올리지 못해서 생각하다가 순서대로(앞 사람 먼저 확인 후 뒷 사람) 빌리니 해결했다
---


### [조이스틱](https://programmers.co.kr/learn/courses/30/lessons/42860)

#### [코드]


```java
코드 작성란
```

<br>

#### [해결방안]

- 작성란

<br>

#### [어려웠던 부분]

- 작성란
---

### [큰 수 만들기](https://programmers.co.kr/learn/courses/30/lessons/42883)

#### [코드]


```java
코드 작성란
```

<br>

#### [해결방안]

- 작성란

<br>

#### [어려웠던 부분]

- 작성란
---

### [구명보트](https://programmers.co.kr/learn/courses/30/lessons/42885)

#### [코드]


```java
코드 작성란
```

<br>

#### [해결방안]

- 작성란

<br>

#### [어려웠던 부분]

- 작성란
---