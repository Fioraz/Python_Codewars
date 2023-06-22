def CodelandUsernameValidation(strParam):
  if len(strParam) < 4 or len(strParam) > 25:
    return False
  elif not strParam[0].isalpha:
    return False
  elif strParam[-1] == "_":
    return False
  for char in strParam:
    if not (char.isalnum() or char == "_"):
      return False
  return True

# keep this function call here 
print(CodelandUsernameValidation(input()))