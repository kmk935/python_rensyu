import tkinter

# ウィンドウ作成
root = tkinter.Tk()
root.title("ダンジョン＆パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

# キャンバス作成
canvas = tkinter.Canvas(width=620, height=434)
canvas.place(x=10,y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray")

# 画像データを読み込み
images = [tkinter.PhotoImage(file="img/chap6-mapfield.png"),
          tkinter.PhotoImage(file="img/chap6-mapwall.png"),
          tkinter.PhotoImage(file="img/chap6-mapgoal.png"),
          tkinter.PhotoImage(file="img/chap6-mapkey.png"),
          tkinter.PhotoImage(file="img/chap6-mapman.png")]

# マップデータ
MAX_WIDTH = 10
MAX_HEIGHT = 7
map_data = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 2, 0, 0, 1, 3, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

root.mainloop()
