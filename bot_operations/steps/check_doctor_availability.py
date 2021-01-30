# -*- coding: utf-8 -*-
from bot_operations.models import ChatBotRequest
from bot_operations.steps.base_menu import Menu
from bot_operations.locale.translations import generic, errors, home, check_doctor


class CheckDoctorAvailability(Menu):
    def availability_service(self, request):  # 200
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
                session.level = 201
                session.operation = 'check_doctor_availability'
                session.save()
                return self.message_proceed(menu_text)
            elif body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["choice unavailable"]
                menu_text += home[self.lang]["doctor availability"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += home[self.lang]["doctor availability"]
            return self.message_proceed(menu_text)

    def availability_date(self, request):  # 201
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
                session.level = 202
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

    def get_appointment_hour(self, request):  # 202
        session = ChatBotRequest.objects.get(transId=self.session_id)
        try:
            body = int(self.loggedString)
            if body in range(7, 16):
                menu_text = check_doctor[self.lang]["select a doctor"]
                session.level = 203
                # Select appointment hour
                session.hour = self.loggedString
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

    def get_a_doctor_confirm(self, request): # 203
        session = ChatBotRequest.objects.get(transId=self.session_id)
        try:
            body = int(self.loggedString)
            if body in range(1, 9):
                # set doctor name
                doctor = ''
                if self.loggedString == '1': doctor = 'Antoine Gabriel';
                if self.loggedString == '2': doctor = 'Cyrille Stephane';
                if self.loggedString == '3': doctor = 'Alima Christelle';
                if self.loggedString == '4': doctor = 'Anita Amougou';
                if self.loggedString == '5': doctor = 'Laetitia Manga';
                if self.loggedString == '6': doctor = 'Paterson Réné';
                if self.loggedString == '7': doctor = 'Ankel Henriette';
                if self.loggedString == '8': doctor = 'Manuella Atangana';
                session.level = 1
                session.save()
                parameters = {
                    "doctor": doctor,
                    "day": session.day,
                    "hour": session.hour,
                }
                menu_text = check_doctor[self.lang]["confirm doctor availability"] % parameters
                return self.message_proceed(menu_text)
            elif body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["choice unavailable"]
                menu_text += check_doctor[self.lang]["select a doctor"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += check_doctor[self.lang]["select a doctor"]
            return self.message_proceed(menu_text)
        return 0

    def execute(self, request):
        menu = {
            200: lambda: self.availability_service(request),
            201: lambda: self.availability_date(request),
            202: lambda: self.get_appointment_hour(request),
            203: lambda: self.get_a_doctor_confirm(request),
        }
        return menu.get(self.level, lambda: self.home(request))()