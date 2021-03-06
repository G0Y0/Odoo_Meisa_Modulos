# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class herencia_res_partner(models.Model): 
    _inherit = "res.partner" 
    codigo = fields.Integer(string='codigo', required=True) 
 
    fecha_alta = fields.Datetime(string='fecha_alta', required=True) 
 
    fecha_baja = fields.Datetime(string='fecha_baja', required=False) 
 
    fecha_evaluacion = fields.Datetime(string='fecha_evaluacion', required=False) 
 
    numero_incidencias = fields.Integer(string='numero_incidencias', required=True)
  
    x_clasificacion = fields.Selection([('historico', 'Historico'),('provisional','Provisional'),('certificado','Certificado')])

    x_incidencias_historico = fields.Integer(string='Numero de incidencias totales', required=True)

    x_fecha_inicio = fields.Datetime(string='Fecha de inicio', required=True) 

    x_fecha_fin = fields.Datetime(string='Fecha de expiracion', required=False)

    x_razon_social = fields.Char(string='Razon social', required=False)

    x_codigo_contable = fields.Integer(string='Codigo contable', required=False) 
   

    @api.onchange('active')
    def cambiar_fecha_baja(self):
        self.fecha_baja = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @api.one
    def toggle_active(self):
        if self.active:
            self.fecha_baja = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.active = False
        else:
           self.fecha_baja = ''
           self.active = True
