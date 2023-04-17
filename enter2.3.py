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
w = 540
h = 200
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

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
        msb.showinfo(title="Выполнен вход", message="Вы успешно вошли в личный кабинет.")
        main()
        return person


def show_password():
    if check_v1.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

auth_frame = Frame(root, bg='light blue')
auth_frame.grid(row=0, column=0)

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
    auth_frame.grid_remove()
    up_frame = Frame(root, bg='light blue')
    up_frame.grid(row=0, column=0, sticky='news')
    up_frame.grid_rowconfigure(0, weight=1)
    up_frame.grid_columnconfigure(1, weight=1)

    label2 = Label(up_frame, text="Добро пожаловать в базу данных.", bg='light green')
    label2.grid(row=0, column=1)

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
    label3.grid(row=0, column=2)


    # btnShowData = Button(up_frame, text="Загрузить", command=show_data, bg='light green')
    # btnShowData.grid(row=1, column=2, padx=10)

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


    # print(tableList)
    # Окно эксперимента

    # print(person)
    cursor.execute("SELECT idlevel, Pers_Name, RPName, idResearchProject FROM researchproject JOIN personnel ON idPersonnel = Personnel_idPersonnel "
                   "JOIN level ON idLevel = Level_idLevel WHERE idPersonnel = " + str(person) + " ")
    record = cursor.fetchone()
    # print(record[2])

    def Exp():
        up_frame.grid_remove()
        exp_frame = Frame(root, bg='light blue')
        exp_frame.grid(row=0, column=0)
        rp = 2
        butexp = []
        butname = []
        butid = []
        cursor.execute("SELECT idExperiment, ExpName FROM experiment WHERE ResearchProject_idResearchProject = " + str(record[3]) +" ")
        for r in cursor.fetchall():
            butid.append(str(r[0]))
            butname.append(str(r[1]))
        but = dict(zip(butid, butname))
        k = len(butname)

        def ExpMin():
            exp_frame.grid_remove()
            em_frame = Frame(root, bg='light blue')
            em_frame.grid(row=0, column=0)
            print('ASS')
            # print(butname[j])
            # text = butexp.cget('text')
            # print(text)
            labelexpname = Label(em_frame, text="{}".format(butname[j]), bg='light green')
            labelexpname.grid(row=0, column=0)

            def Back():
                em_frame.grid_remove()
                exp_frame.grid()

            btnBack = Button(em_frame, text="Вернуться на страницу экспериментов.", command=Back, bg='light green')
            btnBack.grid(row=k + 2, column=1)

        for j in range(k):
            butexp.append(Button(exp_frame, text='{}'.format(butname[j]), command=ExpMin, bg='light green'))
            butexp[j].grid(row=j, column=1)

        def NewExp():
            pass
        btnNewExp = Button(exp_frame, text="Новый эксперимент", command=NewExp, bg='light green')
        btnNewExp.grid(row=k+1, column=1)

        def Back():
            exp_frame.grid_remove()
            up_frame.grid()
            root.geometry("540x200")
        btnBack = Button(exp_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
        btnBack.grid(row=k+2, column=1)


    btnExp = Button(up_frame, text="Мои эксперименты", command=Exp, bg='light green')
    btnExp.grid(row=2, column=1)

    # Окно методики
    def Met():
        up_frame.grid_remove()
        met_frame = Frame(root, bg='light blue')
        met_frame.grid(row=0, column=0)

        def Back():
            met_frame.grid_remove()
            up_frame.grid()
            root.geometry("540x200")
        btnBack = Button(met_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
        btnBack.grid(row=0, column=0)


    btnMet = Button(up_frame, text="Добавить методику", command=Met, bg='light green')
    btnMet.grid(row=3, column=1)

    # Окно просмотра по исходному реагенту и тд
    def Reag():
        up_frame.grid_remove()
        reag_frame = Frame(root, bg='light blue')
        reag_frame.grid(row=0, column=0)

        labelreag0 = Label(reag_frame, text="Поиск эксперимента по веществу", bg='light green')
        labelreag0.grid(row=1, column=0)

        labelreag1 = Label(reag_frame, text="Выберите исходное вещество", bg='light green')
        labelreag1.grid(row=2, column=0)

        cbxreag1 = ttk.Combobox(reag_frame, values=[], width=35)
        cbxreag1.grid(row=2, column=1)

        try:
            reaglist1 = []
            cursor.execute("SELECT ReagName1 FROM reagent WHERE ReagType_idReagType = 1;")
            for row in cursor.fetchall():
                reaglist1.append(row)
            cbxreag1['values'] = reaglist1
        except:
            cnx.rollback()

        def getreag1():
            reag1get = cbxreag1.get()
            print(reag1get)
        btngetreag1 = Button(reag_frame, text="Выбрать", command=getreag1, bg='light green')
        btngetreag1.grid(row=2, column=3)

        labelreag2 = Label(reag_frame, text="Выберите активное вещество", bg='light green')
        labelreag2.grid(row=3, column=0)

        cbxreag2 = ttk.Combobox(reag_frame, values=[], width=35)
        cbxreag2.grid(row=3, column=1)

        try:
            reaglist2 = []
            cursor.execute("SELECT ReagName1 FROM reagent WHERE ReagType_idReagType = 4;")
            for row in cursor.fetchall():
                reaglist2.append(row)
            cbxreag2['values'] = reaglist2
        except:
            cnx.rollback()

        def getreag2():
            reag2get = cbxreag2.get()
            print(reag2get)
        btngetreag2 = Button(reag_frame, text="Выбрать", command=getreag2, bg='light green')
        btngetreag2.grid(row=3, column=3)

        def Back():
            reag_frame.grid_remove()
            up_frame.grid()
            root.geometry("540x200")
        btnBack = Button(reag_frame, text="Вернуться на начальную страницу.", command=Back, bg='light green')
        btnBack.grid(row=5, column=0)


    btnReag = Button(up_frame, text="Поиск по веществу", command=Reag, bg='light green')
    btnReag.grid(row=4, column=1)


root.mainloop()
