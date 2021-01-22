from django.contrib import admin
from django.urls import path
from bot_operations.views import BotPortal


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bot/request/', BotPortal.as_view, name="bot_operations"),
]
