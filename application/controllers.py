from flask import render_template, request, redirect
from flask import current_app as app
from application.preprocessing import *

# Define route for grading essays
@app.route('/', methods=['GET', 'POST'])
def grade_essay():
    if request.method == 'POST':
        # Retrieve the uploaded file or the essay text from the request
        essay = request.files.get('file') or request.form.get('essay')

        # Perform grading using your trained model
        # grading_result = your_model.grade_essay(essay)

        # Return the grading result to the user
        # return render_template('result.html', result=grading_result)

    return render_template('index.html')