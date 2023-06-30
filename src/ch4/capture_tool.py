"""
プログラムを実行するには「pyautogui」が必要です。
$ pip install pyautogui

※ (メモ) pyautogui(0.9.54) は macOSで使う場合に、バグがありうまく動きません。
"""

import pyautogui
import datetime
import tkinter as tk
from tkinter import simpledialog

# 画面をキャプチャする
screenshot = pyautogui.screenshot()

# ファイル名を作成する
now = datetime.datetime.now()
filename = now.strftime("%Y%m%d%H%M%S") + ".png"

# キャプチャした画像をファイルに保存する
screenshot.save(filename)

# ユーザーに入力ダイアログを出して、画像タイトルを尋ねる
root = tk.Tk()
root.withdraw()
image_title = simpledialog.askstring("画像タイトル", "画像のタイトルを入力してください:")

# マークダウン形式でファイル「manual.md」にリンクを追記する
with open("manual.md", "a") as file:
    file.write(f"- [{image_title}]({filename})\n")

