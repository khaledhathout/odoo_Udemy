from odoo import models, fields, api


class MyOrdersItems(models.Model):
    _name = 'my.orders.items'
    _description = 'Empty Empty Empty Empty Empty Empty Empty Empty '

    itemName = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
