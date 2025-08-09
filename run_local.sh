run_local.sh
    #!/usr/bin/env sh

    export FLASK_APP=app/server.py
    export FLASK_ENV=development

    # Run the Flask application
    flask run  