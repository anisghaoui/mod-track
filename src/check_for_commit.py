import os.path as osp


def load_track_list(path="./track_list.txt"):
    with open(path, 'r') as file:
        track_list = file.readlines()
        return track_list


def check_for_commit(repo_url: str):
    TOKEN = ""
    req = f'curl - L \
        - H "Accept: application/vnd.github+json" \
        - H "Authorization: Bearer {TOKEN}" \
        - H "X-GitHub-Api-Version: 2022-11-28" \
        https://api.github.com/repos/{OWNER}/{REPO}/commits/'
    import requests

    json_data = {
        'text': 'Hello, World!',
    }

    response = requests.post(
        'https://hooks.slack.com/services/asdfasdfasdf', json=json_data)
    pass


if __name__ == "__main__":
    track_list = load_track_list()
    repository = track_list[0]
    check_for_commit(repository)
