import re
import sys
import os
from collections import Counter
import matplotlib.pyplot as plt

class MiRNAAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.species_counts = Counter()

    def analyze_file(self):
        species_codes = []
        with open(self.file_path, "r") as file:
            for line in file:
                match = re.match(r'^>(\w+)', line)
                if match:
                    species_codes.append(match.group(1))
        self.species_counts = Counter(species_codes)

    def filter_species_counts(self, threshold):
        filtered_species_counts = {species: count for species, count in self.species_counts.items() if count >= threshold}
        return filtered_species_counts

    def plot_species_counts(self, species_counts):
        sorted_species_counts = sorted(species_counts.items(), key=lambda x: x[1])
        species = [item[0] for item in sorted_species_counts]
        counts = [item[1] for item in sorted_species_counts]

        plt.figure(figsize=(10, 6))
        plt.bar(species, counts)
        plt.xlabel('Species')
        plt.ylabel('Count')
        plt.title('Number of miRNA per Species (Lowest to Highest)')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def run_analysis(self, threshold):
        self.analyze_file()
        total_species = len(self.species_counts)
        print("Total number of species:", total_species)
        filtered_species_counts = self.filter_species_counts(threshold)
        self.plot_species_counts(filtered_species_counts)

# Specify the file path to the mature.fa file on your computer
file_path = r"C:\Users\user\AdvancedP\Exam answers\mature.fa"
# Create an instance of the MiRNAAnalyzer class and run the analysis
analyzer = MiRNAAnalyzer(file_path)
analyzer.run_analysis(threshold=220)
