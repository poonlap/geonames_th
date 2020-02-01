# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)
class geonames_th(models.Model):
     _name = 'geonames_th.geonames_th'

# try to load translation but doesn't work.
     @api.model
     def _init(self):
         self.env['res.model'].sudo()._update_translations()

#     self.env['res.lang'].load_lang('TH')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100