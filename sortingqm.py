from tkinter import *
from tkinter import ttk
import random
from threading import Thread
from quicksort import quickSort
from mergesort import mergeSort
import time

root = Tk()
root.title('Quick Sort vs Merge Sort')
root.maxsize(1200, 500)
root.config(bg='black')

#variabel
data1 = []
data2 = []

def Generate():
    global data1
    global data2
    canvasQ.delete('all')
    canvasM.delete('all')
    size = int(sizeEntry.get())
    
    data1 = []
    data2 = []
    for _ in range(size):
        data1.append(random.randrange(1, 100))

    for i, val in enumerate(data1):
        data2.append(val)

    drawData1(data1, ['red' for x in range(len(data1))])
    drawData2(data2, ['red' for x in range(len(data2))])

def startAlgorithm():
    Thread(target = quick_sort).start()
    Thread(target = merge_sort).start()

def quick_sort():
    start_time = time.time()
    quickSort(data1, 0, len(data1)-1, drawData1, 0)
    drawData1(data1, ['green' for x in range(len(data1))])
    print("Quick Sort : --- %s seconds ---" % (time.time() - start_time))

def merge_sort():
    start_time = time.time()
    mergeSort(data2, drawData2, 0)
    drawData2(data2, ['green' for x in range(len(data2))])
    print("Merge Sort : --- %s seconds ---" % (time.time() - start_time))

def drawData1(data, colorArray):
    canvasQ.delete('all')
    c_height = 380
    c_width = 400
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
       #topleft
       x0 = i * x_width + offset + spacing
       y0 = c_height - height * 340
       #bottom right
       x1 = (i+1) * x_width + offset + spacing
       y1 = c_height


       canvasQ.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])


    root.update()

def drawData2(data, colorArray):
    canvasM.delete('all')
    c_height = 380
    c_width = 400
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
       #topleft
       x0 = i * x_width + offset + spacing
       y0 = c_height - height * 340
       #bottom right
       x1 = (i+1) * x_width + offset + spacing
       y1 = c_height


       canvasM.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    root.update()


#FRAME
UI_frame = Frame(root, width= 600, height= 200, bg='grey')
UI_frame.grid(row=1, column=0, padx=10, pady=5)
UI_frame2 = Frame(root, width= 600, height= 200, bg='grey')
UI_frame2.grid(row=1, column=2, padx=10, pady=5)


canvasQ = Canvas(root, width=400, height=380, bg='cyan')
canvasQ.grid(row=0, column=0, padx=10, pady=5)
canvasM = Canvas(root, width=400, height=380, bg='cyan')
canvasM.grid(row=0, column=2, padx=10, pady=5)
MainConsole = Frame(root, width= 200, height= 200, bg='grey')
MainConsole.grid(row=0, column=1, padx=10, pady=5)

#userInterface
#Row0 MainConsole
Label(MainConsole, text="Nilai N", bg='Grey').grid(row=0, column=0, padx = 10, pady=5)
sizeEntry = ttk.Entry(MainConsole)
sizeEntry.grid(row=0, column=1, padx=10, pady=5)
Button(MainConsole, text='Generate', command=Generate, bg='yellow').grid(row=1, column=1, padx=10, pady=5)
Button(MainConsole, text='Start', command=startAlgorithm, bg='green').grid(row=2, column=1, padx=10, pady=5)
#Row1
Label(UI_frame, text='Quick Sort', bg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
Label(UI_frame2, text='Merge Sort', bg='white').grid(row=0, column=1, padx=5, pady=5, sticky=W)


root.mainloop()
