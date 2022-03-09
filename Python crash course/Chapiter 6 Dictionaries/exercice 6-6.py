favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil' : 'python',
    'brigitte' : 'Visual basic', 
}

employees = ['brigitte', 'jean-francois', 'sarah', 'jen']

if employees:
    for employee in employees:
        if employee not in favorite_languages.keys():
            print(f'Please {employee.title()} take a moment to fill the poll.')
        else:
            favorite = favorite_languages[employee]
            print(f"Thanks {employee.title()} for taking the poll. I see that you like {favorite.title()}.")