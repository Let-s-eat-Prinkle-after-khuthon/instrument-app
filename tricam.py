import cv2
import mediapipe as mp
import requests

url = "http://52.79.251.174:3000/inst/tri"

# MediaPipe Hands 모듈 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 나타냄

now = ""
past = ""

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    cv2.imwrite("register.jpg",frame)
    finger = []

    if not ret:
        break

    # BGR을 RGB로 변환
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 손 감지
    results = hands.process(rgb_frame)

    # 감지된 손이 있으면 손가락 표시
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            i = 0
            for point in hand_landmarks.landmark:
                # 각 손가락 끝점 좌표 추출
                
                if(i % 4 == 0 and i >= 4):
                    x, y = int(point.x * frame.shape[1]), int(point.y * frame.shape[0])
                    finger.append([x,y])
                    cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

                i = i + 1
    
    bit = "X"
    now = "X"
    with open('note.txt', 'r') as file:
            lines = file.readlines()
    for line in lines:
            values = line.strip().split(',')
            if len(values) == 6:
                x_min, y_min, x_max, y_max, confidence, class_label = map(float, values)
                annotation = {
                    "x_min": x_min,
                    "y_min": y_min,
                    "x_max": x_max,
                    "y_max": y_max,
                    "confidence": confidence,
                    "class_label": class_label}

                cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
                                    
                if len(finger) > 0:
                    size = annotation["x_max"] - annotation["x_min"]
                    dx = int(size) / 8

                    for loc in finger:
                        if (loc[0] < annotation["x_max"] and loc[0] > annotation["x_min"]):
                            if (loc[1] < annotation["y_max"] and loc[1] > annotation["y_min"]):
                                bit = "O"
                                now = "0"
                                break;
                        
    req = { "inst" : "tri", "note" : bit }
    if (now != past):
        past = now
        requests.post(url, data=req) 
                              
                        
                
    
    # 프레임 표시
    cv2.imshow('Hand Tracking', frame)
        
    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 객체와 창 해제
cap.release()
cv2.destroyAllWindows()
