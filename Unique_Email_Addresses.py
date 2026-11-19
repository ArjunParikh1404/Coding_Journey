# Given a list of email addresses, count the number of unique emails.
# Rules:
# 1. Ignore everything after '+' in the local name.
# 2. Ignore all '.' in the local name.
# Time Complexity = O(n * m), Space Complexity = O(n)

emails = input("Enter the emails separated by space : ").split()

unique_emails = set()

p1 = 0

while p1 < len(emails):
    email = emails[p1]

    local, domain = email.split("@")

    local = local.split("+")[0]
    local = local.replace(".", "")

    new_email = local + "@" + domain

    unique_emails.add(new_email)

    p1 += 1

print("unique emails =", len(unique_emails))
