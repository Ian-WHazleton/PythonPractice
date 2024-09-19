import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    #ints
    CalTextBoxStng = "0"
    CalList = []
    LastOp = ""
    NewNumber = False

    #images 

    #GUI setup
    def __init__(self):
        super().__init__()
        
        #create grid Layout 
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure((0,1,2,3,), weight=1)

        #Configure window
        self.title("PyCalculator")
        self.geometry(f"{450}x{600}")

        #create Sections
        self.NumPad = customtkinter.CTkFrame(self, width=450, corner_radius=0)
        self.NumPad.grid(row=3,column=0, rowspan=6)
        self.NumPad.grid_rowconfigure(6,weight=1)
        self.NumPad.grid_columnconfigure(5,weight=1)

        self.TopCal = customtkinter.CTkFrame(self,width=450,corner_radius=0)
        self.TopCal.grid(row=2,column=0)
        
        self.CalTextBox = customtkinter.CTkLabel(
            self.TopCal,
            text=self.CalTextBoxStng,
            font=("Times",30)
        )
        self.CalTextBox.grid(row=0,column=0)


        #create Buttons
        #Bottom of calculator
        self.ButtonNegate = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.Negate(),
            text= "+/-", width = 100,height=65,font=("Times",25)
        )
        self.ButtonNegate.grid(row=6,column=1)
        self.Button0 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("0"),
            text="0",width = 100,height=65,font=("Times",50)
        )
        self.Button0.grid(row=6,column=2)
        self.ButtonDec = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("."),
            text=".",width = 100,height=65,font=("Times",50)   
        )
        self.ButtonDec.grid(row=6,column=3)
        self.ButtonEqual = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.Equal(),
            text="=",width = 100,height=65,font=("Times bold",50,)   
        )
        self.ButtonEqual.grid(row=6,column=4)
        #Math
        self.ButtonPlus = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.PlusBut(),
            text="+",width = 100,height=65,font=("Times",50,)   
        )
        self.ButtonPlus.grid(row=5,column=4)

        self.ButtonSub = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.SubBut(),
            text="-",width = 100,height=65,font=("Times",50,)   
        )
        self.ButtonSub.grid(row=4,column=4)

        self.ButtonMult = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.MultBut(),
            text="x",width = 100,height=65,font=("Times",50,)   
        )
        self.ButtonMult.grid(row=3,column=4)

        self.ButtonDivde = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.DivdeBut(),
            text="÷",width = 100,height=65,font=("Times",50,)   
        )
        self.ButtonDivde.grid(row=2,column=4)

        self.ButtonBack = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.Equal(),
            text="=",width = 100,height=65,font=("Times bold",50,)   
        )
        self.ButtonEqual.grid(row=6,column=4)

        #Buttons 1-9
        self.Button1 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("1"),
            text="1",width = 100,height=65,font=("Times",50)
        )
        self.Button1.grid(row=5,column=1,padx=1,pady=1)

        self.Button2 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("2"),
            text="2",width = 100,height=65,font=("Times",50)
        )
        self.Button2.grid(row=5,column=2,padx=1,pady=1)
        self.Button3 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("3"),
            text="3",width = 100,height=65,font=("Times",50)
        )
        self.Button3.grid(row=5,column=3,padx=1,pady=1)
        self.Button4 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("4"),
            text="4",width = 100,height=65,font=("Times",50)
        )
        self.Button4.grid(row=4,column=1,padx=1,pady=1)
        self.Button5 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("5"),
            text="5",width = 100,height=65,font=("Times",50)
        )
        self.Button5.grid(row=4,column=2,padx=1,pady=1)
        self.Button6 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("6"),
            text="6",width = 100,height=65,font=("Times",50)
        )
        self.Button6.grid(row=4,column=3,padx=1,pady=1)
        self.Button7 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("7"),
            text="7",width = 100,height=65,font=("Times",50)
        )
        self.Button7.grid(row=3,column=1,padx=1,pady=1)
        self.Button8 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("8"),
            text="8",width = 100,height=65,font=("Times",50)
        )
        self.Button8.grid(row=3,column=2,padx=1,pady=1)
        self.Button9 = customtkinter.CTkButton(
            self.NumPad,
            command=lambda: self.TypeNum("9"),
            text="9",width = 100,height=65,font=("Times",50)
        )
        self.Button9.grid(row=3,column=3,padx=1,pady=1)
        
    
    def TypeNum(self,x):
        if self.NewNumber == True:
            self.CalTextBoxStng = x
            self.NewNumber = False
        elif self.CalTextBoxStng == "0":
            if x == ".":
                self.CalTextBoxStng = self.CalTextBoxStng + "."
            else:
                self.CalTextBoxStng = x
        else: 
            self.CalTextBoxStng = str(self.CalTextBoxStng) + x
        self.CalTextBox.configure(text=self.CalTextBoxStng)  # Update the label text


    def Negate(self):
        if self.CalTextBoxStng[0]=="-":
            self.CalTextBoxStng = self.CalTextBoxStng [1:]
        elif self.CalTextBoxStng == "0":
            return
        else:
            self.CalTextBoxStng = "-" + self.CalTextBoxStng
        self.CalTextBox.configure(text=self.CalTextBoxStng)  # Update the label text
        print(int(self.CalTextBoxStng))

    def PlusBut(self):    
        self.CalList.append(int(self.CalTextBoxStng))
        if self.LastOp=="Equal":
            return
        self.LastOp = "Plus"
        self.NewNumber = True
        print(self.CalList)
        if len(self.CalList) >= 2:
            self.Plus()
        self.CalTextBox.configure(text=self.CalTextBoxStng)  # Update the label text
        

    def SubBut(self):
        self.CalList.append(int(self.CalTextBoxStng))
        self.LastOp = "Sub"
        self.NewNumber = True
        print(self.CalList)
        if len(self.CalList) == 2:
            self.Sub()
        self.CalTextBox.configure(text=self.CalTextBoxStng)  # Update the label text
        
    def MultBut(self):
        self.CalList.append(int(self.CalTextBoxStng))
        self.LastOp = "Mult"
        self.NewNumber = True
        print(self.CalList)
        if len(self.CalList) == 2:
            self.Mult()
        self.CalTextBox.configure(text=self.CalTextBoxStng)  # Update the label text
        
    def DivdeBut(self):
        self.CalList.append(int(self.CalTextBoxStng))
        self.LastOp = "Divde"
        self.NewNumber = True
        print(self.CalList)
        if len(self.CalList) == 2:
            self.Divde()
        self.CalTextBox.configure(text=self.CalTextBoxStng)  # Update the label text
        
    def Plus(self):
        self.CalTextBoxStng = self.CalList[0]+self.CalList[1]
        self.CalList.clear()
        self.CalList.append(int(self.CalTextBoxStng))
        print(self.CalList)
        
    def Sub(self):
        self.CalTextBoxStng = self.CalList[0]-self.CalList[1]
        self.CalList.clear()
        self.CalList.append(int(self.CalTextBoxStng))
        print(self.CalList)

    def Mult(self):
        self.CalTextBoxStng = self.CalList[0]*self.CalList[1]
        self.CalList.clear()
        self.CalList.append(int(self.CalTextBoxStng))
        print(self.CalList)

    def Divde(self):
        self.CalTextBoxStng = self.CalList[0]/self.CalList[1]
        self.CalList.clear()
        self.CalList.append(int(self.CalTextBoxStng))
        print(self.CalList)
    

    actions = {
        "Plus":Plus,
        "Sub":Sub,
        "Mult":Mult,
        "Divde":Divde,
    }

    def Equal(self):
        if self.LastOp== "Equal":
            return
        self.CalList.append(int(self.CalTextBoxStng))
        if len(self.CalList) == 2:
            action = self.actions.get(self.LastOp)
            if action:
                action(self)
        self.CalTextBox.configure(text=self.CalTextBoxStng)
        self.LastOp="Equal"
        print(self.CalList,"\n",self.LastOp)
        self.CalTextBoxStng=""
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
