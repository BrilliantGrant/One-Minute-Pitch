# minute-pitch

This is an app that will allow users to submit one minute pitches,upvote on the pitch,and leave comments 

## Description

This application allows users to write a one minute pitch in the four categories provided.

The pitches are organized by categories. Examples of categories: <br> 

- pickup lines
- interview pitches
- product pitches
- promotion pitchess

### categories include:

* Promotion Pitch
* Pickup Lines
* Interview Pitch
* Product Pitch

## User Stories

As a user I would like:
* to view the different categories
* to see the pitches other people have posted
* to submit a pitch in any category
* to comment on the different pitches and leave feedback
* to vote on the pitch and give it a downvote or upvote

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : bri@g.com <br> Username : jane101 <br> Password : doe1 | New user is registered |
| Log in | Your email : bri@g.com<br> Password : doe1 | Logged in |
| Display pitch categories | N/A | List of various pitch categories |
| See pitches from selected category | **Click** a category | Directed to a page with a list of pitches from the selected category |
| Create a pitch | **Click Create A Pitch** | An authenticated user is directed to a page with a form where the user can create and submit a pitch |
| See a pitch | **Click** on a pitch | A user is directed to a page containing the pitch, its comments and its votes |
| Comment on a pitch | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a pitch |
| Upvote on a pitch | **Click** on upvote glyphicon | The votes on the pitch increases by one |
| Downvote on a pitch | **Click** on downvote glyphicon | The votes on the pitch decreases by one |


## Setup/Installation Requirements

* Clone the repository https://github.com/BrilliantGrant/One-Minute-Pitch.git
* install all the requirements in the file > requirements.txt
* open terminal and go to the project folder, run $ ./start.sh

## Known Bugs

There no known bugs

## Technologies Used

* Python3.6
* Flask
* Bootstrap
* Postgres db

### License
s



