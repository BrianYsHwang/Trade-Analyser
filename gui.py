import customtkinter as customtkinter
import matplotlib.pyplot as plt
from MovingAverage import MovingAverage as MA
import numpy as np
from config import API_KEY
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

customtkinter.set_default_color_theme("green")

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Tab creation with .add
        self.add("Menu")
        self.add("Graph")

        # add widgets on tabs
        self.tabMenu()
        self.tabGraph()
        
    def tabMenu(self): 
        self.label = customtkinter.CTkLabel(master=self.tab("Menu"))
        self.label.configure(text="MAIN MENU", padx=450, fg_color=('#00bb7c'), font=(None,20))
        # on the grid, can pad on x or y direction
        self.label.grid(row=0, column=1, padx=20, pady=10)


    def tabGraph(self): 
        plt.style.use('seaborn-v0_8-pastel')

        mdf = MA(API_KEY)
        mdf.retrieve_data('2020-01-01', '2023-01-01', 'AAPL')
        mdf.prepare_data()
        
        # creating a scatterplot of closing prices
        fig, ax = plt.subplots()
        x = mdf.data['date']
        y = mdf.data['close']

        ax.scatter(x,y,label='Closing Prices', color='blue', marker='.')

        canvas = FigureCanvasTkAgg(fig, master=self.tab("Graph"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=customtkinter.BOTH, expand=True)




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.geometry("800x800")    # W x H
        self.title("Trade Analyser Draft")
        
        
        # Tabview WIDGET 
        self.tab_view = MyTabView(master=self, width=800, height=700)    # can enter arguments for width/length of tab
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


# running the app
app = App()
app.mainloop()