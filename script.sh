#!/bin/bash

# git clone 명령어를 통해 리포지토리를 복제합니다.
git clone https://github.com/ultralytics/yolov5

# 복제한 디렉토리로 이동합니다.
cd ./yolov5

# 필요한 패키지들을 설치합니다.
pip install -r requirements.txt

# 다시 상위 디렉토리로 이동합니다.
cd ..

# 모든 .py 파일을 yolov5 디렉토리로 복사합니다.
cp *.py ./yolov5

# weights 디렉토리를 yolov5 디렉토리로 복사합니다.
cp -r weights ./yolov5

# yolov5 디렉토리로 이동합니다.
cd ./yolov5

# 필수 파일을 만듭니다.
touch note.txt
touch register.jpg
python gui.py