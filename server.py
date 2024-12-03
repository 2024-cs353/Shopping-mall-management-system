import threading
import time
import queue
import socket
import json
from mysql_op import *


class Shop:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Shop_op()
        if op1.register(recv['user'], recv['passwd'], recv.get('shop_name', ''), recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        response = json.dumps(data).encode()
        self.conn.send(response)
        print(f"Sent response: {response}")
        self.conn.close()
        print("Connection closed")

    def login(self, recv):
        op1 = Shop_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def addgoods(self, recv):
        op1 = Shop_op()
        if op1.add_goods(recv['user'], recv['goods_name'], recv['goods_type'], recv['goods_prices'], recv['goods_rest']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewgoods(self, recv):
        op1 = Shop_op()
        data = {'result': op1.view_goods(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewtrade(self, recv):
        op1 = Shop_op()
        data = {'result': op1.view_trade(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def selectgoods(self, recv):
        op1 = Shop_op()
        data = {'result': op1.select_goods(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def deletegoods(self, recv):
        op1 = Shop_op()
        if op1.delete_goods(recv['user'], recv['goods_name']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def selectgoodsinfo(self, recv):
        op1 = Shop_op()
        # data={'result':'success'}
        data = {'result': op1.select_goodsinfo(
            recv['user'], recv['goods_name'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updategoods(self, recv):
        op1 = Shop_op()
        if op1.update_goods(recv['user'], recv['old_goods_name'], recv['goods_name'], recv['goods_type'], recv['goods_prices'], recv['goods_rest']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def shopinfo(self, recv):
        op1 = Shop_op()
        data = {'result': op1.shop_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updateshop(self, recv):
        op1 = Shop_op()
        if op1.update_shop(recv['user'], recv['passwd'], recv['shop_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


class Customer:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Customer_op()
        if op1.register(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def login(self, recv):
        op1 = Customer_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewgoods(self, recv):
        op1 = Customer_op()
        data = {'result': op1.view_goods(
            recv['goods_name'], recv['goods_type'], recv['shop_name'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def allgoods(self, recv):
        op1 = Customer_op()
        data = {'result': op1.all_goods()}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def buygoods(self, recv):
        op1 = Customer_op()
        if op1.buy_goods(recv['user'], recv['goods_name'], recv['shop_acc'], recv['trade_num'], recv['trade_money']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewtrade(self, recv):
        op1 = Customer_op()
        data = {'result': op1.view_trade(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def alltrade(self, recv):
        op1 = Customer_op()
        data = {'result': op1.all_trade(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def offtrade(self, recv):
        op1 = Customer_op()
        if op1.off_trade(recv['trade_id']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def cusinfo(self, recv):
        op1 = Customer_op()
        data = {'result': op1.cus_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updatecus(self, recv):
        op1 = Customer_op()
        if op1.update_cus(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(5)
    print("Server started and listening on port 5000")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        shop = Shop(client_socket)
        try:
            recvdata = client_socket.recv(1024).decode()
            print(f"Received data: {recvdata}")
            if recvdata:
                data = json.loads(recvdata)
                if data['type'] == 'register':
                    shop.register(data)
                elif data['type'] == 'login':
                    shop.login(data)
                else:
                    print("Unknown request type")
            else:
                print("No data received from client.")
        except Exception as e:
            print(f"Error handling client data: {e}")
        finally:
            client_socket.close()


if __name__ == "__main__":
    start_server()
