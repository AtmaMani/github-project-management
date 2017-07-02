from github3 import login
import getpass
import csv

# Get credentials
username = input('Enter GitHub username: ')
password = getpass.getpass('enter GitHub password: ')
csv_file = input('Enter path to output csv file: ')
repo_name = input('Enter name of the repo: ')

# Login
gh = login(username, password)
repo_list = list(gh.search_repositories(repo_name))

# Get repo and issue list
repo_hit = repo_list[0]
repo1 = repo_hit.repository

print(repo1.name)
#closed_issue_list = repo1.issues(state = 'closed', sort = 'updated', direction='desc')
issue_iterator = repo1.iter_issues()

# write to csv
with open(csv_file, 'w') as csv_handle:
    field_names = ['Issue_number', 'Title', 'Closed_at', 'User']
    writer = csv.DictWriter(csv_handle, fieldnames= field_names, lineterminator = '\n')
    writer.writeheader()

    for issue in issue_iterator:
        if issue.state == 'open':
          issue_iterator.next
          continue
        # print(str(issue.number) + " | " + issue.title + " | " + str(issue.closed_at) + " | " + str(issue.user.login))
        t1 = issue.closed_at
        d1 = {'Issue_number': str(issue.number),
              'Title': str(issue.title),
              'Closed_at': str.format("{}_{}_{}",t1.year, t1.month, t1.day),
              'User': issue.user.login}
        writer.writerow(d1)
        issue_iterator.next
