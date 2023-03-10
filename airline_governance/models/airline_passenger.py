from odoo import fields, models, api

class airlinePassenger(models.Model):
    _name = "airline.passenger"
    _description = "Passenger Model"

    name = fields.Char('Name', required = True)
    phone_no = fields.Char('Phone No.', required=True)
    email = fields.Char('Email', required=True)
    airline_class = fields.Selection(string='Airline Class', selection=[('first','First'),('business','Business'),('economy','Economy'), ('premium_economy','Premium Economy')])
    seat_no = fields.Char('Seat', required = True)
    from_id = fields.Many2one('res.country.state', string='From', required = True)
    to_id = fields.Many2one('res.country.state', string='To', required = True)
    sequence = fields.Integer()
    nationality = fields.Char('Nationality', required=True)
    flight_id = fields.Many2one('airline.airline', string="Flight", domain="[('arrival_airport_id.city_id','=',to_id),('depart_airport_id.city_id','=',from_id)]")

