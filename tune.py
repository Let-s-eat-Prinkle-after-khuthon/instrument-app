file_path = './note.txt'

with open(file_path, 'r+') as file:
    # 각 줄을 읽어와서 처리
    lines = file.readlines()
    file.seek(0)  # 파일 포인터를 파일의 처음으로 이동

    for line in lines:
        # 쉼표로 분리하여 리스트로 만들기
        values = line.strip().split(',')

        # 첫 번째 값과 세 번째 값을 0으로 바꾸기
        values[0] = str(float(values[0]) + 5)
        values[2] = str(float(values[2]) - 5)

        # 업데이트된 줄을 파일에 쓰기
        file.write(','.join(values) + '\n')

    # 기존 내용 끝까지 삭제
    file.truncate()
