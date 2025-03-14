# The Village Bookshelf

## Introduction

I have created the Village Bookshelf as a community platform for swapping books. Users can list, browse and swap books with other users in their local area. 
This is a great platform for promoting both literacy and sustainability.

## Header

The header includes the logo with the title of The Village Bookshelf written underneath the logo with an overline to look like a shelf.

Header Logo 320px

![Logo 320px](/static/images/logo320px.png)

Header Logo 768px

![Logo 768px](/static/images/logo768px.png)

Header Logo 1024px

![Logo 1024px](/static/images/logo1024px.png)

Header Logo 1440px

![Logo 1440px](/static/images/logo1440px.png)

Header Logo 2560px

![Logo 2560px](/static/images/logo2560px.png)

Also included in the header is the Welcome message and the Nav Bar.

Welcome and Nav Bar 320px

![Welcome Nav Bar 320px](/static/images/welcome320px.png)

Welcome and Nav Bar 768px

![Welcome Nav Bar 768px](/static/images/welcome768px.png)

Welcome and Nav Bar 1024px

![Welcome Nav Bar 1024px](/static/images/welcome1024px.png)

Welcome and Nav Bar 1440px

![Welcome Nav Bar 1440px](/static/images/welcome1440px.png)

Welcome and Nav Bar 2560px

![Welcome Nav Bar 2560px](/static/images/welcom2560px.png)

The header also contains a scroll bar window whcih shows the books that have been loaded on to the database.

Available scrollbar window 320px

![Available Books Scroll Bar window 320px](/static/images/available320px.png)

Available scrollbar window 768px

![Available Books Scroll Bar window 768px](/static/images/available768px.png)

Available scrollbar window 1024px

![Available Books Scroll Bar window 1024px](/static/images/available11024px.png)

Available scrollbar window 1440px

![Available Books Scroll Bar window 1044px](/static/images/available1440px.png)

Available scrollbar window 2560px

![Available Books Scroll Bar window 2560px](/static/images/available2560px.png)

The main section contains the hero section which is repeated in each page. This contains a search bar sothe user can easily search for a book which ever page they are on.

Hero section 320px

![Hero 320px](/static/images/hero320px.png)

Hero section 425px

![Hero 425px](/static/images/hero425px.png)

Hero section 768px

![Hero 768px](/static/images/hero768px.png)

Hero section 1024px

![Hero 1024px](/static/images/hero1024px.png)

Hero section 1440x

![Hero 1440px](/static/images/hero1440px.png)

Hero section 2560px

![Hero 2560px](/static/images/hero2560px.png)

Then the footer section is at the bottom of each page.

Footer 320px

![Footer 320px](/static/images/footer320px.png)

Footer 425px

![Footer 425px](/static/images/footer425px.png)

Footer 768px

![Footer 768px](/static/images/footer768px.png)

Footer 1024px

![Footer 1024px](/static/images/footer1024px.png)

Footer 1440px

![Footer 1440px](/static/images/footer1440px.png)

Footer 2560px

![Footer 2560px](/static/images/footer2560px.png)

## Features

# Nav Bar

Each page contauns a nav bar with links to each of the other pages.
The nav bar options change depending on whether the user is logged in or not.
You can always access the About page, apart from from the add book field and the book detail field.
From both of these pages you can go back to the book list page where you can access the About page.

The home page, when you first visit as a guest, displays a welcome message:

![Welcome, Guset!](/static/images/welcomeguest.png)

And then has 4 options in the Nav Bar, Home, About, Login and Sign Up:

![Home Nav Bar](/static/images/homenavbar.png)

![Home Nav Bar large screens](/static/images/homenavbar-row.png)

The image(s) in the title on each page is also a link back to the Home page.
The About button on the home page, takes you to the About page where there is a discription of what the village bookshelf is, and how it works.
The nav bar on the About page includes links to the Home, login and sign up pages.

The Home button on the About page, takes you back to the Home page as a guest.
The Login button on the About page takes you to the login page.
The Sign up button on the About page takes you to the sign up page.

The Login button on the Home page takes you to the login page.
From the login page, if you have previously created an account, you can fill in your username and password to access the book list as a logged in user with more features available to you.
There is a button for if you have forgotten your password as well as a Home, About and Sign Up button, on thr login page.
If you haven't already created an account, you can create an account by choosing the sign up button from this page also.
The forgotten passwrod button takes you to a page to enter your email to reset your password.
The Home button on the login page takes you back to the Home page as a guest, the About button takes you to the About page and the Sign up button takes you to the sign up page.

The Sign Up button on the home page takes you to the sign up form where you can create an account with a username, email and password.
Once you create an account you are then directed to the booklist page as a logged in user with more features available to you.

