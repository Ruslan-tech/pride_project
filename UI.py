import tkinter as tk
from tkinter import *
from tkinter import ttk


class MainWindow(tk.Tk):
    """Основное рабочее окно с таблицами"""
    __tender_status = ['на рассмотрении', 'участвуем', 'не участвуем']

    def __init__(self, geom: str, title: str) -> None:
        super().__init__()
        self.geometry(geom)
        self.title(title)
        self.btn_view_tender = ttk.Button(text='Посмотреть', command=self.tenders_distributed_form).pack()
        self.notebook = ttk.Notebook()
        self.notebook.pack(expand=True, fill=BOTH)
        self.frame_all = ttk.Frame(self.notebook)
        self.frame_all.pack(expand=True, fill=BOTH)
        self.frame_notebook = ttk.Frame(self.notebook)
        self.frame_notebook.pack(expand=True, fill=BOTH)
        self.frame_inprocess = ttk.Frame(self.notebook)
        self.frame_inprocess.pack(expand=True, fill=BOTH)
        self.frame_wait_res = ttk.Frame(self.notebook)
        self.frame_wait_res.pack(expand=True, fill=BOTH)
        self.frame_win = ttk.Frame(self.notebook)
        self.frame_win.pack(expand=True, fill=BOTH)
        self.notebook.add(self.frame_all, text='Все конкурсы')
        self.notebook.add(self.frame_notebook, text='Распределенные')
        self.notebook.add(self.frame_inprocess, text='Просчет')
        self.notebook.add(self.frame_wait_res, text='Поданные')
        self.notebook.add(self.frame_win, text='Выигранные')
        self.col = ('ID', 'Номер конкурса', 'Заказчик', 'Дата публ.', 'Дата оконч.', 'Сумма', 'Тема',
                    'Ответств.', 'Статус', 'Комментарии')
        self.tree = ttk.Treeview(self.frame_notebook, columns=self.col, show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.tree_all_tenders = ttk.Treeview(self.frame_all, columns=self.col, show="headings")
        self.tree_all_tenders.pack(fill=BOTH, expand=1)
        self.tree_in_process = ttk.Treeview(self.frame_inprocess, columns=self.col, show="headings")
        self.tree_in_process.pack(fill=BOTH, expand=1)
        self.set_column_title()
        self.mainloop()

    def set_column_title(self):
        """Заполнение названий заголовков таблиц"""
        for i in self.col:
            self.tree.heading(i, text=i)
            self.tree_all_tenders.heading(i, text=i)
            self.tree_in_process.heading(i, text=i)

    def tenders_distributed_form(self):
        distrib_form = Toplevel()
        distrib_form.title("Рaспределение конкурса")
        distrib_form.geometry("500x500")
        ttk.Label(distrib_form,  text='Номер конкурса').pack()
        tend_number = ttk.Label(distrib_form, text='').pack()
        ttk.Label(distrib_form, text='Заказчик').pack()
        tend_customer = ttk.Label(distrib_form, text='').pack()
        ttk.Label(distrib_form, text='Дата публикации').pack()
        tend_date_public = ttk.Label(distrib_form, text='').pack()
        ttk.Label(distrib_form, text='Дата подачи').pack()
        tend_date_finish = ttk.Label(distrib_form, text='').pack()
        ttk.Label(distrib_form, text='Сумма конкурса').pack()
        tend_summ = ttk.Label(distrib_form, text='').pack()
        ttk.Label(distrib_form, text='Предмет договора').pack()
        tend_theeme = ttk.Label(distrib_form, text='').pack()
        ttk.Label(distrib_form, text='Ответственый').pack()
        utend_user = ttk.Combobox(distrib_form).pack()
        ttk.Label(distrib_form, text='Статус').pack()
        tend_status = ttk.Combobox(distrib_form, values=self.__tender_status).pack()
        ttk.Label(distrib_form, text='Комментарии').pack()
        tend_comments = ttk.Entry(distrib_form, justify=LEFT).pack(fill=X, padx=20, pady=20)
        btn_ok = ttk.Button(distrib_form, text="OK").pack()
        btn_apply = ttk.Button(distrib_form, text="Применить").pack()
        btn_cancel = ttk.Button(distrib_form, text="Отмена").pack()


# for d in db.select_distrib_man('allTenders', 1):
#     tree.insert("", END, values=d)

# for d in db.select_all_data('allTenders'):
#     tree_all_tenders.insert("", END, values=d)


class AuthWindow(tk.Tk):
    def __init__(self, geom: str, title: str) -> None:
        super().__init__()
        self.geometry(geom)
        self.title(title)
        self.lbl_auth = ttk.Label(self, text='АВТОРИЗАЦИЯ').grid(row=0, column=0)
        self.lbl_entry_username = ttk.Label(self, text='Имя пользователя').grid(row=1, column=0)
        self.entry_username = ttk.Entry().grid(row=1, column=1)
        self.lbl_entry_pass = ttk.Label(text='Пароль').grid(row=2, column=0)
        self.entry_pass = ttk.Entry().grid(row=2, column=1)
        self.btn_login = ttk.Button(text='Войти').grid(row=3, column=0)
        self.btn_exit = ttk.Button(text='Отмена').grid(row=3, column=1)
        self.mainloop()

# auth_wind = AuthWindow("300x200", 'АВТОРИЗАЦИЯ')
