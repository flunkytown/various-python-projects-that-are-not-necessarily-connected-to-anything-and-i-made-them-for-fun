portalsize1 = int(input("portal one size: "))
portalsize2 = int(input("portal tuah size 😂: "))

sizeofourguy = 6

def whatshecomeoutas():
    print(f"our guy is now {sizeofourguy / (portalsize1 / portalsize2)} unitsofmeasurement tall")

if sizeofourguy < portalsize1:
    whatshecomeoutas()
elif sizeofourguy == 0:
    print("what the hell")
elif sizeofourguy > portalsize1:
    print("our guy is too big")