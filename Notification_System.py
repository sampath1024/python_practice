#Notification System
from abc import ABC,abstractmethod
class Notification():
    def __init__(self,notification,message):
        self.notification=notification
        self.message=message
    @abstractmethod
    def send_alerts(self):
        pass

class EmailNotification(Notification):
    def __init__(self,notification,message,payment_method):
        super().__init__(notification,message)
        self.payment_method=payment_method
    @abstractmethod
    def send_alerts(self,):
        print(f"{self.notification}:{self.message} Payment recieved from {self.payment_method}")

class MessageNotificatin(Notification):
    def __init__(self,notification,message,payment_method):
        pass
obj = EmailNotification("Email","order Succesful","UPI")
obj.send_alerts()



