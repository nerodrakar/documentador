import re

def read_python_file(file_path):
    functions_dict = {}

    with open(file_path, 'r') as file:
        file_content = file.read()
        function_pattern = re.compile(r'def\s+(\w+)\((.*?)\):(?:\s*"""(.*?)""")?', re.DOTALL)
        functions = function_pattern.findall(file_content)

        for func_name, func_args, func_description in functions:
            if func_description:  # Verifica se há uma descrição
                args_list = [arg.strip() for arg in func_args.split(',')]
                description = func_description.strip().split('\n\n')[0]
                description_args = re.findall(r'\n\s*([a-zA-Z0-9_]+)\s*\(([^\)]+)\):\s*([^\n]+)', func_description)
                extracted_args = {}
                for arg_name, arg_type, arg_description in description_args:
                    extracted_args[arg_name] = {
                        'type': arg_type.strip(),
                        'description': arg_description.strip()
                    }

                description_returns = re.findall(r'Returns:\s+([^"]+)', func_description, re.DOTALL)
                extracted_returns = {}
                for ret in description_returns:
                    ret_info = re.findall(r'\s*([a-zA-Z0-9_]+)\s*\(([^\)]+)\):\s*([^\n]+)', ret)
                    for ret_name, ret_type, ret_description in ret_info:
                        extracted_returns[ret_name] = {
                            'type': ret_type.strip(),
                            'description': ret_description.strip()
                        }

                functions_dict[func_name] = {
                    'description': description,
                    'args': args_list,
                    'extracted_args': extracted_args,
                    'return': extracted_returns
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
            if func_info['args']:
                if func_info['extracted_args']:
                    for arg_name, arg_info in func_info['extracted_args'].items():
                        md_file.write('    <tr>\n')
                        md_file.write(f'        <td><code>{arg_name}</code></td>\n')
                        md_file.write(f'        <td>{arg_info["description"]}</td>\n')
                        if arg_info["type"] == 'dict':
                            md_file.write(f'        <td>dictionary</td>\n')
                        elif arg_info["type"] == 'str':
                            md_file.write(f'        <td>string</td>\n')
                        elif arg_info["type"] == 'int':
                            md_file.write(f'        <td>integer</td>\n')
                        elif arg_info["type"] == 'bool':
                            md_file.write(f'        <td>boolean</td>\n')
                        else:
                            md_file.write(f'        <td>{arg_info["type"]}</td>\n')
                    md_file.write('    </tr>\n')
                else:
                    for arg_name in func_info['args']:
                        md_file.write('    <tr>\n')
                        md_file.write(f'        <td><code>{arg_name}</code></td>\n')
                        md_file.write(f'        <td>Description not available.</td>\n')
                        md_file.write(f'        <td>None</td>\n')
                        md_file.write('    </tr>\n')
            else:
                md_file.write('    <tr>\n')
                md_file.write(f'        <td><code>None</code></td>\n')
                md_file.write(f'        <td>This function does not receive any input.</td>\n')
                md_file.write(f'        <td>None</td>\n')
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

            if func_info['return']:
                for ret_name, ret_info in func_info['return'].items():
                    md_file.write('    <tr>\n')
                    md_file.write(f'        <td><code>{ret_name}</code></td>\n')
                    md_file.write(f'        <td>{ret_info["description"]}</td>\n')
                    if ret_info["type"] == 'dict':
                        md_file.write(f'        <td>dictionary</td>\n')
                    elif ret_info["type"] == 'str':
                        md_file.write(f'        <td>string</td>\n')
                    elif ret_info["type"] == 'int':
                        md_file.write(f'        <td>integer</td>\n')
                    elif ret_info["type"] == 'bool':
                        md_file.write(f'        <td>boolean</td>\n')
                    else:
                        md_file.write(f'        <td>{ret_info["type"]}</td>\n')
                    md_file.write('    </tr>\n')
            else:
                md_file.write('    <tr>\n')
                md_file.write(f'        <td><code>None</code></td>\n')
                md_file.write(f'        <td>This function does not return any value.</td>\n')
                md_file.write(f'        <td>None</td>\n')
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


file_path = "EASYPLOT.py"
functions_info = read_python_file(file_path)
print(functions_info['line_chart'])

output_file = 'teste/'
generate_md_files(functions_info, output_file)
print(f'Arquivo Markdown gerado com sucesso: {output_file}')


