from flask import redirect
import connexion

from services.sms_service import main as sms_service

# Create the application instance
app = connexion.App(__name__, specification_dir='.')

# Start up message service
# sms_service()

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yaml')

# Just send folks to swagger land
@app.route('/')
def home():
    """
    This function just responds to the browser URL localhost:5000/ by redirecting you to
    the kickass interactive api documentation that our swagger file builds.

    :return: redirect to 'api/ui' with a status code of 302
    """
    return redirect('api/ui', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
