# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _


class projectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"
    _description = "Inherit Project"


    airline_id = fields.Integer()

    kanban_state = fields.Selection([
        ('normal', 'In Progress'),
        ('done', 'Ready'),
        ('blocked', 'Blocked')], string='Status',
        copy=False, default='normal', required=True)

    def _get_default_stage_id(self,stage_id):
        project_id = self.env['project.project'].search([('name', '=', 'Airlines')]).id
        if not project_id:
            return False

        return self.stage_find(project_id, [('name', '=', stage_id)])

    def write(self, vals):
        res = super().write(vals)
        print(vals)
        if 'kanban_state' in vals:
            if vals['kanban_state'] == 'done':
                self.stage_id = self._get_default_stage_id('Done')
            if vals['kanban_state'] == 'blocked':
                self.stage_id = self._get_default_stage_id('Blocked')

        if 'stage_id' in vals:
            if vals['stage_id'] == self._get_default_stage_id('Done'):
                res = self.env['airline.airline'].browse(self.airline_id)
                res.state = 'ready'
        return res

