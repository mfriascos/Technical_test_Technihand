from odoo import http
from odoo.http import request
import requests


class RepositoryController(http.Controller):

    @http.route('/api/commits', type='json', auth='user', methods=['GET'])
    def get_commits(self, repository_id):
        repository = request.env['repository'].sudo().browse(repository_id)
        if not repository:
            return {'error': 'Repository not found'}

        owner_repo = repository.link.replace("https://github.com/", "")
        api_url = f"https://api.github.com/repos/{owner_repo}/commits"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            commits_data = response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

        extracted_commits = []
        for commit in commits_data:
            extracted_commits.append({
                'repo_name': repository.name,
                'commit_hash': commit.get('sha'),
                'date': commit.get('commit').get('author').get('date'),
                'message': commit.get('commit').get('message'),
                'url': commit.get('html_url')
            })

        return extracted_commits
