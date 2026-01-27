from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    custom_id = fields.Char(
        string="External Employee ID",
        index=True,
        help="Employee ID from external system"
    )

    def schedule_mapping(self):
        # Map attachments to employees using external ID

        Attachment = self.env['ir.attachment']
        Employee = self.env['hr.employee']
        Activity = self.env['mail.activity']

        attachments = Attachment.search([
            ('res_model', '=', 'hr.employee'),
            ('custom_id', '!=', False),
        ])

        activities = Activity.search([
            ('res_model', '=', 'hr.employee'),
            ('custom_id', '!=', False),
        ])

        mapped = 0
        skipped = 0

        for att in attachments:
            employee = Employee.search([
                ('custom_id', '=', att.custom_id)
            ], limit=1)

            if employee:
                att.write({
                    'res_id': employee.id
                })


        for act in activities:
            employee = Employee.search([
                ('custom_id', '=', act.custom_id)
            ], limit=1)

            if employee:
                act.write({
                    'res_id': employee.id
                })

class CRMLead(models.Model):
    _inherit = "crm.lead"

    custom_id = fields.Char(
        string="External Lead ID",
        index=True,
        help="Employee ID from external system"
    )

    def schedule_mapping(self):
        # Map attachments to employees using external ID

        Attachment = self.env['ir.attachment']
        Employee = self.env['crm.lead']
        Activity = self.env['mail.activity']

        attachments = Attachment.search([
            ('res_model', '=', 'crm.lead'),
            ('custom_id', '!=', False),
        ])

        activities = Activity.search([
            ('res_model', '=', 'crm.lead'),
            ('custom_id', '!=', False),
        ])

        mapped = 0
        skipped = 0

        for att in attachments:
            employee = Employee.search([
                ('custom_id', '=', att.custom_id)
            ], limit=1)

            if employee:
                att.write({
                    'res_id': employee.id
                })


        for act in activities:
            employee = Employee.search([
                ('custom_id', '=', act.custom_id)
            ], limit=1)

            if employee:
                act.write({
                    'res_id': employee.id
                })

class projectProject(models.Model):
    _inherit = "project.project"

    custom_id = fields.Char(
        string="External Project ID",
        index=True,
        help="Employee ID from external system"
    )

    def schedule_mapping(self):
        # Map attachments to employees using external ID

        Attachment = self.env['ir.attachment']
        Employee = self.env['project.project']
        Activity = self.env['mail.activity']

        attachments = Attachment.search([
            ('res_model', '=', 'project.project'),
            ('custom_id', '!=', False),
        ])

        activities = Activity.search([
            ('res_model', '=', 'project.project'),
            ('custom_id', '!=', False),
        ])

        mapped = 0
        skipped = 0

        for att in attachments:
            employee = Employee.search([
                ('custom_id', '=', att.custom_id)
            ], limit=1)

            if employee:
                att.write({
                    'res_id': employee.id
                })


        for act in activities:
            employee = Employee.search([
                ('custom_id', '=', act.custom_id)
            ], limit=1)

            if employee:
                act.write({
                    'res_id': employee.id
                })


class projectTask(models.Model):
    _inherit = "project.task"

    custom_id = fields.Char(
        string="External Task ID",
        index=True,
        help="Employee ID from external system"
    )

    def schedule_mapping(self):
        # Map attachments to employees using external ID

        Attachment = self.env['ir.attachment']
        Employee = self.env['project.task']
        Activity = self.env['mail.activity']

        attachments = Attachment.search([
            ('res_model', '=', 'project.task'),
            ('custom_id', '!=', False),
        ])

        activities = Activity.search([
            ('res_model', '=', 'project.task'),
            ('custom_id', '!=', False),
        ])

        mapped = 0
        skipped = 0

        for att in attachments:
            employee = Employee.search([
                ('custom_id', '=', att.custom_id)
            ], limit=1)

            if employee:
                att.write({
                    'res_id': employee.id
                })


        for act in activities:
            employee = Employee.search([
                ('custom_id', '=', act.custom_id)
            ], limit=1)

            if employee:
                act.write({
                    'res_id': employee.id
                })

class resPartner(models.Model):
    _inherit = "res.partner"

    custom_id = fields.Char(
        string="External partner ID",
        index=True,
        help="Employee ID from external system"
    )

    def schedule_mapping(self):
        # Map attachments to employees using external ID

        Attachment = self.env['ir.attachment']
        Employee = self.env['res.partner']
        Activity = self.env['mail.activity']

        attachments = Attachment.search([
            ('res_model', '=', 'res.partner'),
            ('custom_id', '!=', False),
        ])

        activities = Activity.search([
            ('res_model', '=', 'res.partner'),
            ('custom_id', '!=', False),
        ])

        mapped = 0
        skipped = 0

        for att in attachments:
            employee = Employee.search([
                ('custom_id', '=', att.custom_id)
            ], limit=1)

            if employee:
                att.write({
                    'res_id': employee.id
                })


        for act in activities:
            employee = Employee.search([
                ('custom_id', '=', act.custom_id)
            ], limit=1)

            if employee:
                act.write({
                    'res_id': employee.id
                })



class HrAttachment(models.Model):
    _inherit = "ir.attachment"

    custom_id = fields.Char(
        string="External Resource Model",
    )


class MailActivity(models.Model):
    _inherit = "mail.activity"

    custom_id = fields.Char(
        string="External Resource Model",
    )