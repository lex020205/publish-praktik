import os
from dotenv import load_dotenv

load_dotenv()
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except Exception:
   
    pass

def create_app():
    from backend import create_app as backend_create_app
    return backend_create_app()



app = create_app()


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)