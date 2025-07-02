# LLM-compressor

Данная работа сделана к качестве итогового проекта курса от Deep Learning School. Необходимо было  
 	
На базе LLM с помощью алгоритма арифметической компрессии реализовать архиватор текста. Сжать Википедию и посчитать её объём. Улучшить коэффициент компрессии с помощью prefix tuning или steering. Обучить модель генерировать распределение для steering-вектора, чтобы ещё сильнее улучшить компрессию.

Основная часть работы находится в ноутбуках Train Pipeline.ipynb и Metrics.ipynb.

## Подготовка

При подготовке работы были изучены научные статьи [Language Modeling is Compression](https://arxiv.org/pdf/2309.10668), [Variational image compression with a scale hyperprior].
Для сжатия используется датасет Wikipedia [Enwik8](https://www.kaggle.com/datasets/nightfury1103/enwik8).


## Обучение
