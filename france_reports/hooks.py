# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "france_reports"
app_title = "France Reports"
app_publisher = "DOKOS"
app_description = "Legal Reports for France"
app_icon = "octicon octicon-diff"
app_color = "#c5cae9"
app_email = "hello@dokos.io"
app_license = "GPLv3"

fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/france_reports/css/france_reports.css"
# app_include_js = "/assets/france_reports/js/france_reports.js"

# include js, css files in header of web template
# web_include_css = "/assets/france_reports/css/france_reports.css"
# web_include_js = "/assets/france_reports/js/france_reports.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "france_reports.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "france_reports.install.before_install"
# after_install = "france_reports.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "france_reports.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"france_reports.tasks.all"
# 	],
# 	"daily": [
# 		"france_reports.tasks.daily"
# 	],
# 	"hourly": [
# 		"france_reports.tasks.hourly"
# 	],
# 	"weekly": [
# 		"france_reports.tasks.weekly"
# 	]
# 	"monthly": [
# 		"france_reports.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "france_reports.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "france_reports.event.get_events"
# }

