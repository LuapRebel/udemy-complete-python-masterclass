import sqlite3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect('music.sqlite')

root = tkinter.Tk()
root.title('Music DB Browser')
root.geometry('1024x768')

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)
root.rowconfigure(2, weight=5)
root.rowconfigure(3, weight=1)

# ===== labels ======
tkinter.Label(root, text='Artists').grid(row=0, column=0)
tkinter.Label(root, text='Albums').grid(row=0, column=1)
tkinter.Label(root, text='Songs').grid(row=0, column=2)

# ===== artists Listbox =====
artistList = tkinter.Listbox(root)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

artistScroll = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=artistList.yview)
artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
artistList['yscrollcommand'] = artistScroll.set

# ===== Albums Listbox =====
albumLV = tkinter.Variable(root)
albumLV.set(("Choose an artist", ))
albumList = tkinter.Listbox(root, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

albumScroll = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=albumList.yview)
albumScroll.grid(row=1, column=1, sticky='nse', rowspan=1)
albumList['yscrollcommand'] = albumScroll.set

# ===== Songs Listbox =====
songLV = tkinter.Variable(root)
songLV.set(("Choose an album",))
songList = tkinter.Listbox(root, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

songScroll = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=songList.yview)
songScroll.grid(row=1, column=2, sticky='nse', rowspan=1)
songList['yscrollcommand'] = songScroll.set

# ===== Main Loop =====
testList = tuple(range(0, 100))
albumLV.set(testList)
root.mainloop()
print('closing database connection')
conn.close()
