#!/usr/bin/env python3
import server
import index
import notifications
import stats
import login
import archive
import secrets

server.app.secret_key = secrets.session_secret
server.app.run(debug=True, threaded=True)