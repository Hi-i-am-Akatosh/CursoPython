# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe 

setup(
    name="Snake",
    version="1.0",
    description="Breve descripcion",
    author="David Navarro",
    author_email="email del autor",
    url="url del proyecto",
    license="tipo de licencia",
    scripts=["main.py"],
    console=["main.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)