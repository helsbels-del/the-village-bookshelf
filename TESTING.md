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

- **Browser(s):** Chrome, Firefox, Safari, Edge
- **Devices tested:** Desktop (2560x1440, 1440x900), Tablet (768px), Mobile (425px, 375px, 320px)
- **Tools used:**
  - [W3C HTML Validator](https://validator.w3.org/)
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - [CI Python Linter](https://pep8ci.herokuapp.com/)

---

## Manual Feature Testing

| Feature        | Test Case                                  | Expected Result                              | Actual Result       | Pass/Fail |
|----------------|---------------------------------------------|-----------------------------------------------|----------------------|------------|
| Sign Up Form   | Submit with valid inputs                    | User created, redirected to book list         | ✅ Passed            | ✅         |
| Login          | Correct username/password                   | Redirected to book list                       | ✅ Passed            | ✅         |
| Login          | Incorrect credentials                       | Error message shown                           | ✅ Passed            | ✅         |
| Add Book       | Valid input                                 | Book saved and appears in book list           | ✅ Passed            | ✅         |
| Edit Book      | Change details and save                     | Book updated                                  | ✅ Passed            | ✅         |
| Delete Book    | Confirm deletion                            | Book removed from database                    | ✅ Passed            | ✅         |
| Request Swap   | Click on a book you don’t own               | Email sent to owner, message displayed        | ✅ Passed            | ✅         |
| Swap Request Again | Click on already requested book        | Message shown: “already requested”            | ✅ Passed            | ✅         |
| Logout         | Click logout                               | Redirected to logged-out page                 | ✅ Passed            | ✅         |

---

## User Journey Testing

| Journey                                    | Outcome                                      | Notes         |
|--------------------------------------------|----------------------------------------------|---------------|
| Sign up → Add Book → Logout → Login again  | Book remains, user session handled correctly | ✅            |
| Visit book details as guest                | Can view book, cannot request swap           | ✅            |
| Try accessing `/add/` when not logged in   | Redirects to login page                      | ✅            |

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

- ✅ **Home Page:** Passed  
- ✅ **Login/Signup Pages:** Passed  
- ✅ **About Page:** Passed  
- ✅ **Book Detail / Add Book / Edit Book:** Passed  

---

## CSS Validation

The full `style.css` file was tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

- ✅ No errors or warnings detected.

---

## Python Code Validation (PEP8)

All `.py` files were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/).

- ✅ All files passed.
- ℹ️ Some long lines were kept intentionally for readability.

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

🖼️ Screenshots for all responsive breakpoints, features, and validation results are available in the `/static/images` folder and referenced in the [README.md](README.md).

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
- Swap request confirmation:  
  ![Swap request success](/static/images/swaprequest-success-message.png)

### Bug Fixes

- Before and after nav alignment fix:  
  ![Broken nav](/static/images/nav-before-fix.png)  
  ![Fixed nav](/static/images/nav-after-fix.png)
