from os import path
from urllib import parse

from git import Repo
from github import Github
import requests


directory = path.realpath(path.curdir)


def create_local_repo(origin_url):
    repo = Repo.init(directory)
    origin = repo.create_remote('{{ cookiecutter.github_username }}', origin_url)
    git = repo.git
    git.add('-A')
    git.commit('-am', 'initial')
    git.push('-u', 'ptpb', 'master')


def create_remote_repo():
    github = Github('{{ cookiecutter.email }}', '{{ cookiecutter.github_token }}')
    org = github.get_organization('{{ cookiecutter.github_username }}')
    repo = org.create_repo('{{ cookiecutter.project_slug }}')
    return repo.ssh_url


def follow_circleci():
    circle_base_url = 'https://circleci.com/api/v1.1/'
    uri = 'project/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/follow?circle-token={{ cookiecutter.circleci_token }}'

    url = parse.urljoin(circle_base_url, uri)

    res = requests.post(url)
    assert res.ok


def main():
    url = create_remote_repo()
    create_local_repo(url)
    follow_circleci()


if __name__ == '__main__':
    main()
