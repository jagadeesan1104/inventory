# Copyright (c) 2023, Jagadeesan and contributors
# For license information, please see license.txt

from frappe import _
import frappe
from frappe.model.document import Document

class MaterialTransfer(Document):
    
    def on_submit(self):
        source_warehouse_qty = frappe.db.get_value('Bin',{'product':self.product,'warehouse':self.source_warehouse},['balance_qty'])
        target_warehouse_qty = frappe.db.get_value('Bin',{'product':self.product,'warehouse':self.target_warehouse},['balance_qty'])
        

        source_warehouse = (source_warehouse_qty or 0) - (self.qty or 0)
        target_warehouse = (target_warehouse_qty or 0) + (self.qty or 0)    

        frappe.db.set_value('Bin',{'warehouse':self.source_warehouse},"balance_qty",source_warehouse)
        frappe.db.set_value('Bin',{'warehouse':self.target_warehouse},"balance_qty",target_warehouse)


    #check whether the warehouse is created in Bin or not
    def validate(self):
        if not frappe.db.exists("Bin",{'warehouse':self.source_warehouse,"product":self.product}):
            frappe.throw(_('Please create a Bin for Source %s'%(self.source_warehouse)))

        elif not frappe.db.exists("Bin",{'warehouse':self.target_warehouse,"product":self.product}):
            frappe.throw(_('Please create a Bin for Source %s'%(self.target_warehouse)))


    #get the preivous source and target warehouse qty details
    @frappe.whitelist()
    def get_previous_warehouse_qty(self):
        datalist = []
        data = {}
        source_warehouse_open_qty = frappe.db.get_value('Bin',{'product':self.product,'warehouse':self.source_warehouse},['opening_qty'])
        target_warehouse_open_qty = frappe.db.get_value('Bin',{'product':self.product,'warehouse':self.target_warehouse},['opening_qty'])
        source_warehouse_balance_qty = frappe.db.get_value('Bin',{'product':self.product,'warehouse':self.source_warehouse},['balance_qty'])
        target_warehouse_balance_qty = frappe.db.get_value('Bin',{'product':self.product,'warehouse':self.target_warehouse},['balance_qty'])
        data.update({
            'source_warehouse_open_qty':source_warehouse_open_qty,
            'target_warehouse_open_qty':target_warehouse_open_qty,
            "source_warehouse_balance_qty":source_warehouse_balance_qty,
            "target_warehouse_balance_qty":target_warehouse_balance_qty
        })
        datalist.append(data.copy())
        return datalist