# -*- coding: utf-8 -*-
from odoo import fields, models,api

class airportModel(models.Model):
    _name = "airport.model"
    _description = "Airport Model"
    _rec_name = "iata_code"
    _rec_names_search = ['iata_code', 'name',]

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    terminal = fields.Integer('Terminal', required = True)
    city = fields.Many2one("res.country.state", string='City')
    country = fields.Many2one("res.country", string='Country', required = True)
    iata_code = fields.Char('IATA Code', required=True)
    sequence = fields.Integer()
    
@api.model
def name_get(self):
    result = []       
    for rec in self:
            result.append((rec.id, rec.iata_code2))       
    return result