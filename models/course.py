# -*- coding: utf-8 -*-

from odoo import models, fields


class open_academy(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'

    name = fields.Char(string='Course')
    title = fields.Char(string='Title')
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsable')
    session_id = fields.One2many('open_academy.session', 'course_id', string="Sessions")
