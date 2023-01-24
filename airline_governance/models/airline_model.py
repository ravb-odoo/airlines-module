# -*- coding: utf-8 -*-
import datetime
from odoo import fields, models, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class airlineModel(models.Model):
    _name = "airline.model"
    _description = "Airline Model"
    _order = "depart_date_time"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'depart_airport_id'

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    type = fields.Selection(string="Type", selection = [('domestic','Domestic'), ('international','International')])
    arrival_date_time = fields.Datetime('Arrival', required = True)
    depart_date_time = fields.Datetime('Departure', required = True)
    arrival_airport_id = fields.Many2one('airport.model', string='Arrival Airport', required = True)
    depart_airport_id = fields.Many2one('airport.model', string= 'Departure Airport', required = True)
    total_distance = fields.Integer('Total Distance (km)' , required = True)
    gate_no = fields.Char('Gate No.', required = True)
    price = fields.Integer("Total Price ", required = True)
    active = fields.Boolean('Active', default = True)
    state = fields.Selection(string='State', selection=[('new','New'),('upcoming','Upcoming'),('landed','Landed'),('maintenance','Maintenance'),('take_off','Take Off')], default='new', tracking=True)
    passenger_ids = fields.One2many('passenger.model', 'flight_id')
    image = fields.Binary("Image", attachment=True, store=True,
                                help="This field holds the image used for as favicon")

    pilot_id = fields.Many2one('crew.model', string= "Pilot" , domain="[('type', '=', 'pilot')]")
    co_pilot_id = fields.Many2one('crew.model', string= "Co-Pilot", domain="[('type', '=', 'co-pilot')]")
    hostess_id = fields.Many2many('crew.model', 'airline_hostess_rel', 'airline_id','hostess_id', string= "Hostess", domain="[('type', '=', 'hostess')]")
    technician_ids = fields.Many2many('crew.model', 'airline_technician_rel', 'airline_id', 'technician_id', string="Technician", domain="[('type', '=', 'technician')]")


    @api.constrains('depart_date_time')
    def _check_time(self):
        date1 = datetime.datetime.now()

        for rec in self:
            duration =  rec.depart_date_time - relativedelta(hours = 2)
            if date1 > rec.depart_date_time:
                rec.state = 'take_off'
            elif date1 < duration:
                rec.state = 'upcoming'
            elif date1 > duration and date1 < rec.depart_date_time:
                rec.state = 'landed'

        
    
    def action_maintenance(self):
        for rec in self:
            rec.state = 'maintenance'

    
    @api.ondelete(at_uninstall=False)
    def _check_state(self):
        for asset in self:
            if asset.state not in ['new', 'take_off']:
                raise UserError(
                    f'You cannot delete a {asset.state} flight.',
                )


    