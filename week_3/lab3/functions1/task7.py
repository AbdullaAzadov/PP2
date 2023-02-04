def has_33(nums):
    str_nums = ''
    for i in nums:
        str_nums+= str(i)
        
    if str_nums.find("33") != -1:
        print(True)
        return True
    else:
        print(False)
        return False

has_33([1, 3, 3]) # → True
has_33([1, 3, 1, 3]) # → False
has_33([3, 1, 3]) # → False