# -*- coding: utf-8 -*-
from bot_operations.models import ChatBotRequest
from bot_operations.steps.base_menu import Menu
from bot_operations.locale.translations import home


class LowLevelMenu(Menu):
    """serves the home menu"""

    def take_an_appointment(self, request):  # 1
        session = ChatBotRequest.objects.get(transId=self.session_id)
        menu_text = home[self.lang]["take an appointment"]
        session.level = 100
        session.save()
        return self.message_proceed(menu_text)

    def check_doctor_availability(self, request):  # 2
        session = ChatBotRequest.objects.get(transId=self.session_id)
        menu_text = home[self.lang]["doctor availability"]
        session.level = 200
        session.save()
        return self.message_proceed(menu_text)

    def start_a_diagnostic(self, request):  # 5
        session = ChatBotRequest.objects.get(transId=self.session_id)
        menu_text = home[self.lang]["start a diagnostic"]
        session.level = 300
        session.save()
        return self.message_proceed(menu_text)

    def check_exams_results(self, request):  # 6
        session = ChatBotRequest.objects.get(transId=self.session_id)
        menu_text = home[self.lang]["check exams results"]
        session.level = 400
        session.save()
        return self.message_proceed(menu_text)

    def execute(self, request):
        menus = {
            '1': lambda: self.take_an_appointment(request),
            '2': lambda: self.check_doctor_availability(request),
            '3': lambda: self.start_a_diagnostic(request),
            '4': lambda: self.check_exams_results(request),
        }
        return menus.get(self.user_response, lambda: self.home(request))()