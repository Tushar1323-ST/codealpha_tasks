import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# 100 FAQ QUESTIONS
# =========================

faqs = [
    ("What are the college timings?", "College timing is 9 AM to 5 PM."),
    ("When does college start?", "College generally starts at 9 AM."),
    ("When does college close?", "College generally closes at 5 PM."),
    ("How can I apply for admission?", "You can apply through the official admission process."),
    ("What courses are available?", "Various engineering courses are available."),
    ("How can I contact the college?", "You can contact the college office during working hours."),
    ("What is the college address?", "Please check the official college website for the address."),
    ("Where is the admission office?", "The admission office is located on the college campus."),
    ("What documents are required for admission?", "Academic certificates, identity proof and other required documents are needed."),
    ("Is there an admission form?", "Yes, students need to complete the required admission form."),

    ("What is the fee structure?", "The fee structure depends on the course and category."),
    ("How can I pay college fees?", "Fees can be paid through the available college payment methods."),
    ("Is online fee payment available?", "Please check with the college accounts department."),
    ("Is scholarship available?", "Scholarships may be available for eligible students."),
    ("Who can apply for scholarship?", "Eligible students can apply according to scholarship rules."),
    ("Where can I apply for scholarship?", "Students can apply through the applicable scholarship portal."),
    ("What is the scholarship deadline?", "The deadline depends on the scholarship scheme."),
    ("Is an income certificate required?", "An income certificate may be required for some scholarships."),
    ("Is caste certificate required?", "It may be required for category-based benefits."),
    ("Is caste validity required?", "Caste validity may be required for applicable category benefits."),

    ("Is attendance compulsory?", "Students are expected to maintain the required attendance."),
    ("What is the minimum attendance?", "The minimum attendance requirement depends on university and college rules."),
    ("What happens if attendance is low?", "Students with low attendance may face academic restrictions."),
    ("Can I take leave?", "Yes, students can take leave according to college rules."),
    ("How can I apply for leave?", "Submit a leave application through the prescribed college process."),
    ("Who is the class teacher?", "Please check your department notice or class group."),
    ("Where is the department office?", "The department office is located in the respective department building."),
    ("How can I contact my department?", "You can contact the department office during working hours."),
    ("Are practical classes conducted?", "Yes, practical classes are conducted as part of engineering courses."),
    ("Are theory classes conducted?", "Yes, theory classes are conducted according to the timetable."),

    ("What is the exam pattern?", "The exam pattern depends on the university and course regulations."),
    ("When are semester exams conducted?", "Semester exams are conducted according to the academic schedule."),
    ("Where can I find the exam timetable?", "The exam timetable is generally published through official notices."),
    ("What is internal assessment?", "Internal assessment evaluates students during the semester."),
    ("What are internal marks?", "Internal marks are awarded through tests, assignments and other activities."),
    ("What is a practical exam?", "A practical exam evaluates practical knowledge and laboratory skills."),
    ("What is a theory exam?", "A theory exam evaluates theoretical knowledge of the subject."),
    ("Can I apply for revaluation?", "Revaluation may be available according to university rules."),
    ("What is a backlog?", "A backlog is a subject that a student has not successfully cleared."),
    ("Can backlog subjects be cleared later?", "Yes, students can clear backlog subjects according to university rules."),

    ("Is there a library?", "Yes, the college has a library facility."),
    ("What are the library timings?", "Library timings are according to the college schedule."),
    ("Can students borrow books?", "Yes, eligible students can borrow books using library facilities."),
    ("How many books can I issue?", "The number of books depends on library rules."),
    ("Can I renew a library book?", "Book renewal may be available according to library rules."),
    ("Is there a digital library?", "Digital library facilities may be available to students."),
    ("Is there a computer lab?", "Yes, computer laboratory facilities are available."),
    ("Is WiFi available in college?", "WiFi availability depends on the campus facilities."),
    ("Are laboratories available?", "Yes, laboratories are available for engineering departments."),
    ("Can students use the computer lab?", "Students can use the computer lab according to lab schedules."),

    ("Is hostel facility available?", "Hostel availability depends on the college campus."),
    ("How can I apply for hostel?", "Hostel applications can be submitted through the college hostel office."),
    ("Is hostel available for first year students?", "Availability depends on hostel capacity and college rules."),
    ("Is mess facility available?", "Mess facilities may be available for hostel students."),
    ("Is transportation available?", "Transportation facilities depend on the college."),
    ("Are buses available?", "College bus availability depends on the transport facility."),
    ("Is parking available?", "Parking facilities are subject to campus rules and availability."),
    ("Is there a canteen?", "A canteen facility may be available on campus."),
    ("Is there a sports ground?", "Sports facilities depend on the college campus."),
    ("Are sports activities conducted?", "Yes, colleges generally conduct various sports activities."),

    ("Is there a placement cell?", "Yes, engineering colleges generally have a training and placement cell."),
    ("What does the placement cell do?", "The placement cell coordinates training, internships and recruitment activities."),
    ("Are campus placements available?", "Campus placement opportunities depend on company participation."),
    ("Are internships available?", "Students can apply for internships through college and external opportunities."),
    ("When does placement training start?", "Placement training schedules depend on the college."),
    ("What skills are needed for placement?", "Technical skills, communication, aptitude and problem-solving skills are useful."),
    ("Are coding classes conducted?", "Coding training may be provided through courses or placement programs."),
    ("Are aptitude classes conducted?", "Aptitude training may be conducted as part of placement preparation."),
    ("Can first year students do internships?", "Students can apply for suitable internships based on eligibility."),
    ("Can students participate in industrial visits?", "Industrial visits may be organized by departments."),

    ("What is Artificial Intelligence?", "Artificial Intelligence enables computers to perform tasks requiring human-like intelligence."),
    ("What is Machine Learning?", "Machine Learning allows computers to learn patterns from data."),
    ("What is Data Science?", "Data Science involves collecting, analyzing and interpreting data."),
    ("Which programming language is useful for AI?", "Python is commonly used for AI and data science."),
    ("Is Python taught in engineering?", "Python may be included depending on the curriculum and branch."),
    ("Is C programming taught?", "C programming is commonly included in engineering fundamentals."),
    ("What is a database?", "A database is an organized collection of data."),
    ("What is SQL?", "SQL is a language used to work with relational databases."),
    ("What is programming?", "Programming is the process of creating instructions for a computer."),
    ("What is NLP?", "NLP stands for Natural Language Processing and helps computers work with human language."),

    ("What is an assignment?", "An assignment is academic work given to students for practice and evaluation."),
    ("Are assignments compulsory?", "Assignments may be compulsory according to subject and college rules."),
    ("What is a mini project?", "A mini project is a small practical project completed by students."),
    ("What is a final year project?", "A final year project is a major project completed as part of engineering."),
    ("Can students work in teams?", "Students may work in teams according to project requirements."),
    ("What is a seminar?", "A seminar is a presentation or discussion on an academic topic."),
    ("What is a workshop?", "A workshop provides practical learning about a particular topic or skill."),
    ("Are technical events conducted?", "Technical events may be organized by departments and student clubs."),
    ("Are cultural events conducted?", "Cultural events may be organized by the college."),
    ("Are student clubs available?", "Student clubs may be available for technical and cultural activities."),

    ("How can I get my identity card?", "Contact the college office for the student identity card process."),
    ("What is a bonafide certificate?", "A bonafide certificate confirms that a student is studying at the institution."),
    ("How can I get a bonafide certificate?", "Apply through the college office or prescribed student service."),
    ("How can I get a leaving certificate?", "Contact the college office and follow the required procedure."),
    ("How can I get a transcript?", "Transcript requests can be made through the college administration office."),
    ("Where can I submit documents?", "Documents should be submitted to the concerned college office."),
    ("How can I update my student information?", "Contact the administration office for information updates."),
    ("Who should I contact for academic issues?", "Contact your department or academic office."),
    ("Who should I contact for fee issues?", "Contact the accounts department for fee-related issues."),
    ("Who should I contact for hostel issues?", "Contact the hostel office or hostel administration.")
]

