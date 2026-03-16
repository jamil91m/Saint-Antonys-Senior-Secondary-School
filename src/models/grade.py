from main import db
from datetime import datetime

class Grade(db.Model):
    """Grade model for storing student grades and marks"""
    __tablename__ = 'grades'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    exam_type = db.Column(db.String(50), nullable=False)  # 'Unit Test', 'Midterm', 'Final', 'Assignment'
    marks_obtained = db.Column(db.Float, nullable=False)
    total_marks = db.Column(db.Float, nullable=False)
    percentage = db.Column(db.Float, nullable=True)
    grade_letter = db.Column(db.String(5), nullable=True)  # 'A+', 'A', 'B', 'C', etc.
    remarks = db.Column(db.Text, nullable=True)
    exam_date = db.Column(db.Date, nullable=False)
    marked_by = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def calculate_percentage(self):
        """Calculate percentage"""
        if self.total_marks > 0:
            self.percentage = (self.marks_obtained / self.total_marks) * 100
        return self.percentage
    
    def assign_grade(self):
        """Assign letter grade based on percentage"""
        percentage = self.calculate_percentage()
        if percentage >= 90:
            self.grade_letter = 'A+'
        elif percentage >= 80:
            self.grade_letter = 'A'
        elif percentage >= 70:
            self.grade_letter = 'B'
        elif percentage >= 60:
            self.grade_letter = 'C'
        else:
            self.grade_letter = 'D'
        return self.grade_letter
    
    def __repr__(self):
        return f'<Grade Student:{self.student_id} Subject:{self.subject} Grade:{self.grade_letter}>'