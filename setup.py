import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webplucker", 
    version="0.0.5",
    author="Shivjeet Singh Bhullar",
    author_email="bhullarshivjeet@gmail.com",
    description="webplucker Is A Fast And Handy Package For Web Scraping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivjeetbhullar/webplucker",
    packages=setuptools.find_packages(),
    install_requires=["lxml",'cssselect','requests','pyppeteer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)
