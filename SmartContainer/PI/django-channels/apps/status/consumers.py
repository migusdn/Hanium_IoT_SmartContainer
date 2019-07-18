from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class StatusConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'status'
        # Join room group
        print(self.room_name)
        print(self.room_group_name)
        print(self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
            #self.room_name
        )
        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'ON',
                'device_num': self.room_name
            }
        )


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'OFF',
                'device_num': self.room_name
            }

        )
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.room_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        device_num = text_data_json['device_num']
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'device_num': device_num
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        device_num = event['device_num']
        print(event)
        # Send message to WebSocket

        self.send(text_data=json.dumps({
            'message': message,
            'device_num': device_num
        }))

class AllStatusConsumer(WebsocketConsumer):
    def connect(self):

        self.room_group_name = 'status'
        # Join room group
        print(self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        device_num = text_data_json['device_num']
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'device_num': device_num
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        device_num = event['device_num']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'device_num': device_num
        }))

class DeviceConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['device_num']
        self.room_group_name = 'status'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
            self.room_name
        )
        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'ON',
                'device_num': self.room_name
            }
        )

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'OFF',
                'device_num': self.room_name
            }
        )
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        device_num = text_data_json['device_num']
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'device_num': device_num
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        device_num = event['device_num']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'device_num': device_num
        }))
