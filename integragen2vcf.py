#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author : Anne-Sophie Denommé-Pichon

import csv
import sys

def printHeader(sampleName):
	print '##fileformat=VCFv4.2'
	print '#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t%s' % sampleName

def printRow(row):
        print '\t'.join((row[1], row[0], row[3], row[13], 'FIXME', '.', '.', '.', 'GT', 'FIXME'))

if __name__ == '__main__':
        lines = iter(sys.stdin) # Transforms stdin into an iterator on rows. Transforme l'entrée standard en itérateur sur lignes (comme avec un « for … in … »)
        rows = csv.reader(lines, delimiter='\t') # Creates an iterator on the TSV rows (it does not load all the lines in memory). Crée un itérateur (ie. ne charge en mémoire qu'une seule ligne à la fois) sur les lignes interprétées en TSV
        next(rows) # Increments (skip the header row). Avance l'itérateur d'un cran (ie. saute la ligne du header)

        secondRow = next(rows) # Gets the second row of the input file. Récupère la deuxième ligne du fichier d'entrée.
        printHeader(secondRow[2]) # Writes the header with the value of the third column of the second row as the sample name. Écrit le header, avec pour nom d'échantillon la valeur dans la troisième cellule de la deuxième ligne
        printRow(secondRow) # Prints the second row of the output file. Affiche la deuxième ligne convertie du fichier de sortie

        # Prints the following rows of the output file. Affiche les lignes suivantes converties du fichier de sortie
        for row in rows:
                printRow(row)
