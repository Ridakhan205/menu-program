cloth="stitched/unstitched"
size="medium/large"
cloth_category="casual/wedding"
season="summer/winter"
colors="light/dark"

cloth=input("which type of do you want ").lower()
size=input("enter what size do you want").lower()
cloth_category=input("from which category do you want:").lower()
colors=input("do you want light colors or dark colors").lower()
season=input("which season dress do you want").lower()



while True:
   if cloth=="stitched" or size=="medium" or colors=="dark"or cloth_category=="casual" or season=="summer":
        print("this kurti is good for you:")
        break
   elif cloth=="unstitched" or size=="large" or colors=="light" or season=="winter" or cloth_category=="wedding":
        print("this lawn dress is good for you:")
        rerun=input("are u satisfied yes/no").lower()
        if rerun=="yes":
            print("thank you:")
            break
        else:
            print("sorry for no more collection:")
            break
   else:
      print("try again")
      break
        