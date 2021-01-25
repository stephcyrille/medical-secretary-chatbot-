#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings


chat_bot_global = {
    "FR": {
        "chatbot greeting": "Salut à vous et bienvenue dans notre sécrétariat médical. Bien vouloir saisir le mot *%s* pour commencer" % settings.HOME_KEYWORD,
        "no choice": "Pas de choix disponibe\n",
    },
    "EN": {
        "chatbot greeting": "Hello and welcome to our medical center. Please, type the word *%s* for starting" % settings.HOME_KEYWORD,
    }
}

base_menu = {
    "FR": {
        "main menu": "Bienvenu chez nous, sélectionner un menu\n\n" 
                     "*1*.Prendre un rendez-vous\n"
                     "*2*.Disponibilité d'un médécin \n"
                     "*3*.Commencer un diagnostique\n"
                     "*4*.Vérifier les résultats d'un examen\n"
    },
    "EN": {
        "main menu": "Welcome, select a number\n\n"
                     "*1*.Take an appointment\n"
                     "*2*.Doctor availability  \n"
                     "*3*.Start a diagnostic\n"
                     "*4*.Check exams results\n"
    },
}

home = {
    "FR": {
        "take an appointment": "Prendre un rendez-vous\n\n",
        "doctor availability": "Disponibilité du médécin\n\n",
        "start a diagnostic": "Commencer un diagnostic\n\n",
        "check exams results": "Vérifier résultat examens\n\n"
    },
    "EN": {
        "take an appointment": "Take an appointment\n\n",
        "doctor availability": "Doctor availability\n\n",
        "start a diagnostic": "Start a diagnostic now\n\n",
        "check exams results": "checks all exams results\n\n",
    },
}



