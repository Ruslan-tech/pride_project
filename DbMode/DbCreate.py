from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String, DateTime, Float, Text, EmailType, ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

metadata = MetaData()

"""Создание таблицы tenders с помощью sqlalchemy"""
tenders = Table ('tenders', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    tender_num = Column(String(20), unique=True), #номер конкурса\тендера
    customer = Column(String(100)), #наименование заказчика
    date_public = Column(DateTime()),   #дата и время размещения конкурса 
    date_finish = Column(DateTime()),   #дата и время окончания подачи документации на конкурс
    tender_summ = Column(Float()),  #сумма конкурса 
    theeme = Column(Text(), nullable=False) #предмет договора по конкурсу
)

"""Создаем таблицу пользователей"""
users = Table ('users', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    name = Column(String(100)), #имя и фамилия пользователя
    email = Column(EmailType),  #почтовый адрес рабочий
    position = Column(String(15))   #должность
)

"""Создаем таблицу конкурсов распределенных по менеджерам"""
distributed_tenders = Table ('distribted_tenders', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    id_user = Column(Integer, ForeignKey('users.id')),  #id пользователя из таблицы users
    id_tender = Column(Integer, ForeignKey('tenders.id')),  #id конкурса\тендера из таблицы tenders
    status = Column(String(15)),    # статус участия в конкурсе: участвуем\не участвуем
    comments = Column(Text(), nullable=False),  #комментарии к конкурсу
    id_company = Column(Integer, ForeignKey('companies.id'))    #id компании из таблицы companies от которой подается заявка на участие в конкурсе 

)#!!!проработать статус согласвания, статус сборки, статус победы, привязка спецификации  

"""Таблица для расчета возможности участия в тендере"""
tenders_calculate = Table('tenders_calculate', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    id_distributed_tenders = Column(Integer, ForeignKey('distributed_tenders.id')), #id распределенного конкурса по ответственному менеджеру
    id_vendor = Column(Integer, ForeignKey('vendors.id')),  #id поставщика из таблицы vendors
    summ_vendor = Column(Float()),  #расчетная сумма расходов по коммерческому предложению от поставщика
    logistic_cost = Column(Float()),    #расходы на логистику
    other_cost = Column(Float()),   #проче расходы
    path_vendor_kp = Column(String(255)),   #путь к папке с КП от поставщика
)

"""Таблица маржинальности в % и в рублях по каждому конкурсу"""
tender_margins = Table ('tender_margins', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    id_distributed_tenders = Column(Integer, ForeignKey('distributed_tenders.id')), #id распределенного конкурса по ответственному менеджеру
    margins_procent = Column(Float()),  #наценка по конкурсу в процентах
    margins_rubls = Column(Float()) #наценка по конкурсу в рублях
)

"""Таблица Поставщиков"""
vendors = Table ('vendors', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    title = Column(String(100)),    #наименование компании поставщика    
    contacts = Column(Text(), nullable=False),  #контакты    
)

"""Таблица заключенных контрактов с поставщиком"""
vendors_contracts = Table('vendors_contracts', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    id_vendor = Column(Integer, ForeignKey('vendors.id')),  #id поставщика
    id_company = Column(Integer, ForeignKey('companies.id')),   #id компании холдинга
    number_contract = Column(String(100)),  #номер договора
    date_of_conclusion = Column(DateTime()),    #дата заключения
    date_of_completion = Column(DateTime()),    #дата завершения
    conditions = Column(Text(), nullable=False),        # условия работы с поставщиком согласно контракта
    contract_path = Column(String(255)) #путь к папке с договором
)

"""Таблица заключенных спецификаций под конкурс"""
vendor_specifications = Table('vendor_specifications', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    id_contract = Column(Integer, ForeignKey('vendors_contracts.id')),  #id контракта из таблицы vendors_contracts
    number_spec = Column(String(100)),  #номер спецификации
    date_of_conclusion = Column(DateTime()),    #дата заключения
    delivery_time = Column(Integer),    #срок поставки в рабочих днях
    conditions_pay = Column(String(100)),    #условия оплаты
    contract_spec = Column(String(255)) #путь к папке со спецификацией
)

"""Таблица компаний входящих в холдинг"""
companies = Table ('companies', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    title = Column(String(100)),    #название
    requisites_path = Column(String(255)),  #путь к папке с реквизитами
    inn = Column(Integer, unique=True), #ИНН компании
    kpp = Column(Integer)   #КПП компании
)

"""Таблица с тематикой конкурсов"""
theemes = Table ('theemes', metadata,
    id = Column(Integer, primary_key=True, auto_increment=True),
    title = Column(String(255)),    #название тематики\предмета договора поставки
    id_vendor = Column(Integer, ForeignKey('vendors.id'))   #id поставщика
)





# data_plus = [(3245123414, 'ПАО Газпромгазораспредление Уфа', '10.11.2022',
# '15.11.2022', 321990.00, 'Поставка газовых котлов', 'Иванов', 'Не рассмотрен')]
# tables_name = ['allTenders', 'distributed_tenders',
# 'calculat_tenders', 'surrender_tenders', 'win_tenders', 'c',
# 'tender_status']


