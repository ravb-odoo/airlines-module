from odoo import fields, models, api

class crewModel(models.Model):
    _name = "crew.model"
    _description = "Crew Model"

    name = fields.Char('Name', required = True)
    type = fields.Selection(string="Crew Type", selection=[('pilot','Pilot'),('co-pilot','Co-Pilot'),('hostess','Air hostess'),('technician','Airline Technician')])
    contact_no = fields.Char('Contact_no', required=True)
    email = fields.Char('Email', required=True)
    sequence = fields.Integer()