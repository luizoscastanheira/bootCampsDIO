import luigi
import pandas as pd

# 1. Tarefa de extração
class ExtractData(luigi.Task):
    def output(self):
        return luigi.LocalTarget("data_raw.csv")

    def run(self):
        # Simulando criação de dados brutos
        with self.output().open("w") as f:
            f.write("nome\nLuiz\nMaria\nJoão")

# 2. Tarefa de transformação
class TransformData(luigi.Task):
    def requires(self):
        return ExtractData()

    def output(self):
        return luigi.LocalTarget("data_transformed.csv")

    def run(self):
        df = pd.read_csv(self.input().path)
        df["nome"] = df["nome"].str.upper()
        df.to_csv(self.output().path, index=False)

# 3. Tarefa de carga
class LoadData(luigi.Task):
    def requires(self):
        return TransformData()

    def output(self):
        return luigi.LocalTarget("pipeline_done.txt")

    def run(self):
        # Apenas marca que o pipeline terminou
        with self.output().open("w") as f:
            f.write("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    luigi.run()