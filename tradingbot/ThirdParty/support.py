# -*- coding: utf-8 -*-
import hashlib
import hmac
import httplib
import json
import os
import time
import urllib
from collections import OrderedDict

import tradingbot.config
import tradingbot.database


def get_data(method, *args):
    """
    :param method: 
    :param args: 
    :return: 
    """
    time.sleep(1)

    server = tradingbot.config.API_URl
    keys = get_keys()
    api_key = keys[0]
    secret_key = keys[1]
    data = ''
    if len(args):
        data = OrderedDict(args[0])

    encoded_data = urllib.urlencode(data)
    sign = hmac.new(secret_key, msg=encoded_data,
                    digestmod=hashlib.sha256).hexdigest().upper()
    headers = {"Api-key": api_key, "Sign": sign}

    conn = httplib.HTTPSConnection(server)
    conn.request("GET", method + '?' + encoded_data, '', headers)

    response = conn.getresponse()
    data = json.load(response)
    conn.close()
    return data


def post_data(method, *args):
    """
    
    :param method: 
    :param args: 
    :return: 
    """
    time.sleep(1)
    server = tradingbot.config.API_URl
    keys = get_keys()
    api_key = keys[0]
    secret_key = keys[1]

    data = OrderedDict(args[0])
    encoded_data = urllib.urlencode(data)
    sign = hmac.new(secret_key, msg=encoded_data,
                    digestmod=hashlib.sha256).hexdigest().upper()
    headers = {"Api-key": api_key, "Sign": sign,
               "Content-type": "application/x-www-form-urlencoded"}

    conn = httplib.HTTPSConnection(server)
    conn.request("POST", method, encoded_data, headers)
    response = conn.getresponse()
    data = json.load(response)
    conn.close()
    return data


def get_rank(el):
    """

    :param el: 
    :return: 
    """
    return (float(el["best_ask"]) / float(el["best_bid"]) - 1) * float(
        el["volume"]) * float(el["vwap"])


def get_pairs(number, exception):
    """
    
    :param number: 
    :param exception: 
    :return: 
    """
    pairs = [el for el in get_data("/exchange/ticker") if
             "/BTC" in el["symbol"] and el["best_bid"] > 10 ** (-6)]

    pairs = sorted(pairs, key=lambda el: get_rank(el), reverse=True)
    tmp = []
    for i, el in enumerate(pairs):
        if el["symbol"] in exception or float(el["best_ask"]) / float(
                el["best_bid"]) > 1.5:
            tmp.append(i)
    for i, el in enumerate(tmp):
        pairs.pop(el - i)

    processed_data = pairs[15:15 + number]

    return processed_data


def get_nonzero_balances():
    data = get_data("/payment/balances", [])
    filtered_data = {}
    for el in data:
        if el["type"] == "total" and el["value"] != 0 and el[
            "currency"] not in tradingbot.config.EXCLUSION_CURRENCY:
            filtered_data["%s/BTC" % el["currency"]] = float(el["value"])
    return filtered_data


def get_balance(value):
    """
    
    :param value: 
    :return: 
    """
    return get_data("/payment/balance", [("currency", value)])["value"]


def make_order(type, pair, price, quantity):
    """
    
    :param type: 
    :param pair: 
    :param price: 
    :param quantity: 
    :return: 
    """
    type_of_action = {"buy": "/exchange/buylimit",
                      "sell": "/exchange/selllimit"}
    order = post_data(type_of_action[type],
                      [('currencyPair', pair), ('price', price),
                       ('quantity', quantity)])
    return order


def close_opened_orders():
    """
    Функция должна закрыть все открытые ордера
    
    :return: 
    """
    result = []
    data = get_data("/exchange/client_orders", [("openClosed", "OPEN")])
    if data["totalRows"] != 0:
        for el in data['data']:
            result.append(post_data(" /exchange/cancellimit",
                                    [("currencyPair", el["currencyPair"]),
                                     ("orderId", el["id"])]))


def sell_all_pairs():
    """
    
    :return: 
    """
    '''сначала нужно получить все пары если баланса не хватает то докупаем и продаем
    пока эта операция делается без записи в бд'''
    print get_nonzero_balances()


def get_keys():
    """
    Functions return secret keys for stock exchange
    return: keys
    """
    project_dir = os.path.dirname(__file__)

    with open(os.path.join(project_dir,"keys.txt"), 'r') as keys_file:
        keys = keys_file.readlines()
        keys[0] = keys[0][:-1]

    return keys


def make_order(type, pair,price,quantity):
    type_of_action = {"buy":"/exchange/buylimit", "sell":"/exchange/selllimit"}
    order = post_data(type_of_action[type],[('currencyPair', pair),('price', price),('quantity', quantity)])
    return order

def get_purchase_price(value):
    return round((value + tradingbot.config.OVER_BURSE) * (1 + tradingbot.config.COMMISSION), 8)

def get_sell_price(currency):
    tmp = get_data("/exchange/ticker",[("currencyPair", "%s/BTC" % currency)])
    return round((float(tmp["best_ask"]) - tradingbot.config.OVER_BURSE) / (1 + tradingbot.config.COMMISSION), 8)

def get_sold_volume(currency, sell_price):
    volume = tradingbot.database.select(["sum(purchased_quantity - sold_quantity)"],
                                        ["symbol == ", "purchase_price <=", "result == "],
                                        ("'%s/BTC'" % currency, sell_price / tradingbot.config.INCOME, 0))
    if volume[0][0] == None:
        result = 0
    else:
        result = volume[0][0]
    return result

def get_num_of_pairs(balance):
    result = tradingbot.config.NUMBER_OF_PAIRS
    if balance / (10 ** (-4)) < tradingbot.config.NUMBER_OF_PAIRS:
        count = int(balance / (10 ** (-4)))
        result = count
    return result

def get_main_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_config_dir():
    return os.path.join(get_main_dir(),"configs")