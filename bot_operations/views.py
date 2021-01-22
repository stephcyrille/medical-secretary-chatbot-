import uuid
from django.conf import  settings
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.renderers import XMLRenderer

from .models import ChatBotRequest
from .locale import translations


class MyXMLRenderer(XMLRenderer):
    """Override XML tag names."""

    root_tag_name = 'Response'


class BotPortal(APIView):
    """
    A view that returns the count of active users in XML.
    """
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    renderer_classes = (MyXMLRenderer,)

    def get_bot_request(self, from_number):
        try:
            req_obj = ChatBotRequest.objects.filter(msisdn=from_number, status='open')
            if req_obj.first() is None:
                _uuid = str(uuid.uuid4())
                tab_uuid = _uuid.split('-')
                transId = (tab_uuid[0] + tab_uuid[3]).upper()
                req = ChatBotRequest(uuid=str(uuid.uuid4()), transId=transId, msisdn=from_number, status='open',
                                     menu_step_name='sante')
                req.save()
                return req
            else:
                return req_obj.first()
        except ChatBotRequest.DoesNotExist:
            session = ChatBotRequest(uuid=str(uuid.uuid4()), transId=transId, msisdn=from_number, status='open',
                                     menu_step_name='sante')
            session.save()
            return session

    def response_text(self, body='', menu_step='', session_instance=None):
        if menu_step != '':
            session_instance.menu_step = menu_step
            session_instance.save()
        response = {
            "Message": {
                "Body": body
            }
        }
        print(response)
        return response

    def post(self, request):
        # In this place, we will create a session after checkin if session with my transId exist
        # We will always check if the user has one pending transaction*

        post_data = request.data
        print(post_data)

        from_number = post_data['From']
        to_number = post_data['From']
        body = post_data['Body'].lower()

        # TODO We will find the ChatBotRequest with from number whose has end_session_time is greater than now time
        session = self.get_bot_request(from_number)

        print (session.menu_step)
        print (session.menu_step_name)

        if settings.HOME_KEYWORD == body:
            session.status = 'close'
            session.save()
            response = {
                "Message": {
                    "Body": translations.base_menu['FR']["main menu"]
                }
            }
            print(response)
            return Response(response)

        else:
            session.status = 'close'
            session.save()
            response = {
                "Message": {
                    "Body": translations.chat_bot_global['FR']["chatbot greeting"]
                }
            }
            print(response)
            return Response(response)
