#Assignment 4 User Interface  
#Muhammad Anwar/100759431 
#April 8, 2023 
#This assignment is based at creating a user interface program that will accept the input of distance and select out of 2 options to convert either kilometers or miles then display the result. As well as include a reset and quit button.

from tkinter import*

#Define function for calculation for kilometers to miles 
def km_mi():
    try:
        km = float(Distance.get())
        mi = km / 1.60934
        calculation.config(text=f"{km} kilometers is equal to {mi:.2f} miles")
    except ValueError:
        calculation.config(text="ERROR: Please enter the correct input")

#Define function for calculation for miles to kilometers
def mi_km():
    try:
        mi = float(Distance.get())
        km = mi * 0.62139
        calculation.config(text=f"{mi} miles is equal to {km:.2f} kilometers")
    except ValueError:
        calculation.config(text="ERROR: Please enter the correct input")
        
#Define function for reset button
def reset(): 
    Distance.delete(0, END)
    calculation.config(text="Conversion")

#Make the window 
window = Tk() 
window.title("KiloMiles Calculator")
window.geometry("400x150")
window.configure(bg='White')

#Create a frame 
frame = Frame(window, padx=20, pady=20, bg='Black')
frame.pack()

#Include a label for distance
label = Label(frame, text="Enter the Distance:", fg='Red', bg='Blue')
label.grid(row=0, columnspan=1)

#Include entry distance  
Distance = Entry(frame, fg='Red', font=("Arial", 15))
Distance.grid(row=0,column=1)

#Make the choice for kilometers to miles 
km_to_mi = Radiobutton(frame, text='Kilometers to Miles', fg='blue', bg='Red', command=km_mi)
km_to_mi.grid(row=1, column=0)

#Make the choice for miles to kilometers 
mi_to_mi = Radiobutton(frame, text='Miles to Kilometers', fg='blue', bg='Red', command=mi_km)
mi_to_mi.grid(row=1, column=1)

#Include the result
calculation = Label(frame, text="Conversion", fg='Purple', bg='Yellow')
calculation.grid(row=2, columnspan=2)

#Make the quit button 
quit_button = Button(frame, text="Quit", fg='Green', bg='orange', command=window.quit)
quit_button.grid(row=3, column=0)

#Make the refresh button  
reset_button = Button(frame, text="Clear/Refresh", fg='Orange', bg='Green', command=reset)
reset_button.grid(row=3, column=1)

#Mainloop to start the program
window.mainloop()