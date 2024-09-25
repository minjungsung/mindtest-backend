import time


CLIENT_LIVENESS_CHECK_INTERVAL = 10

class ClientManager:
    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, client):
        self.clients[client_id] = client

    def unregister_client(self, client_id):
        del self.clients[client_id]

    def send_liveness_check_message(self):
        for client_id, client in self.clients.items():
            pass

def run_client_liveness_check():
    while True:
        global_client_manager.send_liveness_check_message()
        time.sleep(CLIENT_LIVENESS_CHECK_INTERVAL)

global_client_manager = ClientManager()