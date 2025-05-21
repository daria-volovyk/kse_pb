#Видаліть усі дублікати, залиште лише парні числа,
# відсортуйте їх у спадаючому порядку та виведіть результат.
nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]
nums2=[]
nums1=set(nums)
print(nums1)
for i in nums1:
  if i%2==0:
    nums2.append(i)
print(nums2)
nums2.sort(reverse=True)
print(nums2)