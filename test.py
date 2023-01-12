import unittest
import datetime

import secret
import main

repos_gt = {
	'NVIDIA/nvidia-docker': {
		'details':{
		    "id": 45557469,
		    "node_id": "MDEwOlJlcG9zaXRvcnk0NTU1NzQ2OQ==",
		    "name": "nvidia-docker",
		    "full_name": "NVIDIA/nvidia-docker",
		    "private": False,
		    "owner": {
		        "login": "NVIDIA",
		        "id": 1728152,
		        "node_id": "MDEyOk9yZ2FuaXphdGlvbjE3MjgxNTI=",
		        "avatar_url": "https://avatars.githubusercontent.com/u/1728152?v=4",
		        "gravatar_id": "",
		        "url": "https://api.github.com/users/NVIDIA",
		        "html_url": "https://github.com/NVIDIA",
		        "followers_url": "https://api.github.com/users/NVIDIA/followers",
		        "following_url": "https://api.github.com/users/NVIDIA/following{/other_user}",
		        "gists_url": "https://api.github.com/users/NVIDIA/gists{/gist_id}",
		        "starred_url": "https://api.github.com/users/NVIDIA/starred{/owner}{/repo}",
		        "subscriptions_url": "https://api.github.com/users/NVIDIA/subscriptions",
		        "organizations_url": "https://api.github.com/users/NVIDIA/orgs",
		        "repos_url": "https://api.github.com/users/NVIDIA/repos",
		        "events_url": "https://api.github.com/users/NVIDIA/events{/privacy}",
		        "received_events_url": "https://api.github.com/users/NVIDIA/received_events",
		        "type": "Organization",
		        "site_admin": False
		    },
		    "html_url": "https://github.com/NVIDIA/nvidia-docker",
		    "description": "Build and run Docker containers leveraging NVIDIA GPUs",
		    "fork": False,
		    "url": "https://api.github.com/repos/NVIDIA/nvidia-docker",
		    "forks_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/forks",
		    "keys_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/keys{/key_id}",
		    "collaborators_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/collaborators{/collaborator}",
		    "teams_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/teams",
		    "hooks_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/hooks",
		    "issue_events_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/issues/events{/number}",
		    "events_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/events",
		    "assignees_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/assignees{/user}",
		    "branches_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/branches{/branch}",
		    "tags_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/tags",
		    "blobs_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/git/blobs{/sha}",
		    "git_tags_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/git/tags{/sha}",
		    "git_refs_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/git/refs{/sha}",
		    "trees_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/git/trees{/sha}",
		    "statuses_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/statuses/{sha}",
		    "languages_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/languages",
		    "stargazers_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/stargazers",
		    "contributors_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/contributors",
		    "subscribers_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/subscribers",
		    "subscription_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/subscription",
		    "commits_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/commits{/sha}",
		    "git_commits_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/git/commits{/sha}",
		    "comments_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/comments{/number}",
		    "issue_comment_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/issues/comments{/number}",
		    "contents_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/contents/{+path}",
		    "compare_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/compare/{base}...{head}",
		    "merges_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/merges",
		    "archive_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/{archive_format}{/ref}",
		    "downloads_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/downloads",
		    "issues_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/issues{/number}",
		    "pulls_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/pulls{/number}",
		    "milestones_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/milestones{/number}",
		    "notifications_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/notifications{?since,all,participating}",
		    "labels_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/labels{/name}",
		    "releases_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/releases{/id}",
		    "deployments_url": "https://api.github.com/repos/NVIDIA/nvidia-docker/deployments",
		    "created_at": "2015-11-04T18:04:49Z",
		    "updated_at": "2023-01-12T08:36:18Z",
		    "pushed_at": "2023-01-10T14:14:24Z",
		    "git_url": "git://github.com/NVIDIA/nvidia-docker.git",
		    "ssh_url": "git@github.com:NVIDIA/nvidia-docker.git",
		    "clone_url": "https://github.com/NVIDIA/nvidia-docker.git",
		    "svn_url": "https://github.com/NVIDIA/nvidia-docker",
		    "homepage": "",
		    "size": 19852,
		    "stargazers_count": 15625,
		    "watchers_count": 15625,
		    "language": "Makefile",
		    "has_issues": True,
		    "has_projects": True,
		    "has_downloads": True,
		    "has_wiki": True,
		    "has_pages": True,
		    "has_discussions": False,
		    "forks_count": 2007,
		    "mirror_url": None,
		    "archived": False,
		    "disabled": False,
		    "open_issues_count": 262,
		    "license": {
		        "key": "apache-2.0",
		        "name": "Apache License 2.0",
		        "spdx_id": "Apache-2.0",
		        "url": "https://api.github.com/licenses/apache-2.0",
		        "node_id": "MDc6TGljZW5zZTI="
		    },
		    "allow_forking": True,
		    "is_template": False,
		    "web_commit_signoff_required": False,
		    "topics": [
		        "cuda",
		        "docker",
		        "gpu",
		        "nvidia-docker"
		    ],
		    "visibility": "public",
		    "forks": 2007,
		    "open_issues": 262,
		    "watchers": 15625,
		    "default_branch": "main",
		    "permissions": {
		        "admin": False,
		        "maintain": False,
		        "push": False,
		        "triage": False,
		        "pull": True
		    },
		    "temp_clone_token": "",
		    "organization": {
		        "login": "NVIDIA",
		        "id": 1728152,
		        "node_id": "MDEyOk9yZ2FuaXphdGlvbjE3MjgxNTI=",
		        "avatar_url": "https://avatars.githubusercontent.com/u/1728152?v=4",
		        "gravatar_id": "",
		        "url": "https://api.github.com/users/NVIDIA",
		        "html_url": "https://github.com/NVIDIA",
		        "followers_url": "https://api.github.com/users/NVIDIA/followers",
		        "following_url": "https://api.github.com/users/NVIDIA/following{/other_user}",
		        "gists_url": "https://api.github.com/users/NVIDIA/gists{/gist_id}",
		        "starred_url": "https://api.github.com/users/NVIDIA/starred{/owner}{/repo}",
		        "subscriptions_url": "https://api.github.com/users/NVIDIA/subscriptions",
		        "organizations_url": "https://api.github.com/users/NVIDIA/orgs",
		        "repos_url": "https://api.github.com/users/NVIDIA/repos",
		        "events_url": "https://api.github.com/users/NVIDIA/events{/privacy}",
		        "received_events_url": "https://api.github.com/users/NVIDIA/received_events",
		        "type": "Organization",
		        "site_admin": False
		    },
		    "network_count": 2007,
		    "subscribers_count": 438
		},
		'pull_requests_amount': 84,
		'pull_requests_filtered_amount': 0,
		'forks_amount': 1974,
		'issues_amount': 1704,
	},
	'yakimka/python_interview_questions':{
		'details':{
		    "id": 351877974,
		    "node_id": "MDEwOlJlcG9zaXRvcnkzNTE4Nzc5NzQ=",
		    "name": "python_interview_questions",
		    "full_name": "yakimka/python_interview_questions",
		    "private": False,
		    "owner": {
		        "login": "yakimka",
		        "id": 28621349,
		        "node_id": "MDQ6VXNlcjI4NjIxMzQ5",
		        "avatar_url": "https://avatars.githubusercontent.com/u/28621349?v=4",
		        "gravatar_id": "",
		        "url": "https://api.github.com/users/yakimka",
		        "html_url": "https://github.com/yakimka",
		        "followers_url": "https://api.github.com/users/yakimka/followers",
		        "following_url": "https://api.github.com/users/yakimka/following{/other_user}",
		        "gists_url": "https://api.github.com/users/yakimka/gists{/gist_id}",
		        "starred_url": "https://api.github.com/users/yakimka/starred{/owner}{/repo}",
		        "subscriptions_url": "https://api.github.com/users/yakimka/subscriptions",
		        "organizations_url": "https://api.github.com/users/yakimka/orgs",
		        "repos_url": "https://api.github.com/users/yakimka/repos",
		        "events_url": "https://api.github.com/users/yakimka/events{/privacy}",
		        "received_events_url": "https://api.github.com/users/yakimka/received_events",
		        "type": "User",
		        "site_admin": False
		    },
		    "html_url": "https://github.com/yakimka/python_interview_questions",
		    "description": "Вопросы для подготовки к интервью на позицию Python Developer",
		    "fork": False,
		    "url": "https://api.github.com/repos/yakimka/python_interview_questions",
		    "forks_url": "https://api.github.com/repos/yakimka/python_interview_questions/forks",
		    "keys_url": "https://api.github.com/repos/yakimka/python_interview_questions/keys{/key_id}",
		    "collaborators_url": "https://api.github.com/repos/yakimka/python_interview_questions/collaborators{/collaborator}",
		    "teams_url": "https://api.github.com/repos/yakimka/python_interview_questions/teams",
		    "hooks_url": "https://api.github.com/repos/yakimka/python_interview_questions/hooks",
		    "issue_events_url": "https://api.github.com/repos/yakimka/python_interview_questions/issues/events{/number}",
		    "events_url": "https://api.github.com/repos/yakimka/python_interview_questions/events",
		    "assignees_url": "https://api.github.com/repos/yakimka/python_interview_questions/assignees{/user}",
		    "branches_url": "https://api.github.com/repos/yakimka/python_interview_questions/branches{/branch}",
		    "tags_url": "https://api.github.com/repos/yakimka/python_interview_questions/tags",
		    "blobs_url": "https://api.github.com/repos/yakimka/python_interview_questions/git/blobs{/sha}",
		    "git_tags_url": "https://api.github.com/repos/yakimka/python_interview_questions/git/tags{/sha}",
		    "git_refs_url": "https://api.github.com/repos/yakimka/python_interview_questions/git/refs{/sha}",
		    "trees_url": "https://api.github.com/repos/yakimka/python_interview_questions/git/trees{/sha}",
		    "statuses_url": "https://api.github.com/repos/yakimka/python_interview_questions/statuses/{sha}",
		    "languages_url": "https://api.github.com/repos/yakimka/python_interview_questions/languages",
		    "stargazers_url": "https://api.github.com/repos/yakimka/python_interview_questions/stargazers",
		    "contributors_url": "https://api.github.com/repos/yakimka/python_interview_questions/contributors",
		    "subscribers_url": "https://api.github.com/repos/yakimka/python_interview_questions/subscribers",
		    "subscription_url": "https://api.github.com/repos/yakimka/python_interview_questions/subscription",
		    "commits_url": "https://api.github.com/repos/yakimka/python_interview_questions/commits{/sha}",
		    "git_commits_url": "https://api.github.com/repos/yakimka/python_interview_questions/git/commits{/sha}",
		    "comments_url": "https://api.github.com/repos/yakimka/python_interview_questions/comments{/number}",
		    "issue_comment_url": "https://api.github.com/repos/yakimka/python_interview_questions/issues/comments{/number}",
		    "contents_url": "https://api.github.com/repos/yakimka/python_interview_questions/contents/{+path}",
		    "compare_url": "https://api.github.com/repos/yakimka/python_interview_questions/compare/{base}...{head}",
		    "merges_url": "https://api.github.com/repos/yakimka/python_interview_questions/merges",
		    "archive_url": "https://api.github.com/repos/yakimka/python_interview_questions/{archive_format}{/ref}",
		    "downloads_url": "https://api.github.com/repos/yakimka/python_interview_questions/downloads",
		    "issues_url": "https://api.github.com/repos/yakimka/python_interview_questions/issues{/number}",
		    "pulls_url": "https://api.github.com/repos/yakimka/python_interview_questions/pulls{/number}",
		    "milestones_url": "https://api.github.com/repos/yakimka/python_interview_questions/milestones{/number}",
		    "notifications_url": "https://api.github.com/repos/yakimka/python_interview_questions/notifications{?since,all,participating}",
		    "labels_url": "https://api.github.com/repos/yakimka/python_interview_questions/labels{/name}",
		    "releases_url": "https://api.github.com/repos/yakimka/python_interview_questions/releases{/id}",
		    "deployments_url": "https://api.github.com/repos/yakimka/python_interview_questions/deployments",
		    "created_at": "2021-03-26T18:32:00Z",
		    "updated_at": "2023-01-10T19:36:19Z",
		    "pushed_at": "2022-12-05T23:16:04Z",
		    "git_url": "git://github.com/yakimka/python_interview_questions.git",
		    "ssh_url": "git@github.com:yakimka/python_interview_questions.git",
		    "clone_url": "https://github.com/yakimka/python_interview_questions.git",
		    "svn_url": "https://github.com/yakimka/python_interview_questions",
		    "homepage": "",
		    "size": 853,
		    "stargazers_count": 318,
		    "watchers_count": 318,
		    "language": "CSS",
		    "has_issues": True,
		    "has_projects": True,
		    "has_downloads": True,
		    "has_wiki": True,
		    "has_pages": False,
		    "has_discussions": False,
		    "forks_count": 103,
		    "mirror_url": None,
		    "archived": False,
		    "disabled": False,
		    "open_issues_count": 0,
		    "license": {
		        "key": "mit",
		        "name": "MIT License",
		        "spdx_id": "MIT",
		        "url": "https://api.github.com/licenses/mit",
		        "node_id": "MDc6TGljZW5zZTEz"
		    },
		    "allow_forking": True,
		    "is_template": False,
		    "web_commit_signoff_required": False,
		    "topics": [
		        "answers",
		        "interview",
		        "python",
		        "questions",
		        "questions-and-answers"
		    ],
		    "visibility": "public",
		    "forks": 103,
		    "open_issues": 0,
		    "watchers": 318,
		    "default_branch": "master",
		    "permissions": {
		        "admin": False,
		        "maintain": False,
		        "push": False,
		        "triage": False,
		        "pull": True
		    },
		    "temp_clone_token": "",
		    "network_count": 103,
		    "subscribers_count": 7
		},
		'pull_requests_amount': 7,
		'pull_requests_filtered_amount': 0,
		'forks_amount': 85,
		'issues_amount': 7,
	}
}

