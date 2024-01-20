# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lapeliculera_genero(models.Model):
    _name = 'lapeliculera.genero'
    _description = 'Genero cinematografico'
    name = fields.Char(String='Genero', required=True, help="Introduce el genero cinematografico")
    comentario = fields.Text(string='Comentarios')
    pelicula = fields.One2many('lapeliculera.pelicula', 'genero', string='Peliculas')

class lapeliculera_pelicula(models.Model):
    _name = 'lapeliculera.pelicula'
    _description = 'Pelicula'
    name = fields.Char(string='Titulo', required=True, help="Titulo de la pelicula")
    director = fields.Char(string='Director', required=True, help="Introduce el director")
    color = fields.Boolean(string='Color')
    duration = fields.Integer(string='Duracion en minutos')
    industria = fields.Selection([('0', 'Hollywood'), ('1', 'Europa'), ('2', 'Bollywood'), ('3', 'Otros')],default='1', string='Industria')
    fecha = fields.Date(string='Fecha de estreno en España')
    sinopsis = fields.Char(string='Sinopsis')
    genero = fields.Many2one('lapeliculera.genero', string='Genero', required=True)