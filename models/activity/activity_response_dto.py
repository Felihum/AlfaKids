from models.activity.activity import Activity
from models.subject.subject import Subject
from models.professor.professor import Professor


class ActivityResponseDTO:
    def __init__(self, activity: Activity, subject: Subject, professor: Professor):
        self.id = activity.id
        self.title = activity.title
        self.status = activity.status
        self.id_subject = activity.id_subject
        self.id_professor = activity.id_professor
        self.subject_name = subject.name
        self.professor_name = professor.name

    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "status": self.status,
                "id_subject": self.id_subject,
                "id_professor": self.id_professor,
                "subject_name": self.subject_name,
                "professor_name": self.professor_name}
