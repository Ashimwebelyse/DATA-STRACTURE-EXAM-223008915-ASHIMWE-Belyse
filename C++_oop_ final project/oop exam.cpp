#include <iostream>
#include <cstring>
#include <iomanip>  // For setw
#include <cstdio>   // For printf

using namespace std;

struct Score {
    char course[20];
    float mark;
};

class Person {
public:
    virtual void showInfo() = 0;
    virtual ~Person() {}
};

class Student : public Person {
    char id[10];
    Score* scores;
    int scoreCount;

public:
    Student(const char* _id, Score* _scores, int _count) {
        strcpy(id, _id);
        scoreCount = _count;
        scores = new Score[scoreCount];
        for (int i = 0; i < scoreCount; ++i)
            scores[i] = _scores[i];
    }

    ~Student() {
        delete[] scores;
    }

    float computeGPA() {
        float total = 0;
        Score* ptr = scores;
        for (int i = 0; i < scoreCount; ++i)
            total += (ptr + i)->mark;
        return scoreCount ? total / scoreCount : 0;
    }

    void showInfo() override {
        cout << "ID: " << id << "\nCourses:\n";
        for (int i = 0; i < scoreCount; ++i)
            printf(" - %-15s : %.2f\n", scores[i].course, scores[i].mark);
        printf("GPA: %.2f\n\n", computeGPA());
    }

    const char* getId() const {
        return id;
    }
};

Person** people = nullptr;
int personCount = 0;

void addStudent(Student* student) {
    Person** temp = new Person*[personCount + 1];
    for (int i = 0; i < personCount; ++i)
        temp[i] = people[i];
    temp[personCount] = student;
    delete[] people;
    people = temp;
    personCount++;
}

void removeStudent(const char* id) {
    int index = -1;
    for (int i = 0; i < personCount; ++i) {
        Student* s = dynamic_cast<Student*>(people[i]);
        if (s && strcmp(s->getId(), id) == 0) {
            index = i;
            break;
        }
    }
    if (index == -1) {
        cout << "Student with ID " << id << " not found.\n";
        return;
    }

    delete people[index];
    Person** temp = new Person*[personCount - 1];
    for (int i = 0, j = 0; i < personCount; ++i) {
        if (i != index)
            temp[j++] = people[i];
    }
    delete[] people;
    people = temp;
    personCount--;
    cout << "Student removed.\n";
}

void inputAndAddStudent() {
    char id[10];
    int numCourses;

    cout << "Enter Student ID (max 9 chars): ";
    cin >> setw(10) >> id;
    cout << "Enter number of courses: ";
    cin >> numCourses;

    Score* scores = new Score[numCourses];
    for (int i = 0; i < numCourses; ++i) {
        cout << "Enter course name (max 19 chars): ";
        cin >> setw(20) >> scores[i].course;

        do {
            cout << "Enter mark (0–100): ";
            cin >> scores[i].mark;
            if (scores[i].mark < 0 || scores[i].mark > 100)
                cout << "Invalid mark. Please try again.\n";
        } while (scores[i].mark < 0 || scores[i].mark > 100);
    }

    Student* s = new Student(id, scores, numCourses);
    addStudent(s);
    delete[] scores; // No memory leak — already copied into Student
}

void showAllStudents() {
    if (personCount == 0) {
        cout << "No students available.\n";
        return;
    }

    for (int i = 0; i < personCount; ++i)
        people[i]->showInfo();
}

int main() {
    int choice;
    do {
        cout << "\n--- Student Grading System ---\n";
        cout << "1. Add Student\n";
        cout << "2. Remove Student\n";
        cout << "3. Show All Students\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                inputAndAddStudent();
                break;
            case 2: {
                char id[10];
                cout << "Enter student ID to remove: ";
                cin >> setw(10) >> id;
                removeStudent(id);
                break;
            }
            case 3:
                showAllStudents();
                break;
            case 4:
                cout << "Goodbye!\n";
                break;
            default:
                cout << "Invalid choice.\n";
        }
    } while (choice != 4);

    // Cleanup
    for (int i = 0; i < personCount; ++i)
        delete people[i];
    delete[] people;

    return 0;
}

