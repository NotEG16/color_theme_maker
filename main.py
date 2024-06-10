import tkinter as tk
import customtkinter as ctk

from color_frame import ColorFrame

#theme
ctk.set_appearance_mode("Dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Color Theme Maker")

        self.configure(padx=10, pady=10)
        self.resizable(0, 0)


        #list
        self.color_frame = []

        for i in range(4):
            cf = ColorFrame(self)
            cf.grid(row=0, column=i)
            self.color_frame.append(cf)

        #menu
        self.menu = tk.Menu(self)
        self.menu.configure(bg="#ff0000")
        self.configure(menu=self.menu)
        self.menu.add_command(label="Save", command=self.save_color)
        self.menu.add_command(label="Load", command=self.load_colors)

        #adding function that happens after closing window
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.load_colors()

    def save_color(self):       
        with open("my_colors.txt", "w") as colors:    
            for color_frame in self.color_frame:
                print(color_frame.get_color())
                color = color_frame.get_color()
                colors.write(f"{color}\n") 
                
    def load_colors(self):  
        with open("my_colors.txt", "r") as f:            
            data = f.read()
            colors = data.split()
            i = 0
            for cf in self.color_frame:
                print(i, cf)
                cf.set_color(colors[i])
                i += 1
    
    def on_closing(self):
        # when window closes
        # save colors
        self.save_color()
        # close program window    
        self.destroy()
            
           

        
            
            

#enter app
if __name__ == "__main__":
    app = App()
    app.mainloop()

   