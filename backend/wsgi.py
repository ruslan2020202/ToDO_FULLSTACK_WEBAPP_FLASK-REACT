from backend.app import create_app
import backend.config as config

app = create_app(config.TestingConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
