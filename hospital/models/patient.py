from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Holds info about individual patient'

    name = fields.Char(string="Name" , required = True)
    age =fields.Char(string='Age')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other',"Other")
    ], required = True, default='male')
    note = fields.Text(string='Description')
