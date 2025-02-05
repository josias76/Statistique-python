# Librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
from PyPDF2 import PdfMerger


""""
cette fonction rassemble les fichiers pdf
"""


def create_graphics_report():
    merger = PdfMerger()
    pdf_files = ["matplotlib_bar.Pdf","pandas_plot.pdf","seaborn_bars.pdf",
                 "seaborn_boitt_mous.pdf","seaborn_dens_hist.pdf","seaborn_dens_prob.pdf","seaborn_hist.pdf","plotly_express.pdf"]
       
    
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write("Reporting.pdf")
    merger.close()

if __name__ == "__main__":
    file = input("Renseignez votre nom : ")
    create_graphics_report() 