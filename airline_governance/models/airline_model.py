# -*- coding: utf-8 -*-
from odoo import fields, models

class airlineModel(models.Model):
    _name = "airline.model"
    _description = "Airline Model"

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    type = fields.Selection(string="Type", selection = [('domestic','Domestic'), ('international','International')])
    arrival_date_time = fields.Datetime('Arrival', required = True)
    depart_date_time = fields.Datetime('Departure', required = True)
    arrival_airport = fields.Char('Arrival Airport', required = True)
    depart_airport = fields.Char('Departure Airport', required = True)
    total_distance = fields.Integer('Total Distance (km)' , required = True)
    gate_no = fields.Char('Gate No.', required = True)
    price = fields.Integer("Total Price ", required = True)
    active = fields.Boolean('Active', default = True)