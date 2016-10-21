# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################


from openerp.osv import osv, fields


class mail_compose_message(osv.TransientModel):
    _inherit = 'mail.compose.message'

    _columns = {
        'note_id': fields.Many2one('note.note'),
#        'fwd_message': fields.boolean('Forward Message'),
    }
    _defaults = {
    }
    def get_record_data(self, cr, uid, values, context=None):
        if context is None:
            context = {}
        result = super(mail_compose_message,
                       self).get_record_data(cr, uid, values=values,
                                             context=context)
        if context.get('default_subject'):
            result['subject'] = context.get('default_subject')
        return result
