# -*- coding: utf-8 -*-
from odoo import fields, models

class airportModel(models.Model):
    _name = "airport.model"
    _description = "Airport Model"

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    terminal = fields.Integer('Terminal', required = True)
    city = fields.Many2one("res.country.state", string='City', required = True)
    country = fields.Many2one("res.country", string='Country', required = True)
    iata_code = fields.Char('IATA Code', required=True)
    
