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


def handle_client(conn, addr):
    """处理客户端请求的函数"""
    print(f"Connection from {addr}")
    try:
        recvdata = conn.recv(1024).decode()
        if not recvdata:
            print("No data received from client.")
            return

        data = json.loads(recvdata)
        print(f"Received data: {data}")

        if data['id'] == 'shop':
            shop = Shop(conn)
            if data['type'] == 'register':
                shop.register(data)
            elif data['type'] == 'login':
                shop.login(data)
            elif data['type'] == 'add_goods':
                shop.addgoods(data)
            elif data['type'] == 'view_goods':
                shop.viewgoods(data)
            elif data['type'] == 'view_trade':
                shop.viewtrade(data)
            elif data['type'] == 'select_goods':
                shop.selectgoods(data)
            elif data['type'] == 'delete_goods':
                shop.deletegoods(data)
            elif data['type'] == 'select_goodsinfo':
                shop.selectgoodsinfo(data)
            elif data['type'] == 'update_goods':
                shop.updategoods(data)
            elif data['type'] == 'shop_info':
                shop.shopinfo(data)
            elif data['type'] == 'update_shop':
                shop.updateshop(data)
            else:
                print("Unknown shop request type")
        else:
            customer = Customer(conn)
            if data['type'] == 'register':
                customer.register(data)
            elif data['type'] == 'login':
                customer.login(data)
            elif data['type'] == 'view_goods':
                customer.viewgoods(data)
            elif data['type'] == 'all_goods':
                customer.allgoods(data)
            elif data['type'] == 'buy_goods':
                customer.buygoods(data)
            elif data['type'] == 'view_trade':
                customer.viewtrade(data)
            elif data['type'] == 'all_trade':
                customer.alltrade(data)
            elif data['type'] == 'off_trade':
                customer.offtrade(data)
            elif data['type'] == 'cus_info':
                customer.cusinfo(data)
            elif data['type'] == 'update_cus':
                customer.updatecus(data)
            else:
                print("Unknown customer request type")

    except Exception as e:
        print(f"Error handling client {addr}: {e}")
        conn.send(json.dumps({'result': 'fail', 'error': str(e)}).encode())
    finally:
        conn.close()
        print(f"Connection with {addr} closed")


def start_server():
    """启动服务器并处理连接"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(5)
    print("Server started and listening on port 5000")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.daemon = True
        client_thread.start()


if __name__ == "__main__":
    start_server()
