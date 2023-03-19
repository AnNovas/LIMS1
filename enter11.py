from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as msb
from datetime import date
# from mysql.connector import (connection)
# from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='LordSe22anne)',
                              host='localhost', database='mydb')
cursor = cnx.cursor()

root = Tk()
root.title("Кабинет администратора")
root.configure(bg='light blue')

# отцентровывание окна приложения по экрану
w = 450
h = 200
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

up_frame = Frame(root, bg='light blue')
up_frame.grid(row=0, column=0, sticky='news')
up_frame.grid_rowconfigure(0, weight=1)
up_frame.grid_columnconfigure(1, weight=1)

tbx1 = ttk.Entry()
label1 = Label(up_frame, text="Выберите таблицу: ", bg='light green')
label1.grid(row=1, column=0, padx=10)

label2 = Label(up_frame, text="Добро пожаловать в базу данных.", bg='light green')
label2.grid(row=0, column=0, columnspan=2)

cbxTables = ttk.Combobox(up_frame, values=[])
cbxTables.grid(row=1, column=1)

# дата
my_dict_date = {'January': 'января', 'February': 'февраля', 'March': 'марта', 'April': 'апреля',
                'May': 'мая', 'June': 'июня', 'July': 'июля', 'August': 'августа', 'September': 'сентября',
                'October': 'октября', 'Nobember': 'ноября', 'December': 'декабря'}

today = date.today()
dM = today.strftime("%B")
dm = my_dict_date[dM]
dd = today.strftime("%d")
dy = today.strftime("%Y")

label3 = Label(up_frame, text="Сегодня {} {}, {}".format(dd, dm, dy), bg='light green')
label3.grid(row=0, column=2)

