import frappe

def discount(doc,method):
	if doc.grand_total>=500:
		doc.rounded_total = doc.rounded_total - 50
		doc.rounding_adjustment = 50
		frappe.msgprint("Hey you got RS.50 disccount on your purchase.Plese check your Rounding adjustment")