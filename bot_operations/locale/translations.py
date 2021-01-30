#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings

doctors = "*1*. Antoine Gabriel\n*2*. Cyrille Stephane\n*3*. Alima Christelle\n*4*. Anita Amougou\n" \
          "*5*. Laetitia Manga\n*6*. Paterson Réné\n*7*. Ankel Henriette\n*8*. Manuella Atangana\n\n"

services = "*1*. Médécine générale\n*2*. Immunologie\n*3*. Radiologie\n" \
           "*4*. Churigie\n*5*. Neurologie\n*6*. Pneumologie\n*7*. Cardiologie\n" \
           "*8*. Odontologie\n*9*. Dermatologie\n*10*. Traumatologie\n*11*. Médécine intern\n" \
           "*12*. Endoctrinologie\n*13*. Anatomo-pathologie\n*14*. Hématologie\n" \
           "*15*. Gastro-entérologie\n*16*. Urologie\n*17*. Pharmacie\n*18*. Maternité\n" \
           "*19*. Pédiacrie\n*20*. Servcie des urgence\n*21*. Service des grands brulés\n\n"

chat_bot_global = {
    "FR": {
        "chatbot greeting": "Salut à vous et bienvenue dans notre sécrétariat médical. Bien vouloir saisir le mot *%s* pour commencer" % settings.HOME_KEYWORD,
        "no choice": "Pas de choix disponibe\n",
    },
    "EN": {
        "chatbot greeting": "Hello and welcome to our medical center. Please, type the word *%s* for starting" % settings.HOME_KEYWORD,
    }
}

generic = {
    "FR": {
        "select date": "Sélectionner le jour du rendez-vous\n\n"
                       "*1*. Lundi\n"
                       "*2*. Mardi\n"
                       "*3*. Mercredi\n"
                       "*4*. Jeudi\n"
                       "*5*. Vendredi\n"
                       "*6*. Samedi\n\n"
                       "*0*.Revenir à l'acceuil",
        "take an appointment": "Saisir une heure entre 7h et 15h (Uniquemenent le chiffre sans le h)\n\n"
                               "*0*.Revenir à l'acceuil",
    },
    "EN": {
        "select date": "Select appointment date\n\n"
                       "*1*. Monday\n"
                       "*2*. Tuesday\n"
                       "*3*. Wednesday\n"
                       "*4*. Thursday\n"
                       "*5*. Friday\n"
                       "*6*. Saturday\n\n",
        "take an appointment": "Write an hour, between 7am to 3pm\n\n"
    }
}

base_menu = {
    "FR": {
        "main menu": "Bienvenu au sécrétariat médical de l'Ecole National Superieur "
                     "Polytechnique de Douala. Sélectionner un menu\n\n"
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
        "take an appointment": "Sélectionner le service dans lequel vous souhaitez prendre rendez-vous\n\n"
                               "%(services)s"
                               "*0*.Revenir à l'acceuil" % {'services': services},
        "doctor availability": "Sélectionner le service dans lequel vous souhaitez vérifier la disponibilité"
                               "d'un médécin\n\n%(services)s"
                               "*0*.Revenir à l'acceuil" % {'services': services},
        "start a diagnostic": "Entrer votre nom complet\n\n"
                              "*0*.Revenir à l'acceuil",
        "check exams results": "Sélectionner le service dans lequel vous avez éffectué un examen\n\n"
                               "%(services)s"
                               "*0*.Revenir à l'acceuil" % {'services': services},
    },
    "EN": {
        "take an appointment": "Select a service in which you want to take an appointment\n\n"
                               "%(services)s" % {'services': services},
        "doctor availability": "Doctor availability\n\n",
        "start a diagnostic": "Start a diagnostic now\n\n",
        "check exams results": "checks all exams results\n\n",
    },
}

