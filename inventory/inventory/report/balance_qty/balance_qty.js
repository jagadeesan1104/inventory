// Copyright (c) 2023, Jagadeesan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Balance Qty"] = {
	"filters": [
		{
			"fieldname":"warehouse",
			"label": __("Select Warehouse"),
			"fieldtype": "Link",
			"options": "Warehouse",
		},
		{
			"fieldname":"product",
			"label": __("Select Product"),
			"fieldtype": "Link",
			"options": "Product",
		},

	]
};
