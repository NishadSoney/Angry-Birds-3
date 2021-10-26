{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled3.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMz7m+puPLWGC6HEAzWmX6Z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/NishadSoney/Angry-Birds-3/blob/master/Data_Cleaning.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B8NQxk35MdWT"
      },
      "source": [
        "import pandas as pd\n",
        "import csv\n",
        "\n",
        "df = pd.read_csv(\"final.csv\")\n",
        "\n",
        "del df[\"Star_name.2\"]\n",
        "del df[\"Distance.2\"]\n",
        "del df[\"Mass.2\"]\n",
        "del df[\"Radius.2\"]\n",
        "del df[\"Luminosity\"]\n",
        "\n",
        "df.to_csv(\"main.csv\")"
      ],
      "execution_count": 1,
      "outputs": []
    }
  ]
}