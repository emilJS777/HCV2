from src import app
from src.__Parents import ContextInitializer

ContextInitializer.ContextInitializer()
if __name__ == '__main__':
    app.run(debug=True)
