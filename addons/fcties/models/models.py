# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FctiesAlumno(models.Model):
    _name = 'fcties.alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    curso_academico = fields.Selection([
        ('18/19', '18/19'),
        ('19/20', '19/20'),
        ('20/21', '20/21'),
        ('21/22', '21/22'),
        ('22/23', '22/23'),
        ('23/24', '23/24'),
        ('24/25', '24/25'),
        ('25/26', '25/26'),
        ('26/27', '26/27'),
    ], string='Curso Academico', required=True)
    email = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    ciclo_formativo = fields.Selection([
        ('DAM', 'DAM'),
        ('DAW', 'DAW'),
        ('ASIR', 'ASIR'),
    ], string='Ciclo Formativo', required=True)
    periodo_practica = fields.Selection([
        ('abril', 'Abril'),
        ('septiembre', 'Septiembre'),
    ], string='Periodo de Práctica', required=True)
    nota_media = fields.Float(string='Nota Media', required=True)
    nota_media_texto = fields.Char(string='Nota Media en Texto', compute='_compute_nota_media_texto')
    empresapracticas = fields.Many2one('fcties.empresa', string='Empresa donde ha hecho las practicas', required=True)


    @api.depends('nota_media')
    def _compute_nota_media_texto(self):
        for alumno in self:
            if 5 <= alumno.nota_media < 7:
                alumno.nota_media_texto = 'Aprobado'
            elif 7 <= alumno.nota_media < 9:
                alumno.nota_media_texto = 'Notable'
            elif 9 <= alumno.nota_media <= 10:
                alumno.nota_media_texto = 'Sobresaliente'
            else:
                alumno.nota_media_texto = 'Suspendido'


class FctiesEmpresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa'

    name = fields.Char(string='Nombre', required=True)
    persona_contacto = fields.Char(string='Persona de Contacto', required=True)
    telefono_contacto = fields.Char(string='Teléfono de Contacto', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    direccion = fields.Text(string='Dirección')
    alumno = fields.One2many('fcties.alumno','empresapracticas', string='Alumnos')

