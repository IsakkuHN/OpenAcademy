# -*- coding: utf-8 -*-

from string import digits
from odoo import models, fields, api


class open_academy(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    name = fields.Char(string='Session')
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(5,2))
    description = fields.Text(string='Description')
    cupos = fields.Integer(string='Numero de cupos de la sesion')
    instructor_id = fields.Many2one('res.partner', ondelete="set null", string='Instructor')
    course_id= fields.Many2one('open_academy.course', required=True, string='Curso_Id')
    attendee_id= fields.Many2many('res.partner', strings='Attendees')