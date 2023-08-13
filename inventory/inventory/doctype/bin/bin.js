// Copyright (c) 2023, Jagadeesan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bin', {
	opening_qty(frm) {
		if(frm.doc.opening_qty){
			frm.set_value('balance_qty',frm.doc.opening_qty)
		}

	}
});
