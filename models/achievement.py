# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import fields, models, api

class Achievement(models.Model):
    _name = 'gamedesk.game_achievement'
    _description = 'Game achievement model definition'

    id = fields.Integer('ID')
    name = fields.Char('Name')
    image = fields.Binary('Illustration')
    description = fields.Text('Description')
    score = fields.Integer('Score')
    collected_ids = fields.One2many('gamedesk.game_seeker_achievement', 'achievement_id', 'Gained achievements')

class SeekerAchievement(models.Model):
    _name = 'gamedesk.game_seeker_achievement'
    _description = 'Game seeker achievement model definition'

    id = fields.Integer('ID')
    name = fields.Char(related='achievement_id.name')
    description = fields.Text(related='achievement_id.description')
    image = fields.Binary(related='achievement_id.image')
    score = fields.Integer(related='achievement_id.score')
    date = fields.Date('Collected at', required=True, default=lambda self:fields.Datetime.now())
    partner_id = fields.Many2one('res.partner', string='Seeker', required=True, domain='[("is_dungeon_seeker", "=", True)]')
    achievement_id = fields.Many2one('gamedesk.game_achievement', string='Achievement', required=True)
    comment = fields.Text('Description')

class AchievementWizard(models.TransientModel):
    _name = 'gamedesk.game_achievement.wizard'
    _description = 'Add achievement to partner wizard definition'

    achievement_id = fields.Many2one('gamedesk.game_achievement')
    partner_id = fields.Many2one('res.partner')
    comment = fields.Text('Description')

    def action_save(self):
        self.env['gamedesk.game_seeker_achievement'].create({
            "partner_id": self.partner_id.id,
            "achievement_id": self.achievement_id.id,
            "comment": self.comment

        })
        return {
            'name': "Achievements",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'res.partner',
            'res_id': self.partner_id.id,
            'view_id': self.env.ref('base.view_partner_form').id,
            'target': 'current'
        }

