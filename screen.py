from tkinter import *
from tkinter import ttk
from read import read_draw

screen = Tk()

options_year = [2022, 2021, 2020, 2019, 2018, 2017, 2016]

class Application():
    def __init__(self) -> None:
        self.window = screen
        self.screen()
        self.frames()
        self.buttons()
        self.labels()
        self.label_db()
        self.inputs()
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
                                   foreground='white', command='...')
        self.bt_scrapping.place(relx=0.05, rely=0.25, relwidth=0.1, relheight=0.5)
        
        self.bt_read = Button(self.frame0, text='Read', bg='#1f4788',
                                   foreground='white', command=self.show_draw)
        self.bt_read.place(relx=0.2, rely=0.25, relwidth=0.1, relheight=0.5)
        
        self.bt_year = Button(self.frame0, text='Year', bg='#1f4788',
                                   foreground='white', command=self.get_year)
        self.bt_year.place(relx=0.6, rely=0.25, relwidth=0.1, relheight=0.5)


    def labels(self):
        self.lb_draw = Label(self.frame0, text='Draw', background='#19B5FE')
        self.lb_draw.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.5)

        self.combobox = ttk.Combobox(self.frame0, values=options_year)
        self.combobox.set(2022)
        self.combobox.place(relx=0.7, rely=0.25, relwidth=0.1, relheight=0.5)

    def inputs(self):
        self.input_draw = Entry(self.frame0)
        self.input_draw.place(relx=0.45, rely=0.25, relwidth=0.1, relheight=0.5)

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
        print(self.year_selected)

    def show_draw(self):
        self.clean()
        all_draw = read_draw('sorteios')
        for i in all_draw:
            self.draw_list.insert('', 'end', values=i)

        
    def clean(self):
        self.draw_list.delete(*self.draw_list.get_children())
        # self.input_email_user.delete(0, END)
        # self.input_name_user.delete(0, END)
        # self.input_id_user.delete(0, END)
        # self.input_plan_user.delete(0, END)
        # self.input_type_user.delete(0, END)
        # self.input_age_user.delete(0, END)
        # self.input_update_user.delete(0, END)
        # self.input_update1_user.delete(0, END)


