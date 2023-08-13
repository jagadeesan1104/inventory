// Copyright (c) 2023, Jagadeesan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product', {
	product_code(frm) {
		if (frm.doc.product_code) {
			var product_id = frm.doc.product_code;
			var change_upper_case = product_id.toUpperCase();
			frm.set_value('product_code', change_upper_case);
		}
	},
	product_name(frm) {
		if (frm.doc.product_name) {
			var item_name = frm.doc.product_name;
			var change_upper_case = item_name.toUpperCase();
			frm.set_value('product_name', change_upper_case);
		}
	},
});
