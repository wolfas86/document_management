from odoo import models, fields, api

class DocumentReportWizard(models.TransientModel):
    _name = 'document.report.wizard'
    _description = 'Document Report Wizard'

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def generate_report(self):
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to
        }
        return self.env.ref('document_management.document_report_action').report_action(self, data=data)
