'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose: Validate an Email Address
'''
import re
def validate_email_fullmatch(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"
    if re.fullmatch(pattern, email):
        return True
    else:
        return False
print(f"'test@example.com' is valid: {validate_email_fullmatch('test@example.com')}")
print(f"'john.doe123@sub.domain.co.in' is valid: {validate_email_fullmatch('john.doe123@sub.domain.co.in')}")
print(f"'invalid-email' is valid: {validate_email_fullmatch('invalid-email')}")
print(f"'user@domain' (missing TLD) is valid: {validate_email_fullmatch('user@domain')}") 
print(f"'user@domain.toolongtld' (too long TLD) is valid: {validate_email_fullmatch('user@domain.toolongtld')}") 
print()
email_pattern_compiled = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$")

def validate_email_compiled(email):
    if email_pattern_compiled.fullmatch(email):
        return True
    else:
        return False

print(f"'test.user@company.org' is valid: {validate_email_compiled('test.user@company.org')}")
print(f"'bad-email@.com' is valid: {validate_email_compiled('bad-email@.com')}")
print()