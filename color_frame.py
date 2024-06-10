import customtkinter as ctk 


class ColorFrame(ctk.CTkFrame):

    #Class Constructour class
    #call 1 time when making object
    def __init__(self, container):
        super().__init__(container)
        #initial color value
        self.red_value, self.green_value, self.blue_value = "00", "00", "00"
        self.selected_color =   "#" + self.red_value + self.green_value + self.blue_value

        #making layout/intrface
        self.color_box = ctk.CTkLabel(self, fg_color=self.selected_color, text="", height=100, width=100)
        self.color_box.grid(row=0, column=0, columnspan=2, padx=30, pady=10)

        #color display/entry
        self.color_hex = ctk.CTkEntry(self, justify="center", width=100)
        self.color_hex.grid(row=1, column = 0, columnspan=2)
        self.color_hex.insert("end", self.selected_color)


        #Slider
        self.red_label = ctk.CTkLabel(self, text="R")
        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value: self.get_value(value, "red"))
        self.red_slider.set(0)

        self.green_label = ctk.CTkLabel(self, text="G")
        self.green_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value: self.get_value(value, "green"))
        self.green_slider.set(0)

        self.blue_label = ctk.CTkLabel(self, text="B")
        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value: self.get_value(value, "blue"))
        self.blue_slider.set(0)

        #making sliders appear

        self.red_label.grid(row=2, column=0, sticky="W", padx=(5, 0))
        self.red_slider.grid(row=2, column=1, sticky="W", padx=5)

        self.green_label.grid(row=3, column=0, sticky="W", padx=(5, 0))
        self.green_slider.grid(row=3, column=1, sticky="W", padx=5)

        self.blue_label.grid(row=4, column=0, sticky="W", padx=(5, 0))
        self.blue_slider.grid(row=4, column=1, sticky="W", padx=5)


    def get_value(self, value, color):
        #getting value from color and changing it when slider moves

        value = hex(int(value))
        
        #remove a value from left "lstrip", rstrip pemoves from right
        value = value.lstrip("0x")
        #adds zero
        value = value.zfill(2)

        if color == "red":
            self.red_value = value
        if color == "green":
            self.green_value = value
        if color == "blue":
            self.blue_value = value

        self.update_color()        

    def update_color(self):
        self.selected_color = f"#{self.red_value}{self.green_value}{self.blue_value}"
        self.color_box.configure(fg_color=self.selected_color)
        self.color_hex.delete(0, "end")
        self.color_hex.insert(0, self.selected_color)

    def get_color(self):
        return self.selected_color
    
    def set_color(self, color):

        r, g, b = color[1:3], color[3:5], color[5:7]
        self.red_value, self.green_value, self.blue_value = r, g, b

        self.red_slider.set(int(r, 16))
        self.green_slider.set(int(g, 16))
        self.blue_slider.set(int(b, 16))

        self.update_color()


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Color Box")
    
    color_frame = ColorFrame(app)
    color_frame.grid(row=0, column=0)
    

    app.mainloop()
    color_frame.save_colors("my_colors.txt")