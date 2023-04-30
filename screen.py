from tkinter import *
from tkinter import ttk
from read import read_draw, search_draw, search_num, select_num
from mega_sena import Web
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

screen = Tk()

number_search = []
number_set = set()
repetition = []


options_year = [2022, 2021]

class Application():
    def __init__(self) -> None:
        self.window = screen
        self.screen()
        self.frames()
        self.buttons()
        self.labels()
        self.label_db()
        self.inputs()
        self.plot()
        screen.mainloop()

    def screen(self):
        self.window.title("MegaSena")
        self.window.geometry('700x1000')
        self.window.configure(background="#333333")
        self.window.resizable(False, False)

    def frames(self):
        self.frame0 = Frame(self.window, bg='#686868',
                            highlightthickness=0.5, highlightbackground='white')
        self.frame0.place(relx=0.03, rely=0.02, relwidth=0.94, relheight=0.08)
        
        self.frame1 = Frame(self.window, bg='#686868',
                            highlightthickness=0.5, highlightbackground='white')
        self.frame1.place(relx=0.03, rely=0.12, relwidth=0.94, relheight=0.2)
        
        self.frame2 = Frame(self.window, bg='#686868',
                            highlightthickness=0.5, highlightbackground='white')
        self.frame2.place(relx=0.03, rely=0.34, relwidth=0.94, relheight=0.3)
        
        self.frame3 = Frame(self.window, bg='#686868',
                            highlightthickness=0.5, highlightbackground='white')
        self.frame3.place(relx=0.03, rely=0.66, relwidth=0.94, relheight=0.3)

    def buttons(self):
        self.bt_scrapping = Button(self.frame0, text='Scrapping', bg='#1f4788',
                                   foreground='white', command=self.window_scrapping)
        self.bt_scrapping.place(relx=0.05, rely=0.25, relwidth=0.1, relheight=0.5)
        
        self.bt_read = Button(self.frame0, text='Read', bg='#1f4788',
                                   foreground='white', command=self.show_draw)
        self.bt_read.place(relx=0.2, rely=0.25, relwidth=0.1, relheight=0.5)
        
        self.bt_year = Button(self.frame0, text='Year', bg='#1f4788',
                                   foreground='white', command=self.get_year)
        self.bt_year.place(relx=0.6, rely=0.25, relwidth=0.1, relheight=0.5)
        
        self.bt_search = Button(self.frame0, text='Search', bg='#1f4788',
                                   foreground='white', command=self.search_draw)
        self.bt_search.place(relx=0.85, rely=0.25, relwidth=0.1, relheight=0.5)
        
        self.bt_search = Button(self.frame1, text='Search', bg='#1f4788',
                                   foreground='white', command=self.search_faith_num)
        self.bt_search.place(relx=0.35, rely=0.15, relwidth=0.2, relheight=0.2)



    def labels(self):
        self.lb_draw = Label(self.frame0, text='Draw', background='#19B5FE')
        self.lb_draw.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.5)

        self.combobox = ttk.Combobox(self.frame0, values=options_year)
        self.combobox.set(2022)
        self.combobox.place(relx=0.7, rely=0.25, relwidth=0.1, relheight=0.5)

        self.n1 = Label(self.frame1, text=1, background='#19B5FE')
        self.n1.place(relx=0.05, rely=0.4, relwidth=0.1, relheight=0.2)
        
        self.n2 = Label(self.frame1, text=2, background='#19B5FE')
        self.n2.place(relx=0.35, rely=0.4, relwidth=0.1, relheight=0.2)
        
        self.n3 = Label(self.frame1, text=3, background='#19B5FE')
        self.n3.place(relx=0.65, rely=0.4, relwidth=0.1, relheight=0.2)

        self.n4 = Label(self.frame1, text=4, background='#19B5FE')
        self.n4.place(relx=0.05, rely=0.7, relwidth=0.1, relheight=0.2)

        self.n5 = Label(self.frame1, text=5, background='#19B5FE')
        self.n5.place(relx=0.35, rely=0.7, relwidth=0.1, relheight=0.2)

        self.n6 = Label(self.frame1, text=6, background='#19B5FE')
        self.n6.place(relx=0.65, rely=0.7, relwidth=0.1, relheight=0.2)



    def inputs(self):
        self.input_draw = Entry(self.frame0)
        self.input_draw.place(relx=0.45, rely=0.25, relwidth=0.1, relheight=0.5)

        self.input_n1 = Entry(self.frame1)
        self.input_n1.place(relx=0.15, rely=0.4, relwidth=0.1, relheight=0.2)    
        
        self.input_n2 = Entry(self.frame1)
        self.input_n2.place(relx=0.45, rely=0.4, relwidth=0.1, relheight=0.2)    

        self.input_n3 = Entry(self.frame1)
        self.input_n3.place(relx=0.75, rely=0.4, relwidth=0.1, relheight=0.2)    
        
        self.input_n4 = Entry(self.frame1)
        self.input_n4.place(relx=0.15, rely=0.7, relwidth=0.1, relheight=0.2)    

        self.input_n5 = Entry(self.frame1)
        self.input_n5.place(relx=0.45, rely=0.7, relwidth=0.1, relheight=0.2)    

        self.input_n6 = Entry(self.frame1)
        self.input_n6.place(relx=0.75, rely=0.7, relwidth=0.1, relheight=0.2)    


    def label_db(self):
        self.draw_list = ttk.Treeview(self.frame2, height=3,
                                     columns=('col1', 'col2', 'col3',
                                            'col4', 'col5', 'col6', 'col7',))
        
        self.draw_list.heading('#0', text='')
        self.draw_list.heading('#1', text='idDraw')
        self.draw_list.heading('#2', text='n1')
        self.draw_list.heading('#3', text='n2')
        self.draw_list.heading('#4', text='n3')
        self.draw_list.heading('#5', text='n4')
        self.draw_list.heading('#6', text='n5')
        self.draw_list.heading('#7', text='n6')

        self.draw_list.column('#0', width=1)
        self.draw_list.column('#1', width=50)
        self.draw_list.column('#2', width=50)
        self.draw_list.column('#3', width=50)
        self.draw_list.column('#4', width=50)
        self.draw_list.column('#5', width=50)
        self.draw_list.column('#6', width=50)
        self.draw_list.column('#7', width=50)

        self.draw_list.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        
        self.scroll_list = Scrollbar(self.frame2, orient='vertical')
        self.draw_list.configure(yscrollcommand=self.scroll_list.set)
        self.scroll_list.place(relx=0.96 , rely=0.01, relwidth=0.04, relheight=0.98)
        

    def get_year(self):
        self.year_selected = self.combobox.get()
        return self.year_selected
    
    def year_table(self):
        x = self.get_year()
        z = str(x)
        y = 's'+z
        return y


    def show_draw(self):
        table = self.year_table()
        self.clean()
        all_draw = read_draw(table)
        for i in all_draw:
            self.draw_list.insert('', 'end', values=i)
 
    def clean(self):
        self.draw_list.delete(*self.draw_list.get_children())
        self.input_n1.delete(0, END)
        self.input_n2.delete(0, END)
        self.input_n3.delete(0, END)
        self.input_n4.delete(0, END)
        self.input_n5.delete(0, END)
        self.input_n6.delete(0, END)
    
    def window_scrapping(self):
        window = Web('https://asloterias.com.br/resultados-da-mega-sena-2022')
        window.abrir_site('s2022')

        window2 = Web('https://asloterias.com.br/resultados-da-mega-sena-2021')
        window2.abrir_site('s2021')

    def search_draw(self):
        self.clean()
        self.draw_list.delete(*self.draw_list.get_children())
        draw = search_draw('s2022', self.input_draw.get())
        self.draw_list.insert(parent='', index=0, values=draw[0])
        self.input_n1.insert(0, draw[0][1])
        self.input_n2.insert(0, draw[0][2])
        self.input_n3.insert(0, draw[0][3])
        self.input_n4.insert(0, draw[0][4])
        self.input_n5.insert(0, draw[0][5])
        self.input_n6.insert(0, draw[0][6])

    # def search_faith_num(self):
    #     self.draw_list.delete(*self.draw_list.get_children())
    #     faith_draw = search_num(self.input_n1.get())
    #     self.draw_list.insert(parent='', index=0, values=faith_draw[0])

    def search_faith_num(self): 
        table = self.year_table()
        x = select_num(table)
        for i in x:
            if i[0] == self.input_n1.get():
                if i[1] == self.input_n2.get():
                    if i[2] == self.input_n3.get():
                        if i[3] == self.input_n4.get():
                            if i[4] == self.input_n5.get():
                                if i[5] == self.input_n6.get():
                                    print('Find')

    def num_plot(self):
        table = self.year_table()
        x = select_num(table)
        for i in x:
            for k in i:
                number_search.append(k)

        number_search.sort()
        
        for i in number_search:
            number_set.add(i)

    def repetition_count(self):
        z = 1
        for i in range(61):
            x = number_search.count(i)
            repetition.append(x)
        del repetition[0]
            

    def plot(self):
        # import numpy as np
        # self.num_plot()
        # self.repetition_count()

        # cm = 1/2.54  # centimeters in inches
        # figure = plt.Figure(figsize=(10*cm,5*cm), dpi=175)
        # ax = figure.add_subplot(111)
        # canva = FigureCanvasTkAgg(figure, self.frame3)
        # canva.get_tk_widget().place(relx=0.01, rely=0.01)

        # data = repetition


        # def func(pct, allvals):
        #     absolute = int(np.round(pct/100.*np.sum(allvals)))
        #     return f"{pct:.1f}%\n({absolute:d})"
        
        # wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
        #                                 textprops=dict(color="w"))
                                        

        # plt.setp(autotexts, size=8, weight="bold")
        # # ax.set_title("Numbers")

        # plt.show()
        ...
