import customtkinter

class AlgalBloomGui:
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    def __init__(self):
        self.root = customtkinter.CTk()

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.root.geometry("900x900")

        self.button = customtkinter.CTkButton(self.root, text=".", font=('Ariel', 1), command=self.click)
        self.button.pack(padx=1, pady=1)

        self.root.mainloop()
    
    def click(self):
        print("you clicked lil bro!")

AlgalBloomGui()
