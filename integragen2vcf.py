#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Anne-Sophie Denommé-Pichon

import csv
import sys

_homozygousThreshold = 5.

def printHeader(sampleName):
	print '##fileformat=VCFv4.2'
	print '#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t%s' % sampleName

def printRow(rowId, row):
        homozigous = False
        used = int(row[18])
        alts = []
        for nucleotideId, nucleotide in enumerate('ACGT'):
                nucleotideCount = int(row[14 + nucleotideId])
                if nucleotide != row[13] and nucleotideCount >= used / _homozygousThreshold:
                        alts.append(nucleotide)
                        if nucleotideCount >= used * (_homozygousThreshold - 1) / _homozygousThreshold:
                                homozigous = True
        phenotype = '0/1'
        if len(alts) == 2:
                phenotype = '1/2'
        elif len(alts) >= 3:
                print >> sys.stderr, 'Three or more alternatives at line %i (%s)' % (rowId, '\t'.join(row))
        elif homozigous:
                phenotype = '1/1'
        print '\t'.join((row[1], row[0], row[3], row[13], ','.join(alts), '.', '.', '.', 'GT', phenotype))

if __name__ == '__main__':
        lines = iter(sys.stdin) # Transforms stdin into an iterator on rows. Transforme l'entrée standard en itérateur sur lignes (comme avec un « for … in … »)
        rows = csv.reader(lines, delimiter='\t') # Creates an iterator on the TSV rows (it does not load all the lines in memory). Crée un itérateur (ie. ne charge en mémoire qu'une seule ligne à la fois) sur les lignes interprétées en TSV
        next(rows) # Increments (skip the header row). Avance l'itérateur d'un cran (ie. saute la ligne du header)

        secondRow = next(rows) # Gets the second row of the input file. Récupère la deuxième ligne du fichier d'entrée.
        printHeader(secondRow[2]) # Writes the header with the value of the third column of the second row as the sample name. Écrit le header, avec pour nom d'échantillon la valeur dans la troisième cellule de la deuxième ligne
        printRow(2, secondRow) # Prints the second row of the output file. Affiche la deuxième ligne convertie du fichier de sortie

        # Prints the following rows of the output file. Affiche les lignes suivantes converties du fichier de sortie
        for rowId, row in enumerate(rows, 3):
                printRow(rowId, row)
