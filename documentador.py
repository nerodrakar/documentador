import re

def read_python_file(file_path):
    functions_dict = {}

    with open(file_path, 'r') as file:
        file_content = file.read()
        function_pattern = re.compile(r'def\s+(\w+)\((.*?)\):\s*"""(.*?)"""', re.DOTALL)
        functions = function_pattern.findall(file_content)

        for func_name, func_args, func_description in functions:
            args_list = [arg.strip() for arg in func_args.split(',')]
            return_type = re.search(r'Returns:\s+(.*?)\s+', func_description, re.DOTALL)
            return_type = return_type.group(1).strip() if return_type else None

            functions_dict[func_name] = {
                'description': func_description.strip(),
                'args': args_list,
                'return': return_type
            }

    return functions_dict


def generate_md_files(functions_info, output_folder):
    for func_name, func_info in functions_info.items():
        md_filename = f'{output_folder}/{func_name}.md'
        with open(md_filename, 'w') as md_file:
            md_file.write('---\n')
            md_file.write('layout: default\n')
            md_file.write(f'title: {func_name}\n')
            md_file.write('grand_parent: Framework\n')
            md_file.write('parent: Common Library functions\n')
            md_file.write('nav_order: 1\n')
            md_file.write('has_toc: false\n')
            md_file.write('---\n\n')

            md_file.write(f'<h3>{func_name}</h3>\n\n')

            md_file.write(f'<br>\n\n')

            md_file.write(f'<p align = "justify">\n')
            md_file.write(f'    {func_info["description"]}\n')
            md_file.write(f'</p>\n\n')

            md_file.write('```python\n')
            md_file.write(f'{func_name}(')
            md_file.write(', '.join(func_info['args']))
            md_file.write(')\n')
            md_file.write('```\n\n')

            md_file.write('Input variables\n')
            md_file.write('{: .label .label-yellow }\n\n')

            md_file.write('<table style = "width:100%">\n')
            md_file.write('    <thead>\n')
            md_file.write('      <tr>\n')
            md_file.write('        <th>Name</th>\n')
            md_file.write('        <th>Description</th>\n')
            md_file.write('        <th>Type</th>\n')
            md_file.write('      </tr>\n')
            md_file.write('    </thead>\n')

            for arg in func_info['args']:
                md_file.write('    <tr>\n')
                md_file.write(f'        <td><code>{arg}</code></td>\n')
                md_file.write('        <td>Description of the argument</td>\n')
                md_file.write('        <td>Type of the argument</td>\n')
                md_file.write('    </tr>\n')

            md_file.write('</table>\n\n')

            md_file.write('Output variables\n')
            md_file.write('{: .label .label-yellow }\n\n')

            md_file.write('<table style = "width:100%">\n')
            md_file.write('    <thead>\n')
            md_file.write('      <tr>\n')
            md_file.write('        <th>Name</th>\n')
            md_file.write('        <th>Description</th>\n')
            md_file.write('        <th>Type</th>\n')
            md_file.write('      </tr>\n')
            md_file.write('    </thead>\n')

            md_file.write('    <tr>\n')
            md_file.write(f'        <td><code>{func_info["return"]}</code></td>\n')
            md_file.write('        <td>Description of the return value</td>\n')
            md_file.write('        <td>Type of the return value</td>\n')
            md_file.write('    </tr>\n')

            md_file.write('</table>\n\n')

            md_file.write(f'Example 1\n')
            md_file.write('{: .label .label-blue }\n\n')

            md_file.write(f'<p align = "justify">\n')
            md_file.write(f'    <i>\n')
            md_file.write(f'        Use the <code>{func_name}</code> function to perform a task.\n')
            md_file.write(f'    </i>\n')
            md_file.write(f'</p>\n\n')

            md_file.write('```python\n')
            md_file.write('# Example code goes here\n')
            md_file.write('```\n\n')

            md_file.write('```bash\n')
            md_file.write('# Example output goes here\n')
            md_file.write('```\n\n')


# Teste
file_path = "EASYPLOT.py"
functions_info = read_python_file(file_path)

output_file = 'teste/'
generate_md_files(functions_info, output_file)
print(f'Arquivo Markdown gerado com sucesso: {output_file}')


