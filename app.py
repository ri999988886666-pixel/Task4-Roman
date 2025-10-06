import re

def read_students_from_md(filename):
    """
    Чтение данных студентов из markdown файла с новыми метриками
    Возвращает список словарей с информацией о студентах
    """
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Регулярное выражение для поиска строк таблицы с новыми полями
        table_pattern = r'\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\d{4})\s*\|\s*(\d+)\s*\|'
        matches = re.findall(table_pattern, content)
        
        for match in matches:
            full_name, group, college, admission_year, course = match
            if full_name.lower() != 'фио':  # Пропускаем заголовок
                students.append({
                    'full_name': full_name.strip(),
                    'group': group.strip(),
                    'college': college.strip(),
                    'admission_year': int(admission_year),
                    'course': int(course)
                })
                
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        
    return students

def find_student(students, full_name):
    """
    Поиск студента по ФИО (регистронезависимый)
    """
    for student in students:
        if student['full_name'].lower() == full_name.lower():
            return student
    return None

def generate_greeting(student):
    """
    Генерация приветствия с метриками студента
    """
    current_year = 2024  # Можно заменить на получение текущего года
    years_studying = current_year - student['admission_year'] + 1
    
    greeting = f"\n🎓 Добро пожаловать, {student['full_name']}!"
    greeting += f"\n{'='*50}"
    greeting += f"\n📊 Ваши образовательные метрики:"
    greeting += f"\n├─ 🏫 Колледж: {student['college']}"
    greeting += f"\n├─ 👥 Группа: {student['group']}"
    greeting += f"\n├─ 📅 Год поступления: {student['admission_year']}"
    greeting += f"\n├─ 📚 Текущий курс: {student['course']}"
    greeting += f"\n└─ ⏱️ Лет обучения: {years_studying}"
    
    # Дополнительная информация на основе метрик
    if student['course'] == 1:
        greeting += f"\n\n🌟 Вы только начинаете свой образовательный путь!"
    elif student['course'] >= 3:
        greeting += f"\n\n🎯 Вы уже опытный студент! Скоро диплом!"
    
    return greeting

def display_student_info(student):
    """
    Отображение информации о студенте с приветствием
    """
    greeting = generate_greeting(student)
    print(greeting)

def register_new_student(full_name, students, filename):
    """
    Регистрация нового студента с запросом новых метрик
    """
    print(f"\n❌ Студент {full_name} не найден в базе.")
    response = input("Хотите зарегистрироваться? (да/нет): ").lower().strip()
    
    if response == 'да':
        try:
            print("\n📝 Регистрация нового студента:")
            group = input("Введите учебную группу: ")
            college = input("Введите название колледжа: ")
            admission_year = int(input("Введите год поступления: "))
            course = int(input("Введите текущий курс: "))
            
            # Валидация данных
            if admission_year < 2000 or admission_year > 2024:
                print("❌ Ошибка: Некорректный год поступления")
                return None
            if course < 1 or course > 6:
                print("❌ Ошибка: Некорректный номер курса")
                return None
            
            new_student = {
                'full_name': full_name,
                'group': group,
                'college': college,
                'admission_year': admission_year,
                'course': course
            }
            students.append(new_student)
            
            # Добавляем в файл
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f"\n| {full_name} | {group} | {college} | {admission_year} | {course} |")
            
            print("✅ Студент успешно зарегистрирован!")
            return new_student
            
        except ValueError:
            print("❌ Ошибка: Введите корректные числовые значения")
        except Exception as e:
            print(f"❌ Ошибка при регистрации: {e}")
    
    return None

def main():
    """
    Основная функция приложения
    """
    filename = 'students.md'
    students = read_students_from_md(filename)
    
    print("🎓 Система управления студентами")
    print("=" * 50)
    print("Доступные команды:")
    print("• Введите ФИО студента для поиска")
    print("• 'список' - показать всех студентов")
    print("• 'выход' - завершить программу")
    
    while True:
        print("\n" + "-" * 30)
        user_input = input("Введите команду: ").strip()
        
        if user_input.lower() == 'выход':
            print("👋 До свидания!")
            break
        elif user_input.lower() == 'список':
            print("\n📋 Список всех студентов:")
            for i, student in enumerate(students, 1):
                print(f"{i}. {student['full_name']} - {student['group']}")
        else:
            student = find_student(students, user_input)
            
            if student:
                display_student_info(student)
            else:
                new_student = register_new_student(user_input, students, filename)
                if new_student:
                    display_student_info(new_student)

if __name__ == "__main__":
    main()