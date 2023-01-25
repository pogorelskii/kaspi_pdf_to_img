# Конвертация накладной Каспия в отдельные изображения.

## Подготовка

### Устанавливаем python
Скачиваем 11 версию python с
https://www.python.org/downloads/

### Устанавливаем необходимое библиотеки
Установка через файл requirements.txt
```bash
pip install -r requirements.txt
```
или ставим кажду библиотеку отдельно
```bash
pip install requests==2.28.2
pip install pypdfium2==3.19.0
pip install Pillow==9.4.0
```

## Использование скрипта

Скрипт входными параметрами принимает:
- url_pdf - ссылка на накладную каспия
- output_path - путь куда сохранить полученные изображения

```bash
python convert_kaspi_pdf.py -url_pdf 'ссылка_на_накладную_каспи' -output_path 'путь_куда_сложить_результат'
```

Результатом выполнения скрипта является сформированный список изображений (наклеек) полученных из PDF, сохраненный в переданную директорию.
Наименование формируется по следующему принципу out_N.jpg, где N - порядковый номер.

Пример использования:

```bash
python convert_kaspi_pdf.py -url_pdf https://kaspi.kz/medias/sys_master/documents/documents/ha2/ha6/68157055729694/W-238733297-KASPI-LOGISTIC.pdf -output_path C:/kaspi_img/
```
