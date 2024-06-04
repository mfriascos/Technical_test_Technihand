# -*- coding: utf-8 -*-
# from odoo import http


# class GitRepo(http.Controller):
#     @http.route('/git_repo/git_repo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/git_repo/git_repo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('git_repo.listing', {
#             'root': '/git_repo/git_repo',
#             'objects': http.request.env['git_repo.git_repo'].search([]),
#         })

#     @http.route('/git_repo/git_repo/objects/<model("git_repo.git_repo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('git_repo.object', {
#             'object': obj
#         })
