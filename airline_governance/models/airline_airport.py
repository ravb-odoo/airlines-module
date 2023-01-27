# -*- coding: utf-8 -*-
from odoo import fields, models,api

class airlineAirport(models.Model):
    _name = "airline.airport"
    _description = "Airport Model"
    _rec_name = "iata_code"
    _rec_names_search = ['iata_code', 'name',]

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    terminal = fields.Integer('Terminal', required = True)
    country_id = fields.Many2one("res.country", string='Country', required = True)
    city_id = fields.Many2one("res.country.state", string='City', domain="[('country_id','=',country_id)]")
    iata_code = fields.Char('IATA Code', required=True)
    sequence = fields.Integer()

    airline_ids = fields.One2many('airline.airline','depart_airport_id', string="Flights")
    flight_count = fields.Integer("Count" , compute = "_count_flight")
    

    def name_get(self):
        result = []       
        for rec in self:
                result.append((rec.id, ('%s - %s') %(rec.iata_code, rec.name)))    
        return result

    def _count_flight(self):
        for rec in self:
            rec.flight_count = len(rec.airline_ids)
