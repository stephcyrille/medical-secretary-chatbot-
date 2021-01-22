#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings


chat_bot_global = {
    "FR": {
        "chatbot greeting": "Salut à vous et bienvenue sur du sécrétariat médical. Bien vouloir saisir le mot *%s* pour commencer" % settings.HOME_KEYWORD,
        "no choice": "Pas de choix disponibe\n",
    },
    "EN": {
        "chatbot greeting": "Hello and welcome to medical center chat bot. Please, type the word *%s* for starting" % settings.HOME_KEYWORD,
    }
}

base_menu = {
    "FR": {
        "main menu": """
                         Bienvenu chez nous, sélectionner un menu\n\n
                         1.Prendre un rendez-vous\n
                         2.Disponibilité d'un médécin \n
                         3.Commencer un diagnostique\n
                         4.Vérifier les résultats d'un examen\n
                    """
    },
    "EN": {
        "main menu": """
                         Welcome, select a number\n\n
                         1.Take an appointment\n
                         2.Doctor availability  \n
                         3.Start a diagnostic\n
                         4.Check exams result\n
                    """,
    },
}


