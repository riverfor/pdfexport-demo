from app import app
from flask import (jsonify, request,
                   render_template, send_file)
import os
import datetime
import pdfkit
import random


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        args = request.form
        output = '/tmp/name-%d.pdf' % random.randint(1000, 9999)
        pdf_string = """
        First Name\t: {0}
        Last Name\t: {1}
        Email\t: {2}
    """.format(
            args.get('firstName'),
            args.get('lastName'),
            args.get('email')
        )
        pdfkit.from_string(pdf_string, output)

        if os.path.isfile(output):
            now = datetime.datetime.now()
            pdfname = now.strftime('%Y%m%d-%H%M%S')
            return send_file(output, as_attachment=True, attachment_filename=pdfname+'.pdf')

    return render_template('index.html')

@app.route('/report/detail')
def report_detail():
    first_name = request.args.get('firstName')
    last_name = request.args.get('lastName')
    email = request.args.get('email')

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    return render_template('report.html', **data)
