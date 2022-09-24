print("hi,hellow")
print("welcome to mems mastar resturant")
print("I will give you the menu please order what do you want")

d={"soups":{"veg":["garlic","corn","carrot"],
            "nonveg":["chicken","mutton"]}, 
   "starters":{"veg":["babycorncurry","mushroomcurry","cabbagecurry","potatocurry"],
            "nonveg":["chickencurry","muttoncurry","fishcurry","prawnscurry"]},
            
    "quit":{"q":["q"]}
   }

print(d)
d.keys()
d.update({"soups":{"veg"["mushroom"]}})
d["starters"].keys()
d["soups"].keys()
d["quit"].keys()
garlic=70;
corn=120;
carrot=80;
chicken=250;
mutton=350;
babycorncurry=280;
mushroomcurry=160;
cabbagecurry=180;
potatocurry=65;
chickencurry=300;
muttoncurry=400;
fishcurry=380;
prawnscurry=500;
total = 0.0;


while True:
    
    p=input(f"please choose any option from menu:{d.keys()}")
    f=input(f"please let us know would you like to have :{d[p].keys()}")
    m=input(f"please choose dishes you like to have:{d[p][f]}")
    print("Total:",total);
    
    if m.lower() == "garlic":
        print("garlic : 70")
        total += garlic
    elif m.lower() == "corn":
        print("corn : 120")
        total += corn
    elif m.lower() == "carrot":
        print("carrot : 80")
        total += carrot
    elif m.lower() == "chicken":
        print("chicken : 250")
        total += chicken
    elif m.lower() == "mutton":
        print("mutton : 350")
        total += mutton
    elif m.lower() == "babycorncurry":
        print("babycorncurry : 280")
        total += babycorncurry
    elif m.lower() == "mushroomcurry":
        print("mushroomcurry : 160")
        total += mushroomcurry
    elif m.lower() == "cabbagecurry":
        print("cabbagecurry : 180")
        total += cabbagecurry
    elif m.lower() == "potatocurry":
        print("potatocurry : 65")
        total += potatocurry
    elif m.lower() == "chickencurry":
        print("chickencurry : 300")
        total += chickencurry
    elif m.lower() == "muttoncurry":
        print("muttoncurry : 400")
        total += muttoncurry
    elif m.lower() == "fishcurry":
        print("fishcurry : 380")
        total += fishcurry
    elif m.lower() == "prawnscurry":
        print("prawnscurry : 500")
        total += prawnscurry
    
    else:
       
        if m == "quit":
          print("final total:",total);  
