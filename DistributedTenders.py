# from tkinter import *
# from tkinter import ttk
# from main import Tender
# from ex1 import *


# root = Tk()
# root.geometry("1200x600")



# notebook = ttk.Notebook()
# notebook.pack(expand=True, fill=BOTH)

# frame_all = ttk.Frame(notebook)
# frame_all.pack(expand=True, fill=BOTH)
# frame_notebook = ttk.Frame(notebook)
# frame_notebook.pack(expand=True, fill=BOTH)
# frame_inprocess = ttk.Frame(notebook)
# frame_inprocess.pack(expand=True, fill=BOTH)
# frame_wait_res = ttk.Frame(notebook)
# frame_wait_res.pack(expand=True, fill=BOTH)
# frame_win = ttk.Frame(notebook)
# frame_win.pack(expand=True, fill=BOTH)



# notebook.add(frame_all, text='Все конкурсы')
# notebook.add(frame_notebook, text='Распределенные')
# notebook.add(frame_inprocess, text='Просчет')
# notebook.add(frame_wait_res, text='Поданные')
# notebook.add(frame_win, text='Выигранные')

# n = "python DistributedTenders.py"


# col = ('ID', 'Номер конкурса', 'Заказчик', 'Дата публ.', 'Дата оконч.', 'Сумма', 'Тема', 'Ответств.', 'Статус', 'Комментарии')

# tree = ttk.Treeview(frame_notebook, columns=col, show="headings")
# tree.pack(fill=BOTH, expand=1)
# tree_all_tenders = ttk.Treeview(frame_all, columns=col, show="headings")
# tree_all_tenders.pack(fill=BOTH, expand=1)
# tree_in_process = ttk.Treeview(frame_inprocess, columns=col, show="headings")
# tree_in_process.pack(fill=BOTH, expand=1)

# DISTRIBUTED_TEND = []


# for i in col:
#     tree.heading(i, text=i)
#     tree_all_tenders.heading(i, text=i)
#     tree_in_process.heading(i, text=i)


# for d in db.select_distrib_man('allTenders', 1):
#     tree.insert("", END, values=d)

# for d in db.select_all_data('allTenders'):
#     tree_all_tenders.insert("", END, values=d)


# def item_selected(event):
#     for selected in tree.selection():
#         item = tree.item(selected)
#         sel = item["values"]
#         DISTRIBUTED_TEND.clear()
#         for el in sel:
#             DISTRIBUTED_TEND.append(el)
#         lblnum_num["text"] = f"{sel}"

#         return print(DISTRIBUTED_TEND)


# lbl = ttk.Label(text='')
# lbl.pack()

# tree.bind("<<TreeviewSelect>>", item_selected)


# def distributed_tender_info_window():
#     info_win = Toplevel()
#     info_win.geometry("500x300")
#     lbl_tender_num_info = ttk.Label(info_win, text='Номер конкурса').grid(row=0, column=0)
#     lbl_tender_num = ttk.Label(info_win, text=DISTRIBUTED_TEND[1]).grid(row=0, column=1)
#     lbl_tender_cust_info = ttk.Label(info_win, text='Заказчик').grid(row=1, column=0)
#     lbl_tender_cust = ttk.Label(info_win, text=DISTRIBUTED_TEND[2]).grid(row=1, column=1)
#     lbl_tender_datefinish_info = ttk.Label(info_win, text='Дата подачи').grid(row=2, column=0)
#     lbl_tender_datefinish = ttk.Label(info_win, text=DISTRIBUTED_TEND[3]).grid(row=2, column=1)
#     lbl_tender_summ_info = ttk.Label(info_win, text='Сумма конкурса').grid(row=3, column=0)
#     lbl_tender_summ = ttk.Label(info_win, text=DISTRIBUTED_TEND[4]).grid(row=3, column=1)
#     lbl_tender_stat_info = ttk.Label(info_win, text='Статус').grid(row=4, column=0)
#     combbx_stat = ttk.Combobox(info_win, values=db.select_status('tender_status')).grid(row=4, column=1)
#     lbl_comments_info = ttk.Label(info_win, text='Комментарий').grid(row=5, column=0)
#     entry_comments = ttk.Entry(info_win).grid(row=5, column=1)
#     lbl_tender_doc_info = ttk.Label(info_win, text='Документация').grid(row=6, column=0)
#     btn_ok = ttk.Button(info_win, text='OK').grid(row=7, column=0)
#     btn_cancel = ttk.Button(info_win, text="Отмена").grid(row=7, column=1)
#     btn_apply = ttk.Button(info_win, text='Применить').grid(row=7, column=2)
#     l = lblnum_num.cget("text")
#     info_win.title(f"Конкурс {DISTRIBUTED_TEND[1]}")

# btn = ttk.Button(frame_notebook, text='Открыть конкурс', command=distributed_tender_info_window)
# btn.pack()

# root.mainloop()


# class DistributedTenders:
#     def __init__(self ):
#         pass
