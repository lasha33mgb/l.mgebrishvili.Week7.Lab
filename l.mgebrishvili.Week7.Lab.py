{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "7124180b-de2a-489c-8a72-b70e7d02e4fe",
      "cell_type": "code",
      "source": "import random\n\ndef simulate_zkp(trials=20):\n    success_count = 0\n    for _ in range(trials):\n        path_entered = random.choice(['A', 'B'])  # Alice enters randomly through path A or B\n        challenge = random.choice(['A', 'B'])     # Bob asks her to return through A or B\n\n        knows_password = True  # This means Alice is honest and knows the password\n\n        # If she knows the password, she can always go through the secret door\n        if knows_password:\n            success = True\n        else:\n            # If she doesn't know the password, she can only succeed if the challenge matches the entry\n            success = path_entered == challenge\n\n        if success:\n            success_count += 1\n\n    print(f\"Successful responses: {success_count}/{trials}\")\n\nsimulate_zkp()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Successful responses: 20/20\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "cdb370ba-b24e-4a6b-bf05-0ae64a6f282e",
      "cell_type": "code",
      "source": "import random\n\ndef simulate_zkp(trials=20):\n    success_count = 0\n    for _ in range(trials):\n        path_entered = random.choice(['A', 'B'])\n        challenge = random.choice(['A', 'B'])\n        knows_password = False  # <-- MODIFIED to simulate attacker\n\n        if knows_password:\n            success = True\n        else:\n            success = path_entered == challenge\n\n        if success:\n            success_count += 1\n\n    # Original output\n    print(f\"Successful responses: {success_count}/{trials}\")\n    # ADDED output: success rate for attacker\n    print(f\"Success probability: {success_count / trials:.2%}\")\n\nsimulate_zkp()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Successful responses: 12/20\nSuccess probability: 60.00%\n"
        }
      ],
      "execution_count": 3
    },
    {
      "id": "1a57f78a-273f-4a57-ad4f-09272600f503",
      "cell_type": "code",
      "source": "Part 2\n\n# This function calculates the nth Fibonacci number using recursion\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return fibonacci(n - 1) + fibonacci(n - 2)\n\n# Example: get the 5th Fibonacci number\nprint(fibonacci(5))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "5\n"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "0d9ef0e0-0a72-4c0f-b3e3-52b168a51a09",
      "cell_type": "code",
      "source": "# Manually obfuscated version of the Fibonacci function\ndef fx(k):\n    if k <= 1:\n        return k\n    else:\n        return fx(k - 1) + fx(k - 2)\n\nprint(fx(5))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "5\n"
        }
      ],
      "execution_count": 5
    },
    {
      "id": "40582c71-3158-4576-8c2e-86b4669e8925",
      "cell_type": "code",
      "source": "def a(b):\n    if b<=1:\n        return b\n    else:\n        return a(b-1)+a(b-2)\nprint(a(5))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "5\n"
        }
      ],
      "execution_count": 6
    },
    {
      "id": "1aaad90b-ebd2-4502-9beb-afb3fa2424f6",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}