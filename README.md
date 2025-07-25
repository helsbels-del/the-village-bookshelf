# The Village Bookshelf

## Table of Contents

- [Corrections Checklist (Resubmission)](#corrections-checklist-resubmission)
- [Admin Access](#admin-access)
- [Project Overview](#project-overview)  
- [Wireframes and Design](#wireframes-and-design)  
  - [Homepage Redesign](#homepage-redesign)  
  - [Logo and Branding](#logo-and-branding)  
  - [Visual and Layout Changes](#visual-and-layout-changes)  
  - [About Page](#about-page)  
  - [User Info and Login Experience](#user-info-and-login-experience)  
  - [Sign Up and Logged-In Pages](#sign-up-and-logged-in-pages)  
  - [Book Detail Page and Swap Feature](#book-detail-page-and-swap-feature)  
  - [Book Management (Add, Edit, Delete)](#book-management-add-edit-delete)  
  - [Logging Out](#logging-out)  
- [Agile Planning](#agile-planning)  
- [User Stories](#user-stories)  
- [Features](#features)  
- [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)  
- [Technologies Used](#technologies-used)  
- [Prerequisites](#prerequisites)  
- [Local Setup Steps](#local-setup-steps)  
- [Deployment to Heroku](#deployment-to-heroku)  
- [Testing](#testing) 
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

## Corrections Checklist (Resubmission)

This project is a resubmission.
The table below outlines how each item of feedback from the original assessment has been addressed, or see a pdf version in the link..

[Correction checklist (PDF)](/static/images/Corrections-checklist-Assessor-Feedback.pdf)

### Layout / UX (LO1)

| Feedback                                     | Addressed?                                                                                  |
|---------------------------------------------|----------------------------------------------------------------------------------------------|
| Scrollable book section too small, especially on mobile | ✅ Replaced with a clearly listed book list and mobile-friendly cards                    |
| Navigation inconsistent across pages         | ✅ Base template ensures consistent header/footer/navigation                               |
| Sign-up form not working                     | ✅ Fixed and tested with validation, now documented in TESTING.md                         |
| PEP8 issues in `views.py`                   | ✅ Re-validated, passed, and screenshots provided                                          |
| Signup bugs blocked testing of swap          | ✅ Fully tested and documented in both README and TESTING.md                              |

---

### Authentication & Permissions (LO3)

| Feedback                                     | Addressed?                                                                                  |
|---------------------------------------------|----------------------------------------------------------------------------------------------|
| Signup didn’t work                           | ✅ Fixed and proven via manual testing                                                     |
| No way to test swaps                         | ✅ Now possible and tested                                                                 |
| Permissions (e.g., users can't access edit/delete of others’ books) | ✅ Access control tested with examples in TESTING.md                       |
| Login state not clearly shown                | ✅ Added dynamic login status badge ("Guest" or username shown)                           |

---

### Agile Planning (LO1.5, LO1.6, LO1.12)

| Feedback                                     | Addressed?                                                                                  |
|---------------------------------------------|----------------------------------------------------------------------------------------------|
| No clear sprint separation                   | ✅ Two GitHub project boards now reflect Sprint 1 and resubmission sprint                  |

### Debug Mode and Security Correction

In the original submission, `DEBUG = True` and environment variables were mistakenly committed to the repository. This has since been fully corrected:

- All sensitive values have been moved to a `.env` file
- `.env` is included in `.gitignore` and no longer tracked
- `DEBUG` is set using environment variables (`DEBUG = os.getenv("DEBUG") == "True"`)
- The live deployment uses `DEBUG = False` and secure configuration

Note: Earlier Git commits may still contain `DEBUG = True`. These are no longer present in the current codebase, and this issue has been fully addressed as part of the resubmission.

## Project Overview

**The Village Bookshelf** is a Django web app that allows community members to list, browse, and swap books with each other. Designed with a focus on sustainability and local literacy, it provides a simple way to share books and connect readers.

- [Live Site](https://the-village-bookshelf-96bd2f93fc5e.herokuapp.com/)
- [GitHub Repository](https://github.com/helsbels-del/the-village-bookshelf)

## Admin Access

To test admin features (e.g. approving swap requests or verifying book entries), use the following credentials:

- **Admin Login:** HelsBels
- **Password:** Chester20c

[Admin Panel](https://the-village-bookshelf-96bd2f93fc5e.herokuapp.com/admin/)

## Am I Responsive Image

This shows how my home page looks on different screen sizes.

![Am I responsive](/static/images/amiresponsive.png)


## Wireframes and design

As part of the planning for my 4th project, The Village Bookshelf, once I had decided what I was going to do I used the Balsamiq wireframes technology to help design my website pages.

[View Wireframes (PDF)](/static/images/The-Village-Bookshelf-wireframes.pdf)

### Wireframes and Design

As I began building **The Village Bookshelf**, my design evolved significantly from the original wireframes.

---

#### Homepage Redesign

I realised early on that users should be able to browse the available books without needing to log in. To support this, I changed the homepage to include a preview book list that displays the latest 10 added books that the new user can see straight away on the homepage. There is then a link under this book list to take the user to the all books list.

I also added a spyglass icon to each page, other than the home page, after the Nav bar, so that the user can head back to the search bar located on the home page from any other of the main pages.

![home page mobile](/static/images/home-page-mobile.png)

---

#### Logo and Branding

The images from my original wireframes didn’t translate well into the final layout. I kept the **“books with flowers”** image that I purchased from Etsy. I felt it perfectly represented the feel of a village bookshelf. This image became my:

- Main logo  
- Favicon  
- Visual centrepiece, placed above the site title on all pages  

![logo image](/static/images/logo.png)

I styled the title of the site with an overline to resemble a shelf, with the books and flowers sitting above it to create a warm, rustic feel.

The mobile view has one flower image, as the screen sizes gets above 640px wide, it increases to 3 flower images to better fill the space.

![Logo and title large screens](/static/images/logo-title-large.png)

![logo and title mobile](/static/images/logo-title-mobile.png)

---

#### Visual and Layout Changes

- I removed the open book image used in the original mockup.
- I added a **village background image** to reinforce the community theme.
- I applied a **transparency overlay** to make text more readable on top of the background.
- Navigation buttons on the homepage were updated — I replaced the “Book” button with a **Sign Up** button.
- I added a search bar in this hero section which is now only on the homepage.
- There is also a welcome message here.

![village background image with searchbar](/static/images/village-background.png)

---

#### About Page

The **About page**, as well as all other pages, has the same header and footer design as the homepage.

![header](/static/images/header-mobile.png) 


![footer](/static/images/footer-mobile.png)

 As the user clicks through the different pages,
 only the main content changes. This is achieved by using {% block content %}
 and {% endblock %} tags on the base.html page between the header and footer
 and then all other html pages wrap their content in the same block content tags.

 ![about-page](/static/images/about-mobile.png)

The page includes:

- A description of the platform  
- Buttons to return to **Home**, **Login**, or **Sign Up** (the same nav bar in the header).
- The spyglass icon for quick access to the search bar.

![spyglass](/static/images/spyglassonly.png)

---

#### User Info and Login Experience

To improve the user experience, I added a **login status message** to the top-right corner of each page. This displays either:

- `Guest` when users are not logged in  

![tag guest](/static/images/tag-guest.png)

- `{username}` for users who are logged in

![tag user logged in](/static/images/tag-loggedin.png)

On the **Login page**, users enter their username and password. 

![login-page](/static/images/login.png)

If incorrect details are entered, a clear error message is shown.

![incorrect details message](/static/images/incorrect-details-message.png)

If a box if left empty, a clear error message is shown.

![empty-field-message](/static/images/empty-field-message.png)


 This page also includes buttons for:

- Forgot Password? 
- create an account

![forgot password and create account links](/static/images/forgot-password-create-account.png)

---

#### Sign Up and Logged-In Pages

On the **Sign Up page**,

![sign up page](/static/images/sign-up-page.png)

users can create an account with a username, email, and password. 
After successful registration, 

![signup-welcome-message](/static/images/signup-welcome-message.png)

they're redirected to the **Book List** page.

![signed in page](/static/images/signed-in-page.png)

Here, logged-in users:

- See a personalised welcome message  
- Can view all available books  
- Have options to **Add Book**, **Logout**, or visit **About**  
- Can click on any book to access the **Book Detail page**  

---

#### Book Detail Page and Swap Feature

On the **Book Detail** page:

- Guests can view book details but must log in to request a swap  
- Logged-in users see a **Request Swap** button  
- Book owners see options to **Edit**, **Delete**, or **Back to Book List**, along with a message confirming that they own the book  

![book detail guest](/static/images/book-detail-guest.png)

![book detail logged in](/static/images/book-detail-loggedin.png)

![back to booklist button mobile](/static/images/back-to-booklist-mobile.png)

 Note: On the Book Detail page, the "Request Swap" button has slightly different styling at screen widths around 502px.
 This is due to differences in how `<button>` elements render compared to `<a>` tags.
 I preserved this minor difference as it did not impact functionality or user experience, and I prioritized final testing and responsiveness for submission.


If a user requests a swap:

- A success message appears: `Your swap request has been sent!`  

![swap request success message](/static/images/swaprequest-success-message.png)

- Repeat requests show: `You have already requested this book`  

![book already requested message](/static/images/already-requested.png)


#### Book Management (Add, Edit, Delete)

Logged-in users can:

- Add a new book using the **Add Book** button  

![add book button](/static/images/add-book-btn.png)

- Fill in a form and save the details  

![add book form](/static/images/add-book-form.png)

- See a success message: `Your book has been added successfully!`  

![book added success message](/static/images/book-added-success-message.png)

Book owners can:

- Edit or delete their books from the book list when logged in

![User edit and delete links](/static/images/user-edit-delete.png)

- On editing, a success message confirms the update 

![book details updated success message](/static/images/book-details-saved.png)

- On deleting, users are asked for confirmation that they want to delete.

![confirm deletion message](/static/images/confirm-deletion.png)

 If they select cancel, they are taken back to the booklist.

 If they choose delete, they receive a success message
 and then directed back to the booklist.

![book deleted success message](/static/images/book-deleted-success.png)

---

#### Logging Out

When a user logs out:

- They are taken to a **“Logged Out” page** and a `you have been logged out successfully` message flashes up for a few seconds and then disappears.
This is a feature of all the success messages.

![logged out success message](/static/images/logged-out-success.png)

![logged out message](/static/images/loggedout.png)

- The login status updates to `Guest` in the top right corner tag.

- Navigation options include **Login Again** and **Return to Home**


## Agile Planning

This project followed Agile methodology using GitHub Issues and a Project Board.

I created detailed user stories, each linked to a GitHub issue.

Each issue included clear acceptance criteria to guide development and testing.

I used a Kanban board with columns for Todo, In Progress, and Done to visualise work.

I regularly updated the board to reflect the current progress and moved cards between columns as tasks were started or completed.

![agile progress 1](/static/images/agile_1.png)

![agile progress 2](/static/images/agile_2.png)

![agile progress 3](/static/images/agile_3.png)

![agile progress 4](/static/images/agile_4.png)

Agile planning took place across two sprints:

Sprint 1: June 24 – June 30

Sprint 2: July 1 – July 11 (resubmission)

I also used the corrections window as an opportunity to reflect on assessor feedback and implement improvements based on previous gaps. These included:

- Registering the SwapRequest model in the Django admin

- Adding user feedback messages for CRUD actions (this was already there but was not working due to the sign up bugs that were there).

- Securing unauthenticated routes with proper decorators (this was already there but was not working due to the sign up bugs that were there).

- Fixing signup bugs and form layout

- Improving mobile responsiveness and layout consistency

- Enhancing documentation for manual testing and deployment security

[View the GitHub Project Board](https://github.com/users/helsbels-del/projects/9)

[View the GitHub Project Board for re submission](https://github.com/users/helsbels-del/projects/10/views/1)


## User Stories

### Epic - Sign-up and Authentication

**User Story: Signup**
As a new user,  
I want to sign up for an account,  
So that I can request and swap books.

**Acceptance Criteria**
- [ ] I can fill out and submit a signup form
- [ ] A new user is created in the database
- [ ] I am redirected and shown a confirmation message
- [ ] Invalid form inputs trigger clear error messages

### Epic - Access Control

**User Story: Restricted Access for Unauthenticated Users**
As a visitor,  
I want to be prevented from accessing protected pages,  
So that unauthorized actions can’t be taken.

**Acceptance Criteria**
- [ ] Swap request pages are restricted to logged-in users
- [ ] Edit/delete actions require authentication
- [ ] Direct URL access to protected routes is blocked
- [ ] Redirect or login prompt is shown if not authenticated

### Epic - Admin Panel: Swap Request

**User Story: Admin Access to Swap Requests**
As a site administrator,  
I want to view and manage swap requests in the admin panel,  
So that I can monitor and troubleshoot user activity.

**Acceptance Criteria**
- [ ] SwapRequest model is registered in `admin.py`
- [ ] Admin panel displays swap requests clearly
- [ ] Admin can filter or manage requests if needed

### Epic - Feedback for CRUD Actions

**User Story: User Feedback for Actions**

As a user,  
I want confirmation messages when I perform actions,  
So that I know whether the action was successful.

**Acceptance Criteria**

- [ ] A success message is shown after adding a book
- [ ] A confirmation message is shown after editing or deleting
- [ ] Errors (e.g. invalid forms) show helpful feedback
- [ ] Messages are consistent across the site

### Epic - UX/Layout Fix

**User Story: Browse Books Easily**

As a user,  
I want to browse books without cramped or confusing scroll areas,  
So that I can explore available books more comfortably.

**Acceptance Criteria**

- [ ] Book list is clearly visible and now a list rather than a scroll bar.
- [ ] Layout works well on desktop and mobile
- [ ] All books are shown on a separate page with more space

### Epic - Mobile Responsiveness

**User Story: Mobile-Friendly Design**

As a mobile user,  
I want the site layout to adjust to my screen size,  
So that I can use the site without layout issues.

**Acceptance Criteria**

- [ ] Navigation, buttons, and forms are accessible on small screens
- [ ] Book cards resize and stack appropriately
- [ ] No content is cut off or requires horizontal scrolling

### Epic - Testing and Validation

**User Story: Documented Manual Testing**

As a developer,  
I want to clearly document testing steps and outcomes,  
So that others can verify that features work as expected.

**Acceptance Criteria**

- [ ] Manual test table includes feature, steps, expected result, actual result
- [ ] Screenshots of test outcomes are included
- [ ] HTML and PEP8 validation results are shown and explained

### Epic - Environment Security

**User Story: Secure Deployment**

As a developer,  
I want to hide sensitive information,  
So that secrets like API keys or the Django secret key are not exposed.

**Acceptance Criteria**

- [ ] `.env` file is excluded from version control via `.gitignore`
- [ ] Environment variables are accessed using `os.environ`
- [ ] `DEBUG` is set to `False` in production

## Features

### User Authentication & Session Management

- Users can register with a username, email, and password.
- Login uses Django's authentication system with session management.
- Error messages are shown for incorrect credentials or missing fields.
- Secure logout with session cleared and feedback provided.
- Unauthenticated users are restricted from protected views via `@login_required`.

### Book Management

- Logged-in users can:
  - Add books via a form (title, author, description, genre, availability).
  - Edit or delete only their own books.
  - See confirmation messages for all actions (add/edit/delete).
- Guests can view book details but cannot modify or swap.
- Book owners cannot request their own books.

### Swap Requests

- Logged-in users can request a book from the Book Detail page.
- Duplicate requests are prevented with a feedback message.
- Book owners are notified by email when a swap is requested.

### Search and Browse

- Search bar is accessible on all pages (in the hero section).
- Search matches title or author.
- Users can browse:
  - A preview list of the 10 most recent books (on the home page).
  - The full book list from the nav button at the bottom of the latest available books list.

### Responsive Layout & Design

- Mobile-first design with breakpoints for 320px, 768px, 1024px, and 1440px+.
- Key features include:
  - Responsive header with logo and title that adapts across devices.
  - Navigation bar that changes based on login status.
  - Book preview list of latest 10 added books, with clickable book cards.
  - Consistent layout using `base.html` with `{% block content %}`.
  - Background imagery and branding to create a rustic, village feel.

![Responsive Header Example](/static/images/header-mobile.png)

![Responsive Header Example](/static/images/header-large.png)

![Book List mobile](/static/images/booklist-mobile.png)

![Book List large](/static/images/booklist-1024.png)

### Navigation & User Flow

- Spyglass icon allows quick access to search bar from any page.
- Navigation adjusts based on user status (guest vs. logged in).
- Logo is a clickable link to return to the home page.
- Footer remains consistent across all pages for clarity and cohesion.

![nav bar mobile](/static/images/nav-mobile.png)

![nav bar medium](/static/images/nav-medium.png)

![nav bar large](/static/images/nav-large.png)

---

## Entity Relationship Diagram (ERD)

### Book Model

| Field         | Type             | Description              |
|---------------|------------------|--------------------------|
| `title`       | CharField(255)   | Book title               |
| `author`      | CharField(255)   | Author name              |
| `genre`       | CharField(255)   | Book genre               |
| `condition`   | ForeignKey       | Condition of the book    |
| `owner`       | ForeignKey       | Who owns the book        |
| `is_available`| BooleanField     | Is it available          |
| `added_date`  | DateTimeField    | When it was added        |

---

### SwapRequest Model

| Field          | Type             | Description                          |
|----------------|------------------|--------------------------------------|
| `requester`     | ForeignKey       | User requesting the book             |
| `book`          | ForeignKey       | The book being requested             |
| `request_date`  | DateTimeField    | Date/time the swap request was made |

---

### Relationships Summary

- One **User** can own many **Books**
- One **Book** can have many **SwapRequests**
- Each **SwapRequest** links one **User** (as requester) to one **Book**

## Technologies Used

- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS  
- **Database**: SQLite (development), PostgreSQL (production)  
- **Version Control**: Git and GitHub  
- **Hosting**: Heroku  

---

## Prerequisites

Before running the project locally, ensure you have:

- Python 3.12.3  
- pip  
- Virtual environment (e.g. `venv`)  
- Visual Studio Code or another IDE 
- Git and GitHub account 

---

## Local Setup Steps

1. **Clone the repository** 

    To get a local copy of the project, use the following command:

    ```bash
    git clone https://github.com/helsbels-del/village-bookshelf.git

2. **Create and activate a virtual environment**

    python -m venv venv
    venv\Scripts\activate

3. **Install dependencies**

    pip install -r requirements.txt

4. **Apply migrations and set up the database**

    python manage.py migrate

5. **Create a **superuser**

    python manage.py createsuperuser

6. **Run the development server**

   python manage.py runserver

## Deployment to Heroku

1. **Install Heroku-specific dependencies**

    pip install gunicorn dj-database-url psycopg2-binary whitenoise

2. **Update settings.py**

    - Add this to configure the database

    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost')
    }

    - Configure static file handling

    MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',

    ]

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_URL = '/static/'

    - Add allowed hosts

    ALLOWED_HOSTS = ['the-village-bookshelf.herokuapp.com', 'localhost']

3. **Create a Procfile**

    echo "web: gunicorn the-village-bookshelf.wsgi" > Procfile

4. **Generate requirements.txt and runtime.txt**

    pip freeze > requirements.txt
    echo "python-3.12.3" > runtime.txt

5. ** Initialize Git and commit changes

    git init
    git add .
    git commit -m "Prepare for Heroku deployment"

6. **Deploy to Heroku (via Dashboard)**

This project was deployed using **Heroku’s GitHub integration** rather than the CLI.

### Steps Taken

1. Pushed final code to GitHub repository.

2. Logged in to [Heroku Dashboard](https://dashboard.heroku.com).

3. Created a new app: `the-village-bookshelf`.

4. Connected the app to the GitHub repository.

5. Automatic deployment was not enabled.

6. Configured environment variables (via Heroku Settings):

   - `SECRET_KEY`

   - `ALLOWED_HOSTS`

   - `DATABASE_URL`

   - `EMAIL_HOST_USER`

   - `EMAIL_HOST_PASSWORD`

7. Set buildpacks and added `gunicorn`, `whitenoise`, and `dj-database-url` in `requirements.txt`.

8. Ran `collectstatic` from the Heroku console.

9. Made sure all data saved and DEBUG is set to False in the settings. Commit and push to git.

10. Go back to heroku site, log back in if required.

11. Go to Deploy tab and head to the bottom of the page to select Deploy Branch.

![deploy success](/static/images/deploy-success.png)

13. Once the deployment is complete you can select the view button at the bottom of the page.

14. Verified successful deployment at: 

   [https://the-village-bookshelf-96bd2f93fc5e.herokuapp.com](https://the-village-bookshelf-96bd2f93fc5e.herokuapp.com)


## Testing

Full manual testing steps, screenshots of user journeys (including password reset), validator results, and bug fixes are documented in the  
[TESTING.md](TESTING.md) file.

---

## Future Enhancements

- Admin approval of swap requests via dashboard
- A public-facing user profile page
- Pagination for large book collections
- Messaging system for users to arrange swaps

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [CodeAcademy](https://www.codecademy.com/)
- Slack community support (CI help and feedback)
- My mentor, friends and family for testing and feedback, and for keeping me going.
- I used ChatGPT to help make corrections in code that I couldn't fix by myself and to help create the tick emoji icons used in my readme. [emojipedia](https://emojipedia.org/)
I made sure that I understood any code that ChatGPT helped with. I think it is a very useful tool for checking work however  I think it is important not to rely on it to create the code, I have managed to mainly ask for help when I am stuck.

This is my re submission of project 4 and I can see coming back to it how much I had missed on my initial submission.
I was actually pleased to have the opportunity to resubmit this project, as I have really enjoyed working on it over the past few weeks.
I seem to have a much better understanding of it second time around, and also after project 5 - data analytics, I feel I was more prepared for this.

Thanks to the assessor for the feedback from my original submission which helped me know which areas I needed to improve on.
And thank you for assessing this version too.




 




