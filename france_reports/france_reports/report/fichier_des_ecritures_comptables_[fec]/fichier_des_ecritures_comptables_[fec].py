# Copyright (c) 2017, DOKOS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import format_datetime
from frappe import _
from erpnext.accounts.utils import get_account_currency
import re

def execute(filters=None):
        account_details = {}
        for acc in frappe.db.sql("""select name, is_group from tabAccount""", as_dict=1):
                account_details.setdefault(acc.name, acc)

        validate_filters(filters, account_details)

        filters = set_account_currency(filters)

        columns = get_columns(filters)

        res = get_result(filters)

        return columns, res

def validate_filters(filters, account_details):
        if not filters.get('company'):
                frappe.throw(_('{0} is mandatory').format(_('Company')))
                
        if not filters.get('fiscal_year'):
                frappe.throw(_('{0} is mandatory').format(_('Fiscal Year')))

def set_account_currency(filters):

        filters["company_currency"] = frappe.db.get_value("Company", filters.company, "default_currency")
        account_currency = None

        return filters

def get_columns(filters):
	columns = [
		"JournalCode" + ":Link/Againts Voucher:90", "JournalLib" + ":Link/Against Voucher Type:90",
		"EcritureNum" + ":Dynamic Link:90", "EcritureDate" + "::90",
                "CompteNum" + ":Link/Account:100", "CompteLib" + ":Link/Account:200",
                "CompAuxNum" + "::90", "CompAuxLib" + "::90",
                "PieceRef" + "::90", "PieceDate" + "::90",
                "EcritureLib" + "::90", "Debit" + "::90", "Credit" + "::90",
                "EcritureLet" + "::90", "DateLet" + "::90", "ValidDate" + "::90",
                "Montantdevise" + "::90", "Idevise" + "::90"
	]

        return columns

def get_result(filters):
	gl_entries = get_gl_entries(filters)

        result = get_result_as_list(gl_entries, filters)
        
	return result

def get_gl_entries(filters):

	group_by_condition = "group by voucher_type, voucher_no, account" \
		if filters.get("group_by_voucher") else "group by gl.name"

	gl_entries = frappe.db.sql("""
		select
			gl.posting_date as GlPostDate, gl.account, gl.transaction_date, 
			sum(gl.debit) as debit, sum(gl.credit) as credit,
                        sum(gl.debit_in_account_currency) as debitCurr, sum(gl.credit_in_account_currency) as creditCurr,
			gl.voucher_type, gl.voucher_no, gl.against_voucher_type, 
                        gl.against_voucher, gl.account_currency, gl.against, 
                        gl.party_type, gl.party,
                        inv.name as InvName, inv.posting_date as InvPostDate, 
                        pur.name as PurName, inv.posting_date as PurPostDate,
                        jnl.cheque_no as JnlRef, jnl.posting_date as JnlPostDate,
                        pay.name as PayName, pay.posting_date as PayPostDate,
                        cus.customer_name, cus.name as cusName,
                        sup.supplier_name, sup.name as supName
 
		from `tabGL Entry` gl 
                    left join `tabSales Invoice` inv on gl.against_voucher = inv.name
                    left join `tabPurchase Invoice` pur on gl.against_voucher = pur.name
                    left join `tabJournal Entry` jnl on gl.against_voucher = jnl.name
                    left join `tabPayment Entry` pay on gl.against_voucher = pay.name
                    left join `tabCustomer` cus on gl.party = cus.customer_name
                    left join `tabSupplier` sup on gl.party = sup.supplier_name
		where gl.company=%(company)s and gl.fiscal_year=%(fiscal_year)s
		{group_by_condition}
		order by GlPostDate, voucher_no"""\
		.format(group_by_condition=group_by_condition), filters, as_dict=1)

	return gl_entries


def get_result_as_list(data, filters):
	result = []

        company_currency = frappe.db.get_value("Company", filters.company, "default_currency")
        
	for d in data:

                JournalCode = re.split("-|/", d.get("voucher_no"))[0]

                EcritureNum = re.split("-|/", d.get("voucher_no"))[1]

                EcritureDate = format_datetime(d.get("GlPostDate"), "yyyyMMdd")

                CompteNum = d.get("account").split("-")[0]

                if d.get("party_type") == "Customer":
                        CompAuxNum = d.get("cusName")
                        CompAuxLib = d.get("customer_name")
                        
                elif d.get("party_type") == "Supplier":
                        CompAuxNum = d.get("supName")
                        CompAuxLib = d.get("supplier_name")

                else:
                        CompAuxNum = ""
                        CompAuxLib = ""

                ValidDate = format_datetime(d.get("GlPostDate"), "yyyyMMdd")
                
                if d.get("against_voucher_type") == "Sales Invoice":
                        PieceRef = d.get("InvName")
                        PieceDate = format_datetime(d.get("InvPostDate"), "yyyyMMdd")

                elif d.get("against_voucher_type") == "Purchase Invoice":
                        PieceRef = d.get("PurName")
                        PieceDate = format_datetime(d.get("PurPostDate"), "yyyyMMdd")
                        
                elif d.get("against_voucher_type") == "Journal Entry":
                        PieceRef = d.get("JnlRef")
                        PieceDate = format_datetime(d.get("JnlPostDate"), "yyyyMMdd")

                elif d.get("against_voucher_type") == "Payment Entry":
                        PieceRef = d.get("PayName")
                        PieceDate = format_datetime(d.get("PayPostDate"), "yyyyMMdd")

                else:
                        PieceRef = "Aucune Reference"
                        PieceDate = format_datetime(d.get("GlPostDate"), "yyyyMMdd")

                Idevise = d.get("account_currency")

                if Idevise != company_currency:
                        Montantdevise = d.get("debitCurr") \
                                        if d.get("debitCurr") != 0 else d.get("creditCurr")
                else:
                        Montantdevise = d.get("debit") \
                                        if d.get("debit") != 0 else d.get("credit")

                row = [JournalCode, d.get("voucher_type"), EcritureNum, EcritureDate, CompteNum, d.get("account"), CompAuxNum , CompAuxLib , PieceRef, PieceDate, d.get("voucher_no"), d.get("debit"), d.get("credit"), "", "", ValidDate, Montantdevise, Idevise ]

		result.append(row)

	return result
