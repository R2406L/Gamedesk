# -*- coding: utf-8 -*-

from odoo import fields, models, api

class GameEngine(models.Model):
    _name = 'gamedesk.game_engine'
    _inherit = 'mail.thread'
    _description = 'Game engine model definition'

    id = fields.Integer('ID')
    name = fields.Char('Name')
    image = fields.Binary('Illustration')
    description = fields.Text('Short description')

