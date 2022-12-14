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


def show_data():
    ct = my_dict_inv[str(cbxTables.get())]
    st = ''
    # print(my_dict_dict)

    if ct == 'location':
        st = 'idLocation, Loc_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" ")
    elif ct == 'manufacturer':
        st = 'idManufacturer, Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" ")
    elif ct == 'level':  # st = stringtables
        st = 'idLevel, lev_Type, AvailableInfo'
        cursor.execute("SELECT "+st+" FROM "+ct+" ")

    elif ct == 'personnel':
        st = 'idPersonnel, Pers_Name, Position, Login, Password, Lev_Type'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN level ON Level_idLevel = idLevel ")

    elif ct == 'experiment':
        st = 'idExperiment, Pers_Name, ExpCode, Date, Comment '
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN personnel ON Personnel_idPersonnel = idPersonnel ")

    elif ct == 'reagent':
        st = 'idReagent, ReagName1, ReagName2, ReagName3, ReagFormula, DateReceived, ' \
             'EndDateReag, Amount, Units, SerialNumber, CatNumber, CodeReag, Loc_Name, Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                       "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ")

    elif ct == 'solvent':
        st = 'idSolvent, SolvName1, SolvName2, SolvName3, SolvFormula, DateReceived, EndDateSolv,' \
             'SingleAmount, Units, Num_Containers, SerialNumber, CatNumber, CodeSolv,Loc_Name, Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                       "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ")

    elif ct == 'equipment':
        st = 'idEquipment, EquipName, DateReceived, SerialNumber, StorageNumber, Loc_Name, Manuf_Name'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                        "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ")

    elif ct == 'reagusage':
        st = 'idReagUsage, ReagName1, AmUsed, ExpCode'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN reagent ON Reagent_idReagent = idReagent "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ")

    elif ct == 'solvusage':
        st = 'idSolvUsage, SolvName1, AmContUsed, ExpCode'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN solvent ON Solvent_idSolvent = idSolvent "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ")

    elif ct == 'equipusage':
        st = 'idEquipUsage, EquipName, TimeStart, TimeFinish, ExpCode'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN equipment ON Equipment_idEquipment = idEquipment "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ")

    elif ct == 'equipverifinfo':
        st = 'idEquipVerifInfo, EquipName, Calibration, Verification, Attestation, Qualification, Documentation'
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN equipment ON Equipment_idEquipment = idEquipment")

    else:
        pass

    headings = st.split(",")
    for i in range(len(headings)):
        headings[i] = headings[i].lstrip()  # попробовать как нашла
    # print(headings)

    l = len(st)
    k = len(headings)

    # headings = headings[1:l - 1]
    # print(headings, k)

    table_frame = Frame(root, bg='light green')
    table_frame.grid(row=1, column=0)
    table = ttk.Treeview(table_frame, columns=headings, show="headings")

    # column = TreeViewColumn()

    for head in headings:
        table.heading(head, text=str(head))

    # column[0].set_visible(False)

    table.grid(row=0, column=0, columnspan=l)

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
    h = 450
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
        for j in range(len(headings)):
            s_val.append(gv)
            values.append(str(entry[j].get()))
            entry[j].delete(0, END)
        s_val_join = ",".join(s_val)

        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"
                       + ct + "'")
        stTables = ""
        heads = []
        for r in cursor.fetchall():
            stTables += str(r[0]) + ','
            heads.append(str(r[0]))

        for i in range(len(headings)):
            for j in range(len(heads)):
                if headings[i] == heads[j] and i != j:
                    headings[i], headings[j] = headings[j], headings[i]
                    values[i], values[j] = values[j], values[i]
                else:
                    for k, v in my_dict_dt.items():
                        if headings[i] == k:
                            headings[i] = v
                            for k1, v1 in my_dict_dict.items():
                                if headings[i] == k1:
                                    values[i] = v1.get(str(values[i]))
                            if headings[i] == heads[j]:
                                headings[i], headings[j] = headings[j], headings[i]
                                values[i], values[j] = values[j], values[i]
                            else:
                                pass
                        else:
                            pass
        # print(heads)
        # print(headings)
        # print(values)
        x = ''
        for i in range(len(values)):
            if values[i] == None or values[i] == '':
                x = 'error'
                break
        if x == 'error':
            print('Невозможно загрузить')
        else:
            cursor.execute("INSERT INTO " + ct + " VALUES( " + s_val_join + ")", values)
            cnx.commit()
            print('Загрузка осуществлена')

        NoUp1()

    btnAddData = Button(input_frame, text="Добавить", command=add_data, bg='light green')
    btnAddData.grid(row=2, column=0, columnspan=k)

    up_frame.grid_remove()  # способ 1 через grid_remove

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

    def delete_data():
        row_values = []
        for j in range(k):
            if len(entry[j].get()) != 0:
                entry[j].delete(0, END)
        for selected in table.selection():
            rows = table.item(selected)
            row_values = rows['values']
        idms = str(row_values[0])
        cursor.execute("DELETE FROM " + ct + " WHERE (" + str(headings[0]) + " = " + idms + ") ")
        cnx.commit()
        NoUp1()

    btnDeleteData = Button(input_frame, text="Удалить", command=delete_data, bg='light green')
    btnDeleteData.grid(row=5, column=0, columnspan=k)

    # способ 2 напрямую через destroy

    def NoUp():
        table_frame.destroy()
        input_frame.destroy()
        labelSO.destroy()
        up_frame.grid()
        root.geometry("400x200")

    def NoUp1():
        table_frame.destroy()
        input_frame.destroy()
        labelSO.destroy()
        show_data()

    btnNoUp = Button(input_frame, text="Скрыть", command=NoUp, bg='light green')
    btnNoUp.grid(row=3, column=0, columnspan=k)


