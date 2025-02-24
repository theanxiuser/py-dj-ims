# Online Course Management System (OCMS) with Multiple-Choice Question (MCQ) Based Assessment

Key features, that need to develop

### Course Management
- Instructors can create and manage courses with basic details like title and description.
- Student can enroll in available courses

### MCQ Management
- Create MCQs for specific course
- Automatically **grade**/display marks after submission


### User Management
- Student and Instructor registration and login (custom auth)
- Role based access

### ++++++++++++

===============
1. Using templates
2. Using APIs


### Use case
Actor = Instructor, Student,Admin
Tasks = ?


### DB

CustomUser:
    role (student, instructor): Enum
    username: String
    password: String
    email:String
    first_name: String
    last_name: String

Profile
    user: CustomUser (One to One)
    bio: String
    image: String
    phone: String

Course
    title: String
    description: String
    instructor: CustomUser (Many to One) (role = instructor)
    students: CustomUser (Many to Many) (role = student)

MCQs
    course: Course (Many to One)
    question: String
    op1: String
    op2: String
    op3: String
    op4: String
    correct_op: touple

Response
    student: CustomUser (Many to One)
    mcq: MCQs (Many to One)
    selected_op: touple
    is_correct: Boolean


### WebApps
- userauth
- course

### Project
- OCMS


### Relevant Configs
- AUTH_USER_MODEL
- LOGIN_REDIRECT_URL
- LOGOUT_REDIRECT_URL
- STATIC_URL
- STATICFILES_DIRS = []
- MEDIA_URL
- MEDIA_ROOT

### Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app -> home

templates
    - base.html
    home
        - index.html
    auth
        - login.html
        - registration.html