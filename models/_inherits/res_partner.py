
from odoo import api, fields, models

class GamedeskResPartner(models.Model):

    _inherit = 'res.partner'

    is_dungeon_master = fields.Boolean(string='Is dungeon Master', default=False)
    is_dungeon_seeker = fields.Boolean(string='Is dungeon Seeker', default=False)

    achievement_ids = fields.One2many('gamedesk.game_seeker_achievement', 'partner_id', 'Gained achievements')
    ac_score = fields.Integer('Achievement raiting', compute='_compute_score', store=True)
    total_score = fields.Integer('Total score', compute='_compute_total_score')

    is_gm_validation = fields.Boolean(compute='_check_gm_validation')
    is_admin_validation = fields.Boolean(compute='_check_admin_validation')

    @api.depends('achievement_ids')
    def _compute_score(self):
        for s in self:
            s.ac_score = sum([a.score for a in s.achievement_ids])

    def _compute_total_score(self):
        for s in self:
            s.total_score = sum([a.score for a in self.env['gamedesk.game_achievement'].search([])])

    def _check_gm_validation(self):
        for s in self:
            s.is_gm_validation = self.env.user.has_group('gamedesk.gamedesk_gm')

    def _check_admin_validation(self):
        for s in self:
            s.is_admin_validation = self.env.user.has_group('gamedesk.gamedesk_administrator')

    def gane_achievement(self):
        return {
            'name': "Gane achievement",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'gamedesk.game_achievement.wizard',
            'view_id': self.env.ref('gamedesk.gamedesk_game_achievement_wizard_view_form').id,
            'target': 'new'
        }