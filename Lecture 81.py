try:
    Int_Input = int(input())
    Int2_Input = int(input())
    print(Int_Input/Int2_Input)
except ValueError:
    print("Error!! Number Only")
except ZeroDivisionError:
    print("Error !! You Can't Enter 0 ")
except:
    print("Error")