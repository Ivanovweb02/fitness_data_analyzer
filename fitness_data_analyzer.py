def calculate_bmi(curr_weight, curr_height):
    """Calculate the Body Mass Index (BMI)."""
    return weight / (height*2)


def calculate_calories_burned(curr_duration, curr_weight):
    """Calculate the estimated number of calories burned during exercise."""
    met = 3.5
    return f'{(curr_duration *(met * curr_weight) / 200) :.2f}'


def filter_overweight_people(curr_people_data):
    """Filter overweight people based on BMI."""
    curr_overweight_people = []
    for curr_person in curr_people_data:
        curr_bmi = calculate_bmi(curr_person['weight'], curr_person['height'])
        if curr_bmi >= 25:
            curr_overweight_people.append(person)
    return curr_overweight_people


# Main program
people_data = []

print("Enter fitness data for each person (Enter a blank name to finish):")
while True:
    name = input("Enter person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])

    calories_burned = calculate_calories_burned(person['duration'], person['weight'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

overweight_people = filter_overweight_people(people_data)
print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")
