
from flask import Flask, render_template, request
import string
import math

app = Flask(__name__)


COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "letmein",
    "welcome123", "iloveyou", "abc123",
    "123456789", "qwerty", "admin"
}

SEQUENCES = [
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]


def analyze_password(password):
    length = len(password)

    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    common = password.lower() in COMMON_PASSWORDS

    repeated = any(
        password[i] == password[i + 1] == password[i + 2]
        for i in range(max(0, length - 2))
    )

    lower_password = password.lower()
    sequential = any(
        sequence[i:i + 3] in lower_password
        for sequence in SEQUENCES
        for i in range(len(sequence) - 2)
    )

    charset_size = 0

    if has_lowercase:
        charset_size += 26
    if has_uppercase:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += len(string.punctuation)

    entropy = (
        length * math.log2(charset_size)
        if length > 0 and charset_size > 0
        else 0
    )

    # Project-specific heuristic score, from 0 to 10
    score = 0

    if length >= 16:
        score += 4
    elif length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 1:
        score += 1
    if length >= 20:
        score += 2
    elif length >= 18:
        score += 1
    score += sum([
        has_lowercase,
        has_uppercase,
        has_digit,
        has_special
    ])

    if common:
        score -= 4
    if sequential:
        score -= 2
    if repeated:
        score -= 1

    score = max(0, min(10, score))

    if common or length < 8 or score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    recommendations = []

    if length < 12:
        recommendations.append(
            "Use a longer password, ideally 12–16 or more characters."
        )
    if not has_lowercase:
        recommendations.append("Include lowercase letters.")
    if not has_uppercase:
        recommendations.append("Include uppercase letters.")
    if not has_digit:
        recommendations.append("Include numbers.")
    if not has_special:
        recommendations.append("Consider including special characters.")
    if common:
        recommendations.append(
            "Avoid common passwords and predictable phrases."
        )
    if sequential:
        recommendations.append(
            "Avoid predictable sequences such as abc or 123."
        )
    if repeated:
        recommendations.append(
            "Avoid repeating the same character several times in a row."
        )
    if not recommendations:
        recommendations.append(
            "Good character variety and length. Avoid reusing this password."
        )

    return {
        "length": length,
        "has_lowercase": has_lowercase,
        "has_uppercase": has_uppercase,
        "has_digit": has_digit,
        "has_special": has_special,
        "common": common,
        "sequential": sequential,
        "repeated": repeated,
        "entropy": round(entropy, 2),
        "score": score,
        "strength": strength,
        "recommendations": recommendations
    }


@app.route("/", methods=["GET", "POST"])
def home():
    results = None

    if request.method == "POST":
        password = request.form.get("password", "")

        if password:
            results = analyze_password(password)
        else:
            results = {
                "error": "Please enter a password to analyze."
            }

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)