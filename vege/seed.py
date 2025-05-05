from faker import Faker
import random
from .models import Department, StudentID, Student

fake = Faker()

def seed_db(n=10):
    departments_objs = list(Department.objects.all())  # Evaluate the queryset

    if not departments_objs:
        print("❌ No departments found. Please add departments before seeding.")
        return

    for _ in range(n):
        department = random.choice(departments_objs)  # SAFE: avoids index error

        student_id = f'STU-{random.randint(100, 999)}'
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(18, 30)
        student_address = fake.address()

        student_id_obj = StudentID.objects.create(student_id=student_id)

        Student.objects.create(
            department=department,
            student_id=student_id_obj,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address,
        )

    print(f"✅ Successfully seeded {n} students.")