btnShowData = Button(up_frame, text="Загрузить", command=show_data, bg='light green')
btnShowData.grid(row=0, column=2)

my_dict = {'equipment': 'Оборудование', 'equipusage': 'Использование оборудования',
           'equipverifinfo': 'Верификация оборудования', 'experiment': 'Эксперименты',
           'level': 'Уровень', 'location': 'Расположение', 'manufacturer': 'Производитель',
           'personnel': 'Персонал', 'reagent': 'Реагенты', 'reagusage': 'Использование реагентов',
           'solvent': 'Растворитель', 'solvusage': 'Использование растворителей'}

my_dict_inv = dict(map(reversed, my_dict.items()))

my_dict_dt = {'EquipName': 'Equipment_idEquipment', 'ExpCode': 'Experiment_idExperiment',
           'Lev_Type': 'Level_idLevel', 'Pers_Name': 'Personnel_idPersonnel',
           'Loc_Name': 'Location_idLocation', 'Manuf_Name': 'manufacturer_idmanufacturer',
           'ReagName1': 'Reagent_idReagent', 'SolvName1': 'Solvent_idSolvent'}

my_dict_dict = {}

addmdd = {'level': {'Lev_Type, idLevel': 'Level_idLevel'},
          'personnel': {'Pers_Name, idPersonnel': 'Personnel_idPersonnel'},
          'location': {'Loc_Name, idLocation': 'Location_idLocation'},
          'manufacturer': {'Manuf_Name, idManufacturer': 'manufacturer_idmanufacturer'},
          'reagent': {'ReagName1, idReagent': 'Reagent_idReagent'},
          'solvent': {'SolvName1, idSolvent': 'Solvent_idSolvent'},
          'equipment': {'EquipName, idEquipment': 'Equipment_idEquipment'},
          'experiment': {'ExpCode, idExperiment': 'Experiment_idExperiment'}}

acdc = ['equipment', 'experiment', 'level', 'location',
        'manufacturer', 'personnel', 'reagent', 'solvent']

for i in range(len(acdc)):
    for k, v in addmdd.items():
        for k1, v1 in v.items():
            if acdc[i] == k:
                cursor.execute("SELECT " + k1 + " FROM " + str(acdc[i]) + " ")
                list0 = []
                for row in cursor.fetchall():
                    list0.append(row)
                my_dict_dict.update({v1: dict(list0)})
# print(my_dict_dict)

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
