from dataclasses import fields
import frappe


# def get_context(context):
#     context.users = frappe.get_list("Registration", fields=["firstname","lastname","fullname","dateofbirth","mobilenumber","gender","city","state","email","address"])

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
        