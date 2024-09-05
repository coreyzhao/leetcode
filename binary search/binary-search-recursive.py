def binSearch(ls, target, l, r):
  l = 0
  r = ls.length - 1

  if l <= r:
    mid = l + ((r - l) // 2)
    if ls[mid] > target:
        return binSearch(ls, target, l, mid - 1)
    elif ls[mid] < target:
        return binSearch(ls, target, mid + 1, r)
    else:
        return mid
  return -1