class TestFunctions(unittest.TestCase):
	def setUp(self):
		self.repo = list(repos_gt.keys())[1]
		self.token = secret.token

	def test_get_details(self):
		repo = self.repo
		token = self.token

		self.assertEqual(
			main.get_repo_details(repo, token),
			repos_gt[repo]['details']
		)

	def test_get_pull_requests(self):
		repo = self.repo
		token = self.token

		self.assertEqual(
			len(main.get_all_paged_items(repo, token, 'pulls')),
			repos_gt[repo]['pull_requests_amount']
		)

	def test_get_pull_requests_filtered(self):
		repo = self.repo
		token = self.token

		self.assertEqual(
			len(main.get_all_pr_older_than_two_weeks(repo, token)),
			repos_gt[repo]['pull_requests_filtered_amount']
		)

	def test_get_forks(self):
		repo = self.repo
		token = self.token

		self.assertEqual(
			len(main.get_all_paged_items(repo, token, 'forks')),
			repos_gt[repo]['forks_amount']
		)

	def test_get_issues(self):
		repo = self.repo
		token = self.token

		self.assertEqual(
			len(main.get_all_paged_items(repo, token, 'issues')),
			repos_gt[repo]['issues_amount']
		)

	def test_pr_age(self):
		pr = {
			'created_at': '0001-01-01T01:01:01Z'
		}

		self.assertEqual(
			main.calc_pr_age_in_days(pr, check_datetime=datetime.datetime(1, 1, 11, 1, 1, 1)),
			10
		)


if __name__ == "__main__":
  unittest.main()