The sign up page has a form to fill in details and then a sign up button which redirects you to the book list as a logged in user.
There is a Login button which takes you to the login page, a Home button which takes you to the Homepage, as a guest and the About button which takes you to the about page.

When you fill in your details and create an account from the sign up page, you are then directed to the book list page where there is now a welcome message displaying the username so you know you are logged in. There is a search bar dirctly under the welcome message so you can search easily from here, and there is the scroll bar window below the seacrh bar, where you can scroll through the books on the database. Now as you are a logged in user, you havet he option to Add a book. 
The Add Book button, takes you to the book form where you can add details of your book to add. The title, Author and description fields need to be filled out and then there is an available box to tick and a save button to save the details or a cancel button which will take you back to the book list page and not save the details.
Once you save the details, you are directed back to the book list page as a logged in user adn you can now scroll the book list and see your added book.
As you are the book owner, you will also now have options to edit and delete your own book. On the book details page, you are told that this is your own book so you are unable to request a swap. If you click on the edit link, this taked you back to the book form where you can edit the details and then save again.
When you click on the link to delete the book, you recieve a message asking if you are sure you want to delete this book. Here you have the option to cancel or Yes, delete. If you cancel, you are taken back to the book list. If you press yes, delete, you are taken back to the book list and the book has been deleted from the book list.


### User Authentification

User registration - user signs up with a username, email and password.
Login and Logout - Useres authenticate with their credentials and then they can logout.
Session Management - Django uses session cookies to keep track of logged in Users.
Authenticated Features - Loged in Users have other features available: Add book, edit book, delete book, request swap, receive messages.

Sign Up to register.
Here I use a form to collect the details to create a user account.
Django saves the password in the database but his is hashed so not even a superuser can see passwords.
Once registered, useres can access more features.

Logging in.
To log in, a User enters their username and password.
The credentials are checked by Django and a session is started if the credentials are valid.
If incorrect credtials are entered, a message is shown asking you to enter a correct username and password.

![Login error message](/static/images/loginerror.png)

If the login button is pressed before filling in the credentials, a message is shown saying, Please fill in this field.

![Please fill in this field mesaage](/static/images/emptylogin.png)

The session keeps users logged in until they manually log out or close down the browser.

Logging Out.
When the User logs out, their session is cleared and access is limited until they login again.
There is a Thank you for visitig message and then options to either login again or return to home.

![Logged out message](/static/images/loggedout.png)

The login button on the logged out page take you back to the login page.
The Return to home button on hte logged out page takes you back to the Hme page as a guest.

Restricting Access.
As some pages are only accessible to logged in users, the views are tagged with @login_required to ensure that only authenticated users can view theses tagged pages.


If the Sign Up button is pressed before filling in the fields, an error message is shown, saying 'Please fill in this field.

![Please fill in this field message](/static/images/signuperror.png)



### Book Management

Users can add books to the platform.
Users can view and search for books in a booklist (from the databas).
Logged in Users can Edit and Delete their own books.
Logged in Users can request swaps and send and receive messages.

# Book Model
I created a Book model to store the details of the books in the database.

# Entitiy relationship diagram

![Book ERD](/static/images/bookerd.png)

A logged in User can add a book. When logged in they have access to an Add Book button which taked them to a form where thay can enter the book details and when they press save the details are saved to the database and can now be viewed in the book list that is accessible as a logged in User or as a guest.
A view feteches the data from the database to display it in the book list.

Searching for books.
There is a search bar accesible on every page in the main hero section. There is also a search bar under the welcome message when a user is logged in.
The user cn search for title or author.

Editing a book.
A book owner can edit and delete thier own books if they are logged in. 

Swap Request.
When a User is logged in, from the book details page, they can request a swap for any book that isn't their own.
This request sends an email to the book owner.

### Search

### Scrollable Book List

### Reviews/Comments

## Technologies Used

Backend: Django with Python
Frontend: HTML, CSS
Database: SQLite, with support for PostgreSQL
Version Control: Git and GitHub

## Installation

# Prerequisites

- Python 
- pip
- Virtual environment, VSC

### Steps


### Bugs

After updating the images so that they are links back to the home page, I found that my login  was no longer working.
I could tell that it was jsut directing me back to the login page but I couldn't tell why. Eventually, I relaised that I had added an @login_requried tag to the view for the book_list page so that meant that the book list page that it was trying to access would not allow access as you weren't actually logged in yet. I had added this tag as I had realised that if you went to the book detail page, from the home page as a guest, you could then access the booklist page as a signed in user. I thought that adding this tag would stop this from happenng but didn't realise that you wouldn't actually then be able to login to that book list page. I then changed the book detail page so that if you weren't logged in, you weren't given the option to go tot he book list page but could only go back to the home page, where you can access the bok list, but as a guest with limited features available.
