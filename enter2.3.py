from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as msb
from datetime import date
import inspect
# from mysql.connector import (connection)
# from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='LordSe22anne)',
                              host='localhost', database='mydb')
cursor = cnx.cursor()

root = Tk()
root.title("Кабинет администратора")
root.configure(bg='light blue')
def dis():
    pass


# отцентровывание окна приложения по экрану
w = 360
h = 200
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
        return person


def show_password():
    if check_v1.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

auth_frame = Frame(root, bg='light blue')
auth_frame.grid(row=0, column=0, padx = 10, pady=10)

enter_label = Label(auth_frame, text="Добро пожаловать!", bg='light blue', font='Arial 16 bold')
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

login_btn = Button(auth_frame, text="Войти", command=login, bg='light blue')
login_btn.grid(row=3, column=0, columnspan=2)

check_v1 = IntVar(value=0)
check_btn = Checkbutton(auth_frame, text="Показать пароль", bg='light blue', variable=check_v1,
                      onvalue=1, offvalue=0, command=show_password)
check_btn.grid(row=2, column=2)


def main():
    root.geometry("420x250")
    auth_frame.grid_remove()
    root.protocol("WM_DELETE_WINDOW", dis)
    up_frame = Frame(root, bg='light blue')
    up_frame.grid(row=0, column=0, padx = 10, pady=10, sticky='news')
    up_frame.grid_rowconfigure(0, weight=1)
    up_frame.grid_columnconfigure(1, weight=1)
    up_frame.update()

    cursor.execute("SELECT idlevel, Pers_Name, RPName, idResearchProject FROM researchproject JOIN personnel "
                   "ON idPersonnel = Personnel_idPersonnel JOIN level ON idLevel = Level_idLevel WHERE idPersonnel = " + str(person) + " ")
    record = cursor.fetchone()
    # print(record)
    name = record[1]
    level = record[0]
    respr = record[3]
    # print(name)
    label2 = Label(up_frame, text="Добро пожаловать в базу данных, {}.".format(name), bg='light green')
    label2.grid(row=0, column=0)

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

    label3 = Label(up_frame, text="Сегодня {} {}, {}".format(dd, dm, dy), bg='light green')
    label3.grid(row=0, column=1)

    exit_button = Button(up_frame, text="Выход", command=root.destroy, bg='light green')
    exit_button.grid(row=9, column=0, columnspan=2)


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


    # Окно эксперимента

    def Exp():
        # root.geometry("420x200")
        up_frame.grid_remove()

        exp_frame = Frame(root, bg='light green')
        exp_frame.grid(row=0, column=0, padx = 10, pady=10)
        butexp = []
        butname = []
        butid = []
        cursor.execute("SELECT idExperiment, ExpName FROM experiment WHERE ResearchProject_idResearchProject = " + str(respr) +" ")
        for r in cursor.fetchall():
            butid.append(str(r[0]))
            butname.append(str(r[1]))
        # but = dict(zip(butid, butname))
        exp_frame.columnconfigure(index=0, weight=1)
        k = len(butname)
        h = (k+2)*30
        w = 300
        root.geometry(f"{w}x{h}")

        def ExpMin(but_id):

            # print(but_id)
            # print(butid[but_id], butname[but_id])
            exp_frame.grid_remove()
            em_frame = Frame(root, bg='light blue')
            em_frame.grid(row=0, column=0, padx = 10, pady=10)
            labelexpname = Label(em_frame, text="{}".format(butname[but_id]), bg='light green')
            labelexpname.grid(row=0, column=0)

            # Использование реагента
            # headosr = ['idReagUsage', 'ReagName1', 'AmUsed', 'UUnitSN', 'ExpDate']
            # headosreag = ", ".join(headosr)
            headosreag = "idReagUsage, RTypeName, ReagName1, AmUsed, UUnitSN, date_format(ExpDate, '%d.%m.%Y')"

            cursor.execute("select " + headosreag + " from reagusage join reagent on idReagent = Reagent_idReagent "
                            "JOIN reaginfo on idReagInfo = ReagInfo_idReagInfo "
                            "join reagtype on idReagType = ReagType_idReagType "
                           "join experimentdate on idExperimentDate = ExperimentDate_idExperimentDate "
                           "join units on idUnits = Units_idUnits where Experiment_idExperiment = " + str(butid[but_id]) + " and "
                           "ExperimentDate_idExperimentDate <> 1")

            headingsr = ['id', 'Тип реагента', 'Реагент', 'Количество вещества', 'Единицы', 'Дата эксперимента']

            hdr = [2, 2, 1, 2]
            table1_frame = Frame(em_frame, bg='light blue')
            table1_frame.grid(row=1, column=0, padx = 10, pady=10)
            labtab1 = Label(table1_frame, text = 'Использованные реагенты', bg = 'light green')
            labtab1.grid(row=0, column=0)
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

            table1.grid(row=1, column=0, columnspan=l)
            for r in cursor.fetchall():
                table1.insert("", END, values=r)
            d = len(table1.get_children())
            table1['height'] = d+2
            label1 = []
            entry1 = []
            for j in range(lk):
                label1.append(Label(table1_frame, text=hdnsr[j], bg='light green'))
                label1[j].grid(row=2, column=j+1)
                if hdr[j] == 1:
                    entry1.append(Entry(table1_frame))
                    entry1[j].grid(row=3, column=j+1)
                else:
                    entry1.append(ttk.Combobox(table1_frame, values=[]))
                    entry1[j].grid(row=3, column=j + 1)

            label_emp11 = Label(table1_frame, text="", bg='light blue', width=20)
            label_emp11.grid(row=2, rowspan=2, column=0)
            label_emp12 = Label(table1_frame, text="", bg='light blue', width=20)
            label_emp12.grid(row=2, rowspan=2, column=l-1)

            # headose = ['idEquipUsage', 'EquipName', 'TimeStart', 'TimeFinish', 'ExpDate']
            # headoseq = ", ".join(headose)
            # # print(dshj)
            headoseq = "idEquipUsage, ETypeName, EquipName, date_format(TimeStart, '%H:%i') as TimeStart, " \
                       "date_format(TimeFinish, '%H:%i') as TimeFinish, date_format(ExpDate, '%d.%m.%Y')"
            hdq = [2, 2, 1, 1]
            #
            cursor.execute("select " + headoseq + " from equipusage "
                           "join equipment on idEquipment = Equipment_idEquipment "
                            "join equiptype on idEquipType = EquipType_idEquipType "
                           "join experimentdate on idExperimentDate = ExperimentDate_idExperimentDate "
                           "where Experiment_idExperiment = " + str(butid[but_id]) + " and ExperimentDate_idExperimentDate <> 1;")

            headingseq = ['id','Тип оборудования', 'Оборудование', 'Начало использования', 'Конец использования', 'Дата эксперимента']
            # table2_style = ttk.Style()
            # table2_style.configure('Treeview.Heading', rowheight=int(30))
            table2_frame = Frame(em_frame, bg='light blue')
            table2_frame.grid(row=2, column=0, padx = 10, pady=10)
            labtab2 = Label(table2_frame, text='Использованное оборудование', bg='light green')
            labtab2.grid(row=0, column=0)
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


            table2.grid(row=1, column=0, columnspan=m)
            for r in cursor.fetchall():
                table2.insert("", END, values=r)
            d = len(table2.get_children())
            table2['height']=d+2

            label2 = []
            entry2 = []
            for j in range(k):
                label2.append(Label(table2_frame, text=hdnsq[j], bg='light green'))
                label2[j].grid(row=2, column=j+1)
                if hdq[j] == 1:
                    entry2.append(Entry(table2_frame))
                    entry2[j].grid(row=3, column=j+1)
                else:
                    entry2.append(ttk.Combobox(table2_frame, values=[]))
                    entry2[j].grid(row=3, column=j+1)

            label_emp21 = Label(table2_frame, text="", bg='light blue', width=20)
            label_emp21.grid(row=2, rowspan=2, column=0)
            label_emp22 = Label(table2_frame, text="", bg='light blue', width=20)
            label_emp22.grid(row=2, rowspan=2, column=l - 1)
            em_frame.update()
            w = em_frame.winfo_width()
            h = em_frame.winfo_height()+40
            root.geometry(f"{w}x{h}")

            def Back1():
                em_frame.grid_remove()
                Exp()

            btnBack1 = Button(em_frame, text="Вернуться на страницу экспериментов.", command=Back1, bg='light green')
            btnBack1.grid(row=3, column=0)


        for j in range(k):
            butexp.append(Button(exp_frame, text='{}'.format(butname[j]), command=lambda j=j: ExpMin(j), bg='light green'))
            butexp[j].grid(row=j, column=1)

        def NewExp():
            exp_frame.grid_remove()
            nex_frame = Frame(root, bg = 'light blue')
            nex_frame.grid(row=0, column=0, padx = 10, pady=10)
            root.geometry("500x300")

            labelnex = Label(nex_frame, text="Введите название экспримента", bg='light green')
            labelnex.grid(row=0, column=0)
            entrynex = Entry(nex_frame)
            entrynex.grid(row=0, column=1)
            rc = int()
            cursor.execute("select max(idExperiment) from experiment")
            rec = cursor.fetchone()
            rc = (rec[0] + 1)

            def NewExpAdd():
                text = entrynex.get()
                print(text)
                nea = [str(rc), text, str(respr)]
                print(nea)
                neas = "'{}'".format("', '".join(nea))
                print(neas)
                entrynex.delete(0, END)
                cursor.execute("INSERT INTO `mydb`.`experiment` (`idExperiment`, `ExpName`, "
                               "`ResearchProject_idResearchProject`) VALUES (" + neas + ")")
                cnx.commit()



            btnNewExpAdd = Button(nex_frame, text="Добавить новый эксперимент", command=NewExpAdd, bg='light green')
            btnNewExpAdd.grid(row=1, column=1)

            def ToNewExp():
                cursor.execute("select max(idExperiment) from experiment")
                rec = cursor.fetchone()
                recc = rec[0]
                if recc == rc:
                    print("Равны",rc, recc)
                    ExpMin(recc)
            btnToNewExp = Button(nex_frame, text="Перейти к новому эксперименту", command=ToNewExp, bg='light green')
            btnToNewExp.grid(row=2, column=1)

            def Back1():
                nex_frame.grid_remove()
                Exp()

            btnBack1 = Button(nex_frame, text="Вернуться на страницу экспериментов.", command=Back1, bg='light green')
            btnBack1.grid(row=3, column=0)

        btnNewExp = Button(exp_frame, text="Новый эксперимент", command=NewExp, bg='light green')
        btnNewExp.grid(row=k+1, column=1)
        # up_frame.update()
        # rhd = up_frame.winfo_height()
        # print(rhd)

        def Back():
            parent = btnBack.winfo_parent()
            parent1 = btnBack.nametowidget(parent)
            parent1.grid_remove()
            main()
        btnBack = Button(exp_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
        btnBack.grid(row=k+2, column=1)

    btnExp = Button(up_frame, text="Мои эксперименты", command=Exp, bg='light green')
    btnExp.grid(row=2, column=0, columnspan=2)

    # Окно методики
    def Met():
        up_frame.grid_remove()
        met_frame = Frame(root, bg='light blue')
        met_frame.grid(row=0, column=0, padx = 10, pady=10)

        def Back():
            met_frame.grid_remove()
            main()
        btnBack = Button(met_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
        btnBack.grid(row=0, column=0)


    btnMet = Button(up_frame, text="Добавить методику", command=Met, bg='light green')
    btnMet.grid(row=3, column=0, columnspan=2)

    # Окно просмотра по исходному реагенту и тд
    def ReagSearch():
        up_frame.grid_remove()
        root.geometry("1000x400")
        rs_frame = Frame(root, bg='light blue')
        rs_frame.grid(row=0, column=0, padx = 10, pady=10)

        rq_frame = Frame(rs_frame, bg='light blue')
        rq_frame.grid(row=0, column=0, padx = 10, pady=10, sticky=W)

        labelreag0 = Label(rq_frame, text="Поиск эксперимента по веществу", bg='light green')
        labelreag0.grid(row=0, column=0, columnspan=2)

        #поиск по прекурсору
        labelreag1 = Label(rq_frame, text="Выберите исходное вещество", bg='light green')
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
        labelreag2 = Label(rq_frame, text="Выберите активное вещество", bg='light green')
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

        labelreag3 = Label(rq_frame, text="Выберите параметр", bg='light green')
        labelreag3.grid(row=0, column=3)

        labelreag3min = Label(rq_frame, text="Минимум", bg='light green')
        labelreag3min.grid(row=0, column=4)

        labelreag3max = Label(rq_frame, text="Максимум", bg='light green')
        labelreag3max.grid(row=0, column=5)

        labelreag3un = Label(rq_frame, text="Ед. изм.", bg='light green')
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
        lab=[]
        lab_un = []
        entmin=[]
        entmax=[]
        ch_btn=[]
        nt = len(max(row30))
        nu = len(max(row32))
        rlr = range(len(reaglist3))
        ch_AD = []

        for r in rlr:
            ch_AD.append(IntVar(value=0))
            ch_btn.append(Checkbutton(rq_frame, bg='light blue', variable=ch_AD[r]))
            # ch_btn[r].var = ch_AD
            ch_btn[r].grid(row=r + 1, column=2)
            lab.append(Label(rq_frame, text=row30[r], width=nt, bg='light green'))
            lab[r].grid(row=r+1, column=3)
            entmin.append(Entry(rq_frame))
            entmin[r].grid(row=r+1, column=4)
            entmax.append(Entry(rq_frame))
            entmax[r].grid(row=r + 1, column=5)
            lab_un.append(Label(rq_frame, text=row32[r], width=nu, bg='light green'))
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

            chibi_out = []
            request = ""
            # reques = []
            for r in rlr:
                if ch_AD[r].get() == 1:
                    idAD = str(row31[r])
                    en_min = entmin[r].get()
                    en_max = entmax[r].get()
                    if not en_min and not en_max:
                        request = "idAnalyticalData = " + idAD + ""
                    elif en_min and not en_max:
                        request = "idAnalyticalData = " + idAD + " and ADValue >= " + en_min + ""
                    elif not en_min and en_max:
                        request = "idAnalyticalData = " + idAD + " and ADValue <= " + en_max + ""
                    elif en_min and en_max:
                        request = "idAnalyticalData = " + idAD + " and ADValue between " + en_min + " and " + en_max + ""
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

            # reag3get = cbxreag3.get()
            # rg3 = rl3.get(reag3get)
            # if rg3 is None:
            #     pass
            # else:
            #     text3 = "idAnalyticalData = " + str(rg3) + " "
            #     print(text3)
            #     thelist.append(text3)


            # print(chibi_out)
            chubby_out = ""
            if chibi_out:
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
            if thelist:
                cursor.execute("select "+ sdl +" from experiment_has_analyticaldata "
                               "join analyticaldata on idAnalyticalData = AnalyticalData_idAnalyticalData "
                               "join experiment on idExperiment = Experiment_idExperiment "
                               "join experimentdate on idExperiment = experimentdate.Experiment_idExperiment "
                               "join researchproject on idResearchProject = ResearchProject_idResearchProject "
                               "join personnel on idPersonnel=Personnel_idPersonnel "
                               "join reagusage on idExperimentDate=ExperimentDate_idExperimentDate "
                               "join reagent on idReagent = Reagent_idReagent "
                               "join reaginfo on idReagInfo = ReagInfo_idReagInfo "
                               "join reagtype on idReagType = ReagType_idReagtype where " + chubby_out +" order by ExpName")
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
                labtabrgs = Label(tablergs_frame, text='Эксперименты по заданным параметрам', bg='light green')
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


        btngetreag4 = Button(rq_frame, text="Выбрать", command=rg4, bg='light green')
        btngetreag4.grid(row=3, column=0, columnspan=2)

        def Back():
            rs_frame.grid_remove()
            main()
        btnBack = Button(rq_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
        btnBack.grid(row=4, column=0, columnspan=2)
    w=int()
    btnReag = Button(up_frame, text="Поиск по веществу", width=w, command=ReagSearch, bg='light green')
    btnReag.grid(row=4, column=0, columnspan=2)
    w=50
    btnReag.update()

    cursor.execute("SELECT ReagName1, EndDateReag, timestampdiff(day, curdate(), EndDateReag) AS DaysTillExp "
                   "FROM reagent JOIN reaginfo on idReagInfo = ReagInfo_idReagInfo ORDER BY DaysTillExp;")
    x = int()
    for r in cursor.fetchall():
        if r[2]<30:
            x=1
            label34 = Label(up_frame, text = 'Проверьте срок годности реагентов', width=30, bg='orange')
            label34.grid(row=6, column=0, columnspan=2)
            break
        elif r[2]<45:
            x=2

    cursor.execute("SELECT ReagName1, Amount - sum(AmUsed) as lef, MinAmount FROM mydb.reagusage "
                   "join reagent on idReagent = Reagent_idReagent join reaginfo on idReagInfo = ReagInfo_idReagInfo "
                   "group by idReagent;")
    for r in cursor.fetchall():
        if r[1] <= r[2]:
            label66 = Label(up_frame, text='Проверьте запасы реагентов', width=30, bg='orange')
            label66.grid(row=7, column=0, columnspan=2)
            break


    def Reag():
        up_frame.grid_remove()
        rogs_frame = Frame(root, bg='light blue')
        rogs_frame.grid(row=0, column=0, padx = 10, pady=10)

        hle = []
        cursor.execute("select Max(char_length(ReagName1)) as len from reaginfo")
        recordr4 = cursor.fetchone()
        hle.append(recordr4[0])


        cursor.execute("SELECT ReagName1, Amount - sum(AmUsed) as lef, MinAmount, EndDateReag, "
                       "timestampdiff(day, curdate(), EndDateReag) AS DaysTillExp FROM reagent join reagusage "
                       "on idReagent = Reagent_idReagent join reaginfo on idReagInfo = ReagInfo_idReagInfo "
                       "where InStock = 1 group by idReagent order by DaysTillExp asc;")

        horse = ["Название реагента", "Остатки реагента", "Мин. кол-во", "Срок годности",
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
            main()
        btnBack = Button(rogs_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
        btnBack.grid(row=0, column=0)

    btnReag = Button(up_frame, text="Просмотреть реагенты", command=Reag, bg='light green')
    btnReag.grid(row=5, column=0, columnspan=2)
    if x == 2:
        btnReag['bg']='yellow'
    elif x == 1:
        btnReag['bg']='orange'

    def Adm():
        pass

    btnAdm = Button(up_frame, text="Кабинет администратора", command=Adm, bg='light green')
    if level == 2:
        btnAdm.grid(row=8, column=0, columnspan=2)

    # w = up_frame.winfo_width()
    # h = up_frame.winfo_height()
    # root.geometry(f"{w}x{h}")


root.mainloop()
