from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class ControlRfid(models.Model):
    _name = 'control.rfid'
    _description = 'Table for Monitoring the rfid devices in UHF'

    name = fields.Text(required=True)
    uid = fields.Text()
    value = fields.Text()
    types = fields.Selection([('m6enano', 'M6e Nano'), ('geenfc', 'GEENFC')], required=True, default='m6enano')
