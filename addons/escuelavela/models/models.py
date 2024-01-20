# -*- coding: utf-8 -*-

from odoo import models, fields, api


class escuelavela_escuela(models.Model):
    _name = 'escuelavela.escuela'
    _description = 'Escuela'

    name = fields.Char(string='Nombre', required=True)
    logo = fields.Binary(string='Logotipo')
    email = fields.Char(string='Correo electronico')
    phone = fields.Char(string='Teléfono', required=True)
    address = fields.Text(string='Direccion', required=True)
    website = fields.Char(string='Sitio web')
    contact_person = fields.Char(string='Persona de contacto', required=True)

    @api.onchange('email')
    def _onchange_email(self):
        if self.email:
            self.email = self.email.lower()


class escuelavela_cursos(models.Model):
    _name = 'escuelavela.cursos'
    _description = 'Cursos'

    name = fields.Char(string='titulo', required=True)
    duracion = fields.Char(string='Duraccion del curso', required=True)
    horas = fields.Float(str='Horas', required=True)
    precio = fields.Float(string='precio del curso', required=True)


class escuelavela_monitores(models.Model):
    _name = 'escuelavela.monitores'
    _description = 'Monitores'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    codigo_monitor = fields.Char(string='Codigo monitor', required=True)
    telefono = fields.Char(string='Tlf Telefono', required=True)
    email = fields.Char(string='Email', required=True)
    colabora = fields.Many2one('escuelavela.escuela', string='Escuelas colaboradoras')

    @api.onchange('email')
    def _onchange_email(self):
        if self.email:
            self.email = self.email.lower()

    _sql_constraints = [
        ('codigo_monitor_unico', 'UNIQUE(codigo_monitor)', 'El codigo de monitor no se puede repetir'),
    ]


class escuelavela_alumno(models.Model):
    _name = 'escuelavela.alumno'
    _description = 'Alumnos'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    telefono = fields.Char(string='Telefono', required=True)
    email = fields.Char(string='Email', required=True)
    numero_matricula = fields.Char(string='Número de matrícula', required=True)
    escuela = fields.Many2one('escuelavela.escuela', string='Escuela')

    @api.onchange('email')
    def _onchange_email(self):
        if self.email:
            self.email = self.email.lower()