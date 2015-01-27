# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
import openerp.tools
import re
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

class project_scrum_sprint(models.Model):
    _name = 'project.scrum.sprint'
    _description = 'Project Scrum Sprint'
    _order = 'date_start desc'
    def _compute(self):
        self.progress = 42.0

    name = fields.Char('Sprint Name', required=True, size=64),
    date_start = fields.Date('Starting Date', required=True),
    date_stop = fields.Date('Ending Date', required=True),
    project_id = fields.Many2one('project.project', 'Project', required=True, domain=[('scrum','=',1)], help="If you have [?] in the project name, it means there are no analytic account linked to this project."),
    product_owner_id = fields.Many2one('res.users', 'Product Owner', required=True,help="The person who is responsible for the product"),
    scrum_master_id = fields.Many2one('res.users', 'Scrum Master', required=True,help="The person who is maintains the processes for the product"),
    # meeting_ids = fields.One2many('project.scrum.meeting', 'sprint_id', 'Daily Scrum'),
    review = fields.Text('Sprint Review'),
    retrospective = fields.Text('Sprint Retrospective'),
    # backlog_ids = fields.One2many('project.scrum.product.backlog', 'sprint_id', 'Sprint Backlog'),
    progress = fields.Float(compute="_compute", group_operator="avg", type='float', multi="progress", string='Progress (0-100)', help="Computed as: Time Spent / Total Time."),
    effective_hours = fields.Function(_compute, multi="effective_hours", string='Effective hours', help="Computed using the sum of the task work done."),
    expected_hours = fields.Function(_compute, multi="expected_hours", string='Planned Hours', help='Estimated time to do the task.'),
    state = fields.Selection([('draft','Draft'),('open','Open'),('pending','Pending'),('cancel','Cancelled'),('done','Done')], 'State', required=True, default = 'draft'),