def show_data():
    ct = my_dict_inv[str(cbxTables.get())]
    st = ''
    nt = []
    # print(my_dict_dict)
    if ct == 'location':
        st = 'idLocation, Loc_Name'
        nt = [1, 1]
        cursor.execute("SELECT "+st+" FROM "+ct+" ORDER BY idLocation ")
    elif ct == 'manufacturer':
        st = 'idManufacturer, Manuf_Name'
        nt = [1, 1]
        cursor.execute("SELECT "+st+" FROM "+ct+" ORDER BY idManufacturer ")
    elif ct == 'level':  # st = stringtables
        st = 'idLevel, lev_Type, AvailableInfo'
        nt = [1, 1, 1]
        cursor.execute("SELECT "+st+" FROM "+ct+" ORDER BY idLevel ")

    elif ct == 'personnel':
        st = 'idPersonnel, Pers_Name, Position, Login, Password, Lev_Type'
        nt = [1, 1, 1, 1, 1, 2]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN level ON Level_idLevel = idLevel ORDER BY idPersonnel ")

    elif ct == 'experiment':
        st = 'idExperiment, ExpCode, Pers_Name, Date, Comment '
        nt = [1, 1, 2, 1, 1]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN personnel ON Personnel_idPersonnel = idPersonnel ORDER BY idExperiment ")

    elif ct == 'reagent':
        st = 'idReagent, ReagName1, ReagName2, ReagName3, ReagFormula, DateReceived, ' \
             'EndDateReag, Amount, Units, SerialNumber, CatNumber, CodeReag, Loc_Name, Manuf_Name'
        nt = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                       "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ORDER BY idReagent ")

    elif ct == 'solvent':
        st = 'idSolvent, SolvName1, SolvName2, SolvName3, SolvFormula, DateReceived, EndDateSolv,' \
             'SingleAmount, Units, Num_Containers, SerialNumber, CatNumber, CodeSolv, Loc_Name, Manuf_Name'
        nt = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                       "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ORDER BY idSolvent ")

    elif ct == 'equipment':
        st = 'idEquipment, EquipName, DateReceived, SerialNumber, StorageNumber, Loc_Name, Manuf_Name'
        nt = [1, 1, 1, 1, 1, 2, 2]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                        "LEFT JOIN location ON Location_idLocation = idLocation "
                        "LEFT JOIN manufacturer ON manufacturer_idmanufacturer =  idManufacturer ORDER BY idEquipment ")

    elif ct == 'reagusage':
        st = 'idReagUsage, ReagName1, AmUsed, ExpCode'
        nt = [1, 2, 1, 2]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN reagent ON Reagent_idReagent = idReagent "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ORDER BY idReagUsage ")

    elif ct == 'solvusage':
        st = 'idSolvUsage, SolvName1, AmContUsed, ExpCode'
        nt = [1, 2, 1, 2]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN solvent ON Solvent_idSolvent = idSolvent "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ORDER BY idSolvUsage ")

    elif ct == 'equipusage':
        st = 'idEquipUsage, EquipName, TimeStart, TimeFinish, ExpCode'
        nt = [1, 2, 1, 1, 2]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN equipment ON Equipment_idEquipment = idEquipment "
                       "LEFT JOIN experiment ON Experiment_idExperiment = idExperiment ORDER BY idEquipUsage ")

    elif ct == 'equipverifinfo':
        st = 'idEquipVerifInfo, EquipName, Calibration, Verification, Attestation, Qualification, Documentation'
        nt = [1, 2, 1, 1, 1, 1, 1]
        cursor.execute("SELECT "+st+" FROM "+ct+" "
                       "LEFT JOIN equipment ON Equipment_idEquipment = idEquipment ORDER BY idEquipVerifInfo ")

    else:
        pass

    headings = st.split(",")
    for i in range(len(headings)):
        headings[i] = headings[i].lstrip()

    l = len(st)
    k = len(headings)

    table_frame = Frame(root, bg='light green')
    table_frame.grid(row=1, column=0)
    table = ttk.Treeview(table_frame, columns=headings, show="headings")

    for head in headings:
        table.heading(head, text=str(head), anchor=CENTER)

    # column[0].set_visible(False)

    table.grid(row=0, column=0, columnspan=l)

    for r in cursor.fetchall():
        table.insert("", END, values=r)

    vert_scroll = Scrollbar(table_frame, command=table.yview)
    vert_scroll.grid(row=0, column=l+1, sticky="ns")
    table.configure(yscrollcommand=vert_scroll.set)

    labelSO = Label(text="Была выбрана таблица " + str(cbxTables.get()) +
                         ".\n Чтобы выбрать другую таблицу, нажмите кнопку СКРЫТЬ", font='25', bg='light blue')
    labelSO.grid(row=0, column=0, columnspan=k)
    labelSO.update()

    table_frame.update()
    if table_frame.winfo_width() > labelSO.winfo_width():
        w = table_frame.winfo_width()
    else:
        w = labelSO.winfo_width()
    h = 500
    root.geometry(f"{w}x{h}")

    input_frame = Frame(root, bg='light blue')
    input_frame.grid(row=2, column=0)
    label = []
    entry = []
    values = []
    row_values = []
    cbxvals = []
    x = ''

    def check_input1(event):
        value = event.widget.get()
        if value == '':
            entry[j]['values'] = cbxvals
        else:
            data = []
            for item in cbxvals:
                if value.lower() in item.lower():
                    data.append(item)
            entry[j]['values'] = data

    for j in range(k):
        label.append(Label(input_frame, text=headings[j], bg='light green'))
        label[j].grid(row=0, column=j)
        if nt[j] == 1:
            entry.append(Entry(input_frame))
            # entry[j].grid(row=1, column=j)
        else:
            trheads = my_dict_dt[headings[j]]
            # print(trheads)
            for k1, v1 in my_dict_dict.items():
                if trheads == k1:
                    cbxvals = list(v1.keys())
            entry.append(ttk.Combobox(input_frame, values=cbxvals))
        entry[j].grid(row=1, column=j)
        entry[j].bind('<KeyRelease>', check_input1)

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

        # print(values)

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
                                    # print(values[i])
                                    values[i] = v1.get(str(values[i]))
                                    # print(values[i])
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
            msb.showerror(title="Ошибка", message="Ошибка при заполнении полей ввода.")
        else:
            cursor.execute("INSERT INTO " + ct + " VALUES( " + s_val_join + ")", values)
            cnx.commit()
            msb.showinfo(title="Добавление данных", message="Информация добавлена.")
            # print(cursor._last_insert_id)
        NoUp1()

    btnAddData = Button(input_frame, text="Добавить", command=add_data, bg='light green')
    btnAddData.grid(row=2, column=0, columnspan=k)

    up_frame.grid_remove()  # способ 1 через grid_remove

    def select_data():
        # global x
        global row_values
        for j in range(k):
            if len(entry[j].get()) != 0:
                entry[j].delete(0, END)
        for selected in table.selection():
            rows = table.item(selected)
            row_values = rows['values']
        for j in range(k):
            entry[j].insert(0, str(row_values[j]))
        idms = str(row_values[0])

        def update_data():
            x = ''
            for j in range(k):
                values.append(str(entry[j].get()))
            print(row_values)
            print(values)

            for j in range(k):
                if str(row_values[0]) != values[0]:
                    msb.showerror(title="Ошибка", message="Изменение идентификатора возможно только при добавлении новой записи")
                    break
                elif values[j] == '':
                    msb.showerror(title="Ошибка", message="Не все поля ввода заполнены.")
                    break
                elif values[j] != str(row_values[j]):
                    vals = values[j]
                    # hds = headings[j]
                    if nt[j] == 1:
                        hds = headings[j]
                    elif nt[j] == 2:
                        hds = my_dict_dt[headings[j]]
                        for k1, v1 in my_dict_dict.items():
                            if hds == k1:
                                # print(vals)
                                # print(v1)
                                vals = v1.get(str(values[j]))
                                # print(vals)
                                if vals == None:
                                    x = 'error'
                                    break
                    else:
                        hds = headings[j]

                    if x == 'error':
                        msb.showerror(title="Ошибка", message="Ошибка при заполнении полей ввода.")
                    else:
                        print(hds, vals)
                        # print(my_dict_dt)
                        valsus = str(vals)
                        print(ct, hds, valsus, headings[0], idms)
                        query = ("UPDATE " + ct + " SET " + hds + " = " + valsus + " WHERE (" + headings[0] + " = " + idms + ")")
                        print(query)
                        cursor.execute("UPDATE " + ct + " SET " + hds + " = " + valsus + " WHERE (" + headings[0] + " = " + idms + ")")
                        cnx.commit()
                        print(cursor._executed)
                        msb.showinfo(title="Изменение данных", message="Информация изменена.")

                else:
                    pass
            NoUp1()
            # сделать так чтобы апдейт не работал если изменили id: есть

        def delete_data():
            cursor.execute("DELETE FROM " + ct + " WHERE (" + str(headings[0]) + " = " + idms + ") ")
            cnx.commit()
            NoUp1()
            msb.showinfo(title="Удаление", message="Информация удалена.")

        def clean():
            for j in range(k):
                if len(entry[j].get()) != 0:
                    entry[j].delete(0, END)

        btnDeleteData = Button(input_frame, text="Удалить", command=delete_data, bg='light green')
        btnDeleteData.grid(row=4, column=0, columnspan=k)

        btnUpdateData = Button(input_frame, text="Изменить", command=update_data, bg='light green')
        btnUpdateData.grid(row=5, column=0, columnspan=k)

        btnClean = Button(input_frame, text="Очистить", command=clean, bg='light green')
        btnClean.grid(row=6, column=0, columnspan=k)

    btnSelectData = Button(input_frame, text="Выбрать", command=select_data, bg='light green')
    btnSelectData.grid(row=3, column=0, columnspan=k)

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
    btnNoUp.grid(row=7, column=0, columnspan=k)


