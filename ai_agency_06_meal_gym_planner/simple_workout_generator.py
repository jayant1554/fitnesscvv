import json
import requests

class SimpleWorkoutPlannerSystem:
    def __init__(self):
        # Simple workout templates based on user preferences
        self.workout_templates = {
            "beginner": {
                "cardio": {
                    "15": ["5 min warm-up walking", "8 min light jogging", "2 min cool-down stretching"],
                    "30": ["10 min warm-up walking", "15 min moderate cardio", "5 min cool-down"]
                },
                "strength": {
                    "15": ["3 min warm-up", "10 min bodyweight exercises", "2 min cool-down"],
                    "30": ["5 min warm-up", "20 min strength training", "5 min cool-down"]
                }
            }
        }
        
        self.meal_templates = {
            "weight_loss": {
                "breakfast": "Oatmeal with berries and Greek yogurt",
                "lunch": "Grilled chicken salad with vegetables",
                "dinner": "Baked salmon with quinoa and steamed broccoli",
                "snacks": ["Apple with almond butter", "Greek yogurt with nuts"]
            }
        }

    def generate_plan(self, user_info):
        # Extract user information
        fitness_level = user_info.get('fitness_level', 'Beginner').lower()
        workout_type = user_info.get('workout_type', 'Cardio').lower()
        duration = str(user_info.get('workout_duration', '15'))
        goals = user_info.get('goals', ['Weight Loss'])
        equipment = user_info.get('equipment', [])
        focus_areas = user_info.get('focus_areas', [])
        
        # Generate workout plan
        workout_plan = {
            "frequency": f"{user_info.get('workout_days', '5')} days per week",
            "duration": f"{duration} minutes",
            "intensity": user_info.get('intensity', 'Low'),
            "equipment": equipment,
            "focus_areas": focus_areas,
            "daily_structure": self._generate_daily_structure(fitness_level, workout_type, duration),
            "weekly_summary": f"{fitness_level.title()} {workout_type} program for {duration} minutes daily"
        }
        
        # Generate meal plan
        goal_key = goals[0].lower().replace(' ', '_') if goals else 'weight_loss'
        meal_plan = {
            "nutritional_goals": {
                "calories": "1800-2000 per day" if 'weight loss' in goal_key else "2200-2500 per day",
                "protein": "120g per day",
                "carbs": "150g per day",
                "fats": "60g per day"
            },
            "meal_timing": "3 main meals + 2 snacks",
            "weekly_meals": self.meal_templates.get(goal_key, self.meal_templates['weight_loss']),
            "additional_tips": [
                "Drink at least 8 glasses of water daily",
                "Eat protein within 30 minutes after workout",
                "Include vegetables in every meal",
                "Avoid processed foods"
            ]
        }
        
        # Combine into final plan
        final_plan = {
            "workout_plan": workout_plan,
            "meal_plan": meal_plan
        }
        
        return json.dumps(final_plan, indent=2)
    
    def _generate_daily_structure(self, fitness_level, workout_type, duration):
        base_structure = {}
        
        if workout_type == "cardio":
            if duration == "15":
                base_structure = {
                    "Day 1": "5 min warm-up walk + 8 min light cardio + 2 min stretching",
                    "Day 2": "5 min warm-up + 8 min interval training + 2 min cool-down",
                    "Day 3": "5 min warm-up + 8 min steady cardio + 2 min stretching",
                    "Day 4": "5 min warm-up + 8 min dance cardio + 2 min cool-down",
                    "Day 5": "5 min warm-up + 8 min walking/jogging + 2 min stretching"
                }
            else:
                base_structure = {
                    "Day 1": "10 min warm-up + 15 min cardio + 5 min cool-down",
                    "Day 2": "10 min warm-up + 15 min interval training + 5 min stretching",
                    "Day 3": "10 min warm-up + 15 min steady-state cardio + 5 min cool-down"
                }
        else:  # strength training
            if duration == "15":
                base_structure = {
                    "Day 1": "3 min warm-up + 10 min upper body + 2 min stretching",
                    "Day 2": "3 min warm-up + 10 min lower body + 2 min stretching",
                    "Day 3": "3 min warm-up + 10 min full body + 2 min stretching"
                }
            else:
                base_structure = {
                    "Day 1": "5 min warm-up + 20 min upper body + 5 min cool-down",
                    "Day 2": "5 min warm-up + 20 min lower body + 5 min stretching",
                    "Day 3": "5 min warm-up + 20 min full body + 5 min cool-down"
                }
        
        return base_structure

# Usage example:
if __name__ == "__main__":
    planner = SimpleWorkoutPlannerSystem()
    user_info = {
        'age': '34',
        'gender': 'Male',
        'fitness_level': 'Beginner',
        'goals': ['Weight Loss'],
        'workout_duration': '15',
        'workout_type': 'Cardio',
        'equipment': ['Dumbbells'],
        'workout_days': '5',
        'intensity': 'Low',
        'workout_time': 'Morning',
        'warmup_cooldown': 'Yes',
        'focus_areas': ['Upper Body']
    }
    result = planner.generate_plan(user_info)
    print(result)