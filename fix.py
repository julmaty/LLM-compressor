import nbformat

# Пути
input_path = 'Compression with different models.ipynb'
output_path = 'Compression with different models_fixed.ipynb'

# Читаем ноутбук
nb = nbformat.read(input_path, as_version=nbformat.NO_CONVERT)

# Проходим по всем ячейкам и очищаем metadata.widgets
for cell in nb.cells:
    if 'widgets' in cell.metadata:
        del cell.metadata['widgets']

# Сохраняем исправленный ноутбук
nbformat.write(nb, output_path)

print(f"Исправленный файл сохранён как: {output_path}")
