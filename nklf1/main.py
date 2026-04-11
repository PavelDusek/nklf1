from app.main import app as application
import gunicorn

def main():
    application.run(host="0.0.0.0", port="8880", debug=False)

if __name__ == "__main__":
    main()
