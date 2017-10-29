# -*- coding: utf-8 -*-codung
def get_exchange_ticker(*args):
    """
    Получить информацию за последние 24 часа по конкретной паре валют.
    В ответе есть следующие поля:
        max_bid, min_ask - максимальный бид и минимальный аск за последние 24 часа
        best_bid, best_ask - лучшие текущие бид и аск
    :param args: 
    :return: 
    """
    pass

def get_exchange_last_trades(currencyPair, *args):
    """
    Получить информацию о последних сделках (транзакциях) по заданной паре валют.
    Информацию можно получить либо за последний час либо за последнюю минуту.
    
    :param currencyPair: 
    :param args: 
    :return: 
    """
    pass

def get_exchange_order_book(currencyPair, *args):
    """
    Получить ордера по выбранной паре (можно установить признак
     группировки ордеров по ценам)
    :param currencyPair: 
    :param args: 
    :return: 
    """
    pass

def get_exchange_all_order_book(*args):
    """
    Возвращает ордербук по каждой валютной паре
    :param args: 
    :return: 
    """
    pass

def get_exchange_maxbid_minask(*args):
    """
    Возвращает максимальный бид и минимальный аск в текущем стакане
    :param args: 
    :return: 
    """
    pass

def get_exchange_restrictions(*args):
    """
    Возвращает ограничения по каждой паре по мин. размеру ордера и максимальному
     кол-ву знаков после запятой в цене.
    :param args: 
    :return: 
    """
    pass

def get_info_coinInfo(*args):
    """
    возвращает общую информацию по критовалютам:
        name - название
        symbol - символ
        walletStatus - статус кошелька
        normal - Кошелек работает нормально
        delayed - Кошелек задерживается (нет нового блока 1-2 часа)
        blocked - Кошелек не синхронизирован (нет нового блока минимум 2 часа)
        blocked_long - Последний блок получен более 24 ч. назад
        down - Кошелек временно выключен
        delisted - Монета будет удалена с биржи, заберите свои средства
        closed_cashin - Разрешен только вывод
        closed_cashout - Разрешен только ввод
        withdrawFee - комиссия вывод
        minDepositAmount - мин. сумма пополнения
        minWithdrawAmount - мин. сумма вывода
    :param args: 
    :return: 
    """
    pass

def get_exchange_trades(*args):
    """
    По конкретному клиенту получить информацию о его последних сделках,
     результат может быть ограничен, соответствующими параметрами.
    :param args: 
    :return: 
    """
    pass

def get_exchange_client_orders(*args):
    """
    По конкретному клиенту и по конкретной паре валют получить полную информацию
     о его ордерах, информация может быть ограничена
     либо только открытые либо только закрытые ордера.
    :param args: 
    :return: 
    """
    pass

def get_exchange_order(orderId):
    """
    Получить информацию об ордере по его ID
    :param orderId: 
    :return: 
    """
    pass

def get_payment_balances(*args):
    """
    Возвращает массив с балансами пользователя. Для каждой валюты существует
    4 типа балансов: общий (total),
    доступные для торговли средства (available),
    средства в открытых ордерах (trade),
    доступный для вывода (available_withdrawal)
    :param args: 
    :return: 
    """
    pass

def get_payment_balance(*args):
    """
    Возвращает доступный баланс для выбранной валюты
    :param args: 
    :return: 
    """
    pass

def get_payment_history_transactions(start, end, *args):
    """
    Возвращает список транзакций пользователя
    :param start: 
    :param end: 
    :return: 
    """
    pass

def get_payment_history_size(start, end, *args):
    """
    Возвращает количество транзакций пользователя с заданными параметрами
    :param start: 
    :param end: 
    :param args: 
    :return: 
    """
    pass

def get_exchange_commission():
    """
    Возвращает текущую комиссию пользователя
    :return: 
    """
def get_exchange_commissionCommonInfo():
    """
    Возвращает текущую комиссию пользователя
     и объем торгов в USD за последние 30 дней
    :return: 
    """
    pass

def post_exchange_buylimit(currencyPair, price, quantity):
    """
    Открыть ордер (лимитный) на покупку, определенной валюты.
    :param currencyPair: 
    :param price: 
    :param quantity: 
    :return: 
    """
    pass
def post_exchange_selllimit(currencyPair, price, quantity):
    """
    Открыть ордер (лимитный) на продажу определенной валюты. 
    Доп.параметры аналогично покупки.

    :param currencyPair: 
    :param price: 
    :param quantity: 
    :return: 
    """
    pass

def post_exchange_buymarket(currencyPair, quantity):
    """
    Открыть ордер(рыночный) на покупку определенной валюты на заданное количество.
    :return: 
    """
    pass

def post_exchange_sellmarket(currencyPair, quantity):
    """
    Открыть ордер(рыночный) на продажу определенной валюты на заданное количество.
    :param currencyPair: 
    :param quantity: 
    :return: 
    """
    pass

def post_exchange_cancellimit(currencyPair, orderId):
    """
    Отменить ордер (лимитный).
    :param currencyPair: 
    :param orderId: 
    :return: 
    """
    pass
