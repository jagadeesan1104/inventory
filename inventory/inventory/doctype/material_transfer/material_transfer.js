// Copyright (c) 2023, Jagadeesan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Material Transfer', {

	//while enter the qty field will show the previous source and target warehouse qty
	qty(frm) {		
			frm.call('get_previous_warehouse_qty').then((r)=>{
				$.each(r.message,function(i,v){
					if(frm.doc.qty > 0){
						frm.add_child('warehouse_qty',{
							'product':frm.doc.product,
							'source_warehouse':frm.doc.source_warehouse,
							'source_open_qty':v.source_warehouse_open_qty,
							'source_balance_qty':v.source_warehouse_balance_qty,
							'target_warehouse':frm.doc.target_warehouse,
							'target_open_qty':v.target_warehouse_open_qty,
							'target_balance_qty':v.target_warehouse_balance_qty
						})
					}
					else{
						frm.clear_table('warehouse_qty')
					}
				})
				frm.refresh_field('warehouse_qty')
			})
	},
	refresh:function(frm){
		frm.fields_dict['warehouse_qty'].grid.wrapper.find('.grid-add-row').remove(); 	
	}
});
