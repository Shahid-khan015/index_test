from website import create_app

app = create_app()
application = app

# Remove debug mode for production
if __name__ == '__main__':
    app.run()