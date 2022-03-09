def LinearSearch(arr,n,x):
  for i in range(0,n):
    if (arr[i]==x):
      return i
  return "Not found"
