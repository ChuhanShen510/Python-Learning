while 1 == 1:
    temp = input("请输入你的分数：")
    if temp == "e":
        break
    grade = int(temp)

    if grade == 100:
      print("S")
    else:
        if 100> grade >= 90:
            print("A")
        else:
                if 90 > grade >= 80:
                    print("B")
                else:
                    if 80 > grade >= 60:
                        print("C")
                    else:
                        if 60 > grade:
                            print("D")
    
                        
