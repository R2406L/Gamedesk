# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import fields, models, api

class Game(models.Model):
    _name = 'gamedesk.game'
    _inherit = 'mail.thread'
    _description = 'Game model definition'

    id = fields.Integer('ID')
    name = fields.Char('Name')
    image = fields.Binary('Illustration')
    description = fields.Text('Short description')
    duration = fields.Integer('Duration, h', default=4)
    date_start = fields.Datetime('Start play game', required=True)
    minimal_players = fields.Integer('Minimal players', default=4)

    gm_id = fields.Many2one('res.partner', string='Game Master', domain='[("is_dungeon_master", "=", True)]')
    player_ids = fields.Many2many('res.partner', string='Players', domain='[("is_dungeon_seeker", "=", True)]')
    engine_id = fields.Many2one('gamedesk.game_engine', string='Game engine')
    setting_id = fields.Many2one('gamedesk.game_setting', string='Game setting', domain='[("engine_id", "=", engine_id)]')

    free_chairs = fields.Integer('Number of free chairs', compute='_get_chairs')
    is_actual = fields.Boolean('Is actual', compute='_get_actual', search='_search_actual')
    is_mine = fields.Boolean('Is my game', compute='_get_my_games', store=True)

    def _get_chairs(self):
        for s in self:
            s.free_chairs =  round(len(s.player_ids) / s.minimal_players * 100)

    def _search_actual(self, operator, value):
        today = datetime.now()
        recs = self.search([]).filtered(lambda s: s.date_start > today)
        if recs:
           return [('id', 'in', recs.ids)]
        return [('id', 'in', [])]

    @api.depends('date_start')
    def _get_actual(self):
        for s in self:
            s.is_actual = True if s.date_start > datetime.now() else False

    @api.depends('gm_id','player_ids')
    def _get_my_games(self):
        for s in self:
            partner_id = self.env.user.partner_id
            s.is_mine = True if s.gm_id == partner_id or partner_id in s.player_ids else False
