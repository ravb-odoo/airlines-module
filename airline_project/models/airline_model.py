# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, Command, _
from dateutil.relativedelta import relativedelta


class airlineModel(models.Model):
    _inherit = "airline.model"
    _description = "Inherit Airline Model"

    def action_maintenance(self):
        if not self.env['project.project'].search([('name', '=', 'Airlines')]).id:
            self.env['project.project'].create({
                'name': 'Airlines',
                'description': 'Maintenance of airlines'
            })

        for rec in self:
            task_1 = self.env['project.task'].create({
                'name': f'Maintainance for {rec.name}',
                'project_id': self.env['project.project'].search([('name', '=', 'Airlines')]).id,
                'milestone_id': 2,
                'planned_date_begin': datetime.today(),
                'planned_date_end': datetime.today() + relativedelta(hours=1)
            })


        return super().action_maintenance()
