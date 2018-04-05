import re
def validate_code(code):
    return bool(re.match("^[123]", str(code)))



"""



https://www.codewars.com/kata/validate-code-with-simple-regex/train/python



"""
