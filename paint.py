from tkinter import*
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk
from tkinter import messagebox

root = Tk()
root.title('vk paint program')
root.geometry('400x400')
brush_color='black'

def paint(e):
	#brush parameters
	brush_width='%0.0f'% float(my_slider.get())

	# brush_color="green"
	# brush type =BUTT,ROUND,PROJECTING
	brush_type2 =brush_type.get()
	x1 =e.x-1
	y1 =e.y-1

	x2 =e.x+1
	y2 = e.y+1
	my_canvas.create_line(x1,y1,x2,y2,fill=brush_color,width=brush_width,capstyle=brush_type2,smooth=True)
# CAPSTYLE IS USED TO SELECT DIFFERENT BRUSHES styles
#creatimg canvas
def change_brush_size(thing):
	slider_label.config(text='%0.0f'% float(my_slider.get()))
# change brush color
def change_brush_color():
	global brush_color
	brush_color= "black"
	# [1] to take hex code
	brush_color= colorchooser.askcolor(color=brush_color)[1]
# change_canvas_color
def change_canvas_color():
	global bg_color
	bg_color= "black"
	# [1] to take hex code         
	bg_color= colorchooser.askcolor(color=bg_color)[1]
	my_canvas.config(bg=bg_color)
# deleteall
def clear_screen():
	my_canvas.delete(ALL)
	my_canvas.config(bg="white")
def save_as_png():
	result=filedialog.asksaveasfilename(initialdir='c:/paint/',filetypes=(("png files", "*png"),("all files","*jpg")))
	result_label=Label(root,text=result)
	result_label.pack(pady=20)
	if result.endswith('.png'):
		pass
	else:
		result=result+'.png'
	# ???????? grabbing coordinates for x and y for window and canvas and save the stuff
	if result:
		x=root.winfo_rootx()+my_canvas.winfo_x()
		y=root.winfo_rooty()+my_canvas.winfo_y()
		x1=x+my_canvas.winfo_width()
		y1=y+my_canvas.winfo_height()
		ImageGrab.grab().crop((x,y,x1,y1)).save(result)
		# popup success msg
		messagebox.showinfo("image saved","your image is saved")

w=500
h=400
my_canvas=Canvas(root,width=w,height=h ,bg="white")
my_canvas.pack(pady=20)
# my_canvas.create_line(x1,y1,x2,y2,fill="red")
# button 1 when click it activate button 3 is right button
my_canvas.bind('<B1-Motion>',paint)

#BRUSH OPTION FRAME
brush_option_frame=Frame(root)
brush_option_frame.pack(pady=20)
#brush size
brush_size_frame=LabelFrame(brush_option_frame,text="Brush Size")
brush_size_frame.grid(row=0, column=0,padx=50)
#brush slider00000000000
my_slider=ttk.Scale(brush_size_frame,from_ =1,to=100,command=change_brush_size,orient=VERTICAL,value=10)
my_slider.pack(pady=10, padx=10)
#brush slider label
slider_label=Label(brush_size_frame,text=my_slider.get())
slider_label.pack(pady=5)
#brush type
brush_type_frame=LabelFrame(brush_option_frame,text="brush type",height=400)
brush_type_frame.grid(row=0,column=1,padx=50)
brush_type=StringVar()
brush_type.set("round")
#Create radio Buttons for Brush type
brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type,value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type,value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type,value="projecting")
brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)
# w is west to incline all text west

#change colors
change_colors_frame=LabelFrame(brush_option_frame,text="change colors")
change_colors_frame.grid(row=0,column=2)

#change brush color button
brush_color_button=Button(change_colors_frame,text="brush color", command=change_brush_color)
brush_color_button.pack(pady=10,padx=10)
#change canvas background color
canvas_color_button=Button(change_colors_frame,text="canvas color", command=change_canvas_color)
canvas_color_button.pack(pady=10,padx=10)
# program options frame
option_frame= LabelFrame(brush_option_frame,text="Program options")
option_frame.grid(row=0,column=3,padx=50)

clear_button=Button(option_frame,text='clear screen',command=clear_screen)
clear_button.pack(padx=10,pady=10)

save_image_button=Button(option_frame,text="save image PNG",command=save_as_png)
save_image_button.pack(pady=10,padx=10)

root.mainloop()
# to convert into an .exe file we must install pyinstaller and command is pyinstaller.exe --onefile --windowed paint.py