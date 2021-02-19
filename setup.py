from setuptools import setup


setup(
    name="statsbombpy",
    version="0.2",
    description="easily stream StatsBomb data into Python",
    long_description="easily stream StatsBomb data into Python",
    url="https://github.com/statsbomb/statsbombpy",
    download_url="https://github.com/statsbomb/statsbombpy/archive/v0.2.tar.gz",
    author="StatsBomb",
    author_email="support@statsbombservices.com",
    packages=["statsbombpy"],
    install_requires=[
        "cashier",
        "inflect",
        "nose2",
        "pandas",
        "requests",
        "requests-cache",
    ],
)
