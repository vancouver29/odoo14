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

from odoo import api, fields, models, exceptions


class Course(models.Model):
    _name = "openacademy.course"
    _description = "OpenAcademy Courses"

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', string="Responsible", ondelete='set null', index=True)
    sessions_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description!"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique!"),
    ]


class Session(models.Model):
    _name = "openacademy.session"
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string='instructor')
    course_id = fields.Many2one('openacademy.course', string='Course', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    active = fields.Boolean(default=True)

    taken_seats = fields.Float(string="Taken seats percent", compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats


    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats can not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can not be an attendee!")

