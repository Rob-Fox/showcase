# from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from SCRUM.models import Task, User, Project#, TeamMember
# from asgiref.sync import async_to_sync

# class TaskConsumer(SyncConsumer):
#     def connect(self, event):
#         self.send({
#             "type":"websocket.accept",
#         })

#     def send(self,event):
#         self.send({
#             "type":"websocket"
#         })

#     def receive(self,event):
#         self.send({
#             "type":"websocket.send",
#             "text":event["text"],
#         })

#     def disconnect(self,close_code):
#         return



class TaskConsumer(WebsocketConsumer):
    def connect(self):
        # print(self)
        self.accept()
    
    
    def receive(self,text_data):
        dataJSON = json.loads(text_data)
        if 'task' in dataJSON.keys():
            #existing task
            column = dataJSON['column']
            task = dataJSON['task']
            # print('column: ')
            # print(column)
            # print('Task: ')
            # print(task)
            self.send(text_data=json.dumps({
                'column':column
            }))
        else:
            #new task
            name = dataJSON['name']
            creator = User.objects.get(id=self.scope['session']['user'])
            project = Project.objects.get(id=dataJSON['project'])
            newTask = Task.objects.create(status='backlog', name=name, creator=creator, project=project)
            newTask.save()
            print(newTask.id)
            self.send(text_data=json.dumps({
                'id': newTask.id
            }))



    
    def disconnect(self, close_code):
        print('WEBSOCKET PROBLEM')
        print(close_code)
        # pass