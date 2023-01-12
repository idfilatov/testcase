import requests
import os
from datetime import datetime
from flask import Flask, jsonify, request
import logging
import logging.handlers

import main
import secret

token = secret.token

app = Flask(__name__)


@app.route('/details', methods=['GET'])
def get_details():
	repo = request.args.get('repo')

	return main.get_repo_details(repo, token)


@app.route('/pulls', methods=['GET'])
def get_pull_requests():
	repo = request.args.get('repo')

	return main.get_all_paged_items(repo, token, 'pulls')


@app.route('/pulls_filtered', methods=['GET'])
def get_pull_requests_filtered():
	repo = request.args.get('repo')

	return main.get_all_pr_older_than_two_weeks(repo, token)


@app.route('/forks', methods=['GET'])
def get_forks():
	repo = request.args.get('repo')

	return main.get_all_paged_items(repo, token, 'forks')


@app.route('/issues', methods=['GET'])
def get_issues():
	repo = request.args.get('repo')

	return main.get_all_paged_items(repo, token, 'issues')


if __name__ == '__main__':
	log_file_dir = os.path.join(
		os.path.dirname(os.path.abspath(__file__)),
		'logs'
	)
	os.makedirs(log_file_dir, exist_ok=True)

	log_file_path = os.path.join(log_file_dir, 'git-api.log')

	file_handler = logging.handlers.RotatingFileHandler(
		log_file_path,
		maxBytes=10 * 1024 * 1024,
		backupCount=3
	)
	file_handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(logging.Formatter(
	    '{asctime}  {levelname:<10s} {message}', style='{'
	))

	logging.basicConfig(
		level=logging.DEBUG,
		handlers=[file_handler]
	)

	app.run(debug=True)