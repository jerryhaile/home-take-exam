import Levenshtein
import matplotlib.pyplot as plt

class LevenshteinDistanceAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.let7a_mirnas = []
        self.distances = []

    def extract_let7a_mirnas(self):
        with open(self.file_path, "r") as file:
            miRNA_name = ""
            sequence = ""
            for line in file:
                if line.startswith(">"):
                    if miRNA_name != "":
                        if miRNA_name.startswith("hsa-let-7"):
                            self.let7a_mirnas.append((miRNA_name, sequence))
                    miRNA_name = line.strip()[1:]
                    sequence = ""
                else:
                    sequence += line.strip()

            if miRNA_name.startswith("-let-7"):
                self.let7a_mirnas.append((miRNA_name, sequence))

    def calculate_pairwise_distances(self):
        for mirna, seq in self.let7a_mirnas:
            print("Pairwise Levenshtein distances for", mirna)
            for other_mirna, other_seq in self.let7a_mirnas:
                if mirna != other_mirna:
                    distance = Levenshtein.distance(seq, other_seq)
                    self.distances.append(distance)
                    print(f"Levenshtein distance between {mirna} and {other_mirna}: {distance}")

    def generate_histogram_plot(self):
        plt.hist(self.distances, bins=10)  # Adjust the number of bins as needed
        plt.xlabel("Levenshtein Distance")
        plt.ylabel("Frequency")
        plt.title("Distribution of Levenshtein Distances")
        plt.show()

    def run_analysis(self):
        self.extract_let7a_mirnas()
        self.calculate_pairwise_distances()
        self.generate_histogram_plot()


# Specify the file path to the mature.fa file on your computer
file_path = r"C:\Users\user\AdvancedP\Exam answers\mature.fa"

# Create an instance of the LevenshteinDistanceAnalyzer class and run the analysis
analyzer = LevenshteinDistanceAnalyzer(file_path)
analyzer.run_analysis()
