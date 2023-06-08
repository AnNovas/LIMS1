from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as msb
from datetime import date
import textwrap as tw
# from tkinter import font
# import inspect
# from mysql.connector import (connection)
# from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='LordSe22anne)',
                              host='localhost', database='mydb')
cursor = cnx.cursor()

root = Tk()
root.title("AeroLIS")
root.configure(bg='light blue')
def dis():
    pass

# defaultFont = font.nametofont("TkDefaultFont")
# defaultFont.configure(size=14)

# отцентровывание окна приложения по экрану
w = 360
h = 150
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# root.rowconfigure(index=0, weight=1)
# root.columnconfigure(index=0, weight=1)

person = ''

def login():
    global person
    login = str(username_entry.get())
    password = str(password_entry.get())
    cursor.execute("SELECT idPersonnel FROM personnel WHERE Login = '" + login + "' AND Password = '" + password + "' ")
    result = cursor.fetchone()
    if result is None:
        msb.showerror(title="Ошибка", message="Неверный логин или пароль.")
    else:
        person = (result[0])
        # msb.showinfo(title="Выполнен вход", message="Вы успешно вошли в личный кабинет.")
        password_entry.delete(0, END)
        username_entry.delete(0, END)
        main()
        # return person



def show_password():
    if check_v1.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

auth_frame = Frame(root, bg='light blue')
auth_frame.grid(row=0, column=0, padx = 10, pady=10)

enter_label = Label(auth_frame, text="Добро пожаловать!", bg='light blue', font = 14)
enter_label.grid(row=0, column=0, columnspan=3)

username_label = Label(auth_frame, text="Введите логин:", bg='light blue')
username_label.grid(row=1, column=0)
username_entry = Entry(auth_frame)
username_entry.grid(row=1, column=1)

password_entry_str = StringVar()
password_label = Label(auth_frame, text="Введите пароль:", bg='light blue')
password_label.grid(row=2, column=0)
password_entry = Entry(auth_frame, show="*", textvariable=password_entry_str)
password_entry.grid(row=2, column=1)

login_btn = Button(auth_frame, text="Войти", command=login, bg='thistle1')
login_btn.grid(row=3, column=0, columnspan=3)

check_v1 = IntVar(value=0)
check_btn = Checkbutton(auth_frame, text="Показать пароль", bg='light blue', variable=check_v1,
                      onvalue=1, offvalue=0, command=show_password)
check_btn.grid(row=2, column=2)


