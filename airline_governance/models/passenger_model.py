from odoo import fields, models

class passengerModel(models.Model):
    _name = "passenger.model"
    _description = "Passenger Model"

    name = fields.Char('Name', required = True)
    airline_class = fields.Selection(string='Airline Class', selection=[('first','First'),('business','Business'),('economy','Economy'), ('premium_economy','Premium Economy')])
    seat_no = fields.Char('Seat', required = True)
    froms = fields.Char('From', required = True)
    to = fields.Char('To', required = True)
    nationality = fields.Char('Nationality', required=True)
    flight_id = fields.Many2one('airline.model', string="Flight")