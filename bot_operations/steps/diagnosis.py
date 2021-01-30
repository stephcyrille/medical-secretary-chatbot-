# -*- coding: utf-8 -*-
from bot_operations.models import ChatBotRequest
from bot_operations.steps.base_menu import Menu
from bot_operations.locale.translations import generic, errors, home, diagnosis


class Diagnosis(Menu):
    def get_name(self, request):  # 300
        session = ChatBotRequest.objects.get(transId=self.session_id)
        if not len(self.loggedString) < 3:
            menu_text = diagnosis[self.lang]["user age"]
            session.level = 301
            session.operation = 'diagnosis'
            session.name = self.loggedString
            session.save()
            return self.message_proceed(menu_text)
        try:
            body = int(self.loggedString)
            if body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["bad string"]
                menu_text += home[self.lang]["start a diagnostic"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += home[self.lang]["start a diagnostic"]
            return self.message_proceed(menu_text)

    def get_age(self, request):  # 301
        session = ChatBotRequest.objects.get(transId=self.session_id)
        try:
            body = int(self.loggedString)
            # Set diagnosis age from 2 to 90 years old
            if body in range(2, 91):
                menu_text = diagnosis[self.lang]["user gender"]
                session.level = 302
                session.age = body
                session.save()
                return self.message_proceed(menu_text)
            if body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["invalid entry"]
                menu_text += diagnosis[self.lang]["user age"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += diagnosis[self.lang]["user age"]
            return self.message_proceed(menu_text)

    def get_gender(self, request):  # 302
        session = ChatBotRequest.objects.get(transId=self.session_id)
        if not len(self.loggedString) < 3:
            menu_text = diagnosis[self.lang]["medical background"]
            session.level = 303
            session.gender = self.loggedString
            session.save()
            return self.message_proceed(menu_text)
        try:
            body = int(self.loggedString)
            if body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["bad string"]
                menu_text += diagnosis[self.lang]["user gender"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += diagnosis[self.lang]["user gender"]
            return self.message_proceed(menu_text)

    def get_medical_background(self, request): # 303
        session = ChatBotRequest.objects.get(transId=self.session_id)
        if not len(self.loggedString) < 3:
            menu_text = diagnosis[self.lang]["ache zone"]
            session.level = 304
            session.medical_background = self.loggedString
            session.save()
            return self.message_proceed(menu_text)
        try:
            body = int(self.loggedString)
            if body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["bad string"]
                menu_text += diagnosis[self.lang]["medical background"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += diagnosis[self.lang]["medical background"]
            return self.message_proceed(menu_text)

    def get_ache_zone(self, request): # 304
        session = ChatBotRequest.objects.get(transId=self.session_id)
        if not len(self.loggedString) < 3:
            menu_text = diagnosis[self.lang]["symptoms"]
            session.level = 305
            session.ache_zone = self.loggedString
            session.save()
            return self.message_proceed(menu_text)
        try:
            body = int(self.loggedString)
            if body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["bad string"]
                menu_text += diagnosis[self.lang]["ache zone"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += diagnosis[self.lang]["ache zone"]
            return self.message_proceed(menu_text)

    def get_symptoms(self, request): # 305
        session = ChatBotRequest.objects.get(transId=self.session_id)
        if not len(self.loggedString) < 3:
            menu_text = diagnosis[self.lang]["end diagnosis"]
            session.level = 1
            session.symptoms = self.loggedString
            session.save()
            return self.message_proceed(menu_text)
        try:
            body = int(self.loggedString)
            if body == 0:
                return self.home(request)
            else:
                menu_text = errors[self.lang]["bad string"]
                menu_text += diagnosis[self.lang]["symptoms"]
                return self.message_proceed(menu_text)
        except Exception as e:
            print("Exception ", e.__str__())
            menu_text = errors[self.lang]["invalid entry"]
            menu_text += diagnosis[self.lang]["symptoms"]
            return self.message_proceed(menu_text)

    def execute(self, request):
        menu = {
            300: lambda: self.get_name(request),
            301: lambda: self.get_age(request),
            302: lambda: self.get_gender(request),
            303: lambda: self.get_medical_background(request),
            304: lambda: self.get_ache_zone(request),
            305: lambda: self.get_symptoms(request),
        }
        return menu.get(self.level, lambda: self.home(request))()