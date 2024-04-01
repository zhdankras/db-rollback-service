import os
import requests

params = {
    'token': os.environ.get('GITLAB_TOKEN'),
    'ref': 'main'
}

headers = {
    'PRIVATE-TOKEN': os.environ.get('PRIVATE_TOKEN')
}

def cleanup_and_migration_request():
    response = requests.post('https://gitlab.overhull.<YOUR_ORGANIZATION>.ru/api/v4/projects/26/trigger/pipeline', params=params)
    if response.status_code == 201:
        return response.json()
    else:
        return None
    
def get_status_pipeline(pipeline_id):
    response = requests.get(f'https://gitlab.overhull.<YOUR_ORGANIZATION>.ru/api/v4/projects/26/pipelines/{pipeline_id}', headers=headers)
    return response.json()
