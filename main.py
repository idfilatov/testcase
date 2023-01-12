import requests
import os
from datetime import datetime

import secret


def get_repo_details(repo, token):
	r = requests.get(
		f'https://api.github.com/repos/{repo}',
		headers={'Authorization': f'Bearer {token}'} if token else None
	)
	details = r.json()

	return details


def get_all_paged_items(repo, token, items_type, state='all'):
	all_items = []

	# через апи посчитаются вилки только первого уровня вложенности
	# а вилки вилок считаются на github.com
	# (апи вернет меньше чем на сайте)

	# через апи issues с ключом state=all вернутся те, которых нет на github.com
	# (апи вернет больше чем на сайте)

	page = 1
	while True:
		r = requests.get(
			f'https://api.github.com/repos/{repo}/{items_type}?state={state}&per_page=100&page={page}',
			headers={'Authorization': f'Bearer {token}'} if token else None
		)
		items = r.json()
		all_items += items
		amount_of_items_per_page = len(items)

		page += 1
		if amount_of_items_per_page == 0:
			break

	return all_items


def calc_pr_age_in_days(pr, check_datetime=datetime.now()):
	pr_created_at = pr.get('created_at', '0001-01-01T01:01:01Z')
	dt = datetime.fromisoformat(pr_created_at[:-1])
	delta_in_days = (check_datetime - dt).days

	return delta_in_days


def get_all_pr_older_than_two_weeks(repo, token):
	all_opened_pr = get_all_paged_items(repo, token, 'pulls', state='open')
	filtered_pr = [pr for pr in all_opened_pr if calc_pr_age_in_days(pr) >= 14]

	return filtered_pr


if __name__ == '__main__':

	# repo = 'NVIDIA/nvidia-docker'
	# repo = 'torvalds/linux'
	repo = 'yakimka/python_interview_questions'

	token = secret.token

	# print(os.path.dirname(os.path.abspath(__file__)))

	details = get_repo_details(repo, token)
	print(f'{repo} repo details:')
	print(details)

	token = None

	# print(os.path.dirname(os.path.abspath(__file__)))

	details = get_repo_details(repo, token)
	print(f'{repo} repo details without token:')
	print(details)

	# all_pr = get_all_paged_items(repo, token, 'pulls')
	# print(f'{repo} repo have {len(all_pr)} pull request (both open and closed)')
	
	# all_pr_older_than_two_weeks = get_all_pr_older_than_two_weeks(repo, token)
	# print(f'{repo} repo have {len(all_pr_older_than_two_weeks)} open pull request older than 2 weeks')

	# issues = get_all_paged_items(repo, token, 'issues')
	# print(f'{repo} repo have {len(issues)} issues')

	# forks = get_all_paged_items(repo, token, 'forks')
	# print(f'{repo} repo have {len(forks)} forks')