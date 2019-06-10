# -*- coding: utf-8 -*-

from odoo import models, fields, api
from timeit import default_timer
import time

class module_two(models.Model):
	_name = 'module_two.module_two'
	
	#Référence de l'enregistrement
	ref = fields.Char("Référence", help='Exemple : Ref/001/06-06-19')
	
	#informations sur l'employer
	full_name = fields.Char('Nom et Prénom', required=True)
	email = fields.Char('E-mail')
	post = fields.Selection((('chef',"Chef d'entreprise"),('dg','Directeur'),('tech1','Rédacteur Contenu'),('tech2','Web Master'),('tech3','Developpeur Informatique'),('tech4','Consultant'),('rh1','Responsable Ressources Humaines'),('rh2','Gestionnaire de Communauté et Marketing'),('stg','Stagiaire'),('assi',"Responsable d'Assistance")), string="Poste")
	
	#informations sur la mission
	day_date = fields.Date('Date', required=True, help='Date du jour')
	time = fields.Float('Durée', required=True, help='Temps passé sur la tâche heures:minutes')
	service = fields.Selection((('dev','Technique / Développement '), ('rh','Ressources Humaines'), ('ass','Assistance'),('pros','Prospection'),('mark','Marketing'),('cli','Service Client')),'Service', required=True)
	project = fields.Char('Projet', required=True, help='Titre du projet')
	note = fields.Text('Note', help='Note supplémentaire')
	
	#informations notebook
	client_prospect = fields.Char('Client / Prospect', help="Nom ou Référence du Client si il y'en a")
	devis_facture = fields.Char('Devis / Facture', help="Référence de la facture si il y'en a une")
	invoiceable = fields.Boolean('Temps facturable', help='Temps facturabl ou pas')
	description = fields.Text('Description', help=' Tâches effectuées, avancement, état actuel ...')
	
	start = default_timer()	
	
	def updateTime():
		now = default_timer() - start
		minutes, seconds = divmod(now, 60)
		hours, minutes = divmod(minutes, 60)
		str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
		print(str_time)
	#@api.multi
	#def init():
		#while (True) :
		#	updateTime()
		#	time.sleep(1)
			
