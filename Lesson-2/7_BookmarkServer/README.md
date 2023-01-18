# Bookmark Server

In this exercise, you'll create a *bookmark server* or URL-shortening service,
similar to `TinyURL.com` or `goo.gl`, but with no persistent storage.

This server will accept a URL and a short name, check that the URL actually
works (returns an HTTP 200), then store it in a Python dictionary.

See `BookmarkServer.py` for starter code and instructions.

## Tasks

* [ ] Write the `CheckURI` function. This function should take a URI as an argument, and return True if that URI could be successfully fetched, and **False** if it can't.
* [ ] Write the code inside a function named `do_GET` that sends a **303 Redirect** to a known name.
* [ ] Write the code for a function `do_POST` that sends a **400 Error** if the form fields are not present in the POST.
* [ ] Write the code inside `do_POST` that sends a **303 Redirect** to the form after saving a newly submitted URI.
* [ ] Write the code inside `do_POST` that sends a **404 Not Found** if a URI is not successfully checked (i.e. CheckURI returns **False**).