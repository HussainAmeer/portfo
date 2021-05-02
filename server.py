from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import csv
# @app.route('/')
# def hello_world():
#     return 'Hello, Ameer Hussain!'

# @app.route('/')
# def hello_world():
#     return render_template('./index.html')

# @app.route('/<username>/<int:post_id>') #<>dinamically receive the data
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


@app.route('/') #<>dinamically receive the data
def my_home():
    return render_template('./index.html')

#Dynamically
@app.route('/<page_name>') #<>dinamically receive the data
def my_page(page_name):
    return render_template(page_name)

#Write to txt
def write_to_file(data):
	with open('C:/Users/Admin/Desktop/PythonFiles/WebServer/database.txt', mode='a') as database:  #absolute path!
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('C:/Users/Admin/Desktop/PythonFiles/WebServer/database.csv', mode='a', newline='') as database2:  #absolute path!
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])		
		
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
		if request.method =='POST':
			try:
				data= request.form.to_dict()
				write_to_csv(data)
				return redirect('/thankyou.html')
			except:
				return 'Did not save to DataBase'
		else:
			return 'Something Went Wrong, Try Again!'
	 
# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

# @app.route('/works.html')
# def works():
#     return render_template('./works.html')


###
# @app.route('/blog')
# def blog():
#     return 'This is Blog'

# @app.route('/favicon.ioc')
# def blog2():
#     return 'This is Blog2'