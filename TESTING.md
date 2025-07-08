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

This file documents all manual testing and validation efforts for **The Village Bookshelf** Django web application. It includes individual feature testing, user journey testing, form validation, and accessibility/security checks.

---

## Test Environment

- **Browser(s):** Chrome, Firefox, Safari
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
| Book Details         | ✅                | ✅            | Guest sees limited options       |
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

| Bug Description                                  | Fix Applied                                          |
|--------------------------------------------------|------------------------------------------------------|
| Login not working after signup                   | Fixed `@login_required` mistakenly applied to `book_list` view |
| Sign up form rendering strangely                 | Adjusted form structure and CSS                      |
| 2560px layout misalignment                       | Improved, but still limited by CSS knowledge         |
| Nav buttons out of alignment at certain widths   | Added media queries for better spacing               |

---

## Screenshots

🖼️ Screenshots for all responsive breakpoints, features, and validation results are available in the `/static/images` folder and referenced in the [README.md](README.md).
