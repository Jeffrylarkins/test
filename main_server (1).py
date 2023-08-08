from flask import Flask, request

app = Flask(__name__)

@app.route('/ocr', methods = ['POST'])

def arg():

    DocumentUniqueID = request.form['document_name']
    FileType = request.form['application_type']
    ContainerName = request.form['container_name']
    account_key = request.form['account_key']
    account_name = request.form['account_name']
    destination_container_name = request.form['destination_container']
    db_for_log = request.form['log_connection_string']

    return f"Got arguments {DocumentUniqueID},{FileType},{ContainerName},{account_key}"


if __name__ == "__main__":
    app.run()