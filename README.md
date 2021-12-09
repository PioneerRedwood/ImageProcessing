# 파이썬 / 이미지 프로세싱 - KOREAN

## 파일 선택하여 열기 (pdf, png, jpg 확장자)
=> Matlab 혹은 다른 라이브러리를 활용해 렌더링

## 좌표 추출하기
=> 기록된 좌표에 대한 텍스트 파일 저장
문자열 태그나 변수 이름을 지정할 수 있음

## 문제점
- 특정 구역에 서명을 기재하는 것처럼 정확한 좌표가 필요
- 로드된 이미지를 변환하는 것
    - 작동하지 않음, 이미지가 움직이지 않음
- 말그대로 수퍼-닌자인 `🐱‍👤imutils🐱‍👤` 라이브러리를 사용하면 해결!
- 일반적인 pip 패키지 경로: C:\Users\$USERNAME\AppData\Local\Programs\Python\Python39\Lib\site-packages

## `imutils` 사용
- `cv2.EVENT_MOUSEWHEEL` 변수를 통해 보이는 페이지의 y 포지션을 볼 수 있음
- 이미지 처음 로드 시 크기를 적절하게 변경

## 키보드 입력
- Q, esc; exit program 프로그램 나가기
- DataType; N: None, D: Data, C: Check, S: Signature (태그 기능)
- 추후에, 저장하는 모듈을 추가할 예정

## 알림
만약 해당 기능을 자동으로 사용하기 원한다면, .exe 형태로 빌드, 컴파일하여 서버에서 실행하십시오.


## 프로젝트 마무리
- openCV를 사용한 이미지로부터 좌표 구하기를 시도
- `imutils`를 사용하여 이미지를 핸들
- `tkinter`를 사용하여 추가, 저장, 삭제, 수정으로 추적
- 프로젝트 끝맺음, 실제 이미지에서의 좌표와 렌더된 이미지의 좌표의 차이가 상이


# Python / ImageProcessing - English

## Open file select (extension type pdf, png, jpg)
=> using MatLab or other libraries rendering them

## Point out where you want extract coordinate
=> Save text file recorded coordinate infos
you can choose additional string tag or variable names ...

## Problem
- We need a precise coordinates like writing signature down in specific position.
- How about transform the image loaded window?
    - Not worked, the image did not move.
- Added helper library: imutils IT IS A LITTERALLY 🐱‍👤SUPER NINZA🐱‍👤 FOR ME.
- Generally using by pip package install path is C:\Users\$USERNAME\AppData\Local\Programs\Python\Python39\Lib\site-packages

## Using imutils
- cv2.EVENT_MOUSEWHEEL makes scroll showing paging another y position
- when image first loaded resize for image size pretty

## Keyboard input
- Q, esc; exit program
- DataType; N: None, D: Data, C: Check, S: Signature
- Later, save module will be added

#### Notice
If you want to make it automatically, build and compile to .exe file 
And execute in server-side


## End of project
- Getting coordinates of image                           => using opencv in python (cv2)
- Handling image pages                                   => using imutils module
- Tracking them with adding, getting, deleting, editing  => using tkinter for UI
- End of project, because of the gap of coordinates between real image and redered image
