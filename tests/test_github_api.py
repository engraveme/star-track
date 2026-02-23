# Authentication is defined via github.Auth
import os

from dotenv import load_dotenv
from github import Auth, Github

# Load environment variables from .env file
load_dotenv()

# using an access token from environment variable
auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

# Public Web Github
g = Github(auth=auth)

# 获取当前用户
me = g.get_user()
print(me.login, me.email, me.public_repos)

# 获取其他用户
# octocat = g.get_user("octocat")
# for repo in octocat.get_repos()[:3]:
#     print(repo.name, repo.stargazers_count)

repo = g.get_repo("eaglebetter/star-track")

# 基础信息
print(repo.name, repo.description, repo.stargazers_count)
print("最后推送时间:", repo.pushed_at)  # 注意：用 pushed_at 而非 _updated_at [10]

# 获取 Topics
print(repo.get_topics())

# 流量统计 [2]
# views = repo.get_views_traffic(per="week")
# print(f"本周访问量: {views['count']}, 独立访客: {views['uniques']}")

# 克隆统计
# clones = repo.get_clones_traffic(per="day")
# for day in clones["clones"]:
#     print(day.timestamp, day.count)

# 创建 Issue
# repo.create_issue(
#     title="自动创建的 Issue", body="由 PyGithub 脚本生成", labels=["automation"]
# )

# 获取开放的 Issue
for issue in repo.get_issues(state="open"):
    print(f"#{issue.number}: {issue.title}")


# 获取 PR（PR 本质是特殊的 Issue）
pulls = repo.get_pulls(state="open")
for pr in pulls:
    print(pr.title, pr.user.login)
