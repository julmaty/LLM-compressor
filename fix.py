import nbformat

input_path = 'Compression with different models.ipynb'
output_path = 'Compression with different models_fixed.ipynb'

# Read the notebook
nb = nbformat.read(input_path, as_version=nbformat.NO_CONVERT)

# Remove widgets metadata at notebook level
if 'widgets' in nb.metadata:
    del nb.metadata['widgets']

# Remove widgets metadata from each cell
for cell in nb.cells:
    if 'widgets' in cell.metadata:
        del cell.metadata['widgets']

# Write the fixed notebook
nbformat.write(nb, output_path)

output_path
