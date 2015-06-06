# Movie Trailer Website

By [@gabsong](https://twitter.com/gabsong).

A static HTML site generator written in Python.
It creates a site that showcases movie posters and their trailers.

---

## Installation

### Dependencies
To run this Python project, you'll need the following prerequisites installed:

- Python 2.7.10 (download from https://www.python.org/downloads/)
- Google Chrome (download from https://www.google.com/chrome/) or any other
modern web browser
- Internet connection (needed to load Bootstrap 3.x and jQuery 1.x)

### Files
`media.py`
- Defines the structure of the parent class Video and child classes Movie and
TvShow, with all of its attributes. Add attributes class attributes here.

`entertainment_center.py`
- Contains instances of the class Movie, with hardcoded movie objects and all
of its relevant information, including poster image url and YouTube trailer
url. Add additional movies here.

`fresh_tomatoes.py`
- Contains methods for creating the movie trailer site, including the HTML
and CSS boilerplate. Modify site structure or style elements here.

`test.py`
- Abstraction of the script that executes the static HTML site generator in
fresh_tomatoes with the movies in entertainment_center as input.

### Running the program
To run the project execute:
```python
python test.py
```
in the terminal from within the project directory.

## About

This project is part of the Full Stack Nanodegree offered by Udacity.

## License

The base code is the work of Kunal Chawla, computer science instructor at
Udacity. Visit the course **Programming Foundations with Python** on
http://www.udacity.com.