btnShowData = Button(up_frame, text="Загрузить", command=show_data, bg='light green')
btnShowData.grid(row=1, column=2, padx=10)

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

def check_input(event):
    value = event.widget.get()
    if value == '':
        cbxTables['values'] = tableList_bc
    else:
        data = []
        for item in tableList_bc:
            if value.lower() in item.lower():
                data.append(item)
        cbxTables['values'] = data


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
    cbxTables.bind('<KeyRelease>', check_input)
except:
    cnx.rollback()

# Окно эксперимента
def Exp():
    up_frame.grid_remove()
    exp_frame = Frame(root, bg='light blue')
    exp_frame.grid(row=0, column=0)

    def Back():
        exp_frame.grid_remove()
        up_frame.grid()
        root.geometry("400x200")
    btnBack = Button(exp_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
    btnBack.grid(row=0, column=0)


btnExp = Button(up_frame, text="Добавить эксперимент", command=Exp, bg='light green')
btnExp.grid(row=2, column=1)

# Окно методики
def Met():
    up_frame.grid_remove()
    met_frame = Frame(root, bg='light blue')
    met_frame.grid(row=0, column=0)

    def Back():
        met_frame.grid_remove()
        up_frame.grid()
        root.geometry("400x200")
    btnBack = Button(met_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
    btnBack.grid(row=0, column=0)


btnMet = Button(up_frame, text="Добавить методику", command=Met, bg='light green')
btnMet.grid(row=3, column=1)


root.mainloop()
