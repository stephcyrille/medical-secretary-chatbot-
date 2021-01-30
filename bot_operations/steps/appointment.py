# -*- coding: utf-8 -*-
from bot_operations.models import ChatBotRequest
from bot_operations.steps.base_menu import Menu
from bot_operations.locale.translations import appointment, errors, home, generic


class Appointment(Menu):
    def appointment_service(self, request):  # 100
        session = ChatBotRequest.objects.get(transId=self.session_id)
        try:
            body = int(self.loggedString)
            choice_range = range(1, 22)
            if body in choice_range:
                menu_text = generic[self.lang]["select date"]
                if self.loggedString == '1': session.department = 'Médécine générale';
                if self.loggedString == '2': session.department = 'Immunologie';
                if self.loggedString == '3': session.department = 'Radiologie';
                if self.loggedString == '4': session.department = 'Churigie';
                if self.loggedString == '5': session.department = 'Neurologie';
                if self.loggedString == '6': session.department = 'Pneumologie';
                if self.loggedString == '7': session.department = 'Cardiologie';
                if self.loggedString == '8': session.department = 'Odontologie';
                if self.loggedString == '9': session.department = 'Dermatologie';
                if self.loggedString == '10': session.department = 'Traumatologie';
                if self.loggedString == '11': session.department = 'Médécine interne';
                if self.loggedString == '12': session.department = 'Endoctrinologie';
                if self.loggedString == '13': session.department = 'Anatom-pathologie';
                if self.loggedString == '14': session.department = 'Hémætologie';
                if self.loggedString == '15': session.department = 'Gastro-entérologie';
                if self.loggedString == '16': session.department = 'Urologie';
                if self.loggedString == '17': session.department = 'Pharmæcie';
                if self.loggedString == '18': session.department = 'Maternité';
                if self.loggedString == '19': session.department = 'Pédiacrie';
                if self.loggedString == '20': session.department = 'Service des urgences';
                if self.loggedString == '21': session.department = 'Service de grands brulés';
                session.level = 101
                session.operation = 'appointment'
                session.save()
                return self.message_proceed(menu_text)
            elif body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["choice unavailable"]
                menu_text += home[self.lang]["take an appointment"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += home[self.lang]["take an appointment"]
            return self.message_proceed(menu_text)

    def appointment_date(self, request):  # 101
        session = ChatBotRequest.objects.get(transId=self.session_id)
        try:
            body = int(self.loggedString)
            if body in range(1, 7):
                menu_text = generic[self.lang]["take an appointment"]
                if self.loggedString == '1':
                    session.day = 'Lundi'
                if self.loggedString == '2':
                    session.day = 'Mardi'
                if self.loggedString == '3':
                    session.day = 'Mercredi'
                if self.loggedString == '4':
                    session.day = 'Jeudi'
                if self.loggedString == '5':
                    session.day = 'Vendredi'
                if self.loggedString == '6':
                    session.day = 'Samedi'
                session.level = 102
                session.save()
                return self.message_proceed(menu_text)
            elif body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["choice unavailable"]
                menu_text += generic[self.lang]["select date"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += generic[self.lang]["select date"]
            return self.message_proceed(menu_text)

    def confirm_appointment(self, request):  # 102
        session = ChatBotRequest.objects.get(transId=self.session_id)
        try:
            body = int(self.loggedString)
            if body in range(7, 16):
                parameters = {
                    "day": session.day,
                    "hour": self.loggedString,
                }
                menu_text = appointment[self.lang]["confirm an appointment"] % parameters
                session.level = 5
                session.save()
                return self.message_proceed(menu_text)
            elif body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["choice unavailable"]
                menu_text += generic[self.lang]["take an appointment"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += generic[self.lang]["take an appointment"]
            return self.message_proceed(menu_text)

    def execute(self, request):
        menu = {
            100: lambda: self.appointment_service(request),
            101: lambda: self.appointment_date(request),
            102: lambda: self.confirm_appointment(request),
        }
        return menu.get(self.level, lambda: self.home(request))()