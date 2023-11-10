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

def run_a_sh_with_params():
    run_a_sh("piano", "0.3")

# 버튼 생성
button_tune = tk.Button(root, text="튜닝하기", command=run_tune)
button_a_sh = tk.Button(root, text="악기 검출", command=run_a_sh_with_params)


# 버튼 배치
button_tune.pack(pady=10)
button_a_sh.pack(pady=10)

# GUI 시작
root.mainloop()
