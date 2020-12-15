import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

"""Consumer class which handle Connect, Disconnect, send and receive messages,
 sending to everyone if someone enter or leave the chat"""

class Consumer(WebsocketConsumer):
    def connect(self):
        self.person_name = self.scope['url_route']['kwargs']['person_name']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name

        )
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":self.person_name+" Joined Chat"
            }
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":self.person_name+" Left Chat"
            }
        ) #Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def receive(self, text_data=None, bytes_data=None):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':self.person_name+" : "+message
            }
        )

    def chat_message(self,event):
        message=event['message']
        #send message to Websocket
        self.send(text_data=json.dumps({
            'message':message
        }))