# Bioscripts
## Описание пакета
В данном пакете представлены утилиты для обработки биоинформатических данных
FASTA,FASTQ, GBK, BlAST-таблиц.
На данный момент, пакет состоит из следующих функций:
1. filter_fastq (фильтрация данных по заданным параметрам)
2. convert_multiline_fasta_to_oneline (перевод данных FASTA из многострочного в однострочный формат)
3. parse_blast_output (поиск лучшего hit. Результат выводится в виде отсортированного 
по алфавиту списка.)

## Структура пакета
```
-/
|- README.md
|- главный скрипт.py # основные функции
|- helpers/
    |- fastq.py       # вспомогательные функции для filter_fastq
    |- bio_files.py   # вспомогательные функции для 
    convert_multiline_fasta_to_oneline,
    parse_blast_output
```

## Как использовать
1. Для использования функция необходимо склонировать репозитарий на свой компьютер
```bash
git clone@git@github.com:Treivenik/Bioscripts.git
```

2. Убедитесь что на Вашем ПК установлен Python
```bash
pyton --version
```
3. Установитe Python, при его отсутствии

3. "Сырые" данные FASTA, FASTQ, результаты BLAST удобнее сохранить в папке Bioscripts (в таком случае для задания пути достаточно будет
указывать имя файла), но абсолютный путь так же подойдет. Проверьте чтоб файл лежал в папке,
которую Python использует как PATH.
4. После запуска Python  импортируйте необходимую функцию командой 
```python
from bioscripts import filter_fastq
from bioscripts import convert_multiline_fasta_to_oneline 
from bioscripts import parse_blast_output
```
5. Подсказки по принимаемым функциями аргументам смотри в коде.

## Автор
Никифорова Татьяна

