# Copyright (c) 2023, Jagadeesan and contributors
# For license information, please see license.txt

import frappe
from frappe import _

from frappe.model.document import Document

class Bin(Document):
	def validate(self):
		if frappe.db.exists('Bin',{'product':self.product,'warehouse':self.warehouse}):
			frappe.throw(_('Already same Warehouse and Product has been Created '))
