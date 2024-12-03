import socket
import json


class Send_data:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect(('127.0.0.1', 5000))
            print("Connected to server on 127.0.0.1:5000")
        except Exception as e:
            print(f"Failed to connect to server: {e}")

    def message(self, data):
        try:
            json_data = json.dumps(data)
            self.s.send(json_data.encode())
            print(f"Sent data: {json_data}")

            recvdata = self.s.recv(1024).decode()
            print(f"Received data: {recvdata}")

            if not recvdata:
                print("No data received from server.")
                return None

            return json.loads(recvdata)
        except Exception as e:
            print(f"Error during communication: {e}")
            return None
        finally:
            self.s.close()
            print("Connection closed")

    def close(self):
        try:
            self.s.close()
            print("Connection closed")
        except Exception as e:
            print(f"Failed to close connection: {e}")
