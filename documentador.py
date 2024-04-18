import inspect
import importlib.util

def generate_md_from_py(file_path):
    # Carrega o módulo
    spec = importlib.util.spec_from_file_location("module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    md = "---\nlayout: default\ntitle: Function Info\ngrand_parent: Framework\nparent: Common Library functions\nnav_order: 1\nhas_toc: false\n---\n\n"

    for name, obj in inspect.getmembers(module):
        # Verifica se o objeto é uma função
        if inspect.isfunction(obj):
            # Obtém a assinatura da função
            signature = inspect.signature(obj)
            parameters = [param for param in signature.parameters.values()]
            params = ", ".join([f"<code>{param.name}</code>: {param.annotation}" if param.annotation != inspect.Parameter.empty else f"<code>{param.name}</code>" for param in parameters])
            # Obtém a anotação de retorno da função
            return_annotation = signature.return_annotation if signature.return_annotation != inspect.Parameter.empty else "None"

            # Formata o Markdown para a função
            md += f"\n\n<h3>{name}</h3>\n\n"
            md += f"<p align='justify'>\nThe function {name} does something.\n</p>\n\n"
            md += f"```python\nx_pop = {name}("
            for param in parameters:
                md += f"{param.name}, "
            md = md[:-2] + ")\n```\n\n"
            md += f"<p align='justify'>\nInput variables\n</p>\n\n"
            md += "<table style='width:100%'>\n<thead>\n<tr>\n<th>Name</th>\n<th>Description</th>\n<th>Type</th>\n</tr>\n</thead>\n"
            for param in parameters:
                md += f"<tr>\n<td><code>{param.name}</code></td>\n<td>Description of {param.name}</td>\n<td>{param.annotation}</td>\n</tr>\n"
            md += "</table>\n\n"
            md += f"<p align='justify'>\nOutput variables\n</p>\n\n"
            md += "<table style='width:100%'>\n<thead>\n<tr>\n<th>Name</th>\n<th>Description</th>\n<th>Type</th>\n</tr>\n</thead>\n"
            md += f"<tr>\n<td><code>x_pop</code></td>\n<td>Description of x_pop</td>\n<td>{return_annotation}</td>\n</tr>\n"
            md += "</table>\n\n"

    # Escreve o Markdown em um arquivo
    with open("function_info.md", "w") as f:
        f.write(md)

# Caminho para o arquivo .py
file_path = "EASYPLOT.py"
# Gerar Markdown com as informações das funções
generate_md_from_py(file_path)
