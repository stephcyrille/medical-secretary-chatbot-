# -*- coding: utf-8 -*-
from bot_operations.models import ChatBotRequest
from bot_operations.steps.base_menu import Menu
#from ussdPortal.libs.ussd.locale.translations import airtime, errors, home
from django.conf import settings as app_settings


class Appointment(Menu):
    def airtime_or_data(self, request):  # 21
        session = ChatBotRequest.objects.get(transId=self.session_id)
        if self.loggedString == '1':
            # menu_text = airtime[self.lang]["buy airtime"]
            menu_text = ''
            session.level = 22
            session.operation = 'buy_airtime'
            session.save()
            return self.ussd_proceed(menu_text)
        if self.loggedString == '2':
            # menu_text = airtime[self.lang]["buy data"]
            menu_text = ""
            session.level = 28
            session.operation = 'buy_data'
            session.save()
            return self.ussd_proceed(menu_text)

        elif self.loggedString == '6':
            return self.home(request)

        elif self.loggedString == '0':
            return self.home(request)

        else:
            #menu_text = errors[self.lang]["bad choice"]
            menu_text = ""
            return self.ussd_proceed(menu_text)

    def execute(self, request):
        menu = {
            21: lambda: self.airtime_or_data(request),
            22: lambda: self.get_amount(request),
            23: lambda: self.confirm_message(request),
            24: lambda: self.ending_session(request),

            25: lambda: self.get_another_phone_number(request),
            26: lambda: self.another_phone_confirm_message(request),
            27: lambda: self.another_phone_ending_session(request),

            28: lambda: self.global_bundle_choices(request),
            29: lambda: self.categorized_bundle_choices(request),
            30: lambda: self.bundle_confirm_message(request),
            31: lambda: self.bundle_ending_session(request),
        }
        return menu.get(self.level, lambda: self.home(request))()