from odoo import models, fields

class DocumentManagement(models.Model):
    _name = 'document.management'
    _description = 'Dokumentų valdymas'

    name = fields.Char('Pavadinimas', required=True)
    description = fields.Text('Aprašymas')
    company_id = fields.Many2one('res.company', string='Įmonė')
