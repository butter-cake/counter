from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secret'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def tracker():
    if 'key_name' in session:
        session['key_name'] = session['key_name']+1
    else:
        session['key_name'] = 1
    return render_template('server.html', counting = session['key_name'])

@app.route('/destroy_session')
def destroy():
    session.clear()		# clears all keys
    #return render_template('server.html', counting = 1)
    return redirect("/")
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.