appointment = {
    "FR": {
        "confirm an appointment": "La prise de rendez vous a été enregistré avec succès pour "
                                  "%(day)s à %(hour)s heure. Merci de nous faire confiance\n\n"
                                  "*0*.Revenir à l'acceuil",
    },
    "EN": {
        "confirm an appointment": "An appointment is taken %(day)s at %(hour)s \n\n",
    }
}

check_doctor = {
    "FR": {
        "select a doctor": "Sélectionner le nom du médécin\n\n"
                           "%(doctors)s"
                           "*0*.Revenir à l'acceuil" % {'doctors': doctors},
        "confirm doctor availability": "Le  Dr. %(doctor)s est disponible le %(day)s à partir de %(hour)s heure."
                                       "Merci de nous faire confiance\n\n"
                                       "*0*.Revenir à l'acceuil",
    },
    "EN": {
        "select a doctor": "Select the name of the doctor\n\n"
                           "%(doctors)s" % {'doctors': doctors},
        "confirm doctor availability": "Dr. %(doctor)s is available on %(day)s from %(hour)s o'oclock\n\n",
    }
}

diagnosis = {
    "FR": {
        "user age": "Entrer votre age\n\n"
                    "*0*.Revenir à l'acceuil",
        "user gender": 'Entrer votre sexe\n\n'
                       '*0*.Revenir à l\'acceuil',
        "medical background": "Préciser vos antécédants médicaux et allergies\n\n"
                              "*0*.Revenir à l'acceuil",
        "ache zone": "Préciser la zone du corp vous faisant soufrir\n\n"
                            "*0*.Revenir à l'acceuil",
        "symptoms": "Décrire les symptomes apparents\n\n"
                            "*0*.Revenir à l'acceuil",
        "end diagnosis": "Merci de nous avoir soumis toutes ces informations. Elle seront analysées par "
                         "un médécin dans les plus brefs délais.\nPar ailleur, nous vous conseillons "
                         "de prendre rendez-vous chez le médécin.\n\n"
                         "*0*.Revenir à l'acceuil",
    },
    "EN": {
        "user age": "Entrer votre age\n\n"
                    "*0*.Revenir à l'acceuil",
        "user gender": 'Entrer votre sexe\n\n'
                       '*0*.Revenir à l\'acceuil',
        "medical background": "Préciser vos antécédants médicaux et allergies\n\n"
                              "*0*.Revenir à l'acceuil",
        "ache zone": "Préciser la zone du corp vous faisant soufrir\n\n"
                            "*0*.Revenir à l'acceuil",
        "symptoms": "Décrire les symptomes apparents\n\n"
                            "*0*.Revenir à l'acceuil",
        "end diagnosis": "Merci de nous avoir soumis toutes ces informations."
                         "Nous vous conseillons d'aller voir un médécin\n\n"
                         "*0*.Revenir à l'acceuil",
    }
}

exams_result = {
    "FR": {
        "user name": "Saisir votre nom complet\n\n"
                     "*0*.Revenir à l'acceuil",
        "exams result": "Résultats exames de %(name)s\n"
                        "%(results)s\n\n"
                        "*0*.Revenir à l'acceuil",
    },
    "EN": {
        "user name": "Saisir votre nom complet\n\n"
                     "*0*.Revenir à l'acceuil",
        "exams result": "Résultats exames de %(name)s\n\n"
                        "%(results)s\n\n"
                        "*0*.Revenir à l'acceuil",
    }
}

errors = {
    "FR": {
        "invalid entry": "*La réponse saisie n'est pas valide*\n\n",
        "choice unavailable": "*Le nombre saisie ne correspond à aucun menu*\n\n",
        "bad string": "*Bien vouloir saisir une chaine de caractère correcte*\n\n",
    },
    "EN": {
        "invalid entry": "Invalid response\n\n",
        "choice unavailable": "*Le nombre saisie ne correspond à aucun menu*\n\n",
        "bad string": "*Bien vouloir saisir une chaine de caractère correcte*\n\n",
    }
}
