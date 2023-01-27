# -*- coding: utf-8 -*-
from odoo import api, fields, models, Command, _


class projectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"
    _description = "Inherit Project"

    kanban_state = fields.Selection([
        ('normal', 'In Progress'),
        ('done', 'Ready'),
        ('blocked', 'Blocked')], string='Status',
        copy=False, default='normal', required=True)

    def _get_default_stage_id(self):
        project_id = self.env['project.project'].search([('name', '=', 'Airlines')]).id
        if not project_id:
            return False
        print('wdfdvf')

        return self.stage_find(project_id, [('name', '=', 'Done')])

    @api.depends('kanban_state')
    def write(self, vals):
        res = super().write(vals)
        print(vals)
        if 'stage_id' in vals:
            if vals['kanban_state'] == 'done':
                print(vals['kanban_state'])
            self.stage_id_change()
        if 'kanban_state' in vals:
            self.env['project.task'].search([('id', '=', self.id)]).kanban_state_change()
        stage_id = self._get_default_stage_id()
        # if vals['kanban_state'] == 'done':
        #     print("hel",self.id)
        return res

    
    def stage_id_change(self):
        stage_id = self._get_default_stage_id()
        print(stage_id)
        pass

    def kanban_state_change(self):
        # your code here
        print("sd",self.id)
        pass