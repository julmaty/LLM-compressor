import nbformat

input_path = 'Steering vector with hyper prior.ipynb'
output_path = 'Steering vector with hyper prior_fixed.ipynb'

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
