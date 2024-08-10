from app import app

if __name__ == "__main__":
    app.run(debug=True)


"""
NOTE TO SELF:
Next steps are making links from select page send movie id to another function to get the other movie details.

Should first check id to make sure the movie doesn't already exist in the database (more reliable of a check than just title)

Build function in GetMovie class possible? Have add call when link is clicked

use id from selection to make API call for remaining movie details for db
"""