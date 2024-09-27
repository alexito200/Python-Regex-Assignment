# Task 1: Email Extraction Enhancement
# Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

emails = re.findall(pattern, text)
print(emails)
