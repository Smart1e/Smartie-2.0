import tkinter as tk
from time import sleep

loop = 0
root = tk.Tk()
root.geometry("1000x806")
root.configure(bg = "#ff9494")
root.resizable(False, False)
if loop == 1:
    sleep(2)





class sign_in_ui():
    in_root = True
    
    
    canvas = tk.Canvas(root,bg = "#ff9494",height = 806,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    
    
    img0 = tk.PhotoImage(file = f"Data/sign_in/img0.png")
    b0 = tk.Button(image = img0,borderwidth = 0,highlightthickness = 0,command=lambda: sign_in_ui.transition("1000x806", "442x806"),relief = "flat")
    
    img1 = tk.PhotoImage(file = f"Data/sign_in/img1.png")
    b1 = tk.Button(image = img1,borderwidth = 0,highlightthickness = 0,state="normal",relief = "flat")
       
    img2 = tk.PhotoImage(file = f"Data/sign_in/img2.png")
    b2 = tk.Button(image = img2,borderwidth = 0,highlightthickness = 0,state="normal",relief = "ridge")
          
    Entry0_img = tk.PhotoImage(file = f"Data/sign_in/img_textBox0.png")
    Entry0_bg = canvas.create_image(499.5, 439.5,image = Entry0_img)
    Entry0 = tk.Entry( bd = 0,bg = "#FFD1D1",highlightthickness = 0)
    
    Entry1_img = tk.PhotoImage(file = f"Data/sign_in/img_textBox1.png")
    Entry1_bg = canvas.create_image(511.5, 204.5,image = Entry1_img)
    Entry1 = tk.Entry(bd = 0,bg = "#FFD1D1",highlightthickness = 0)
    """
    Here is the explanation for the code above:
    1. The first line is the path to the python language file.
    2. The second line is the path to the image file used for the button.
    3. The third line is the code that creates the button.
    4. The fourth line is the path to the image file used for the button.
    5. The fifth line is the code that creates the button.
    6. The sixth line is the path to the image file used for the button.
    7. The seventh line is the code that creates the button.
    8. The eighth line is the path to the image file used for the text box.
    9. The ninth line is the code that creates the text box.
    10. The tenth line is the code that creates the text box.
    11. The eleventh line is the path to the image file used for the text box.
    12. The twelfth line is the code that creates the text box.
    13. The thirteenth line is the code that creates the text box. 
    """

    def transition(passthrough1, passthrough2):
        sign_in_ui.remove()
        sign_in_ui.in_root = False
        window_size = update_root_size(root)
        window_size.update_size_x(passthrough1, passthrough2)
        
        """
        Here is the explanation for the code above:
        1. We get the root window size and the passthrough windows size.
        2. We remove the sign_in_ui and set it's in_root to False.
        3. We update the root window size
        4. We update the passthrough window size
        """

    def add():
        

        sign_in_ui.b0.place(x = 384, y = 566,width = 231,height = 223)   
        sign_in_ui.Entry0.place(x = 274, y = 413,width = 451,height = 51)     
        sign_in_ui.b1.place(x = 365, y = 307,width = 269,height = 65)
        sign_in_ui.Entry1.place(x = 286, y = 178,width = 441,height = 41)
        sign_in_ui.b2.place(x = 365, y = 72,width = 269,height = 65)

        """
        Here is the explanation for the code above:
        1. First, we import the tkinter module. 
        2. Next, we create a class named Window. 
        3. We initialise the window by using the __init__ method. 
        4. Then, we create the window by using the create_window method. 
        5. We set the window size and title using the title and geometry methods. 
        6. We set the window icon by using the iconbitmap method. 
        7. We create the background image by using the PhotoImage method. 
        8. We create a canvas by using the Canvas method. 
        9. We set the background image to the canvas by using the create_image method. 
        10. We set the canvas size by using the pack method. 
        11. We create the widgets by using the Button, Label, Entry, and Text methods. 
        12. We set the widget attributes by using the place method. 
        13. Finally, we run the mainloop method.
        """
        
        
    def remove():
        sign_in_ui.b0.destroy()
        sign_in_ui.Entry0.destroy()   
        sign_in_ui.b1.destroy()
        sign_in_ui.Entry1.destroy()
        sign_in_ui.b2.destroy()
        sign_in_ui.canvas.delete("all")
        
        """
        Destroys all of the sign in widgets.
        """

class update_root_size(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs, bg='#FF9494')
        self._count = 0
        
        """
        Here is the explanation for the code above:
        1. The __init__ function is called when an instance of the class is created. 
        2. tk.Label.__init__(self, *args, **kwargs, bg='#FF9494') calls the __init__ function of the tk.Label class. 
        3. self._count = 0 sets the default value for the _count variable to 0.
        """

    def update_size_x(self, old_size, new_size):

        
        old_num =  old_size.split('x')
        old_x = int(old_num[0])
        old_y = int(old_num[1])
        
        new_num = new_size.split('x')
        new_x = int(new_num[0])
        new_y = int(new_num[1])
        
        global sign_in
        
        if old_x > new_x:
            root.geometry(f"{old_x}x{old_y}")
            old_x = old_x - 2
            current_size = f"{old_x}x{old_y}"
            self.after(2, lambda: self.update_size_x(current_size, new_size))
            
        """
        Here is the explanation for the code above:
        1. We use the .split() method on the old_size and new_size variables to split them into a list.
        2. We use the int() function to convert the string values into integers.
        3. We use the global keyword to make the sign_in variable global so that we can access it from anywhere in the program.
        4. We use an if statement to check if the old_x value is greater than the new_x value. If it is, we set the window's geometry to the current size.
        5. We subtract 2 from the old_x variable.
        6. We set the current_size variable to the old_x and old_y variables, and use the f-string to convert them into a string.
        7. We use the .after() method to delay the execution of the recursive function for 2 milliseconds.
        8. We call the recursive function again, and pass the current_size and new_size variables as the arguments.
        """
    
    def update_size_y(self, old_size, new_size):
        old_num =  old_size.split('x')
        old_x = int(old_num[0])
        old_y = int(old_num[1])
        
        new_num = new_size.split('x')
        new_x = int(new_num[0])
        new_y = int(new_num[1])
        
        global sign_in
        
        if old_y > new_y:
            root.geometry(f"{old_x}x{old_y}")
            old_y = old_y - 2
            current_size = f"{old_x}x{old_y}"
            self.after(2, lambda: self.update_size_y(current_size, new_size))
        """
        Here is the explanation for the code above:
        1. old_size is the current size of the window
        2. new_size is the size that the window should be
        3. old_num and new_num are the list of the x and y dimensions of the old_size and new_size
        4. old_x and old_y are the x and y dimensions of the old_size
        5. new_x and new_y are the x and y dimensions of the new_size
        6. The if statement checks if the old_y is greater than the new_y
        7. If it is, the root.geometry() method is used to set the current size of the window
        8. Then, old_y is decreased by 2
        9. current_size is set to the new window size
        10. self.after() is used to call the update_size_y() method again with the new window size and new_size as arguments
        11. This is repeated until the window reaches its new size
        """







size = update_root_size(root)
size.grid(row=900, column=900)
sign_in_ui.add()


root.mainloop()
