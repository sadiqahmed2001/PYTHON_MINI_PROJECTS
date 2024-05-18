import random

class WorkoutGenerator:
    def __init__(self):
        self.exercises = {
            'Warm-up': ['Jumping Jacks', 'Arm Circles', 'Leg Swings', 'High Knees', 'Torso Twists'],
            'Cardio': ['Running', 'Cycling', 'Jump Rope', 'Burpees', 'Mountain Climbers'],
            'Upper Body': ['Push-ups', 'Pull-ups', 'Dumbbell Rows', 'Bicep Curls', 'Tricep Dips'],
            'Lower Body': ['Squats', 'Lunges', 'Deadlifts', 'Calf Raises', 'Leg Press'],
            'Core': ['Planks', 'Russian Twists', 'Crunches', 'Leg Raises', 'Bicycle Crunches'],
            'Cool-down': ['Stretching', 'Deep Breathing', 'Foam Rolling', 'Yoga Poses']
        }

    def generate_workout(self):
        workout = {}

        # Select random exercises from each category
        for category, exercise_list in self.exercises.items():
            workout[category] = random.choice(exercise_list)

        return workout

def display_workout(workout):
    print("Your Random Workout:")
    for category, exercise in workout.items():
        print(f"{category}: {exercise}")

def main():
    print("Welcome to the Random Workout Generator!")
    generator = WorkoutGenerator()

    # Generate and display a random workout
    workout = generator.generate_workout()
    display_workout(workout)

if __name__ == "__main__":
    main()
