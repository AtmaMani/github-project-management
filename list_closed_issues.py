from github3 import login
import getpass
import csv

# Get credentials
username = input('Enter username: ')
password = getpass.getpass('enter password: ')
csv_file = input('Enter path to output csv file: ')

# Login
gh = login(username, password)
repo_list = list(gh.repositories(type = 'member'))

# Get repo and issue list
repo1 = repo_list[0]
print(repo1.name)
closed_issue_list = repo1.issues(state = 'closed', sort = 'updated', direction='desc')

# write to csv
with open(csv_file, 'w') as csv_handle:
    field_names = ['Issue_number', 'Title', 'Closed_at', 'User']
    writer = csv.DictWriter(csv_handle, fieldnames= field_names, lineterminator = '\n')
    writer.writeheader()

    for issue in closed_issue_list:
        # print(str(issue.number) + " | " + issue.title + " | " + str(issue.closed_at) + " | " + str(issue.user.login))
        t1 = issue.closed_at
        d1 = {'Issue_number': str(issue.number),
              'Title': str(issue.title),
              'Closed_at': str.format("{}_{}_{}",t1.year, t1.month, t1.day),
              'User': issue.user.login}
        writer.writerow(d1)
