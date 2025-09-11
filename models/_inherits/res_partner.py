
from odoo import api, fields, models

class GamedeskResPartner(models.Model):

    _inherit = 'res.partner'

    is_dungeon_master = fields.Boolean(string='Is dungeon Master', default=False)
    is_dungeon_seeker = fields.Boolean(string='Is dungeon Seeker', default=False)