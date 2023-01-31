# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, Command, _
from dateutil.relativedelta import relativedelta


class airlineAirline(models.Model):
    _inherit = "airline.airline"
    _description = "Inherit Airline Model"

    def action_maintenance(self):

        if not self.env['project.project'].search([('name', '=', 'Airlines')]).id:
            fold = [False, False, True, True]
            sequences = [1, 2, 3, 4]
            name = ['New','In Progress','Done', 'Blocked']
            stage_1, stage_2, stage_3, stage_4 = self.env['project.task.type'].create([{
                'name': name[i],
                'fold': fold[i],
                'sequence': sequences[i],
            } for i in range(len(fold))])
            
            stages = stage_1 + stage_2 + stage_3 + stage_4
            self.env['project.project'].create({
                'name': 'Airlines',
                'description': 'Maintenance of airlines',
                'type_ids': [Command.link(stage_id) for stage_id in stages.ids],
            })

        for rec in self:
            task_1 = self.env['project.task'].create({
                'name': f'Maintainance for {rec.name}',
                'project_id': self.env['project.project'].search([('name', '=', 'Airlines')]).id,
                'milestone_id': 1,
                'planned_date_begin': datetime.today(),
                'planned_date_end': datetime.today() + relativedelta(hours=1),
                'airline_id': rec.id,
            })



        return super().action_maintenance()
