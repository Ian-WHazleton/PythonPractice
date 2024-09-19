import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    # Initial values
    CalTextBoxStng = "0"
    CalList = []
    LastOp = ""
    NewNumber = False
    LastWasOperator = False  # Track last button pressed

    def __init__(self):
        super().__init__()
        
        # Create grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3,), weight=1)

        # Configure window
        self.title("PyCalculator")
        self.geometry(f"{450}x{600}")

        # Create sections
        self.NumPad = customtkinter.CTkFrame(self, width=450, corner_radius=0)
        self.NumPad.grid(row=3, column=0, rowspan=6)
        self.TopCal = customtkinter.CTkFrame(self, width=450, corner_radius=0)
        self.TopCal.grid(row=2, column=0)

        self.CalTextBox = customtkinter.CTkLabel(
            self.TopCal,
            text=self.CalTextBoxStng,
            font=("Times", 30)
        )
        self.CalTextBox.grid(row=0, column=0)

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            ("+", self.PlusBut, 5, 4),
            ("-", self.SubBut, 4, 4),
            ("x", self.MultBut, 3, 4),
            ("÷", self.DivdeBut, 2, 4),
            ("0", lambda: self.TypeNum("0"), 6, 2),
            (".", lambda: self.TypeNum("."), 6, 3),
            ("=", self.Equal, 6, 4),
            ("+/-", self.Negate, 6, 1)
        ]

        for text, command, row, col in button_texts:
            button = customtkinter.CTkButton(
                self.NumPad,
                command=command,
                text=text,
                width=100,
                height=65,
                font=("Times", 50)
            )
            button.grid(row=row, column=col, padx=1, pady=1)

        for i in range(1, 10):
            button = customtkinter.CTkButton(
                self.NumPad,
                command=lambda x=i: self.TypeNum(str(x)),
                text=str(i),
                width=100,
                height=65,
                font=("Times", 50)
            )
            button.grid(row=(5 - (i - 1) // 3), column=(i - 1) % 3 + 1, padx=1, pady=1)

    def TypeNum(self, x):
        if self.NewNumber:
            self.CalTextBoxStng = x
            self.NewNumber = False
            self.LastWasOperator = False
        elif self.CalTextBoxStng == "0":
            if x == ".":
                self.CalTextBoxStng += "."
            else:
                self.CalTextBoxStng = x
        else:
            self.CalTextBoxStng += x
        self.CalTextBox.configure(text=self.CalTextBoxStng)

    def Negate(self):
        if self.CalTextBoxStng[0] == "-":
            self.CalTextBoxStng = self.CalTextBoxStng[1:]
        elif self.CalTextBoxStng == "0":
            return
        else:
            self.CalTextBoxStng = "-" + self.CalTextBoxStng
        self.CalTextBox.configure(text=self.CalTextBoxStng)

    def set_operation(self, operation):
        if self.LastWasOperator:
            return  # Prevent processing if last button was an operator

        self.CalList.append(int(self.CalTextBoxStng))
        if len(self.CalList) == 2:
            method = getattr(self, operation, None)
            if callable(method):
                self.CalTextBoxStng = str(method())
            self.CalList.clear()
            self.CalList.append(int(self.CalTextBoxStng))

        self.LastOp = operation
        self.NewNumber = True
        self.LastWasOperator = True  # Set the flag to True
        self.CalTextBox.configure(text=self.CalTextBoxStng)

    def PlusBut(self): self.set_operation("Plus")
    def SubBut(self): self.set_operation("Sub")
    def MultBut(self): self.set_operation("Mult")
    def DivdeBut(self): self.set_operation("Divde")

    def Plus(self):
        return self.CalList[0] + self.CalList[1]

    def Sub(self):
        return self.CalList[0] - self.CalList[1]

    def Mult(self):
        return self.CalList[0] * self.CalList[1]

    def Divde(self):
        return self.CalList[0] / self.CalList[1]

    def Equal(self):
        if self.LastWasOperator:
            return  # Prevent processing if last button was an operator
        self.CalList.append(int(self.CalTextBoxStng))
        if len(self.CalList) == 2:
            method = getattr(self, self.LastOp, None)
            if callable(method):
                self.CalTextBoxStng = str(method())
        self.CalTextBox.configure(text=self.CalTextBoxStng)
        self.LastOp = "Equal"
        self.CalTextBoxStng = ""
        self.LastWasOperator = False  # Reset the flag

if __name__ == "__main__":
    app = App()
    app.mainloop()
