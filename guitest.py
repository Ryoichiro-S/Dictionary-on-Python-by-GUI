#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import os



#pandas Excel 読込

"""d=df['分類'].value_counts().to_dict()
categoly=[]
for key,value in d.items():
    categoly.append(key+"({})".format(value))"""

file="//相対パスをかくtranslate.xlsx"

def  first_gui():

    def database(file):
        df=pd.read_excel(file)
        return df
    database(file)
    def change_db():
        root.withdraw()
        fTyp=[("","*xlsx")]
        iDir=os.path.abspath(os.path.dirname(__file__))
        tk.messagebox.showinfo("辞書アプリ","変更するエクセルデータを選んでください")
        file=tk.filedialog.askopenfilename(ftypes=fTyp,initialdir=iDir)
        tk.messagebox.showinfo("辞書アプリ",file)
        database(file)



    def newdis():
        text=entry1.get()
        root.destroy()
        result_gui(text)


    def explore():
        #entryウィジェットのテキストを読み取る
        text=entry1.get()
        return text

    #GUI ベース部分
    root = tk.Tk()
    root.title("辞書アプリ")
    root.geometry("400x300")
    #データーベースの変更
    frame=tk.Frame(root,bd=2,relief="ridge")
    frame.pack(fill="x")
    button=tk.Button(frame,text="データーベースの変更",command=change_db)
    button.pack()


    #検索画面

    label1=tk.Label(root,text="English→日本語",font=25)
    label1.pack(fill="x")

    frame1=tk.Frame(root,pady=10)
    frame1.pack()
    #チェックボタン
    #初期値をチェックしている状態にする
    bln=tk.BooleanVar()
    bln.set(True)
    check1=tk.Checkbutton(frame1,variable=bln)
    check1.pack(side="left")
    label2=tk.Label(frame1,font=("",14),text="英単語")
    label2.pack(side="left")
    entry1=tk.Entry(frame1,font=("",14),justify="center",width=15)
    entry1.pack()
    button1=tk.Button(root,text="検索",
                        font=("",16),
                        width=10,bg="gray",command=newdis)

    button1.pack()
    root.mainloop()







def result_gui(keywords):
    df=pd.read_excel(file)
    d=df['分類'].value_counts().to_dict()
    categoly=[]
    for key,value in d.items():
        categoly.append(key+"({})".format(value))

    def return_button():
        root.destroy()
        first_gui()
    def quit_button():
        root.destroy()
    #print(categoly)
    #callback関数
    #結果表示
#    def explore_botton(keywords):
    root = tk.Tk()
    root.title("辞書アプリ")
    root.geometry("400x300")



    df_result=df[df["英語"]==str(keywords)]
    ja=df_result["日本語"].values.tolist()
    lframe1=tk.LabelFrame(root,text="日本語",width=300,height=60,relief="groove")
    lframe1.pack(padx=5,pady=5)
    entry2=tk.Entry(lframe1,font=("",14),justify="center",width=200)
    entry2.pack()
    entry2.insert(tk.END,ja)

    #label5=tk.Label(lframe1,font=("",30),text=ja)
    #label5.pack()

    frame3=tk.Frame(root,pady=10)
    frame3.pack()
    botton2=tk.Button(frame3,text="もう一度",command=return_button)
    botton2.pack(side="left")
    botton3=tk.Button(frame3,text="終了する",command=quit_button)
    botton3.pack(side="left")
    root.mainloop()





# メインループ
first_gui()


#次やること
#データーベースを変える方法
