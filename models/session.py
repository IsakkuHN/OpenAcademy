# -*- coding: utf-8 -*-

from email.policy import default
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
    instructor_id = fields.Many2one('res.partner', ondelete="set null", string='Instructor', domain=['|',('instructor', '=', True),
                                                                                                            ('category_id.name','ilike',"Teacher")])
    course_id= fields.Many2one('open_academy.course', required=True, string='Curso_Id')
    attendee_id= fields.Many2many('res.partner', strings='Attendees')
    activo= fields.Boolean(default=True)

    asistencia = fields.Float(string="Cupos ocupados", compute='_asistencia')

    #Porcentaje de los asientos ocupados
    @api.depends('cupos','attendee_id')
    def _asistencia(self):
        for i in self:
            if not i.cupos:
                i.asistencia = 0.0
            else:
                i.asistencia = 100.0*len(i.attendee_id)/i.cupos
    