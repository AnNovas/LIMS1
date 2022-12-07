from tkinter import *
from tkinter import ttk
import mysql.connector
# from mysql.connector import (connection)
# from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='LordSe22anne)',
                              host='localhost', database='mydb')
cursor = cnx.cursor()

root = Tk()
root.title("Кабинет администратора")
root.geometry("400x200")
root.configure(bg='light blue')
# root.iconbitmap(r'ae2kb-xsi88-001.ico')

up_frame = Frame(root, bg='light blue')
up_frame.grid(row=0, column=0)

tbx1 = ttk.Entry()
label1 = Label(up_frame, text="Выберите таблицу: ", bg='light green')
label1.grid(row=0, column=0)

cbxTables = ttk.Combobox(up_frame, values=[])
cbxTables.grid(row=0, column=1)

my_dict = {'equipment': 'Оборудование', 'equipusage': 'Использование оборудования',
           'equipverifinfo': 'Верификация оборудования', 'experiment': 'Эксперименты',
           'level': 'Уровень', 'location': 'Расположение', 'manufacturer': 'Производитель',
           'personnel': 'Персонал', 'reagent': 'Реагенты', 'reagusage': 'Использование реагентов',
           'solvent': 'Растворитель', 'solvusage': 'Использование растворителей'}

my_dict_inv = dict(map(reversed, my_dict.items()))


def show_data():
    ct = my_dict_inv[str(cbxTables.get())]

    if ct == 'location':
        st = 'Loc_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" ")
    elif ct == 'manufacturer':
        st = 'Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" ")
    elif ct == 'level':  # st = stringtables
        st = 'lev_Type, AvailableInfo'
        cursor.execute("SELECT "+st+" FROM "+ct+" ")

    elif ct == 'personnel':
        st = 'Pers_Name, Position, Login, Password, Lev_Type'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN level ON Level_idLevel = idLevel ")
    elif ct == 'experiment':
        st = 'Pers_Name, ExpCode, Date, Comment '
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN personnel ON Personnel_idPersonnel = idPersonnel ")

    elif ct == 'reagent':
        st = 'ReagName1, ReagName2, ReagName3, ReagFormula, DateReceived, ' \
             'EndDateReag, Amount, Units, SerialNumber, CatNumber, CodeReag, Loc_Name, Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                       "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ")
    elif ct == 'solvent':
        st = 'SolvName1, SolvName2, SolvName3, SolvFormula, DateReceived, EndDateSolv,' \
             'SingleAmount, Units, Num_Containers, SerialNumber, CatNumber, CodeSolv,Loc_Name, Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" LEFT JOIN location ON Location_idLocation = idLocation "
                       "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ")
    elif ct == 'equipment':
        st = 'EquipName, DateReceived, SerialNumber, StorageNumber,Loc_Name, Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                        "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ")

    elif ct == 'reagusage':
        st = 'ReagName1, AmUsed, ExpCode'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN reagent ON Reagent_idReagent = idReagent "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ")
    elif ct == 'solvusage':
        st = 'SolvName1, AmContUsed, ExpCode'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN solvent ON Solvent_idSolvent = idSolvent "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ")
    elif ct == 'equipusage':
        st = 'EquipName, TimeStart, TimeFinish, ExpCode'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN equipment ON Equipment_idEquipment = idEquipment "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ")

    elif ct == 'equipverifinfo':
        st = 'EquipName, Calibration, Verification, Attestation, Qualification, Documentation'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN equipment ON Equipment_idEquipment = idEquipment")
    else:
        pass

    headings = st.split(",")

    table_frame = Frame(root, bg='light green')
    table_frame.grid(row=1, column=0)
    table = ttk.Treeview(table_frame, columns=headings, show="headings")

    for head in headings:
        table.heading(head, text=str(head))

    l = len(st)
    k = len(headings)

    table.grid(row=0, column=0, columnspan=l)

    st = st[:l - 1]

    # cursor.execute("SELECT "+st+" FROM "+ct+"")
    for r in cursor.fetchall():
        table.insert("", END, values=r)

    vert_scroll = Scrollbar(table_frame, command=table.yview)
    vert_scroll.grid(row=0, column=l+1, sticky="ns")
    table.configure(yscrollcommand=vert_scroll.set)

    labelSO = Label(text="Была выбрана таблица " + ct +
                         ".\n Чтобы выбрать другую таблицу, нажмите кнопку СКРЫТЬ", font='25', bg='light blue')
    labelSO.grid(row=0, column=0, columnspan=k)
    labelSO.update()

    table_frame.update()
    if table_frame.winfo_width() > labelSO.winfo_width():
        w = table_frame.winfo_width()
    else:
        w = labelSO.winfo_width()
    h = 400
    root.geometry(f"{w}x{h}")

    input_frame = Frame(root, bg='light blue')
    input_frame.grid(row=2, column=0)
    label = []
    entry = []
    values = []

    for j in range(k):
        label.append(Label(input_frame, text=headings[j], bg='light green'))
        label[j].grid(row=0, column=j)
        entry.append(Entry(input_frame))
        entry[j].grid(row=1, column=j)

    def add_data():
        gv = "%s"
        s_val = []
        for j in range(k):
            s_val.append(gv)
            values.append(str(entry[j].get()))
            entry[j].delete(0, END)
        s_val_join = ",".join(s_val)

        cursor.execute("INSERT INTO " + ct + " VALUES(UUID_SHORT(), " + s_val_join + ")", values)
        cnx.commit()


        show_data()

    btnAddData = Button(input_frame, text="Добавить", command=add_data, bg='light green')
    btnAddData.grid(row=2, column=0, columnspan=k)

    up_frame.grid_remove()  # способ 1 через grid_remove

    # btmDelData = Button(input_frame, text = "Удалить")

    def select_data():
        row_values = []
        for j in range(k):
            if len(entry[j].get()) != 0:
                entry[j].delete(0, END)
        for selected in table.selection():
            rows = table.item(selected)
            row_values = rows['values']
        for j in range(k):
            entry[j].insert(0, str(row_values[j]))

    btnSelectData = Button(input_frame, text="Выбрать", command=select_data, bg='light green')
    btnSelectData.grid(row=4, column=0, columnspan=k)

    # способ 2 напрямую через destroy

    def NoUp():
        table_frame.destroy()
        input_frame.destroy()
        labelSO.destroy()
        up_frame.grid()
        root.geometry("400x200")

    btnNoUp = Button(input_frame, text="Скрыть", command=NoUp, bg='light green')
    btnNoUp.grid(row=3, column=0, columnspan=k)


btnShowData = Button(up_frame, text="Загрузить", command=show_data, bg='light green')
btnShowData.grid(row=0, column=2)


try:
    cursor.execute("SHOW tables;")
    shtbl = cursor.fetchall()
    tableList = []
    for table in shtbl:
        tableList.append(table)

    tableList_bc = []
    for e in tableList:
        tableList_bc.append(my_dict[e[0]])
    cbxTables['values'] = tableList_bc
except:
    cnx.rollback()

root.mainloop()
