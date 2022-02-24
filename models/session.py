# -*- coding: utf-8 -*-

from asyncio import exceptions
from email.policy import default
from string import digits
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


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
    fecha_final = fields.Date(string="Fecha final", store=True, compute='_obtener_fecha_final', inverse='_establecer_fecha_final')
    asistentes_curso = fields.Integer(string="Cantidad de alumnos", compute='_num_asistentes_curso', store = True)

    #Porcentaje de los asientos ocupados
    @api.depends('cupos','attendee_id')
    def _asistencia(self):
        for i in self:
            if not i.cupos:
                i.asistencia = 0.0
            else:
                i.asistencia = 100.0*len(i.attendee_id)/i.cupos

    #Onchange 
    @api.onchange('cupos','attendee_id')
    def _validar_cupos(self):
        if self.cupos < 0:
            return {
                'warning':{
                    'title':"Valor de cupos incorrecto",
                    'message':"El numero de cupos de la sesion no puede ser negativo"
                }
            }
        if self.cupos < len(self.attendee_id):
            return {
                'warning':{
                    'title':"Lista de asistentes completa",
                    'message':"El numero de asistentes de la sesion excede los cupos de la misma"
                }
            }

    #Revisar la lista de asistentes
    @api.constrains('attendee_id','instructor_id')
    def _validar_asistentes(self):
        for record in self.attendee_id:
            if record == self.instructor_id:
                raise ValidationError("Un instructor no puede formar parte de la lista de asistentes")

    @api.depends('duration', 'start_date')
    def _obtener_fecha_final(self):
        for record in self:
            if not(record.start_date and record.duration):
                record.fecha_final = record.start_date
                continue
            comienzo = fields.Datetime.from_string(record.start_date)
            duracion = timedelta(days=record.duration, seconds=-1)
            record.fecha_final = comienzo + duracion
    
    def _establecer_fecha_final(self):
        for record in self:
            if not (record.start_date and record.fecha_final):
                continue

            fecha_inicial = fields.Datetime.from_string(record.start_date)
            fecha_final = fields.Datetime.from_string(record.fecha_final)
            record.duration = (fecha_final-fecha_inicial).days + 1

    @api.depends('attendee_id')
    def _num_asistentes_curso(self):
        for i in self:
            i.asistentes_curso = len(i.attendee_id)