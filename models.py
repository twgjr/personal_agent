import subprocess


class ModelNotFoundException(Exception):
    def __init__(self, model_name):
        super().__init__(f"Error: model '{model_name}' not found.")


def check_model_pulled(model_name):
    try:
        subprocess.run(
            ["ollama", "show", model_name, "--modelfile"],
            check=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
        )
        print(f"Model '{model_name}' found.")
    except subprocess.CalledProcessError as e:
        if f"model '{model_name}' not found" in e.stderr:
            print(f"model '{model_name}' not found")
            try:
                subprocess.run(["ollama", "pull", model_name], check=True)
            except subprocess.CalledProcessError as e:
                if f"Error: pull model manifest: file does not exist" in e.stderr:
                    raise ModelNotFoundException(model_name)
                else:
                    raise  # rethrow the error if soemthing else
        else:
            raise  # rethrow the error if soemthing else
