#!/usr/bin/env python3
"""
Script to view database contents
"""
import sqlite3
from database import get_connection, init_db
import os

def view_all_data():
    """Display all students and grades from the database"""
    
    # Initialize database if needed
    init_db()
    
    # Get connection
    conn = get_connection()
    cursor = conn.cursor()
    
    print("=" * 80)
    print("DATABASE CONTENTS - STUDENT PERFORMANCE TRACKER")
    print("=" * 80)
    
    # Get all students
    cursor.execute("SELECT roll_number, name FROM students ORDER BY roll_number")
    students = cursor.fetchall()
    
    print(f"\n📊 TOTAL STUDENTS: {len(students)}")
    print("-" * 80)
    
    if students:
        for student in students:
            roll, name = student
            print(f"\n👤 Student: {name}")
            print(f"   Roll Number: {roll}")
            
            # Get grades for this student
            cursor.execute("""
                SELECT subject, grade 
                FROM grades 
                WHERE roll_number = ? 
                ORDER BY subject
            """, (roll,))
            grades = cursor.fetchall()
            
            if grades:
                print("   📝 Grades:")
                for subject, grade in grades:
                    print(f"      • {subject}: {grade}/100")
                
                # Calculate average
                total = sum(g[1] for g in grades)
                avg = total / len(grades)
                print(f"   📊 Average: {avg:.2f}/100")
            else:
                print("   📝 No grades entered yet")
    
    # Summary statistics
    print("\n" + "=" * 80)
    print("📈 SUMMARY STATISTICS")
    print("=" * 80)
    
    # Get grade statistics
    cursor.execute("""
        SELECT subject, 
               COUNT(*) as student_count,
               ROUND(AVG(grade), 2) as avg_grade,
               MAX(grade) as max_grade,
               MIN(grade) as min_grade
        FROM grades
        GROUP BY subject
        ORDER BY subject
    """)
    
    subject_stats = cursor.fetchall()
    
    if subject_stats:
        print("\nSubject-wise Statistics:")
        for subject, count, avg_grade, max_grade, min_grade in subject_stats:
            print(f"\n📚 {subject}:")
            print(f"   • Students: {count}")
            print(f"   • Class Average: {avg_grade}/100")
            print(f"   • Highest Score: {max_grade}/100")
            print(f"   • Lowest Score: {min_grade}/100")
    
    # Database file info
    print("\n" + "=" * 80)
    print("💾 DATABASE FILE INFO")
    print("=" * 80)
    db_path = os.path.abspath("students.db")
    file_size = os.path.getsize("students.db") if os.path.exists("students.db") else 0
    print(f"\nLocation: {db_path}")
    print(f"Size: {file_size / 1024:.2f} KB")
    
    conn.close()

if __name__ == "__main__":
    view_all_data()