def main():
    root.geometry("330x300")
    auth_frame.grid_remove()
    root.protocol("WM_DELETE_WINDOW", dis)
    up_frame = Frame(root, bg='light blue')
    up_frame.grid(row=0, column=0, padx = 10, pady=10, sticky='news')
    up_frame.grid_rowconfigure(0, weight=1)
    up_frame.grid_columnconfigure(1, weight=1)
    up_frame.update()

    cursor.execute("SELECT Level_idlevel, Pers_Name from personnel WHERE idPersonnel = " + str(person) + " ")
    record = cursor.fetchone()
    # print(record)
    level = record[0]
    name = record[1]
    label2 = Label(up_frame, text="Добро пожаловать в базу данных, {}".format(name), bg='thistle1')
    label2.grid(row=0, column=0)

    cursor.execute("select researchproject_idResearchProject, RPName from researchproject_has_personnel "
                   "join researchproject on researchproject_idResearchProject = idResearchProject "
                   "join personnel on personnel_idPersonnel = idPersonnel "
                   "join status_rp on status_rp_idstatus_rp = idstatus_rp "
                   "where Personnel_idPersonnel = "+ str(person) +" and status_rp_idstatus_rp = 1")
    record1 = cursor.fetchall()
    papername = []
    respr = []

    for recr in record1:
        respr.append(recr[0])
        papername.append(recr[1])

    res_dict = dict(zip(papername, respr))

    # print(name)


    # дата
    my_dict_date = {'January': 'января', 'February': 'февраля', 'March': 'марта', 'April': 'апреля',
                    'May': 'мая', 'June': 'июня', 'July': 'июля', 'August': 'августа', 'September': 'сентября',
                    'October': 'октября', 'Nobember': 'ноября', 'December': 'декабря'}

    today = date.today()
    dM = today.strftime("%B")
    dm = my_dict_date[dM]
    dd = today.strftime("%d")
    dy = today.strftime("%Y")
    dtd = today.strftime("%Y-%m-%d")
    # print(dtd)

    label3 = Label(up_frame, text="Сегодня {} {}, {}".format(dd, dm, dy), bg='thistle1')
    label3.grid(row=1, column=0)

    exit_button = Button(up_frame, text="Выход", command=root.destroy, bg='thistle1')
    exit_button.grid(row=12, column=0, columnspan=2)


    my_dict = {'equipment': 'Оборудование',
               'equipusage': 'Использование оборудования',
               'equipverifinfo': 'Верификация оборудования',
               'experiment': 'Эксперименты',
               'level': 'Уровень',
               'location': 'Расположение',
               'personnel': 'Персонал',
               'reagent': 'Реагенты',
               'reagusage': 'Использование реагентов',
               'analyticaldata': 'Аналитические данные',
               'equiptype': 'Тип оборудования',
               'experimentdate': 'Опыт',
               'literature': 'Литературные источники',
               'physchemproperties': 'Физико-химические свойства',
               'process': 'Процессы',
               'status': 'Статус',
               'processstage': 'Стадия',
               'units': 'Единицы измерения количества реагента',
               'parameters': 'Параметры',
               'methodology': 'Методика',
               'reagent_has_physchemproperties': 'Физико-химические свойства вещества',
               'reaginfo': 'Номенклатура реагента',
               'reagtype': 'Тип реагента',
               'researchproject': 'Научно-исследовательские работы',
               'stagetype': 'Тип стадии',
               'experiment_has_analyticaldata': 'Аналитические данные эксперимента',
               'methodology_has_literature': 'Литературные источники методики',
               'process_has_parameters': 'Параметры процесса'}

    # my_dict_inv = dict(map(reversed, my_dict.items()))
    my_dict_inv = dict(map(reversed, my_dict.items()))

    my_dict_dt = {'EquipName': 'Equipment_idEquipment',
                  'ExpCode': 'Experiment_idExperiment',
                  'Lev_Type': 'Level_idLevel',
                  'Pers_Name': 'Personnel_idPersonnel',
                  'Loc_Name': 'Location_idLocation',
                  'ReagName1': 'Reagent_idReagent',
                  'PSName': 'ProcessStage_idProcessStage',
                  'RTypeName': 'ReagType_idReagType',
                  'ETypeName': 'EquipType_idEquipType',
                  'StType': 'Status_idStatus',
                  'UUnitSN': 'Units_idUnits',
                  'STName': 'StageType_idStageType',
                  'MetName': 'Methodology_idMethodology',
                  'PropName': 'PhysChemProperties_idPhysChemProperties',
                  'DOI': 'Literature_idLiterature',
                  'RPCode': 'ResearchProject_idResearchProject',
                  'ParSN': 'Parameters_idParameters',
                  'AnDataSN': 'AnalyticalData_idAnalyticalData'}

    my_dict_dict = {}

    addmdd = {'level': {'Lev_Type, idLevel': 'Level_idLevel'},
              'personnel': {'Pers_Name, idPersonnel': 'Personnel_idPersonnel'},
              'location': {'Loc_Name, idLocation': 'Location_idLocation'},
              'reagent': {'ReagName1, idReagent': 'Reagent_idReagent'},
              'equipment': {'EquipName, idEquipment': 'Equipment_idEquipment'},
              'experiment': {'idExperiment': 'Experiment_idExperiment'},
              'processstage': {'PSName, idProcessStage': 'ProcessStage_idProcessStage'},
              'reagtype': {'RTypeName, idReagType': 'ReagType_idReagType'},
              'equiptype': {'ETypeName, idEquipType': 'EquipType_idEquipType'},
              'status': {'StType, idStatus': 'Status_idStatus'},
              'units': {'UUnitSN, idUnits': 'Units_idUnits'},
              'stagetype': {'STName, idStageType': 'StageType_idStageType'},
              'methodology': {'MetName, idMethodology': 'Methodology_idMethodology'},
              'physchemproperties': {'PropName, idPhysChemProperties': 'PhysChemProperties_idPhysChemProperties'},
              'literature': {'DOI, idLiterature': 'Literature_idLiterature'},
              'researchproject': {'idResearchProject': 'ResearchProject_idResearchProject'},
              'parameters': {'ParSN, idParameters': 'Parameters_idParameters'},
              'analyticaldata': {'AnDataSN, idAnalyticalData': 'AnalyticalData_idAnalyticalData'}, '': {'': ''}
              }

    acdc = ['equipment', 'experiment', 'level', 'location',
            'personnel', 'reagent', 'processstage',
            'reagtype', 'equiptype', 'status', 'units', 'stagetype', 'methodology',
            'physchemproperties', 'literature', 'researchproject', 'parameters', 'analyticaldata']

    # for i in range(len(acdc)):
    #     for k, v in addmdd.items():
    #         for k1, v1 in v.items():
    #             if acdc[i] == k:
    #                 cursor.execute("SELECT " + k1 + " FROM " + str(acdc[i]) + " ")
    #                 list0 = []
    #                 for row in cursor.fetchall():
    #                     list0.append(row)
    #                 my_dict_dict.update({v1: dict(list0)})
    # print(my_dict_dict)

    tablesls1 = ['level', 'location', 'personnel', 'equiptype', 'units', 'stagetype',
                 'status', 'processstage',  'methodology', 'reagtype']
    tablesls2 = ['equipment', 'equipverifinfo', 'experiment', 'reagent', 'reaginfo''analyticaldata',
                 'physchemproperties', 'parameters', 'researchproject']
    tablesls3 = ['literature', 'experimentdate', 'process', 'reagusage', 'equipusage', 'reagent_has_physchemproperties',
                 'experiment_has_analyticaldata', 'methodology_has_literature', 'process_has_parameters']

    # def wrap(string, lenght = 8):
    #     return '\n'.join.textwrap.wrap(string, lenght)


    # Окно эксперимента

    def Exp():
        root.geometry("330x300")
        up_frame.grid_remove()

        exp_frame = Frame(root, bg='light blue')
        exp_frame.grid(row=2, column=0, padx = 10, pady=10)

        labelmyexp = Label(exp_frame, text = "Мои эксперименты", bg = 'thistle1')
        labelmyexp.grid(row=0, column=1)
        labelnameexp = Label(exp_frame, text="Научно-исследовательская работа \n '{}'".format(lbres), bg='thistle1')
        labelnameexp.grid(row=1, column=1)

        butexp = []
        butname = []
        butid = []
        cursor.execute("SELECT idExperiment, ExpName FROM experiment WHERE ResearchProject_idResearchProject = " + rpid +" ")
        for r in cursor.fetchall():
            butid.append(str(r[0]))
            butname.append(str(r[1]))

        # lenexp = max(len(lp) for lp in butname)
        # lpfd = len(butname)
        # but = dict(zip(butid, butname))

        exp_inv = dict(zip(butname, butid))
        lkk = len(butname)
        exp_var = Variable(value=butname)
        listofexp = Listbox(exp_frame, listvariable=exp_var, selectmode='single', width=40)
        listofexp.grid(row=2, rowspan=8, column=1)

        # listofexp.update()
        # loe_len=listofexp.winfo_height()

        expscroll = Scrollbar(exp_frame, command=listofexp.yview)
        if lkk > 10:
            expscroll.grid(row=2, rowspan=8, column=2, sticky='ns')
            listofexp.configure(yscrollcommand=expscroll.set)

        # def listb(event):
        #     for i in listofexp.curselection():
        #         nbtnm = listofexp.get(i)
        #         nbtid = exp_inv[nbtnm]
        #         print(nbtid, nbtnm)
        # listofexp.bind("<<ListboxSelect>>", listb)




        # exp_frame.columnconfigure(index=0, weight=1)
        # k = len(butname)
        # h = (k+5)*30
        # labelnameexp.update()
        # lenlab = labelnameexp.winfo_width()
        # print(lenlab)
        # w = lenlab + 40
        # w = 400
        # root.geometry(f"{w}x{h}")

        global but_id
        def listb(event):
            global but_id
            for j in listofexp.curselection():
                # but_id = j
                print(j)
                ExpMin(j)


        def ExpMin(but_id):
            root.geometry("1200x350")
            # print(but_id)
            # print(butid[but_id], butname[but_id])
            btnm = ''
            btid = ''

                # btnm = listofexp.get(j)
                # btid = exp_inv[btnm]
                # print(btid, btnm, but_id)
            btid = butid[but_id]
            btnm = butname[but_id]
            exp_frame.grid_remove()
            emout_frame = Frame(root, bg='light blue')
            emout_frame.grid(row=0, column=0)
            style_emframe = ttk.Style()
            style_emframe.theme_use('default')
            style_emframe.configure("TNotebook", background='light blue', borderwidth=0)
            style_emframe.configure("TNotebook.Tab", background='slategray3')
            style_emframe.map("TNotebook.Tab", background=[("selected", "thistle1")])
            style_emframe.configure("Treeview.Heading", background = 'thistle1')
            style_emframe.configure("TCombobox", fieldbackground="white")
            style_emframe.map("TCombobox", fieldbackground=[("readonly", "white")])
            em_frame = ttk.Notebook(emout_frame)

            # em_frame = Frame(root, bg='light blue')
            # em_frame.grid(row=0, column=0, padx = 10, pady=10)
            labelexpname = Label(emout_frame, text="{}".format(btnm), bg='thistle1')
            labelexpname.grid(row=0, column=0)

            # def chexpname():
            #     pass
            # btnchexpname = Button(em_frame, text="Изменить название эксперимента", command=chexpname, bg = 'thistle1')
            # btnchexpname.grid(row=0, column=1)

            # Использование реагента
            # headosr = ['idReagUsage', 'ReagName1', 'AmUsed', 'UUnitSN', 'ExpDate']
            # headosreag = ", ".join(headosr)

            headosreag = "idReagUsage, PSName, STName, RTypeName, ReagName1, AmUsed, UUnitSN, date_format(ExpDate, '%d.%m.%Y')"

            cursor.execute("select " + headosreag + " from reagusage join reagent on idReagent = Reagent_idReagent "
                            "JOIN reaginfo on idReagInfo = ReagInfo_idReagInfo "
                            "join reagtype on idReagType = ReagType_idReagType "
                           "join experimentdate on idExperimentDate = ExperimentDate_idExperimentDate "
                           "join units on idUnits = Units_idUnits "
                            "join stagetype on idStageType = StageType_idStageType "
                            "join processstage on idProcessStage = ProcessStage_idProcessStage "
                            "where Experiment_idExperiment = " + btid + " and ExperimentDate_idExperimentDate <> 1")

            headingsr = ['id', 'Стадия', 'Тип Стадии', 'Тип реагента', 'Реагент', 'Количество вещества', 'Единицы', 'Дата эксперимента']

            hdr = [2, 2, 1, 2]
            table1_frame = Frame(em_frame, bg='light blue')
            table1_frame.grid(row=0, column=0, padx = 10, pady=10)
            table1 = ttk.Treeview(table1_frame, columns=headingsr, show="headings")
            hd = []
            l = len(headingsr)
            hdnsr = headingsr[1:l-1]
            # print(hdnsr)
            lk = len(hdnsr)
            # print(lk)
            for head in headingsr:
                table1.heading(head, text=str(head))
                hd.append(len(head))
            # print(hd)

            for r in cursor.fetchall():
                table1.insert("", END, values=r)
            d = len(table1.get_children())
            table1['height'] = d+2

            table1.grid(row=1, rowspan=d+3, column=0, columnspan=l)

            tb1lg = []
            tb1lg.append(0)
            cursor.execute("select Max(char_length(PSName)) as len from processstage")
            record11 = cursor.fetchone()
            tb1lg.append(record11[0])
            cursor.execute("select Max(char_length(STName)) as len from stagetype")
            record12 = cursor.fetchone()
            tb1lg.append(record12[0])
            cursor.execute("select Max(char_length(RTypeName)) as len from reagtype")
            record13 = cursor.fetchone()
            tb1lg.append(record13[0])
            cursor.execute("select Max(char_length(ReagName1)) as len from reaginfo")
            record14 = cursor.fetchone()
            tb1lg.append(record14[0])
            tb1lg.append(len(headingsr[5]))
            tb1lg.append(len(headingsr[6]))
            tb1lg.append(len(headingsr[7]))
            # print(tb1lg)

            # УБРАЛА ШИРИНУ ВРЕМЕННО
            for h in range(l):
                table1.column(h, width=tb1lg[h] * 8)

            table1["displaycolumns"]=headingsr[1:]

            label1 = []
            for j in range(lk):
                label1.append(Label(table1_frame, text=hdnsr[j], bg='thistle1'))
                label1[j].grid(row=d+4, column=j+1)

            cbxST1 = ttk.Combobox(table1_frame, values=[], state = 'readonly')
            cbxST1.grid(row=d+5, column=2)
            def getST1(event):
                global tb16
                if cbxST1:
                    cbxST1.set('')

                ST1get = cbxPS1.get()
                idPS1 = str(tb15[ST1get])
                tb160 = []
                tb161 = []
                cursor.execute("SELECT STName, idStageType FROM stagetype JOIN processstage on idProcessStage = ProcessStage_idProcessStage "
                               "WHERE ProcessStage_idProcessStage = "+ idPS1+"")
                for row in cursor.fetchall():
                    tb160.append(row[0])
                    tb161.append(row[1])
                tb16 = dict(zip(tb160, tb161))
                tb1list6 = list(tb16.keys())
                cbxST1['values'] = tb1list6

            tb150 = []
            tb151 = []
            cursor.execute("SELECT PSName, idProcessSTage FROM processstage")
            for row in cursor.fetchall():
                tb150.append(row[0])
                tb151.append(row[1])
            tb15 = dict(zip(tb150, tb151))
            tb1list5 = list(tb15.keys())

            cbxPS1 = ttk.Combobox(table1_frame, values=tb1list5, state = 'readonly')
            cbxPS1.grid(row=d+5, column=1)
            cbxPS1.bind('<<ComboboxSelected>>', getST1)

            entryAMRG = Entry(table1_frame)
            entryAMRG.grid(row=d+5, column=5)
            entryURG = Entry(table1_frame, state = 'readonly', readonlybackground = 'white')
            entryURG.grid(row=d+5, column=6)

            tb12 = {}
            def getunits(event):
                global tb12
                global tb14
                Rget = cbxRG.get()
                # print(Rget)
                # print(tb12)
                idR = str(tb12[Rget])
                # print(idR)
                tb140 = []
                tb141 = []
                cursor.execute("SELECT UUnitSN, idUnits FROM units JOIN reagent on idUnits = Units_idUnits "
                    "WHERE idReagent = " + idR + "")
                for row in cursor.fetchall():
                    # print(row[0], row[1])
                    tb140.append(row[0])
                    tb141.append(row[1])
                tb14 = dict(zip(tb140, tb141))
                tb1list4 = list(tb14.keys())
                # print(tb1list4)
                tb1400 = tb140[0]
                entryURG['state'] = 'normal'
                entryURG.delete(0, END)
                entryURG.insert(0, tb1400)
                entryURG['state'] = 'readonly'

            # #по выбранному типу реагентов создается словарик названий и запускается функция выбора единиц

            cbxRG = ttk.Combobox(table1_frame, values=[], state = 'readonly')
            cbxRG.grid(row=d+5, column=4)
            # tb12 = []
            def getreag(event):
                global tb12
                if cbxRG:
                    cbxRG.set('')
                    entryURG['state'] = 'normal'
                    entryURG.delete(0, END)
                    entryURG['state'] = 'readonly'

                TRget = cbxTRG.get()
                idTR = str(tb11[TRget])
                tb120 = []
                tb121 = []
                cursor.execute("SELECT ReagName1, idReagent FROM reagent JOIN reaginfo on idReagInfo = ReagInfo_idReagInfo "
                               "WHERE ReagType_idReagType = "+ idTR+" and InStock = 1")
                for row in cursor.fetchall():
                    tb120.append(row[0])
                    tb121.append(row[1])
                tb12 = dict(zip(tb120, tb121))
                tb1list2 = list(tb12.keys())
                cbxRG['values'] = tb1list2
                cbxRG.bind('<<ComboboxSelected>>', getunits)

            #создаем словарик и список для первого комбобокса, на keyrelease будет запускаться создание второго словаря
            tb110 = []
            tb111 = []
            cursor.execute("SELECT RTypeName, idReagType FROM reagtype")
            for row in cursor.fetchall():
                tb110.append(row[0])
                tb111.append(row[1])
            tb11 = dict(zip(tb110, tb111))
            tb1list1 = list(tb11.keys())
            cbxTRG = ttk.Combobox(table1_frame, values=tb1list1, state = 'readonly')
            cbxTRG.grid(row=d+5, column=3)
            cbxTRG.bind('<<ComboboxSelected>>', getreag)

            # label_emp11 = Label(table1_frame, text="", bg='light blue')
            # label_emp11.grid(row=5, rowspan=5, column=0)
            label_emp12 = Label(table1_frame, text="", bg='light blue', width=20)
            label_emp12.grid(row=d+5, rowspan=2, column=l-1)

            def T1Add():
                global tb12
                errort1 = int(0)
                try:
                    eamg = float(entryAMRG.get())
                except ValueError:
                    errort1 = 1


                if cbxST1.get() and cbxRG.get() and entryAMRG.get() and errort1 !=1:
                    idps = str(tb15[cbxPS1.get()])
                    idst = str(tb16[cbxST1.get()])



                    # print(cbxST1.get(), tb16[cbxST1.get()])
                    # print(cbxRG.get(), tb12[cbxRG.get()])
                    # print(entryAMRG.get())
                    # print(cbxPS1.get(), ips)
                    # print("тип btid", type(btid))
                    # print("тип ips", type(ips))

                    cursor.execute("select idExperimentDate from experimentdate "
                                   "join stagetype on idStageType = StageType_idStageType "
                                   "where Experiment_idExperiment = " + btid + " "
                                    "and ProcessStage_idProcessStage = " + idps + " ")
                    rced = cursor.fetchone()

                    t1add1 = []
                    idrced = 0
                    if rced is None:
                        print("нету")
                        cursor.execute("select max(idExperimentDate) from experimentdate")
                        rcexpdmax = cursor.fetchone()
                        rcexpdmax0 = rcexpdmax[0]
                        idrcexpdnew = str(rcexpdmax0 + 1)

                        t1add1.append(idrcexpdnew)
                        t1add1.append(dtd)
                        t1add1.append(btid)
                        t1add1.append(idst)

                        print(idrcexpdnew)
                        print(dtd)
                        print(btid)
                        print(idst)
                        print(t1add1)
                        t1add1str = ", ".join(f"'{x}'" for x in t1add1)
                        print(t1add1str)

                        cursor.execute("insert into experimentdate (idExperimentDate, ExpDate, Experiment_idExperiment,"
                                       " StageType_idStageType) values ("+ t1add1str +")")
                        cnx.commit()
                        idrced = idrcexpdnew

                    else:
                        idrced = rced[0]
                        print("есть", idrced)

                    print("мы прошли if", idrced)
                    T1Add2 = []
                    cursor.execute("select max(idReagUsage) from reagusage")
                    recT1Add = cursor.fetchone()
                    idRUT1Add = recT1Add[0]
                    nidT1add = idRUT1Add + 1
                    T1Add2.append(nidT1add)
                    T1Add2.append(entryAMRG.get())
                    T1Add2.append(tb12[cbxRG.get()])
                    T1Add2.append(idrced)
                    print(T1Add2)
                    t1add2str = ", ".join(f"'{x}'" for x in T1Add2)
                    print(t1add2str)

                    cursor.execute("insert into reagusage (idReagUsage, AmUsed, Reagent_idReagent, "
                          "ExperimentDate_idExperimentDate) values ("+ t1add2str +")")
                    cnx.commit()
                    # print(but_id)

                    emout_frame.grid_remove()
                    ExpMin(int(but_id))

                else:
                    print("пусто")
                    msb.showerror(title="Ошибка", message="Проверьте внесенные данные.")

            btnT1Add = Button(table1_frame, text="Добавить", bg='thistle1', command = T1Add)
            btnT1Add.grid(row=d+6, column=4)

            # btnT1Chs = Button(table1_frame, text="Выбрать", bg='thistle1')
            # btnT1Chs.grid(row=6, column=2)
            # btnT1Upd = Button(table1_frame, text="Изменить", bg='thistle1')
            # btnT1Upd.grid(row=6, column=3)
            # btnT1Del = Button(table1_frame, text="Удалить", bg='thistle1')
            # btnT1Del.grid(row=6, column=4)



            btnT1AddCom = Button(table1_frame, text="Добавить комментарий", bg='thistle1')
            btnT1AddCom.grid(row=d+7, column=4)


            # headose = ['idEquipUsage', 'EquipName', 'TimeStart', 'TimeFinish', 'ExpDate']
            # headoseq = ", ".join(headose)
            # # print(dshj)
            headoseq = "idEquipUsage, PSName, STName, ETypeName, EquipName, date_format(TimeStart, '%H:%i') as TimeStart, " \
                       "date_format(TimeFinish, '%H:%i') as TimeFinish, date_format(ExpDate, '%d.%m.%Y')"
            hdq = [2, 2, 1, 1]
            #
            cursor.execute("select " + headoseq + " from equipusage "
                           "join equipment on idEquipment = Equipment_idEquipment "
                            "join equiptype on idEquipType = EquipType_idEquipType "
                           "join experimentdate on idExperimentDate = ExperimentDate_idExperimentDate "
                            "join stagetype on idStageType = StageType_idStageType "
                            "join processstage on idProcessStage = ProcessStage_idProcessStage "
                           "where Experiment_idExperiment = " + str(btid) + " ")

            headingseq = ['id','Стадия', 'Тип Стадии','Тип оборудования', 'Оборудование', 'Начало использования', 'Конец использования', 'Дата эксперимента']
            # table2_style = ttk.Style()
            # table2_style.configure('Treeview.Heading', rowheight=int(30))

            table2_frame = Frame(em_frame, bg='light blue')
            table2_frame.grid(row=2, column=0, padx = 10, pady=10)
            # labtab2 = Label(table2_frame, text='Использование оборудования', bg='thistle1')
            # labtab2.grid(row=0, column=2, columnspan=2)
            table2 = ttk.Treeview(table2_frame, columns=headingseq, show="headings")
            m = len(headingseq)
            hdnsq = headingseq[1:m-1]
            # print(hdnsq)
            k = len(hdnsq)
            # print(m, k)

            #попытки сделать заголовок в несколько строк
            # headins = headingseq[1:]
            # print(headins)
            # table2.heading("#0", text=headingseq[0])
            # # for head in headins:
            # x=1
            # dr = str(x)
            # drt = "#"
            # drth = f'"{drt}{dr}"'
            #
            # print(drth)
            # for head in range(len(headins)):
            #     h = (head+1)
            #     hr = f'"{drt}{str(h)}"'
            #     print(hr)
            #     table2.heading(hr, text=headins[head])

            for head in headingseq:
                table2.heading(head, text=str(head))

            for r in cursor.fetchall():
                table2.insert("", END, values=r)
            dd = len(table2.get_children())
            table2['height']=dd+2
            table2.grid(row=0, rowspan=dd+3, column=0, columnspan=m)

            tb2lg = []
            tb2lg.append(0)
            tb2lg.append(record11[0])
            tb2lg.append(record12[0])
            cursor.execute("select Max(char_length(ETypeName)) as len from equiptype")
            record21 = cursor.fetchone()
            tb2lg.append(record21[0])
            cursor.execute("select Max(char_length(EquipName)) as len from equipment")
            record22 = cursor.fetchone()
            tb2lg.append(record22[0])
            tb2lg.append(len(headingseq[5]))
            tb2lg.append(len(headingseq[6]))
            tb2lg.append(len(headingseq[7]))

            for h in range(m):
                table2.column(h, width=tb2lg[h] * 8)
            table2["displaycolumns"] = headingseq[1:]

            label2 = []
            for j in range(k):
                label2.append(Label(table2_frame, text=hdnsq[j], bg='thistle1'))
                label2[j].grid(row=dd+4, column=j+1)

            cbxST2 = ttk.Combobox(table2_frame, values=[], state = 'readonly')
            cbxST2.grid(row=dd+5, column=2)

            def getST2(event):
                global tb26
                if cbxST2:
                    cbxST2.set('')
                ST2get = cbxPS2.get()
                idPS2 = str(tb25[ST2get])
                tb260 = []
                tb261 = []
                cursor.execute(
                    "SELECT STName, idStageType FROM stagetype JOIN processstage on idProcessStage = ProcessStage_idProcessStage "
                    "WHERE ProcessStage_idProcessStage = " + idPS2 + "")
                for row in cursor.fetchall():
                    tb260.append(row[0])
                    tb261.append(row[1])
                tb26 = dict(zip(tb260, tb261))
                tb2list6 = list(tb26.keys())
                cbxST2['values'] = tb2list6

            tb250 = []
            tb251 = []
            cursor.execute("SELECT PSName, idProcessSTage FROM processstage")
            for row in cursor.fetchall():
                tb250.append(row[0])
                tb251.append(row[1])
            tb25 = dict(zip(tb250, tb251))
            tb2list5 = list(tb25.keys())
            cbxPS2 = ttk.Combobox(table2_frame, values=tb2list5, state = 'readonly')
            cbxPS2.grid(row=dd+5, column=1)
            cbxPS2.bind('<<ComboboxSelected>>', getST2)

            entryTiSt = Entry(table2_frame)
            entryTiSt.grid(row=dd+5, column=5)

            entryTiFi = Entry(table2_frame)
            entryTiFi.grid(row=dd+5, column=6)

            cbxEQ = ttk.Combobox(table2_frame, values=[], state = 'readonly')
            cbxEQ.grid(row=dd+5, column=4)

            def geteq(event):
                global tb22
                if cbxEQ:
                    cbxEQ.set('')
                TEQget = cbxTEQ.get()
                idTEQ = str(tb21[TEQget])
                tb220 = []
                tb221 = []
                cursor.execute("SELECT EquipName, idEquipment FROM equipment WHERE EquipType_idEquipType = " + idTEQ + "")
                for row in cursor.fetchall():
                    tb220.append(row[0])
                    tb221.append(row[1])
                tb22 = dict(zip(tb220, tb221))
                tb2list2 = list(tb22.keys())
                cbxEQ['values'] = tb2list2


            # создаем словарик и список для первого комбобокса, на keyrelease будет запускаться создание второго словаря
            tb210 = []
            tb211 = []
            cursor.execute("SELECT ETypeName, idEquipType FROM equiptype")
            for row in cursor.fetchall():
                tb210.append(row[0])
                tb211.append(row[1])
            tb21 = dict(zip(tb210, tb211))
            tb2list1 = list(tb21.keys())
            cbxTEQ = ttk.Combobox(table2_frame, values=tb2list1, state = 'readonly')
            cbxTEQ.grid(row=dd+5, column=3)
            cbxTEQ.bind('<<ComboboxSelected>>', geteq)

            def T2Add():
                global tb22
                global tb26
                if cbxST2.get() and cbxEQ.get() and entryTiSt.get() and entryTiFi.get():
                    idps = str(tb25[cbxPS2.get()])
                    idst = str(tb26[cbxST2.get()])
                    # print(cbxST1.get(), tb16[cbxST1.get()])
                    # print(cbxRG.get(), tb12[cbxRG.get()])
                    # print(entryAMRG.get())
                    # print(cbxPS1.get(), ips)
                    # print("тип btid", type(btid))
                    # print("тип ips", type(ips))

                    cursor.execute("select idExperimentDate from experimentdate "
                                   "join stagetype on idStageType = StageType_idStageType "
                                   "where Experiment_idExperiment = " + btid + " "
                                    "and ProcessStage_idProcessStage = " + idps + " ")
                    rced = cursor.fetchone()

                    t2add1 = []
                    idrced = 0
                    if rced is None:
                        print("нету")
                        cursor.execute("select max(idExperimentDate) from experimentdate")
                        rcexpdmax = cursor.fetchone()
                        rcexpdmax0 = rcexpdmax[0]
                        idrcexpdnew = str(rcexpdmax0 + 1)

                        t2add1.append(idrcexpdnew)
                        t2add1.append(dtd)
                        t2add1.append(btid)
                        t2add1.append(idst)

                        print(idrcexpdnew)
                        print(dtd)
                        print(btid)
                        print(idst)
                        print(t2add1)
                        t2add1str = ", ".join(f"'{x}'" for x in t2add1)
                        print(t2add1str)

                        cursor.execute("insert into experimentdate (idExperimentDate, ExpDate, Experiment_idExperiment,"
                                       " StageType_idStageType) values ("+ t2add1str +")")
                        cnx.commit()
                        idrced = idrcexpdnew
                    else:
                        idrced = rced[0]
                        print("есть", idrced)

                    print("мы прошли if", idrced)
                    T2Add2 = []
                    cursor.execute("select max(idEquipUsage) from equipusage")
                    recT2Add = cursor.fetchone()
                    idRUT2Add = recT2Add[0]
                    nidT2add = idRUT2Add + 1
                    T2Add2.append(nidT2add)
                    endTi = ':00'
                    TiSt = entryTiSt.get() + endTi
                    TiFi = entryTiFi.get() + endTi
                    T2Add2.append(TiSt)
                    T2Add2.append(TiFi)
                    T2Add2.append(tb22[cbxEQ.get()])
                    T2Add2.append(idrced)
                    print(T2Add2)
                    t2add2str = ", ".join(f"'{x}'" for x in T2Add2)
                    print(t2add2str)
                    cursor.execute("insert into equipusage (idEquipUsage, TimeStart, TimeFinish, Equipment_idEquipment, "
                          "ExperimentDate_idExperimentDate) values ("+ t2add2str +")")
                    cnx.commit()

                    emout_frame.grid_remove()
                    ExpMin(int(but_id))
                else:
                    print("пусто")

            # nbv = em_frame.index(em_frame.select())
            # nbnm = em_frame.select()
            # print(nbnm)
            btnT2Add = Button(table2_frame, text="Добавить", bg='thistle1', command = T2Add)
            btnT2Add.grid(row=dd+6, column=4)
            # btnT2Chs = Button(table2_frame, text="Выбрать", bg='thistle1')
            # btnT2Chs.grid(row=6, column=2)
            # btnT2Upd = Button(table2_frame, text="Изменить", bg='thistle1')
            # btnT2Upd.grid(row=6, column=3)
            # btnT2Del = Button(table2_frame, text="Удалить", bg='thistle1')
            # btnT2Del.grid(row=6, column=4)

            # добавление комментариев должно работать для эксперимента целиком, но добавляются-то использования
            btnT2AddCom = Button(table2_frame, text="Добавить комментарий", bg='thistle1')
            btnT2AddCom.grid(row=dd+7, column=4)

            # label_emp21 = Label(table2_frame, text="", bg='light blue', width=5)
            # label_emp21.grid(row=2, rowspan=2, column=0)

            label_emp22 = Label(table2_frame, text="", bg='light blue', width=20)
            label_emp22.grid(row=dd+5, rowspan=2, column=l - 1)

            #############################################################################
            table3_frame = Frame(em_frame, width=200, height=200, bg='light blue')
            table3_frame.grid(row=0, column=1, padx=10, pady=10)
            cursor.execute("select MetName, Meth_text, idMethodology from methodology where Experiment_idExperiment = "+ btid + "")
            meth3_rec = cursor.fetchone()
            meth3_nm = meth3_rec[0]
            meth3_txt = meth3_rec[1]
            idmeth = meth3_rec[2]

            label3 = Label(table3_frame, text = '{}'.format(meth3_nm), bg='thistle1')
            label3.grid(row=0, column=0)

            meth3_textbox = Text(table3_frame, height=10, width=100)
            meth3_textbox.grid(row=1, column=0, rowspan=10)
            meth3_textbox.insert("1.0", meth3_txt)

            meth3scroll = Scrollbar(table3_frame, command=meth3_textbox.yview)
            meth3scroll.grid(row=1, column=1, rowspan=10, sticky='ns')
            meth3_textbox.configure(yscrollcommand=meth3scroll.set)

            def change_meth():
                mth3_txt = meth3_textbox.get("1.0", "end-1c")
                mt3 = "\'{}\'".format(mth3_txt)
                print(mt3)
                cursor.execute("update methodology set Meth_text = "+ mt3 +" where idMethodology = " + str(idmeth) +"")
                cnx.commit()

            btnT2AddCom = Button(table3_frame, text="Изменить методику", command=change_meth, bg='thistle1')
            btnT2AddCom.grid(row=12, column=0)

            label3 = Label(table3_frame, text='Название эксперимента', bg='thistle1')
            label3.grid(row=0, column=2)
            ch_name = Entry(table3_frame, width = 35)
            ch_name.insert(0, btnm)
            ch_name.grid(row=1, column=2)

            def change_name():
                if ch_name.get() != btnm:
                    print(ch_name.get())
                    cursor.execute("update experiment set ExpName = '" + ch_name.get() +"' where idExperiment = "+ btid +"")
                    cnx.commit()


            btnT2AddCom = Button(table3_frame, text="Изменить", command=change_name, bg='thistle1')
            btnT2AddCom.grid(row=2, column=2)

            ##################################################################################
            table4_frame = Frame(em_frame, bg='light blue')
            table4_frame.grid(row=1, column=1, padx=10, pady=10)
            # labelandata = Label(table4_frame, text='Аналитические данные', bg='thistle1')
            # labelandata.grid(row=0, column=0)

            labelAD1 = Label(table4_frame, text = 'Номер образца', bg='thistle1')
            labelAD1.grid(row=1, column=0)

            cursor.execute("select sample from experiment_has_analyticaldata where Experiment_idExperiment= " +btid + " "
                            "group by Experiment_idExperiment, sample order by sample")
            sample = []
            for row in cursor.fetchall():
                sample.append(row[0])

            rowAD40 = []
            rowAD41 = []
            rowAD42 = []

            cursor.execute("SELECT AnDataName, idAnalyticalData, ADUnitsSN FROM analyticaldata "
                           "join experiment_has_analyticaldata on idAnalyticalData = AnalyticalData_idAnalyticalData "
                           "where Experiment_idExperiment = " +btid + " and chosen = 1 group by idAnalyticalData "
                                                                      "order by idAnalyticalData")

            for row in cursor.fetchall():
                rowAD40.append(row[0])
                rowAD41.append(row[1])
                rowAD42.append(row[2])

            rlAD4 = dict(zip(rowAD40, rowAD41))
            reaglistAD4 = list(rlAD4.keys())
            nt = len(max(rowAD40))
            nu = len(max(rowAD42))+5
            rlr4 = range(len(reaglistAD4))
            lr4 = len(reaglistAD4)

            lab4 = []
            lab_un4 = []

            lab_samnum = []
            for r in rlr4:
                lab4.append(Label(table4_frame, text=rowAD40[r], width=nt, bg='thistle1'))
                lab4[r].grid(row=r + 3, column=0)
                lab_un4.append(Label(table4_frame, text=rowAD42[r], width=nu, bg='thistle1'))
                lab_un4[r].grid(row=r + 3, column=1)


            prev_val_many = []
            def prevval(event):
                prev_val = event.widget.get()
                prev_val_many.append(prev_val)
                print(prev_val)
            new_val_many = []
            loc1 = []
            loc2 = []
            def newval(event):
                new_val = ''
                if not event.widget.get():
                    new_val = event.widget.get()
                    print("nope")
                else:
                    new_valfl = float(event.widget.get())
                    new_val = str(new_valfl)
                    # try:
                    #     new_valfl = float(event.widget.get())
                    #     new_val = str(new_valfl)
                    # except TypeError:
                    #     msb.showerror(title="Ошибка", message="Проверьте введенные данные.")

                new_val_many.append(new_val)
                location1 = event.widget.grid_info()["row"]
                loc1.append(location1)
                location2 = event.widget.grid_info()["column"]
                loc2.append(location2)
                # locs = event.widget.grid_info()
                print(new_val)
                print(location1, location2)
                # print(locs)

            ent4 = []
            for s in range(len(sample)):
                lab_samnum.append(Label(table4_frame, text=sample[s], width=nu, bg='thistle1'))
                lab_samnum[s].grid(row=1, column=s+2)
                cursor.execute("select AnalyticalData_idAnalyticalData, ADValue, idExperiment_has_AnalyticalData "
                               "from experiment_has_analyticaldata where Experiment_idExperiment= " + btid + " "
                                                                                                             "and sample = " +
                               sample[s] + " ")
                idAD = []
                ADV = []
                idEAD = []
                for row in cursor.fetchall():
                    idAD.append(row[0])
                    if row[1] is None:
                        ADV.append('')
                    else:
                        ADV.append(str(row[1]))
                    idEAD.append(row[2])
                adlen = range(len(idAD))
                ent4.append([])
                for r in rlr4:
                    ent4[s].append(Entry(table4_frame))
                    ent4[s][r].grid(row=r + 3, column=s+2)
                    ent4[s][r].bind('<FocusIn>', prevval)
                    ent4[s][r].bind('<FocusOut>', newval)
                    for al in adlen:
                        if idAD[al] == rowAD41[r]:
                            ent4[s][r].insert(0, ADV[al])
            def focs(event):
                btnAddAD1.focus_set()

            new_val_add = []
            prev_val_comp = []
            def add_AD1many():
                loc11 = []
                loc22 = []
                for num in range(len(new_val_many)):
                    if prev_val_many[num] != new_val_many[num]:
                        new_val_add.append(new_val_many[num])
                        loc101 = loc1[num] - 3
                        loc202 = loc2[num] - 2
                        loc11.append(loc101)
                        loc22.append(loc202)
                        if not new_val_many[num]:
                            cursor.execute("delete from experiment_has_analyticaldata "
                                       "where Experiment_idExperiment= " + btid + " "
                                           "and sample = " + str(sample[loc202]) + " "
                                           "and AnalyticalData_idAnalyticalData= " + str(rowAD41[loc101]) + "")
                            cnx.commit()
                            print("deleted", new_val_many[num], prev_val_many[num])
                        elif not prev_val_many[num]:
                            cursor.execute(
                                "select max(idExperiment_has_AnalyticalData) from experiment_has_analyticaldata")
                            recors = cursor.fetchone()
                            nid = recors[0]
                            nid1 = nid + 1
                            chosen = '1'
                            values4 = []
                            values4.append(nid1)
                            values4.append(btid)
                            values4.append(sample[loc202])
                            values4.append(new_val_many[num])
                            values4.append(chosen)
                            values4.append(rowAD41[loc101])
                            print(values4)

                            try:
                                cursor.execute("update experiment_has_analyticaldata set ADValue = " + new_val_many[num] + " "
                                  "where Experiment_idExperiment= " + btid + " "
                                    "and sample = " + str(sample[loc202]) + " "
                                    "and AnalyticalData_idAnalyticalData= " + str(rowAD41[loc101]) + "")
                                cnx.commit()
                            except:
                                cursor.execute("insert into experiment_has_analyticaldata values(%s, %s, %s, %s, %s, %s) ", values4)
                                cnx.commit()

                            print("smth new", new_val_many[num], prev_val_many[num])

                        else:
                            cursor.execute("update experiment_has_analyticaldata set ADValue = " + new_val_many[num] + " "
                                  "where Experiment_idExperiment= " + btid + " "
                                    "and sample = " + str(sample[loc202]) + " "
                                    "and AnalyticalData_idAnalyticalData= " + str(rowAD41[loc101]) + "")
                            cnx.commit()
                            print("changed", new_val_many[num], prev_val_many[num])


                # for new in range(len(new_val_add)):
                #     pass
                    # cursor.execute("update experiment_has_analyticaldata set ADValue = "+ str(ent4[r].get()) +" "
                    #                     "where idExperiment_has_AnalyticalData = "+ str(idvals[r]) +"")
                print(prev_val_many)
                print(new_val_many)
                print(loc1)
                print(loc2)
                print(new_val_add)
                print(loc11)
                print(loc22)

                # print("sample", sample)
                # print("idAnData", rlAD4)
                prev_val_many.clear()
                new_val_many.clear()
                loc1.clear()
                loc2.clear()
                # emout_frame.grid_remove()
                # ExpMin(int(but_id))
                # em_frame.select(table4_frame)
                # print("list were cleared")
                # print(prev_val_many)
                # print(new_val_many)
                # print(loc1)
                # print(loc2)


            btnAddAD1 = Button(table4_frame, text="Изменить", command=add_AD1many, bg='thistle1')
            btnAddAD1.grid(row=lr4+3, column=0, columnspan=3)

            btnAddAD1.bind('<Enter>', focs)


            # em_frame.update()
            # w = em_frame.winfo_width()
            # h = em_frame.winfo_height()+40
            # root.geometry(f"{w}x{h}")
            em_frame.add(table1_frame, text='Использование реагентов')
            em_frame.add(table2_frame, text='Использование оборудования')
            em_frame.add(table3_frame, text='Методика')
            em_frame.add(table4_frame, text='Аналитические данные')
            em_frame.grid(row=1, column=0)

            def Back1():
                emout_frame.grid_remove()
                Exp()


            btnBack1 = Button(emout_frame, text="Вернуться на страницу экспериментов.", command=Back1, bg='thistle1')
            btnBack1.grid(row=3, column=0)

        listofexp.bind("<<ListboxSelect>>", listb)
        # for j in range(k):
        #     butexp.append(Button(exp_frame, text='{}'.format(butname[j]), command=lambda j=j: ExpMin(j), bg='thistle1'))
        #     butexp[j].grid(row=j+3, column=3)

        def NewExp():
            exp_frame.grid_remove()
            nex_frame = Frame(root, bg = 'light blue')
            nex_frame.grid(row=0, column=0, padx = 10, pady=10)
            root.geometry("600x500")

            labelnex = Label(nex_frame, text="Введите название экспримента", bg='thistle1', width=30)
            labelnex.grid(row=0, column=1)
            entrynex = Entry(nex_frame, width=30)
            entrynex.grid(row=1, column=1)

            meth_text = Text(nex_frame, height = 10, width = 70)
            meth_text.grid(row=2, column=0, columnspan=3)

            methscroll = Scrollbar(nex_frame, command=meth_text.yview)
            methscroll.grid(row=2, column=4, sticky='ns')
            meth_text.configure(yscrollcommand=methscroll.set)

            row330 = []
            row331 = []
            cursor.execute("SELECT AnDataName, idAnalyticalData FROM analyticaldata ")

            for row in cursor.fetchall():
                row330.append(row[0])
                row331.append(row[1])

            ad3 = dict(zip(row330, row331))
            add3 = list(ad3.keys())
            nt = len(max(row330))
            len_ad = len(add3)
            adr = range(len_ad)

            ad_lab3 = []
            ch3_btn = []
            ch3_AD = []

            check_list = Text(nex_frame, height=9, width=nt, state="disabled", cursor="arrow", bg="thistle1", relief = 'raised')
            check_list.grid(row=3, column=1, pady= 5)

            check_scroll = Scrollbar(nex_frame, command=check_list.yview)
            check_scroll.grid(row=3, column=2, sticky='nsw')
            check_list.configure(yscrollcommand=check_scroll.set)

            for r in adr:
                ch3_AD.append(IntVar(value=0))
                ch3_btn.append(Checkbutton(check_list, text=add3[r], width=nt, anchor="w", bg='thistle1', variable=ch3_AD[r]))
                check_list.window_create("end", window=ch3_btn[r])
                check_list.insert("end", "\n")


            def NewExpAdd():
                ch = int()
                for r in adr:
                    if ch3_AD[r].get() == 1:
                        ch = 1
                        break
                if entrynex.get() and len(meth_text.get("1.0", END)) > 1 and ch == 1:
                    rc = int()
                    cursor.execute("select max(idExperiment) from experiment")
                    rec = cursor.fetchone()
                    rc = (rec[0] + 1)
                    text = entrynex.get()
                    print(text)
                    nea = [str(rc), text, rpid]
                    print(nea)
                    neas = "'{}'".format("', '".join(nea))
                    print(neas)
                    # entrynex.delete(0, END)
                    cursor.execute("INSERT INTO `experiment` (`idExperiment`, `ExpName`, "
                                   "`ResearchProject_idResearchProject`) VALUES (" + neas + ")")
                    cnx.commit()

                    mthtxt = meth_text.get("1.0", "end-1c")
                    cursor.execute("select max(idMethodology) from methodology")
                    mtc = cursor.fetchone()
                    mtcc = (mtc[0]+1)
                    mtname = "Методика " + text
                    print(mtcc, mtname, mthtxt, rc)
                    mea = [str(mtcc), mtname, mthtxt, str(rc)]
                    meas = "'{}'".format("', '".join(mea))

                    cursor.execute("insert into `methodology` (`idMethodology`, `MetName`, `Meth_text`, "
                                   "`Experiment_idExperiment`) VALUES (" + meas + ")")
                    cnx.commit()
                    # meth_text.delete("1.0", "end")

                    ch3_lst = []
                    for r in adr:
                        if ch3_AD[r].get() == 1:
                            cursor.execute("select max(idExperiment_has_AnalyticalData) from experiment_has_analyticaldata")
                            recor = cursor.fetchone()
                            nidd = recor[0]
                            nidd1 = nidd + 1
                            chosenn = '1'
                            smp = '1'
                            vals_meth = []
                            vals_meth.append(nidd1)
                            vals_meth.append(rc)
                            vals_meth.append(smp)
                            vals_meth.append(chosenn)
                            vals_meth.append(row331[r])
                            cursor.execute("insert into experiment_has_analyticaldata (idExperiment_has_AnalyticalData, "
                                           "Experiment_idExperiment, sample, chosen, AnalyticalData_idAnalyticalData) "
                                           "values(%s, %s, %s, %s, %s) ", vals_meth)
                            cnx.commit()
                    nex_frame.grid_remove()
                    NewExp()
                else:
                    msb.showerror(title="Ошибка", message="Заполните все поля.")

            btnNewExpAdd = Button(nex_frame, text="Добавить новый эксперимент", command=NewExpAdd, bg='thistle1', width=30)
            btnNewExpAdd.grid(row=len_ad+3, column=1)

            def ToNewExp():
                pass
                # cursor.execute("select max(idExperiment) from experiment")
                # rec = cursor.fetchone()
                # recc = rec[0]
                # if recc == rc:
                #     print("Равны",rc, recc)
                    # Exp()
                    # ExpMin(recc)
            btnToNewExp = Button(nex_frame, text="Перейти к новому эксперименту", command=ToNewExp, bg='thistle1', width=30)
            btnToNewExp.grid(row=len_ad+4, column=1)

            def Back1():
                nex_frame.grid_remove()
                Exp()

            btnBack1 = Button(nex_frame, text="Вернуться на страницу экспериментов.", command=Back1, bg='thistle1', width=30)
            btnBack1.grid(row=len_ad+5, column=1)

        btnNewExp = Button(exp_frame, text="Новый эксперимент", command=NewExp, bg='thistle1')
        btnNewExp.grid(row=13, column=1)
        # up_frame.update()
        # rhd = up_frame.winfo_height()
        # print(rhd)

        def Back():
            exp_frame.grid_remove()
            up_frame.grid(row=0, column=0, padx = 10, pady=10, sticky='news')
        btnBack = Button(exp_frame, text="Вернуться на начальную страницу.", command=Back, bg='thistle1')
        btnBack.grid(row=14, column=1)

    btnExp = Button(up_frame, text="Мои эксперименты", command=Exp, bg='thistle1', width=30)


    if len(respr) >1:
        global rpid
        global lbres
        print("несколько работ", res_dict)
        lab_choose = Label(up_frame, text="Выберите научную работу", bg='thistle1')
        lab_choose.grid(row=2, column=0)

        res_var = Variable(value=papername)
        listofres = Listbox(up_frame, listvariable=res_var, selectmode='single', width=36, height=4)
        listofres.grid(row=3, column=0)

        res_scroll = Scrollbar(up_frame, command=listofres.yview)
        len_res = len(respr)
        if len_res > 4:
            res_scroll.grid(row=3, column=1, sticky='ns')
            listofres.configure(yscrollcommand=res_scroll.set)
        else:
            print("меньше 4")

        def list_res(event):
            for i in listofres.curselection():
                global rpid
                global lbres
                lbres = listofres.get(i)
                rpid = str(res_dict[lbres])
                print(rpid, lbres)
                # rpid = lbresid
                listofres.grid_remove()
                lab_choose.grid_remove()
                btnExp.grid(row=4, column=0, columnspan=2)

                def backchoose():
                    lab_choose.grid(row=2, column=0)
                    listofres.grid(row=3, column=0)
                    btnExp.grid_remove()
                    btnBackChoose.grid_remove()

                btnBackChoose = Button(up_frame, text="Выбрать научную работу", command=backchoose, width=30, bg='thistle1')
                btnBackChoose.grid(row=5, column=0)

        listofres.bind("<<ListboxSelect>>", list_res)

    else:
        print("одна работа")
        rpid = str(respr[0])
        lbres = papername[0]
        btnExp.grid(row=4, column=0, columnspan=2)

    # Окно просмотра по исходному реагенту и тд
    def ReagSearch():
        up_frame.grid_remove()
        root.geometry("1000x400")
        rs_frame = Frame(root, bg='light blue')
        rs_frame.grid(row=0, column=0, padx = 10, pady=10)

        rq_frame = Frame(rs_frame, bg='light blue')
        rq_frame.grid(row=0, column=0, padx = 10, pady=10, sticky=W)

        labelreag0 = Label(rq_frame, text="Поиск эксперимента по веществу", bg='thistle1')
        labelreag0.grid(row=0, column=0, columnspan=2)

        #поиск по прекурсору
        labelreag1 = Label(rq_frame, text="Выберите исходное вещество", bg='thistle1')
        labelreag1.grid(row=1, column=0)

        cbxreag1 = ttk.Combobox(rq_frame, values=[], width=35)
        cbxreag1.grid(row=1, column=1)

        row10 = []
        row11 = []
        cursor.execute("SELECT ReagName1, idReagent FROM reagent JOIN reaginfo on idReagInfo = ReagInfo_idReagInfo "
                       "WHERE ReagType_idReagType = 1")
        for row in cursor.fetchall():
            row10.append(row[0])
            row11.append(row[1])
        rl1=dict(zip(row10, row11))
        reaglist1 = list(rl1.keys())
        cbxreag1['values'] = reaglist1

        #поиск по активному
        labelreag2 = Label(rq_frame, text="Выберите активное вещество", bg='thistle1')
        labelreag2.grid(row=2, column=0)

        cbxreag2 = ttk.Combobox(rq_frame, values=[], width=35)
        cbxreag2.grid(row=2, column=1)

        row20 = []
        row21 = []
        cursor.execute("SELECT ReagName1, idReagent FROM reagent JOIN reaginfo "
                       "on idReagInfo = ReagInfo_idReagInfo WHERE ReagType_idReagType = 4")
        for row in cursor.fetchall():
            row20.append(row[0])
            row21.append(row[1])
        rl2 = dict(zip(row20, row21))
        # print(rl2)
        reaglist2 = list(rl2.keys())
        # print(reaglist2)
        cbxreag2['values'] = reaglist2

        labelreag3 = Label(rq_frame, text="Выберите параметр", bg='thistle1')
        labelreag3.grid(row=0, column=3)

        labelreag3min = Label(rq_frame, text="Минимум", bg='thistle1')
        labelreag3min.grid(row=0, column=4)

        labelreag3max = Label(rq_frame, text="Максимум", bg='thistle1')
        labelreag3max.grid(row=0, column=5)

        labelreag3un = Label(rq_frame, text="Ед. изм.", bg='thistle1')
        labelreag3un.grid(row=0, column=6)

        row30 = []
        row31 = []
        row32 = []
        cursor.execute("SELECT AnDataName, idAnalyticalData, ADUnitsSN FROM analyticaldata ")

        for row in cursor.fetchall():
            row30.append(row[0])
            row31.append(row[1])
            row32.append(row[2])

        rl3 = dict(zip(row30, row31))
        reaglist3 = list(rl3.keys())
        nt = len(max(row30))
        nu = len(max(row32))
        rlr = range(len(reaglist3))


        lab_un = []
        entmin=[]
        entmax=[]

        lab = []
        ch_btn=[]
        ch_AD = []

        for r in rlr:
            ch_AD.append(IntVar(value=0))
            ch_btn.append(Checkbutton(rq_frame, bg='light blue', variable=ch_AD[r]))
            ch_btn[r].grid(row=r + 1, column=2)
            lab.append(Label(rq_frame, text=row30[r], width=nt, bg='thistle1'))
            lab[r].grid(row=r+1, column=3)
            entmin.append(Entry(rq_frame))
            entmin[r].grid(row=r+1, column=4)
            entmax.append(Entry(rq_frame))
            entmax[r].grid(row=r + 1, column=5)
            lab_un.append(Label(rq_frame, text=row32[r], width=nu, bg='thistle1'))
            lab_un[r].grid(row=r + 1, column=6)


        def rg4():
            thelist = []
            reag1get = cbxreag1.get()
            rg1 = rl1.get(reag1get)
            if rg1 is None:
                pass
            else:
                text1 = "idReagent = " + str(rg1) + " "
                print(text1)
                thelist.append(text1)

            reag2get = cbxreag2.get()
            rg2 = rl2.get(reag2get)
            if rg2 is None:
                pass
            elif rg1 is not None and rg2 is not None:
                msb.showerror(title="Ошибка", message="Можно выбрать только один реагент.")
            else:
                text2 = "idReagent = " + str(rg2) + " "
                print(text2)
                thelist.append(text2)
            print("here", thelist)
            if not thelist:
                print("empty")
                thelist.append(" idReagType in (1,4) ")
            chibi_out = []
            request = ""
            # reques = []
            error = int(0)
            for r in rlr:
                if ch_AD[r].get() == 1:
                    idAD = str(row31[r])
                    en_min = entmin[r].get()
                    en_max = entmax[r].get()
                    if not en_min and not en_max:
                        request = "idAnalyticalData = " + idAD + ""
                    elif en_min and not en_max:
                        try:
                            enmi = float(en_min)
                            en_min = str(enmi)
                            request = "idAnalyticalData = " + idAD + " and ADValue >= " + en_min + ""
                        except ValueError:
                            error = 1
                    elif not en_min and en_max:
                        try:
                            enmx = float(en_max)
                            en_max = str(enmx)
                            request = "idAnalyticalData = " + idAD + " and ADValue <= " + en_max + ""
                        except ValueError:
                            error = 1
                    elif en_min and en_max:
                        try:
                            enmi = float(en_min)
                            en_min = str(enmi)
                            enmx = float(en_max)
                            en_max = str(enmx)
                            request = "idAnalyticalData = " + idAD + " and ADValue between " + en_min + " and " + en_max + ""
                        except ValueError:
                            error = 1


                    # print(request)
                    reques = [request]
                    thelis = thelist + reques
                    print("thelis", thelis)
                    thelistt = 'and '.join(thelis)
                    print("thelistt", thelistt)
                    chibi = f'({thelistt})'
                    print("chibi", chibi)
                    chibi_out.append(chibi)
                    print("chibi_out", chibi_out)

            print("chibi_out", chibi_out)
            chubby_out = ""
            if error == 1:
                msb.showerror(title="Ошибка", message="Проверьте внесенные данные")
            elif chibi_out:
                chubby_out = ' or '.join(chibi_out)
            else:
                chubby_out = 'and '.join(thelist)
            print("chubby_out", chubby_out)



            lent = []
            dfh = ['Pers_Name', 'RPName', 'ExpName', 'ReagName1', 'sample', 'AnDataName', 'ADValue', 'ADUnitsSN']
            sdl = ", ".join(dfh)
            cursor.execute("select Max(char_length(Pers_Name)) as len from personnel")
            record1 = cursor.fetchone()
            lent.append(record1[0])
            cursor.execute("select Max(char_length(RPName)) as len from researchproject")
            record2 = cursor.fetchone()
            lent.append(record2[0])
            cursor.execute("select Max(char_length(ExpName)) as len from experiment")
            record3 = cursor.fetchone()
            lent.append(record3[0])
            cursor.execute("select Max(char_length(ReagName1)) as len from reaginfo")
            record4 = cursor.fetchone()
            lent.append(record4[0])
            cursor.execute("select Max(char_length(sample)) as len from experiment_has_analyticaldata")
            record5 = cursor.fetchone()
            lent.append(record5[0])
            cursor.execute("select Max(char_length(AnDataName)) as len from analyticaldata")
            record6 = cursor.fetchone()
            lent.append(record6[0])
            cursor.execute("select Max(char_length(ADValue)) as len from experiment_has_analyticaldata")
            record7 = cursor.fetchone()
            lent.append(record7[0])
            cursor.execute("select Max(char_length(ADUnitsSN)) as len from analyticaldata")
            record8 = cursor.fetchone()
            lent.append(record8[0])
            # print(lent)
            if chubby_out:
                cursor.execute("select "+ sdl +" from experiment_has_analyticaldata "
                               "join analyticaldata on idAnalyticalData = AnalyticalData_idAnalyticalData "
                               "join experiment on idExperiment = Experiment_idExperiment "
                               "join experimentdate on idExperiment = experimentdate.Experiment_idExperiment "
                               "join researchproject on idResearchProject = ResearchProject_idResearchProject "
                                "join researchproject_has_personnel on idResearchProject = "
                                            "researchproject_has_personnel.researchproject_idResearchProject "
                               "join personnel on idPersonnel = personnel_idPersonnel "
                               "join reagusage on idExperimentDate=ExperimentDate_idExperimentDate "
                               "join reagent on idReagent = Reagent_idReagent "
                               "join reaginfo on idReagInfo = ReagInfo_idReagInfo "
                               "join reagtype on idReagType = ReagType_idReagtype where " + chubby_out +" "
                                "and Secrecy = 0 and status_rp_idstatus_rp = 1 order by ExpName")
                # print(cursor._last_executed)
                heas4 = ["Имя", "Научная работа", "Название эксперимента", "Название реагента", "Образец", "Аналитический параметр",
                         "Величина", "Ед. изм."]
                hleh = []
                for h in heas4:
                    hleh.append(len(h))
                # print(hleh)
                lp = []
                for h in range(len(heas4)):
                    if hleh[h] > lent[h]:
                        lp.append(hleh[h])
                    else:
                        lp.append(lent[h])
                # print(lp)
                tablergs_frame = Frame(rs_frame, bg='light blue')
                tablergs_frame.grid(row=1, column=0, padx = 10, pady=10)
                labtabrgs = Label(tablergs_frame, text='Эксперименты по заданным параметрам', bg='thistle1')
                labtabrgs.grid(row=0, column=0)
                tablergs = ttk.Treeview(tablergs_frame, columns=heas4, show="headings")
                m = len(heas4)
                for head in heas4:
                    tablergs.heading(head, text=str(head))
                for h in range(m):
                    tablergs.column(h, width=lp[h]*8)

                tablergs.update()
                tablergs.grid(row=1, column=0, columnspan=m)
                for r in cursor.fetchall():
                    tablergs.insert("", END, values=r)

                # d = len(tablergs.get_children())
                # tablergs['height'] = d
                vert_scroll_rgs = Scrollbar(tablergs_frame, command=tablergs.yview)
                vert_scroll_rgs.grid(row=1, column=m + 1, sticky="ns")
                tablergs.configure(yscrollcommand=vert_scroll_rgs.set)
                rs_frame.update()
                w = rs_frame.winfo_width()
                h = rs_frame.winfo_height() + 40
                root.geometry(f"{w}x{h}")


        btngetreag4 = Button(rq_frame, text="Выбрать", command=rg4, bg='thistle1')
        btngetreag4.grid(row=3, column=0, columnspan=2)

        def Back():
            rs_frame.grid_remove()
            up_frame.grid(row=0, column=0, padx = 10, pady=10, sticky='news')
            root.geometry("330x300")

        btnBack = Button(rq_frame, text="Вернуться на начальную страницу.", command=Back, bg='thistle1')
        btnBack.grid(row=4, column=0, columnspan=2)

    btnReag = Button(up_frame, text="Поиск экспериментов",command=ReagSearch, bg='thistle1', width=30)
    btnReag.grid(row=7, column=0, columnspan=2)

    btnReag.update()

    cursor.execute("SELECT ReagName1, EndDateReag, timestampdiff(day, curdate(), EndDateReag) AS DaysTillExp "
                   "FROM reagent JOIN reaginfo on idReagInfo = ReagInfo_idReagInfo ORDER BY DaysTillExp;")
    x = int()
    for r in cursor.fetchall():
        if r[2]<30:
            x=1
            label34 = Label(up_frame, text = 'Проверьте срок годности реагентов', width=30, bg='orange')
            label34.grid(row=9, column=0, columnspan=2)
            break
        elif r[2]<45:
            x=2

    cursor.execute("SELECT ReagName1, Amount - sum(AmUsed) as lef, MinAmount FROM mydb.reagusage "
                   "join reagent on idReagent = Reagent_idReagent join reaginfo on idReagInfo = ReagInfo_idReagInfo "
                   "group by idReagent;")
    for r in cursor.fetchall():
        if r[1] <= r[2]:
            label66 = Label(up_frame, text='Проверьте запасы реагентов', width=30, bg='orange')
            label66.grid(row=10, column=0, columnspan=2)
            break


    def Reag():
        up_frame.grid_remove()
        rogs_frame = Frame(root, bg='light blue')
        rogs_frame.grid(row=0, column=0, padx = 10, pady=10)

        hle = []
        cursor.execute("select Max(char_length(ReagName1)) as len from reaginfo")
        recordr4 = cursor.fetchone()
        hle.append(recordr4[0])

        cursor.execute("SELECT ReagName1, Amount - sum(AmUsed) as lef, MinAmount, UUnitSN, date_format(EndDateReag, '%d.%m.%Y'), "
                       "timestampdiff(day, curdate(), EndDateReag) AS DaysTillExp FROM reagent join reagusage "
                       "on idReagent = Reagent_idReagent join reaginfo on idReagInfo = ReagInfo_idReagInfo "
                       "join units on idUnits = Units_idUnits "
                       "where InStock = 1 group by idReagent order by DaysTillExp asc;")

        horse = ["Название реагента", "Остатки реагента", "Мин. кол-во", "Ед. изм.", "Срок годности",
                 "Осталось дней"]


        horse1 = horse[1:]
        for h in horse1:
            hle.append(len(h))

        table4_frame = Frame(rogs_frame, bg='light blue')
        table4_frame.grid(row=2, column=0)
        table4 = ttk.Treeview(table4_frame, columns=horse, show="headings")
        for head in horse:
            table4.heading(head, text=str(head))
        m = len(horse)
        for h in range(m):
            table4.column(h, width=hle[h] * 8)

        table4.grid(row=1, column=0, columnspan=m)
        for r in cursor.fetchall():
            table4.insert("", END, values=r)
        # d = len(table4.get_children())
        # table4['height'] = d
        vert_scroll4 = Scrollbar(table4_frame, command=table4.yview)
        vert_scroll4.grid(row=1, column=m + 1, sticky="ns")
        table4.configure(yscrollcommand=vert_scroll4.set)
        rogs_frame.update()
        w = rogs_frame.winfo_width() + 30
        h = rogs_frame.winfo_height() + 50
        root.geometry(f"{w}x{h}")
        root.update()

        def Back():
            rogs_frame.grid_remove()
            up_frame.grid(row=0, column=0, padx = 10, pady=10, sticky='news')
            root.geometry("330x300")

        btnBack = Button(rogs_frame, text="Вернуться на начальную страницу.", command=Back, bg='thistle1')
        btnBack.grid(row=0, column=0)

    btnReag = Button(up_frame, text="Просмотреть реагенты", command=Reag, bg='thistle1', width=30)
    btnReag.grid(row=8, column=0, columnspan=2)
    # if x == 2:
    #     btnReag['bg']='yellow'
    # elif x == 1:
    #     btnReag['bg']='orange'

    def Adm():
        up_frame.grid_remove()
        adm_frame = Frame(root, bg='light blue')
        adm_frame.grid(row=0, column=0, padx = 10, pady=10)

        def AdmPers():
            pass

        btnAdmPers = Button(adm_frame, text="Сотрудники", command=AdmPers, bg='thistle1', width=30)
        btnAdmPers.grid(row=1, column=0, columnspan=2)

        def AdmRP():
            pass

        btnAdmRP = Button(adm_frame, text="Научно-исследовательские работы", command=AdmRP, bg='thistle1', width=30)
        btnAdmRP.grid(row=2, column=0)

        def AdmReag():
            pass

        btnAdmReag = Button(adm_frame, text="Реагенты", command=AdmReag, bg='thistle1', width=30)
        btnAdmReag.grid(row=3, column=0)

        def AdmEquip():
            pass

        btnAdmEquip = Button(adm_frame, text="Оборудование", command=AdmEquip, bg='thistle1', width=30)
        btnAdmEquip.grid(row=4, column=0)

        def Back():
            adm_frame.grid_remove()
            up_frame.grid(row=0, column=0, padx = 10, pady=10, sticky='news')
            root.geometry("330x300")

        btnBack = Button(adm_frame, text="Вернуться на начальную страницу.", command=Back, bg='thistle1', width=30)
        btnBack.grid(row=5, column=0)



    btnAdm = Button(up_frame, text="Кабинет администратора", command=Adm, bg='thistle1', width=30)
    if level == 2:
        btnAdm.grid(row=11, column=0, columnspan=2)

    # w = up_frame.winfo_width()
    # h = up_frame.winfo_height()
    # root.geometry(f"{w}x{h}")


root.mainloop()
