# -*- coding: utf-8 -*-
from bot_operations.models import ChatBotRequest
from bot_operations.steps.base_menu import Menu
from bot_operations.locale.translations import generic, errors, home, exams_result


class ExamsResult(Menu):
    def get_department(self, request):  # 400
        session = ChatBotRequest.objects.get(transId=self.session_id)
        try:
            body = int(self.loggedString)
            choice_range = range(1, 22)
            if body in choice_range:
                menu_text = exams_result[self.lang]["user name"]
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
                session.level = 401
                session.operation = 'exams_result'
                session.save()
                return self.message_proceed(menu_text)
            elif body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["choice unavailable"]
                menu_text += home[self.lang]["check exams results"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += home[self.lang]["check exams results"]
            return self.message_proceed(menu_text)

    def get_name(self, request):  # 401
        results = "*1*. Examen #REF1288HCRT: Positif\n" \
                  "*2*. Examen #REF7280HOPA: Négatif\n" \
                  "*3*. Examen #REF021R88JT: Négatif\n" \
                  "*4*. Examen #REF2288Y1RO: Négatif\n"
        session = ChatBotRequest.objects.get(transId=self.session_id)
        if not len(self.loggedString) < 3:
            session.level = 5
            session.name = self.loggedString
            parameters = {
                "name": self.loggedString,
                "results": results,
            }
            menu_text = exams_result[self.lang]["exams result"] % parameters
            session.save()
            return self.message_proceed(menu_text)
        try:
            body = int(self.loggedString)
            if body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["bad string"]
                menu_text += exams_result[self.lang]["user name"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += exams_result[self.lang]["user name"]
            return self.message_proceed(menu_text)

    def execute(self, request):
        menu = {
            400: lambda: self.get_department(request),
            401: lambda: self.get_name(request),
        }
        return menu.get(self.level, lambda: self.home(request))()