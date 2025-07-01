# -*- coding: utf-8 -*-

from odoo import fields, models, api

class GameSetting(models.Model):
    _name = 'gamedesk.game_setting'
    _description = 'Game setting model definition'

    id = fields.Integer('ID')
    name = fields.Char('Name')
    engine_id = fields.Many2one('gamedesk.game_engine')
