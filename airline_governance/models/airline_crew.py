from odoo import fields, models, api

class airlineCrew(models.Model):
    _name = "airline.crew"
    _description = "Crew Model"

    name = fields.Char('Name', required = True)
    type = fields.Selection(string="Crew Type", selection=[('pilot','Pilot'),('co-pilot','Co-Pilot'),('hostess','Air hostess'),('technician','Airline Technician')])
    contact_no = fields.Char('Contact_no', required=True)
    email = fields.Char('Email', required=True)
    gender = fields.Selection(string="Gender", selection = [('male','Male'), ('female','Female'), ('other','Other')])
    sequence = fields.Integer()
    color = fields.Integer('Color', default = 0)