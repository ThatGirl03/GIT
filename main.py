import os
from website import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port from the environment, default to 5000 for local testing
    app.run(host='0.0.0.0', port=port, debug=True)
