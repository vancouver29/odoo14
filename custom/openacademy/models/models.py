# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# class openacademy1(models.Model):
#     _name = 'openacademy1.openacademy1'
#     _description = 'openacademy1.openacademy1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api, fields, models


class Course(models.Model):
    _name = "openacademy.course"
    _description = "OpenAcademy Courses"

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', string="Responsible", ondelete='set null', index=True)
    sessions_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")


class Session(models.Model):
    _name = "openacademy.session"
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string='instructor')
    course_id = fields.Many2one('openacademy.course', string='Course', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
