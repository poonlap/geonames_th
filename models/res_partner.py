# Copyright 2016 Nicolas Bessi, Camptocamp SA
# Copyright 2018 Tecnativa - Pedro M. Baeza
# Copyright 2020 Poonlap V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"
    @api.onchange("zip_id")
    def _onchange_zip_id(self):
        if self.zip_id:
            vals = {
                "city_id": self.zip_id.city_id,
                "zip": self.zip_id.name,
                "city": self.zip_id.city_id.name.split(", ")[1] if len(self.zip_id.city_id.name.split(", ")) == 2 else self.zip_id.city_id.name.split(", ")[0],
                "street2": self.zip_id.city_id.name.split(", ")[0] if len(self.zip_id.city_id.name.split(", ")) == 2 else '',
            }
            if self.zip_id.city_id.country_id:
                vals.update({"country_id": self.zip_id.city_id.country_id})
            if self.zip_id.city_id.state_id:
                vals.update({"state_id": self.zip_id.city_id.state_id})
            self.update(vals)
        elif not self.country_enforce_cities:
            self.city_id = False

