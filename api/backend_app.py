###
# Main application interface
###

# import the create app function 
# that lives in src/__init__.py
from backend.rest_entry import create_app

# create the app object
app = create_app()

if __name__ == '__main__':
    # we want to run in debug mode (for hot reloading) 
    # this app will be bound to port 4000. 
    # Take a look at the docker-compose.yml to see 
    # what port this might be mapped to... 
    app.run(debug = True, host = '0.0.0.0', port = 4000)
    #This starts the flask container 
    #Youre running it in debug mode so you get more specific error messages
    #The 0.0.0.0 means it accepts from all IP addresses 
    #The 4000 is what port it is running on - the testing file there a line that redirects it to port 
    #4001 because you cant have the same port for your testing and your group testing 
