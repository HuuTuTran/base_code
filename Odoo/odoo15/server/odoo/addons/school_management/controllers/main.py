import werkzeug.utils
from odoo import http
import werkzeug
from odoo.http import request
import json
class MainControllers(http.Controller):
    @http.route('/my-controller', auth='public')
    def my_controller(self, **kwargs):
        return "Hello from my controller!"
    @http.route('/my-controller/<int:id>', auth='user',type='http')
    def get(self, id):
        return f"The ID is {id}" 
    @http.route('/redirects/<string:url>', auth='user',type='http')
    def redirects(self, url):
        return werkzeug.utils.redirect(url)
    
    @http.route(["/get_all_students"],type="http",auth="user")    
    def get_all_students(self):
        lst = []
        record = request.env['school_management.students'].search([])
        for row in record:
            s = {'student':{}}
            s['student']['name']= row.name
            s['student']['email'] = row.email
            lst.append(s)
            print(row.name,row.email)
        # print(record)
        return json.dumps(lst)     
