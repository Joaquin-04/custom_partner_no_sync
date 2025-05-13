from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _commercial_fields(self):
        return ['company_registry', 'industry_id']  # Solo estos campos se comportarán como comerciales

    """
    @api.model
    def _address_fields(self):
        "Campos de dirección que no sincronizaremos"
        return []  # Lista vacía desactiva sincronización

    def _fields_sync(self, values):
        "Desactiva toda sincronización automática"
        # 1. Comportamiento base sin lógica de sincronización
        return  

    @api.onchange('parent_id')
    def onchange_parent_id(self):
        "Elimina autocompletado de dirección"
        return {}
    """


    