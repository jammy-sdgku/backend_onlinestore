run_local.sh
    #!/usr/bin/env sh

    export FLASK_APP=App/server.py
    export FLASK_ENV=development

    # Run the Flask application
    flask run  