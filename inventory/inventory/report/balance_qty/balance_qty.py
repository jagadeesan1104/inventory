# Copyright (c) 2023, Jagadeesan and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint


def execute(filters=None):
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters):
    columns = [
        _('Product') +":Link/Product:150",_('Warehouse') + ":Link/Warehouse:150",_('Opening Qty') + ":Data:150",_('Balance Qty') + ":Data:150"
        
    ]
    return columns

def get_data(filters):
    data = []
    if(filters.warehouse):
        bin = frappe.db.get_all('Bin',{'docstatus':0,'warehouse':filters.warehouse},['*'])
        for item_bin in bin:
            row = [item_bin.product,item_bin.warehouse,item_bin.opening_qty,item_bin.balance_qty]
            data.append(row)
    elif (filters.product):   
        bin = frappe.db.get_all('Bin',{'docstatus':0,'product':filters.product},['*'])
        for item_bin in bin:
            row = [item_bin.product,item_bin.warehouse,item_bin.opening_qty,item_bin.balance_qty]
            data.append(row)
    else:
        bin = frappe.db.get_all('Bin',{'docstatus':0},['*'])
        for item_bin in bin:
            row = [item_bin.product,item_bin.warehouse,item_bin.opening_qty,item_bin.balance_qty]
            data.append(row)           
    return data