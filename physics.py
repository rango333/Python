print("Determine the joules of work supplied by a given object at a given distance\n")

while True:
  mass1 = input("Enter metric mass of object (ex kg): ")
  object_mass = int(mass1)
  acceleration1 = input("Enter metric acceleration of object (ex m/s**2): ")
  object_acceleration = int(acceleration1)
  distance1 = input("Enter metric distance (ex meters): ")
  object_distance = int(distance1)

  def get_force(mass, acceleration):
    return mass * acceleration
  force = get_force(object_mass, object_acceleration)
  print("The object supplies", force, "Newtons of force.")

  def get_work(mass, acceleration, distance):
    force1 = mass * acceleration * distance
    return force1
  train_work = get_work(object_mass, object_acceleration, object_distance)
  print("\nThe object does", train_work, "Joules of work over", object_distance, "meters.")

  continue_again = input("Continue again? (y/n): ")
  if continue_again.lower() != "y":
    break