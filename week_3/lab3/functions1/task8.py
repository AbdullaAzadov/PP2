def spy_game(nums):
        str_nums = ''
        for i in nums:
            str_nums+= str(i)

        tmp_str = str_nums
        null1 = tmp_str.find("0")
        tmp_str.replace("0", "", 1)
        null2 = tmp_str.find("0")   
        seven = tmp_str.find("7")

        if (str_nums.find("007") != -1) or (null1 <= null2 < seven):
            print(True)
            return True
        else:
            print(False)
            return False

spy_game([1,2,4,0,0,7,5]) # --> True
spy_game([1,0,2,4,0,5,7]) # --> True
spy_game([1,7,2,0,4,5,0]) # --> False