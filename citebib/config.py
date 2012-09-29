#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser

def write_default_config_latex(inifile):
    """
    Write a default configuration file for latex

    :param inifile: ini file name
    """
    fields = {
        'article' : ('author, journal (year)'),  
    }

    config = configparser.ConfigParser()


    for entry in fields:
        content = {'format': fields[entry], 'authorlength': 2}
        config[entry] = content


    with open(inifile, 'w') as configfile:
        config.write(configfile)


def write_default_config_bibtex(inifile):
    """
    Write a default configuration file for bibtex

    :param inifile: ini file name
    """
    reqfields = {
        'article' : ('author', 'title', 'journal', 'volume', 'year', 'pages'),
        'book' : ('author', 'editor', 'title', 'publisher', 'year'),
        'booklet' : ('title'),
        'conference' : ('author', 'title', 'booktitle', 'year'),
        'inproceedings' : ('author', 'title', 'booktitle', 'year'),
        'inbook' : ('author', 'editor', 'title', 'chapter', 'pages', 'publisher', 'year'),
        'incollection' : ('author', 'title', 'bookpublisher', 'year'),
        'manual' : ('title'),
        'mastersthesis' : ('author', 'title', 'school', 'year'),
        'misc' : (''),
        'phdthesis' : ('author', 'title', 'school', 'year'),
        'proceedings' : ('title', 'year'),
        'techreport' : ('author', 'title', 'institution', 'year')
        }
    fields = ('author', 'editor', 'publisher', 'bookpublisher', 
            'title', 'booktitle', 'journal', 'volume', 'year', 'pages', 'institution')
    config = configparser.ConfigParser()

    content = {}
    for el in reqfields:
        for field in fields:
            if field in reqfields[el]:
                content.update({field: True})
            else:
                content.update({field: False})
        config[el] = content

    with open(inifile, 'w') as configfile:
        config.write(configfile)



if __name__ == '__main__':
    write_default_config_latex('toto.ini')
    write_default_config_bibtex('bibtex.ini')