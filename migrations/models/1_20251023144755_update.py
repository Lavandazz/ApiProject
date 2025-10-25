from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "blacklistedtoken" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" VARCHAR(200) NOT NULL
);
COMMENT ON TABLE "blacklistedtoken" IS 'Модель для сохранения токена в черный лист токенов для дальнейшей проверки валидности токенов при входе';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "blacklistedtoken";"""


MODELS_STATE = (
    "eJztWm1z2jgQ/isef0pnch1wTEnvGxBy5ZqEm4RcO30Zj7AFaGLL1JabMB3+++nFRvJr7R"
    "YSmOOLx6x2rd3Hy6NdWT90z3egG77uBQTZLtT/1H7oGHjsJjt0qulguZQDTEDAlBvpQFGa"
    "hiQANqHiGXBDSEUODO0ALQnyMZXiyHWZ0LepIsJzKYow+hZBi/hzSBYwoAOfv1Ixwg58gm"
    "Hyc/lgzRB0nZSzyGFzc7lFVksuG2FyyRXZbFPL9t3Iw1J5uSILH2+0ESZMOocYBoBA9ngS"
    "RMx95l0caBKR8FSqCBcVGwfOQOQSJdyaGNg+ZvhRb0Ie4JzN8ofRNrvm+dkb85yqcE82ku"
    "5ahCdjF4YcgZuJvubjgAChwWGUuBFExGtLQzdYgKAYu41BBj7qdBa+BKwq/BKBBFAmzZYQ"
    "9MCT5UI8Jwv6s91pVeD1b+928K53e0K1XrFofJrIIsFv4iFDjDFQJYiqZzkoJ/CpJA0zZo"
    "cCaAV+k+HHCXPaC8NvrgrbyXXvI0fUW8UjV+ObvxJ1BebB1bifQdcOIIvfAiQP7gUdIciD"
    "xQCnLTP4OrHp6+RmP9HWaQzOGLurmFuq0B9dD+8mvet/Uq/gojcZshEjBX8iPXmTSfTNQ7"
    "QPo8k7jf3UPo1vhhxBPyTzgM8o9SafdOYTiIhvYf/RAo5Cg4k0AWbNCHz2oFARE0yB/fAI"
    "AsfKjfiGX6abH/IMLysBGMz5a2HgMjfjRa3v0se4KKRveuI/QFy08OV0KlfAqdQmG+2fLY"
    "X6l6hltm12PYP8avJrh1+n7GramjIgRDMuMtvSzuQWZotLxNVRniTuz1VjQ5kU5FRbYlJD"
    "6HbluKk83OTenL3VpGvxHG0xRZ2ZoDJRQZCxqKUCkgvvLZefqxJhPFNcjifKhSJcOteUYW"
    "U2EVDsheJxEqJi3CRQ1TF1avEe07mgZ3jimDTHpKmVNMdy+vnL6YT6a5fTicGhVH/pctpo"
    "1SmnqVZpOc3H1vtSF9z6xU0wl1eu/4Ffs/2tT98pDoqJRTvh5i3F0FYoxznllu1Z1jImwG"
    "6O1VoKC6VcePXr684eOH7kvmfnvuQfUJf6Ev3tMN/O0UtvI9TivXYF77Ub855EOgphEOah"
    "7sdml+9voQtKthViQrunj0hIbf8WmXWSK4k0aX53yf0MkiLu5/JK7o8SjS32e79PhLPfaB"
    "y2NPuRhZ+dhVku8vsGTKzaHCIb19rTrdjSze/ohlFjEBWTw6zlu3VQ7Jaj2M2huAQk8PHK"
    "Q3YTINNWRywFltADyG0C48bgEP/RRqdOW9kp7yo7+VwMw0c/KFhVqjJR2hxmHm6tTlWhRK"
    "FFixz0vYAe+z6tKQEuWaVVuwyeU2q4K0A3mbrtz1398fgq9a2lP8p+z7q/7g8pwBxeqoQI"
    "lMv4L9X+rGs61v67qP3L9n5UuKp7gGZ7QEZb2cKdyfJ6izW4pu40F2zKFHYIe+LXsXd4kR"
    "0cqxF4isXPEdwPftkOiOmGqxloisX/CbTccpfGMA/gpR9ANMfv4YrjOKIeAWwXVQ+ZnZr9"
    "w69sUaPiADxuKExNDRoeDQqKgmHQuxv0LoZ6KvOKN1wbo3Z4pUAWNYWFilF7mY9JPRgge1"
    "FUUsQjlQUFkDrHE5V7RmVVi+h3GISFBwHL+0zF5DDbTKNTr1+vathzHTv7azQAMVY/TAB3"
    "0qfTGQnEBacm/74b35ScmJQmGSDvMQ3ws4NscqqxY25f9xPWChRZ1KluPXc4NXsO9TR95J"
    "E9oP/SZxXW/wEpSfPo"
)
