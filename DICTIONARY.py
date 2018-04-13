#russel john cortez
#DICTIONARY

print(" ")
print("WAR WEAPON")
print(" ")
WEAPON= {
            "M4A1" : "A.RIFLE",
            "MP5" : "SMG",
            "TOMYGUN" : "SMG",
            "COLT1911" : "PISTOL",
            "AK47" : "A.RIFLE",
            "GLOCK18" : "PISTOL",
            "BAYONET" : "MELEE",
            "KARAMBIT" : "MELEE",
            "SCAR LIGHT" : "A.RIFLE",
            "M16A4" : "A.RIFLE",
            "STYR AUG" : "A.RIFLE",
            "MAUSER" : "S.RIFLE",
            "M24" : "S.RIFLE",
            "AWP" : "S.RIFLE",
            "MACHETE" : "MELEE"
    }

for key, val in WEAPON.items():
    print(key, "===", val)

#add in dictionary
WEAPON["CZ700"] = "S.RIFLE"
WEAPON["M249"] = "MACHINE GUN"
WEAPON["KRISS VECTOR"] = "SMG"
WEAPON["GALIL"] = "MACHINE GUN"
WEAPON["SPAS12"] = "SHOTGUN"
WEAPON["BENELI M4"] = "SHOTGUN"

print("-"*10)

for key, value in sorted(WEAPON.items()):     #SORT
    print(key, "===", value)
