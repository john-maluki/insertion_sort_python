numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertion_sort(arr):
  i = 0
  for x in range(1, len(arr)):
    value = arr[x]
    i = x - 1
    while i >= 0:
      if value < arr[i]:
        arr[i + 1] = arr[i] #shift the number at the slot i right into slot i + 1
        arr[i] = value #shift value left into slot i
        i -= 1
      else:
        break
      

insertion_sort(numbers);

print(numbers)
