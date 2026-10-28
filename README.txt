Docs-as-Code Prototype — what this is and how to use it
========================================================

WHAT THIS IS
------------
A small practice documentation site. The pages are built from writing
samples that already existed as PDFs; each page's words are the sample's
own words, converted to plain-text Markdown files you can edit.

The point of the package is the workflow, the same one used for the
portfolio site:

    edit the text  ->  rebuild the pages  ->  drop the folder on Netlify

WHAT'S IN THE FOLDER
--------------------
index.html and the other .html files
    The finished web pages. These are what Netlify publishes.

src/
    The Markdown source files — one per page. This is where you write
    and edit. index.md is the home page.

build.py
    The small script that turns the Markdown files in src/ into the
    HTML pages, all sharing the same header, navigation, and styling.

README.txt
    This file.

HOW TO EDIT A PAGE
------------------
1. Open the page's file in src/ in any text editor
   (for example, src/empowering-users.md).
2. Change the text. A few Markdown basics:
      #  Big heading        ##  Smaller heading
      -  Bullet point       1. Numbered list
      **bold**              *italic*
      [link text](other-page.html)
3. Save the file.
4. Rebuild: open a terminal in this folder and run

       python3 build.py

   (One-time setup: the build needs the Python "markdown" package.
   If the build complains it is missing, run:  pip install markdown)
5. Check the result by opening index.html in a browser.

HOW TO PUBLISH
--------------
Drag this whole folder onto Netlify Drop, the same way the portfolio
site was published. Everything the site needs is in the folder —
the pages, the sources, and the build script travel together.

ADDING A PAGE
-------------
Create a new .md file in src/ starting with a "# Title" line, run the
build again, and the new page appears in the navigation automatically.
Link to it from src/index.md if you want it listed on the home page.