# Separate questions and answers
questions = [item[0] for item in faqs]
answers = [item[1] for item in faqs]

# Convert questions into numbers
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


# =========================
# CHATBOT FUNCTION
# =========================

def get_answer():

    user_question = entry.get().strip()

    if user_question == "":
        messagebox.showwarning(
            "Warning",
            "Please enter your question."
        )
        return

    # Convert user question into vector
    user_vector = vectorizer.transform(
        [user_question]
    )

    # Calculate similarity
    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    # Find best matching question
    best_match = similarity.argmax()

    # Get answer
    answer = answers[best_match]

    # Display conversation
    chat_box.insert(
        tk.END,
        "You: " + user_question + "\n"
    )

    chat_box.insert(
        tk.END,
        "Bot: " + answer + "\n\n"
    )

    # Clear input box
    entry.delete(0, tk.END)

    # Scroll to bottom
    chat_box.see(tk.END)


# =========================
# CLEAR CHAT
# =========================

def clear_chat():

    chat_box.delete(
        "1.0",
        tk.END
    )


# =========================
# MAIN WINDOW
# =========================

window = tk.Tk()

window.title(
    "AI FAQ Chatbot"
)

window.geometry(
    "750x650"
)


# Heading
title = tk.Label(
    window,
    text="AI FAQ Chatbot",
    font=("Arial", 22, "bold")
)

title.pack(
    pady=15
)


# Information
info = tk.Label(
    window,
    text="Ask questions about college, admission, fees, exams, library, hostel, placements, AI, etc.",
    font=("Arial", 10)
)

info.pack(
    pady=5
)


# Chat area
chat_box = tk.Text(
    window,
    height=25,
    width=80,
    font=("Arial", 11)
)

chat_box.pack(
    padx=20,
    pady=10
)


# Bottom frame
bottom_frame = tk.Frame(
    window
)

bottom_frame.pack(
    pady=10
)


# Question input
entry = tk.Entry(
    bottom_frame,
    width=55,
    font=("Arial", 12)
)

entry.pack(
    side=tk.LEFT,
    padx=5
)


# Ask button
ask_button = tk.Button(
    bottom_frame,
    text="Ask",
    command=get_answer,
    font=("Arial", 12, "bold")
)

ask_button.pack(
    side=tk.LEFT,
    padx=5
)


# Clear button
clear_button = tk.Button(
    bottom_frame,
    text="Clear",
    command=clear_chat,
    font=("Arial", 12)
)

clear_button.pack(
    side=tk.LEFT,
    padx=5
)


# Press Enter to ask
entry.bind(
    "<Return>",
    lambda event: get_answer()
)


# Start application
window.mainloop()