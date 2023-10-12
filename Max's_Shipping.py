# # Determine weight of package and the cheapest way to ship the package
    
while True:
    # Enter pachage weight
    weight = int(input("Enter a weight: "))

    # Ground and drone shipping price by weight
    if weight <= 2:
        cost_ground = weight * 1.50 +20
        cost_drone = weight * 4.50
    elif 2 < weight <= 6:
        cost_ground = weight * 3.00 + 20
        cost_drone = weight * 9.00
    elif 6 < weight <= 10:
        cost_ground = weight * 4.00 + 20
        cost_drone = weight * 12.00
    elif weight > 10:
        cost_ground = weight * 4.75 + 20
        cost_drone = weight * 14.25

    # Ground_premium flat rate without weight charge
    cost_ground_premium = 125.00

    print("Ground shipping is $", ("{:.2f}".format(cost_ground)))
    print("Ground shipping premium is $", ("{:.2f}".format(cost_ground_premium)))
    print("Drone shipping is $", ("{:.2f}".format(cost_drone)))

    if cost_ground < cost_ground_premium and cost_ground < cost_drone:
        print("\nGround shipping is the cheapest")
    if cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
        print("\nGround shipping premium is the cheapest")
    if cost_drone < cost_ground and cost_drone < cost_ground_premium:
        print("\nGround shipping is the cheapest")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break