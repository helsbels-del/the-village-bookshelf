# Manual Testing & Validation Results – *The Village Bookshelf*

## Table of Contents

- [Introduction](#introduction)
- [Test Environment](#test-environment)
- [Manual Feature Testing](#manual-feature-testing)
- [User Journey Testing](#user-journey-testing)
- [Form Validation](#form-validation)
- [Access Control Testing](#access-control-testing)
- [HTML Validation](#html-validation)
- [CSS Validation](#css-validation)
- [Python Code Validation (PEP8)](#python-code-validation-pep8)
- [Bugs and Fixes](#bugs-and-fixes)
- [Screenshots](#screenshots)

---

## Introduction

This file documents all manual testing and validation performed for **The Village Bookshelf** Django web application. It includes individual feature testing, user journey testing, form validation, and accessibility/security checks.

---

## Test Environment

- **Browser(s):** Chrome, Firefox, Edge
- **Devices tested:** Desktop (2560, 1440, 1024), Tablet (768px), Mobile (425px, 375px, 320px)
- **Tools used:**
  - [W3C HTML Validator](https://validator.w3.org/)
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - [CI Python Linter](https://pep8ci.herokuapp.com/)

---

## Manual Feature Testing

| Feature        | Test Case                                  | Expected Result                              | Actual Result       | 
|----------------|---------------------------------------------|-----------------------------------------------|----------------------|
| Sign Up Form   | Submit with valid inputs                    | User created, redirected to book list         | ✅ Passed            | 
| Login          | Correct username/password                   | Redirected to book list                       | ✅ Passed            | 
| Login          | Incorrect credentials                       | Error message shown                           | ✅ Passed            | 
| Add Book       | Valid input                                 | Book saved and appears in book list           | ✅ Passed            | 
| Edit Book      | Change details and save                     | Book updated                                  | ✅ Passed            | 
| Delete Book    | Confirm deletion                            | Book removed from database                    | ✅ Passed            | 
| Request Swap   | Click on a book you don’t own               | Email sent to owner, message displayed        | ✅ Passed            | 
| Swap Request Again | Click on already requested book        | Message shown: “already requested”            | ✅ Passed            | 
| Logout         | Click logout                               | Redirected to logged-out page                 | ✅ Passed            | 

---

## User Journey Testing

| Journey                                                                 | Outcome                                      | Notes                                                       |
|-------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|
| Sign up → Add Book → Logout → Login again                              | Book remains, user session handled correctly | ✅                                                          |
| Visit book details as guest                                             | Can view book, cannot request swap           | ✅                                                          |
| Try accessing `/add/` when not logged in                                | Redirects to login page                      | ✅                                                          |
| Forgot password → Submit email → Receive reset link (manual check)     | Password reset email received (if configured) | If not configured, manual check of backend / logs accepted |
| Reset password → Enter new password → Login with new password          | Redirected to login → New password works     | ✅                                                          |
| Visit `/edit/` for a book not owned by the user                         | Redirects or shows "not authorized" message  | Confirms ownership logic enforced                          |
| Try to request swap on own book                                         | Swap button not visible                      | Logic enforced in template                                 |
| Submit Add Book with empty fields                                       | Error messages shown                         | Confirms form validation                                   |
| Submit Login with only username (no password)                           | Error shown                                  | ✅                                                         |


---

## Form Validation

| Form             | Empty submission | Invalid data | Correct submission |
|------------------|------------------|--------------|---------------------|
| Sign Up Form     | Error messages shown | Error messages shown | ✅ Pass        |
| Login Form       | Error shown if missing fields | ✅ Pass | ✅ Pass         |
| Add Book         | Error on empty fields | N/A        | ✅ Pass             |

---

## Access Control Testing

| Page                 | Logged In Access | Guest Access | Notes                         |
|----------------------|------------------|--------------|-------------------------------|
| Home                 | ✅                | ✅            | Both see books, but guest limited |
| Book Details         | ✅                | ✅            | Guest cannot request a swap      |
| Add Book             | ✅                | ❌            | Guest is redirected to login     |
| Edit/Delete Book     | ✅ (owner only)   | ❌            | Proper ownership checks enforced |
| Book List            | ✅                | ✅            | Shown with role-appropriate buttons |

---

## HTML Validation

All major pages were tested using the W3C [HTML Validator](https://validator.w3.org/). Minor fixes such as unclosed tags and incorrect nesting were corrected.

- see screenshots below for results. All pages passed. 

---

## CSS Validation

The full `style.css` file was tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

- No errors or warnings detected. See screenshots below.

---

## Python Code Validation (PEP8)

All `.py` files were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/).

- All files passed. See screenshots below.


---

## Bugs and Fixes

| Bug Description | Cause | Fix Applied | Status |
|------------------|-------|-------------|--------|
| Login not working after signup | `@login_required` applied too early in view logic | Re-ordered view logic and added conditional decorators | ✅ Fixed |
| Sign up form layout broken | Missing form-control classes and incorrect template structure | Updated `signup.html` to use form fields directly | ✅ Fixed |
| Book cards misaligned at 1440px | Container width too narrow | Added a wider max-width and media query for 1440px+ | ✅ Fixed |
| Navigation buttons shifted on mobile | Padding/margin not responsive | Added media queries to adjust layout | ✅ Fixed |
| Guest could access `/add/` via direct URL | Missing `@login_required` decorator | Added decorator to view | ✅ Fixed |
| Swap request success message not showing | Logic error in message tags or redirect | Fixed logic to ensure message loads after redirect | ✅ Fixed |


---

## Screenshots

Screenshots for all responsive breakpoints, features, and validation results are available in the `/static/images` folder and referenced below or in the [README.md](README.md).

### Responsive Layout

- Mobile View (375px)

  ![Mobile homepage](/static/images/home-page-mobile.png)

- Tablet View (768px)

  ![Tablet layout](/static/images/home-page-tablet.png)

- Desktop View (1440px)

  ![Desktop layout](/static/images/home-page-desktop.png)

### Feature Testing

- Signup error:  

  ![Signup empty field error](/static/images/empty-field-message.png)

- Add Book

  ![add book success](/static/images/add-book-success.png)

- Edit Book saved

  ![book updates saved](/static/images/book-details-saved.png)

- Swap request confirmation:  

  ![Swap request success](/static/images/swaprequest-success-message.png)

- Incorrect details entered

  ![incorrect details](/static/images/incorrect-details-message.png)

- Confirm Book delete

  ![confirm deletion](/static/images/confirm-deletion.png)

- Book details saved

  ![book details saved](/static/images/book-details-saved.png)

- Bookswap Request

  ![bookswap request](/static/images/swaprequest-success-message.png)

- Already Requested

  ![already-requested](/static/images/already-requested.png)

- Logout Message

  ![logout-message](/static/images/logout-message.png)

- logged out

  ![logged-out](/static/images/logged-out.png)

- Page Not Found

  ![page not found](/static/images/page-not-found.png)

### Password section

## HTML Validation

- Home Page

![Home HTML Validation](/static/images/html-val-homepage.png)

- About

![About HTML Validation](/static/images/html-val-about.png)

- Login

![Login HTML Validation](/static/images/html-val-login.png)

- Signup

![Signup HTML Validation](/static/images/html-val-signup.png)

- Booklist

![Booklist HTML Validation](/static/images/html-val-booklist.png)

- Add Book

![Add Book HTML Validation](/static/images/html-val-add-book.png)

- Edit Book

![Edit Book HTML Validation](/static/images/html-val-edit.png)

- Delete Book

![Delete Book HTML Validation](/static/images/html-val-delete.png)

- Logout

![Logout HTML Validation](/static/images/html-val-logout.png)

- Password Reset

![Password Reset HTML Validation](/static/images/html-val-password-reset.png)

- Password Reset Done

![Password Reset Done HTML Validation](/static/images/html-val-password-reset-done.png)

## CSS Validation

- CSS Validation results

![CSS Validation Results](/static/images/css-val.png)

## Python Code Validation (PEP8)

- Views

![views PEP8 results](/static/images/pep8-views.py.png)

- URLS

![urls PEP8 results](/static/images/pep8-urls.py.png)

- Models

![models PEP8 results](/static/images/pep8-models.py.png)

- Forms

![forms PEP8 results](/static/images/pep8-forms.py.png)

- Apps

![apps PEP8 results](/static/images/pep8-apps.py.png)

- Admin

![admin PEP8 results](/static/images/pep8-admin.py.png)