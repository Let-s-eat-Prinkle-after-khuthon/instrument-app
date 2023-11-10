import tkinter as tk
import subprocess
from multiprocessing import Process

def run_tune():
    subprocess.run(["python", "tune.py"])

def run_a_sh(inst,conf):
    subprocess.run(["python","instrument_detect.py","--weights","./weights/" + inst + ".pt", "--img", "416", "--conf", conf, "--source", "register.jpg"])

# GUI 생성
root = tk.Tk()
root.title("버튼 프로그램")
root.geometry("400x300")

# Entry 위젯을 사용하여 두 개의 파라미터를 입력받을 수 있게 함
param1_entry = tk.Entry(root, width=20)
param2_entry = tk.Entry(root, width=20)

def run_a_sh_with_params():
    param1 = param1_entry.get()
    param2 = param2_entry.get()
    run_a_sh(param1, param2)

# 버튼 생성
button_tune = tk.Button(root, text="튜닝하기", command=run_tune)
button_a_sh = tk.Button(root, text="악기 검출", command=run_a_sh_with_params)

# Entry 위젯 배치
param1_entry.pack(pady=5)
param2_entry.pack(pady=5)

# 버튼 배치
button_tune.pack(pady=10)
button_a_sh.pack(pady=10)

# GUI 시작
root.mainloop()
