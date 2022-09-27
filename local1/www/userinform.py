from dataclasses import fields
import frappe

listuser = []
def get_context(context):
        for info in listuser:
                context.users = info
        listuser.clear()


@frappe.whitelist()
def userData(data):
        global all
        data = frappe.db.get_list("Registration",filters={'email':data},fields=["photo","firstname","lastname","fullname","dateofbirth","mobilenumber","gender","city","state","email","address","signature"])
        listuser.append(data)
        