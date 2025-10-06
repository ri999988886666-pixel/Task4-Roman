import pytest
import os
import tempfile
from app import read_students_from_md, find_student, generate_greeting

class TestStudentData:
    def test_read_students_with_new_metrics(self):
        students = read_students_from_md('students.md')
        assert len(students) > 0
        student = students[0]
        assert 'full_name' in student
        assert 'group' in student
        assert 'college' in student
        assert 'admission_year' in student
        assert 'course' in student

    def test_find_student_by_full_name(self):
        test_students = [
            {
                'full_name': 'Иванов Иван Иванович',
                'group': 'ТВ-101',
                'college': 'Технический колледж',
                'admission_year': 2023,
                'course': 2
            }
        ]
        student = find_student(test_students, 'Иванов Иван Иванович')
        assert student is not None
        assert student['group'] == 'ТВ-101'

    def test_student_metrics_validation(self):
        students = read_students_from_md('students.md')
        for student in students:
            assert 2000 <= student['admission_year'] <= 2024
            assert 1 <= student['course'] <= 6
            assert student['full_name'] != ''

class TestGreetingLogic:
    def test_generate_greeting_contains_all_metrics(self):
        test_student = {
            'full_name': 'Тестовый Студент',
            'group': 'ТЕСТ-101',
            'college': 'Тестовый колледж',
            'admission_year': 2023,
            'course': 2
        }
        greeting = generate_greeting(test_student)
        assert test_student['full_name'] in greeting
        assert test_student['group'] in greeting

    def test_greeting_course_specific_messages(self):
        first_year_student = {
            'full_name': 'Студент 1 курс',
            'group': 'ГР-101',
            'college': 'Колледж',
            'admission_year': 2024,
            'course': 1
        }
        greeting_1 = generate_greeting(first_year_student)
        assert 'начинаете' in greeting_1.lower()

    def test_student_years_calculation(self):
        test_student = {
            'full_name': 'Тестовый Студент',
            'group': 'ТЕСТ-101',
            'college': 'Тестовый колледж',
            'admission_year': 2022,
            'course': 3
        }
        greeting = generate_greeting(test_student)
        assert '3' in greeting

class TestIntegration:
    def test_complete_student_workflow(self):
        students = read_students_from_md('students.md')
        assert len(students) > 0
        if students:
            existing_student = find_student(students, students[0]['full_name'])
            assert existing_student is not None
            greeting = generate_greeting(existing_student)
            assert existing_student['full_name'] in greeting

    def test_data_consistency(self):
        students = read_students_from_md('students.md')
        for student in students:
            expected_min_course = 2024 - student['admission_year'] + 1
            assert abs(student['course'] - expected_min_course) <= 1

            import pytest
from app import generate_greeting, register_new_student
import io
import sys

class TestGreetingLogic:
    """Тесты для логики приветствия и регистрации"""
    
    def test_generate_greeting_contains_all_metrics(self):
        """Тест, что приветствие содержит все метрики"""
        test_student = {
            'full_name': 'Тестовый Студент',
            'group': 'ТЕСТ-101',
            'college': 'Тестовый колледж',
            'admission_year': 2023,
            'course': 2
        }
        
        greeting = generate_greeting(test_student)
        
        # Проверяем наличие всех метрик в приветствии
        assert test_student['full_name'] in greeting
        assert test_student['group'] in greeting
        assert test_student['college'] in greeting
        assert str(test_student['admission_year']) in greeting
        assert str(test_student['course']) in greeting
        
        # Проверяем дополнительные вычисляемые метрики
        assert 'Лет обучения' in greeting
    
    def test_greeting_course_specific_messages(self):
        """Тест специальных сообщений для разных курсов"""
        # Тест для первого курса
        first_year_student = {
            'full_name': 'Студент 1 курс',
            'group': 'ГР-101',
            'college': 'Колледж',
            'admission_year': 2024,
            'course': 1
        }
        
        greeting_1 = generate_greeting(first_year_student)
        assert 'начинаете' in greeting_1.lower()
        
        # Тест для старших курсов
        senior_student = {
            'full_name': 'Студент 3 курс',
            'group': 'ГР-301',
            'college': 'Колледж',
            'admission_year': 2022,
            'course': 3
        }
        
        greeting_3 = generate_greeting(senior_student)
        assert 'опытный' in greeting_3.lower() or 'диплом' in greeting_3.lower()
    
    def test_student_years_calculation(self):
        """Тест расчета лет обучения"""
        test_student = {
            'full_name': 'Тестовый Студент',
            'group': 'ТЕСТ-101',
            'college': 'Тестовый колледж',
            'admission_year': 2022,
            'course': 3
        }
        
        greeting = generate_greeting(test_student)
        # Должно быть 3 года обучения (2024-2022+1)
        assert '3' in greeting  # Лет обучения
        import pytest
from app import read_students_from_md, find_student, generate_greeting

def test_read_students():
    students = read_students_from_md('students.md')
    assert len(students) > 0
    print('✅ Тест чтения студентов прошел')

def test_find_student():
    test_students = [
        {
            'full_name': 'Иванов Иван Иванович',
            'group': 'ТВ-101',
            'college': 'Технический колледж',
            'admission_year': 2023,
            'course': 2
        }
    ]
    student = find_student(test_students, 'Иванов Иван Иванович')
    assert student is not None
    assert student['group'] == 'ТВ-101'
    print('✅ Тест поиска студента прошел')

def test_generate_greeting():
    test_student = {
        'full_name': 'Тестовый Студент',
        'group': 'ТЕСТ-101',
        'college': 'Тестовый колледж',
        'admission_year': 2023,
        'course': 2
    }
    greeting = generate_greeting(test_student)
    assert test_student['full_name'] in greeting
    assert test_student['group'] in greeting
    assert test_student['college'] in greeting
    assert str(test_student['admission_year']) in greeting
    assert str(test_student['course']) in greeting
    print('✅ Тест генерации приветствия прошел')

def test_greeting_course_messages():
    first_year_student = {
        'full_name': 'Студент 1 курс',
        'group': 'ГР-101',
        'college': 'Колледж',
        'admission_year': 2024,
        'course': 1
    }
    greeting_1 = generate_greeting(first_year_student)
    assert 'начинаете' in greeting_1.lower()
    print('✅ Тест сообщений для курсов прошел')

def test_student_validation():
    students = read_students_from_md('students.md')
    for student in students:
        assert 2000 <= student['admission_year'] <= 2024
        assert 1 <= student['course'] <= 6
        assert student['full_name'] != ''
    print('✅ Тест валидации данных прошел')

def test_complete_workflow():
    students = read_students_from_md('students.md')
    assert len(students) > 0
    if students:
        student = find_student(students, students[0]['full_name'])
        assert student is not None
        greeting = generate_greeting(student)
        assert student['full_name'] in greeting
    print('✅ Тест полного workflow прошел')

def test_data_consistency():
    students = read_students_from_md('students.md')
    for student in students:
        expected_min_course = 2024 - student['admission_year'] + 1
        assert abs(student['course'] - expected_min_course) <= 1
    print('✅ Тест согласованности данных прошел')

def test_years_calculation():
    test_student = {
        'full_name': 'Тестовый Студент',
        'group': 'ТЕСТ-101',
        'college': 'Тестовый колледж',
        'admission_year': 2022,
        'course': 3
    }
    greeting = generate_greeting(test_student)
    assert '3' in greeting
    print('✅ Тест расчета лет обучения прошел')