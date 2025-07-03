import nbformat

nb = nbformat.read('Compression with different models.ipynb', as_version=4)
for cell in nb.cells:
    md = cell.metadata
    if 'widgets' in md:
        # либо добавляем пустой state
        md['widgets'].setdefault('state', {})
        # либо полностью удаляем:
        # del md['widgets']
nbformat.write(nb, 'fixed.ipynb')