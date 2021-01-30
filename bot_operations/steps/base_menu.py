# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.renderers import XMLRenderer

from bot_operations.models import ChatBotRequest
from bot_operations.locale.translations import base_menu


class MyXMLRenderer(XMLRenderer):
    """Override XML tag names."""

    root_tag_name = 'Response'


class Menu(APIView):
    """
        This version is only stateless, then without session
    """

    renderer_classes = (MyXMLRenderer,)

    def __init__(self, dictData, session_id, session, level, lang):
        self.loggedString = dictData['body']
        self.transId = session_id
        self.messageString = dictData['body']
        self.session_id = session_id
        self.level = level
        self.user_response = dictData['body']
        self.session = session
        # Set session Language
        self.lang = lang

    def execute(self):
        raise NotImplementedError

    def message_proceed(self, body='', menu_step='', session_instance=None):
        """
            Params wil be:
              menu_text     (str)
        """
        # There we will compose response
        response = {
            "Message": {
                "Body": body
            }
        }

        content = response
        return Response(content)

    def home(self, request):
        """serves the home menu"""
        session = ChatBotRequest.objects.get(transId=self.session_id)
        menu_text = base_menu[self.lang]["main menu"]
        session.level = 5
        session.save()

        return self.message_proceed(menu_text)
