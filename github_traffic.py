from datetime import datetime, timedelta

import github
import pymysql
from warnings import filterwarnings
filterwarnings('ignore', category = pymysql.Warning)

def _collect(token, org, repo):
    gh = github.GitHub(access_token=token)
    repositries_data = gh.orgs(org).repos.get(per_page="1000")
    print("total no. of public repository: ", len(repositries_data))

    for rec in repositries_data:
        repo_nm = rec['name']
        forks = rec['forks']
        stargazers_count = rec['stargazers_count']
        watchers_count = rec['watchers_count']
        print("processing repo: ", repo_nm)
        # last 14 days
        commit_since = str(datetime.utcnow() - timedelta(14))[0:10]
        page_no = 1
        commit_info = gh.repos(org)(repo_nm).commits.get(since=commit_since, per_page="100", page=str(page_no))
        temp = commit_info
        while len(temp) > 0:
            page_no = page_no + 1
            temp = gh.repos(org)(repo_nm).commits.get(since=commit_since, per_page="100", page=str(page_no))

        commit_count_dict = {}
        for rec in commit_info:
            date = rec['commit']['author']['date'][:-10]
            commit_count_dict[date] = commit_count_dict.get(date, 0) + 1
        views_14_days = gh.repos(org, repo_nm).traffic.views.get()

        count = 0;
        for view_per_day in views_14_days['views']:
            commit_count = commit_count_dict.get(view_per_day['timestamp'][:-10], 0)
            git_traffic_rec = [repo_nm, view_per_day['timestamp'][:-10], view_per_day['count'], view_per_day['uniques'],
                               commit_count, forks, stargazers_count, watchers_count, datetime.utcnow(),
                               datetime.utcnow()]
            rows_inserted = write_to_db(repo, git_traffic_rec=git_traffic_rec)
            count = count + rows_inserted
        print("records recorded:", count)


def write_to_db(repo, git_traffic_rec):
    try:
        qry = "INSERT IGNORE INTO git_traffic (repo, date, views, uq_views, cmt_cnt, forks, stargazers_count, watchers_count," \
              " row_created, row_updated) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        res = repo.execute(qry, git_traffic_rec)
        return res[0]
    except Exception as e:
        print(repr(e))


def update_github_traffic(repo):
    _collect(token="", org="singnet", repo=repo)
    print("success"
