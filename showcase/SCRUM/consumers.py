from channels.consumer import SyncConsumer
import json
# from asgiref.sync import async_to_sync

class TaskConsumer(SyncConsumer):
    def connect(self, event):
        self.send({
            "type":"websocket.accept",
        })

    def send(self,event):
        self.send({
            "type":"websocket"
        })

    def receive(self,event):
        self.send({
            "type":"websocket.send",
            "text":event["text"],
        })

    def disconnect(self,close_code):
        return



# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept();

#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         user = text_data_json['user']

#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'user': user,

#             }
#         )
        
#     def chat_message(self, event):
#         message = event['message']
#         user = event['user']

#         self.send(text_data=json.dumps({
#             'message': message,
#             'user': user,
#         }))